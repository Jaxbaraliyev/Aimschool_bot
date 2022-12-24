from aiogram.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup,InlineKeyboardMarkup


bizhaq_rus = KeyboardButton(text="📝О нас")
kurs_rus = KeyboardButton(text="📚Курсы")
manzil_rus = KeyboardButton(text="📍Адрес")
royxat_rus = KeyboardButton(text="📋Регистрация")
tarmoq_rus = KeyboardButton(text="🌐Наши социальные сети")
til_sozlamalari_rus = KeyboardButton(text="⚙Языковые настройки")

bosh_menyu_rus = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(bizhaq_rus,kurs_rus,manzil_rus,royxat_rus,tarmoq_rus,til_sozlamalari_rus)


ingliz_tili_rus = KeyboardButton(text="Aнглийский язык🇺🇸")
matem_rus = KeyboardButton(text="Математика🧮")
rus_rus = KeyboardButton(text="Русский язык🇷🇺")
bosh_rus = KeyboardButton(text="Главное меню🏠")

kurs_rus = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(ingliz_tili_rus,matem_rus,rus_rus,bosh_rus)



insta_rus = InlineKeyboardButton(text="Инстаграм", callback_data="insta", url="https://www.instagram.com/aim_school_/")
tele_rus = InlineKeyboardButton(text="Телеграм", callback_data="tele", url="https://t.me/aimschool")


ijtimoiy_rus = InlineKeyboardMarkup().add(insta_rus, tele_rus)


tasdiq_rus = InlineKeyboardButton(text="Подтверждение✅", callback_data="tasdiq_rus")
tahrir_rus = InlineKeyboardButton(text="Редактирование✍", callback_data="tahrir_rus")

royxatdan_otish_rus = InlineKeyboardMarkup().add(tasdiq_rus, tahrir_rus)





til_uzb_rus = KeyboardButton(text="o`zbek - tili🇺🇿")
til_rus_rus = KeyboardButton(text="русский - язык🇷🇺")
bosh_rus = KeyboardButton(text="Главное меню🏠")

um_til_rus = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(til_uzb_rus, til_rus_rus, bosh_rus)



da = InlineKeyboardButton(text="Да✅", callback_data="da")
net = InlineKeyboardButton(text="Нет❌", callback_data="net")

da_net = InlineKeyboardMarkup().add(da, net)
