# парсиинг магазинов для списков подарко
import json
from config_data.config import DATABASE_URL
from database.requests import DatabaseManager
import requests

dsn = DATABASE_URL
db_manager = DatabaseManager(dsn=dsn)


def get_categories(query):
    import requests

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Origin': 'https://www.wildberries.ru',
        'Referer': 'https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=rate&search=%D0%B1%D0%B5%D0%BB%D1%8B%D0%B5+%D0%BD%D0%BE%D1%81%D0%BA%D0%B8',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MDUzNDcxMDYsInZlcnNpb24iOjIsInVzZXIiOiI1OTMzNDAyMyIsInNoYXJkX2tleSI6IjciLCJjbGllbnRfaWQiOiJ3YiIsInNlc3Npb25faWQiOiJkNWVlNWM4MWU0NTc0YWEzOGVjMGQ0OTI3ZTcwZDMzNiIsInVzZXJfcmVnaXN0cmF0aW9uX2R0IjoxNjg2NzMyODczLCJ2YWxpZGF0aW9uX2tleSI6IjUwMDBhMTI5MTcwMTk2MDBkMmM2NGQ2NGIwZDc2Y2FlYzAyYTFmMzk1OWNlNTE5MTRhZmRhNWQ4NjJjZjEyYjUiLCJwaG9uZSI6IklUdStIYWx4VmRucDlPMVlnN04xNEE9PSJ9.BK80fg2hUDmH32L3hhmEgLWybmVT3A3vUDLt5CEm4YwcZ25R3Jm_134GvZb3JL7ojRM0XV4x1-faad8apxZSy2dxNKp08SBovlTxTwA3hTTgeormO4De6SCZJTOfvFI3msOn9tnTrBXL5s6enhbPnoMO_5p5gkLCZIYbF-aFccXH84EUa-vVJ-BJselt07y7_9mS7mPZdRTA4Qf8S8ZkdT2DmuQWtJjkGIAI5BmmYfpdRgJnyiRgqO8_yeykmCNifESDpB3LQx4ne-oieQrYAmlm3oQhXltJFOyCMoRZZlKqv661FbxiJydiYe6La7dLAdOEwWpBctMJZQIAEdD3uA',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-userid': '59334023',
    }

    params = {
        'TestGroup': 'no_test',
        'TestID': 'no_test',
        'appType': '1',
        'curr': 'rub',
        'dest': '-5551775',
        'page': '1',
        'query': query,
        'resultset': 'catalog',
        'sort': 'rate',
        'spp': '29',
        'suppressSpellcheck': 'false',
        'uclusters': '8',
    }

    response = requests.get('https://search.wb.ru/exactmatch/ru/common/v4/search', params=params, headers=headers)

    return response.json()


def prepare_items(response) -> list:
    products = []

    products_row = response.get('data', {}).get('products', None)

    if products_row is not None:
        for product in products_row:
            if product.get('supplierRating') > 4.5 and product.get('feedbacks') > 1000:
                products.append({
                    "id_gift": product.get('id', None),
                    "shop": 'Wildberries',
                    "brand": product.get('brand', None),
                    "name": product.get('name', None),
                    "price": product.get('salePriceU', None) / 100,
                    "supplierRating": product.get('supplierRating', None),
                    "feedbacks": product.get('feedbacks', None)
                })

    return products


async def gift_list_generation(gifts, user_id):
    for gift in gifts.split(','):
        response = get_categories(query=gift)
        list_products = prepare_items(response=response)
        if list_products:
            sorted_items = sorted(list_products, key=lambda item: item["price"])
            cheapest_item, most_expensive_item = sorted_items[0], sorted_items[-1]

            cheapest_item["user_id"] = user_id
            cheapest_item["status"] = 'Дешевый'
            await db_manager.add_generate_gift(gifts_data=cheapest_item)

            most_expensive_item["user_id"] = user_id
            most_expensive_item["status"] = 'Дорогой'
            await db_manager.add_generate_gift(gifts_data=most_expensive_item)

# def read_json(user_id):
#     with open(f'services/gift_list{user_id}.json', 'r') as file:
#         data = json.load(file)
#     sorted_dict = sorted(data, key=lambda items: items["price"])
#     return sorted_dict


# if __name__ == '__main__':
#     main()
#     print(read_json()[0], read_json()[-1])
