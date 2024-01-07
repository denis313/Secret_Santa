from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from database.model import User, Questionnaire, GiftList


class DatabaseManager:
    def __init__(self, dsn):
        self.engine = create_async_engine(dsn, echo=True)
        self.async_session = async_sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)

    # async def create_tables(self):
    #     async with self.async_session() as session:
    #         async with self.engine.begin() as conn:
    #             await conn.run_sync(Base.metadata.create_all)

    # add new user from db
    async def add_user(self, user_data):
        async with self.async_session() as session:
            new_user = User(**user_data)
            session.add(new_user)
            await session.commit()

    # add questionnaire for user from db
    async def add_questionnaire(self, questionnaire_data):
        async with self.async_session() as session:
            new_questionnaire = Questionnaire(**questionnaire_data)
            session.add(new_questionnaire)
            await session.commit()

    # add gift list for user from db
    async def add_gift_list(self, gift_list_data):
        async with self.async_session() as session:
            new_gift_list = GiftList(**gift_list_data)
            session.add(new_gift_list)
            await session.commit()

    # get user by user_id from db
    async def get_user_by_id(self, user_id):
        async with self.async_session() as session:
            result = await session.execute(select(User).where(User.user_id == user_id))
            user = result.scalar()
            return user

    # get questionnaire by user_id from db
    async def get_questionnaire_by_id(self, user_id):
        async with self.async_session() as session:
            query = select(Questionnaire).filter(Questionnaire.user_id == user_id)
            result = await session.execute(query)
            questionnaires = result.scalar()
            return questionnaires

    # get gift list by user_id from db
    async def get_gift_list(self, user_id):
        async with self.async_session() as session:
            g_l = select(GiftList).filter(GiftList.user_id == user_id)
            result = await session.execute(g_l)
            gift_list = result.scalar()
            return gift_list

    # update questionnaire by user_id from db
    async def update_questionnaire(self, user_id, questionnaire_data):
        async with self.async_session() as session:
            update_questionnaire = select(Questionnaire).filter(Questionnaire.user_id == user_id)
            result = await session.execute(update_questionnaire)
            questionnaire = result.scalar()

            if questionnaire:
                for key, value in questionnaire_data.items():
                    setattr(questionnaire, key, value)

                await session.commit()

    # update gift_list by user_id from db
    async def update_gift_list(self, user_id, list_data):
        async with self.async_session() as session:
            update_list = select(GiftList).filter(GiftList.user_id == user_id)
            result = await session.execute(update_list)
            gift_list = result.scalar()

            if gift_list:
                for key, value in list_data.items():
                    setattr(gift_list, key, value)

                await session.commit()
