from aiogram import Router, F, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State, default_state
from aiogram.types import Message, CallbackQuery

from filters.filter import IsPrivate
from LEXICON.lexicon import LEXICON_user, LEXICON_keyboard, LEXICON_FSM
from keyboards.general_keyboards import questionnaire

router = Router()
router.message.filter(IsPrivate())


@router.callback_query(F.data == LEXICON_keyboard["keyboard_start_2"][1])
async def for_new_user(callback: CallbackQuery):
    user = callback.from_user
    if not user:
        await callback.message.answer(text=LEXICON_user["not_in_the_game"].format(name=user.first_name))
    else:
        await callback.message.answer(text=LEXICON_user["in_the_game"].format(name=user.first_name),
                                      reply_markup=questionnaire)


class Questionnaire(StatesGroup):
    name = State()
    sex = State()
    age = State()
    clothing_brand = State()
    color_palette = State()
    sizes = State()
    fashion_style = State()
    hobby = State()
    allergy = State()
    salty_or_sweet = State()
    trips = State()
    

@router.message(F.text == 'Stop 🛑', ~StateFilter(default_state))
async def process_gender_press(message: Message, state: FSMContext):
    await message.answer(LEXICON_FSM["stop"])
    await state.clear()


@router.callback_query(F.data == LEXICON_keyboard["questionnaire"][1], StateFilter(default_state))
async def add_questionnaire(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.edit_message_reply_markup(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        reply_markup=None
    )
    await state.set_state(Questionnaire.name)
    await callback.message.answer(text=LEXICON_FSM["name"][0])


@router.message(StateFilter(Questionnaire.name), F.text.isalpha())
async def add_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Questionnaire.sex)
    await message.answer(text=LEXICON_FSM["sex"][0])


@router.message(StateFilter(Questionnaire.name))
async def add_not_name(message: Message):
    await message.answer(LEXICON_FSM["name"][1])


@router.message(StateFilter(Questionnaire.sex), F.text.isalpha())
async def add_sex(message: Message, state: FSMContext):
    await state.update_data(sex=message.text)
    await state.set_state(Questionnaire.age)
    await message.answer(LEXICON_FSM["age"][0])


@router.message(StateFilter(Questionnaire.sex))
async def add_not_sex(message: Message):
    await message.answer(LEXICON_FSM["sex"][1])


@router.message(StateFilter(Questionnaire.age), F.text.isdigit())
async def add_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Questionnaire.clothing_brand)
    await message.answer(LEXICON_FSM["clothing_brand"][0])


@router.message(StateFilter(Questionnaire.age))
async def add_not_age(message: Message):
    await message.answer(LEXICON_FSM["age"][1])


@router.message(StateFilter(Questionnaire.clothing_brand), F.text.isalpha())
async def add_clothing_brand(message: Message, state: FSMContext):
    await state.update_data(clothing_brand=message.text)
    await state.set_state(Questionnaire.color_palette)
    await message.answer(LEXICON_FSM["color_palette"][0])


@router.message(StateFilter(Questionnaire.clothing_brand))
async def add_not_clothing_brand(message: Message):
    await message.answer(LEXICON_FSM["clothing_brand"][1])


@router.message(StateFilter(Questionnaire.color_palette), F.text.isalpha())
async def add_color_palette(message: Message, state: FSMContext):
    await state.update_data(color_palette=message.text)
    await state.set_state(Questionnaire.sizes)
    await message.answer(LEXICON_FSM["sizes"][0])


@router.message(StateFilter(Questionnaire.color_palette))
async def add_not_color_palette(message: Message):
    await message.answer(LEXICON_FSM["color_palette"][1])


@router.message(StateFilter(Questionnaire.sizes), F.text.isalpha())
async def add_sizes(message: Message, state: FSMContext):
    await state.update_data(sizes=message.text)
    await state.set_state(Questionnaire.fashion_style)
    await message.answer(LEXICON_FSM["fashion_style"][0])


@router.message(StateFilter(Questionnaire.sizes))
async def add_not_sizes(message: Message):
    await message.answer(LEXICON_FSM["sizes"][1])


@router.message(StateFilter(Questionnaire.fashion_style), F.text.isalpha())
async def add_fashion_style(message: Message, state: FSMContext):
    await state.update_data(fashion_style=message.text)
    await state.set_state(Questionnaire.hobby)
    await message.answer(LEXICON_FSM["hobby"][0])


@router.message(StateFilter(Questionnaire.fashion_style))
async def add_not_fashion_style(message: Message):
    await message.answer(LEXICON_FSM["fashion_style"][1])


@router.message(StateFilter(Questionnaire.hobby), F.text.isalpha())
async def add_hobby(message: Message, state: FSMContext):
    await state.update_data(hobby=message.text)
    await state.set_state(Questionnaire.allergy)
    await message.answer(LEXICON_FSM["allergy"][0])


@router.message(StateFilter(Questionnaire.hobby))
async def add_not_hobby(message: Message):
    await message.answer(LEXICON_FSM["hobby"][1])


@router.message(StateFilter(Questionnaire.allergy), F.text.isalpha())
async def add_allergy(message: Message, state: FSMContext):
    await state.update_data(allergy=message.text)
    await state.set_state(Questionnaire.salty_or_sweet)
    await message.answer(LEXICON_FSM["salty_or_sweet"][0])


@router.message(StateFilter(Questionnaire.allergy))
async def add_not_allergy(message: Message):
    await message.answer(LEXICON_FSM["allergy"][1])


@router.message(StateFilter(Questionnaire.salty_or_sweet), F.text.isalpha())
async def add_salty_or_sweet(message: Message, state: FSMContext):
    await state.update_data(salty_or_sweet=message.text)
    await state.set_state(Questionnaire.trips)
    await message.answer(LEXICON_FSM["trips"][0])


@router.message(StateFilter(Questionnaire.salty_or_sweet))
async def add_not_salty_or_sweet(message: Message):
    await message.answer(LEXICON_FSM["salty_or_sweet"][1])


@router.message(StateFilter(Questionnaire.trips), F.text.isalpha())
async def add_trips(message: Message, state: FSMContext):
    await state.update_data(trips=message.text)
    data = await state.get_data()
    await message.answer(LEXICON_FSM["end"])
    for key, value in data.items():
        print(key, '-', value)


@router.message(StateFilter(Questionnaire.trips))
async def add_not_trips(message: Message):
    await message.answer(LEXICON_FSM["trips"][1])
