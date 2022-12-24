from aiogram.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup,InlineKeyboardMarkup

ozbek_tili = InlineKeyboardButton(text="O`zbek tili🇺🇿", callback_data="uzb")
rus_tili = InlineKeyboardButton(text="Русский язык🇷🇺", callback_data="rus")

til_result = InlineKeyboardMarkup().add(ozbek_tili, rus_tili)


biz_haq = KeyboardButton(text="📝Biz haqimizda")
kurslar = KeyboardButton(text="📚Kurslar")
manzil = KeyboardButton(text="📍Manzil")
royxat = KeyboardButton(text="📋Ro`yxatdan o`tish")
tarmoq = KeyboardButton(text="🌐Bizning ijtimoiy tarmoqlar")
til_sozlamalari = KeyboardButton(text="⚙Til sozlamalari")

bosh_menyu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(biz_haq,kurslar,manzil,royxat,tarmoq,til_sozlamalari)


ingliz_tili = KeyboardButton(text="Ingliz tili🇺🇸")
matem = KeyboardButton(text="Matematika🧮")
rus = KeyboardButton(text="Rus tili🇷🇺")
bosh = KeyboardButton(text="Bosh menyu🏠")

kurs = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(ingliz_tili,matem,rus,bosh)


tasdiq = InlineKeyboardButton(text="Tasdiqlash✅", callback_data="tasdiq")
tahrir = InlineKeyboardButton(text="Tahrirlash✍", callback_data="tahrir")

royxatdan_otish = InlineKeyboardMarkup().add(tasdiq, tahrir)



insta = InlineKeyboardButton(text="Instagram", callback_data="insta", url="https://www.instagram.com/aim_school_/")
tele = InlineKeyboardButton(text="Telegram", callback_data="tele", url="https://t.me/aimschool")


ijtimoiy = InlineKeyboardMarkup().add(insta, tele)


til_uz = KeyboardButton(text="o`zbek tili🇺🇿")
til_rus = KeyboardButton(text="русский язык🇷🇺")
bosh = KeyboardButton(text="Bosh menyu🏠")

um_til = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(til_uz, til_rus,bosh)



ha = InlineKeyboardButton(text="Ha✅", callback_data="ha")
yoq = InlineKeyboardButton(text="Yo`q❌", callback_data="yoq")

ha_yoq = InlineKeyboardMarkup().add(ha, yoq)