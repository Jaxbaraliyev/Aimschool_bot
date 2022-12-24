from aiogram import Bot, Dispatcher, types,executor
import logging
from config import API_TOKEN
from keyboards import *
from aiogram.dispatcher.filters.state import StatesGroup,State
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from rus_keyboards import *


class PersonalData(StatesGroup):
    fullname = State()
    tugilgan_sana = State()
    phonenumber = State()
    manzil = State()
    kurslar = State()


class PersonalData_rus(StatesGroup):
    fullname_rus = State()
    tugilgan_sana_rus = State()
    phonenumber_rus = State()
    manzil_russ = State()
    kurslar_rus = State()


ADMIN_CHAT_ID = -1001899484523
ADMIN_CHAT_ID_USER = -1001884936923


logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    ism = message.from_user.full_name
    user_id = message.from_user.id
    username = message.from_user.username
    full_name = message.from_user.full_name
    await message.answer(f"Assalomu alaykum <i>{ism}</i>.Aim school o`quv markazining rasmiy botiga xush kelibsiz😊!\n\n"
                         f"O`zingizga kerakli bo`lgan tilni tanlang:👇", parse_mode="HTML", reply_markup=til_result)
    await bot.send_message(chat_id=ADMIN_CHAT_ID_USER,text=f"Toliq ismi - <b>{full_name}</b>\n"
                                                       f"Username - <b>{username}</b>\n"
                                                       f"Telegram_id - <b>{user_id}</b>", parse_mode="HTML")


@dp.message_handler(commands=['help'])
async def help(message:types.Message):
    await message.answer("Biz sizga qanday yordam ko`rsata olamiz?\n"
                         "O`quv markazimiz adminiga murojaat qiling!\nAdmin -> @mn10112021")


@dp.message_handler(commands=['admin'])
async def admin(message:types.Message):
    admin_bot = "@Ramziddin_17_17"
    admin_markaz = "@mn10112021"
    await message.answer(f"O`quv markaz admini -> {admin_markaz}\n"
                         f"Bot admini -> {admin_bot} ")


@dp.callback_query_handler(lambda c: c.data == "uzb")
async def til_uzb(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, "Siz o`zbek tilini muaffaqiyatli tanladingiz✅!\n\nEndi esa o`zingizga kerakli bo`lgan bo`limni tanlang👇!", reply_markup=bosh_menyu)


@dp.callback_query_handler(lambda c: c.data == "rus")
async def til_uzb(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, "Вы успешно выбрали русский язык✅!\n\n Теперь выберите нужный раздел👇:!", reply_markup=bosh_menyu_rus)


@dp.message_handler()
async def biz_haq(message:types.Message):
    if message.text == "📝Biz haqimizda":
        sarlavha = "<b>Aim school o`quv markazi haqida qisqacha ma`lumot.</b>\n\n"
        sarlavha += "Bizning o`quv markaz 22.02.2022 yilda o`z ish faoliyatini boshlagan.\n"
        sarlavha += "O`quv markazimiz hozirgi kunga qadar juda ko`plab o`quvchilarga bilim berib kelmoqda.\n"
        sarlavha += "Shuningdek o`quv markazimizda siz mutlaqo bepul ta`lim ham olishingiz mumkin. Qanday qilib deysizmi?\n"
        sarlavha += "Har oy oxirida olayotgan bilimlaringiz bo`yicha 100 ballik sistemada imtixon bo`lib o`tadi," \
                    "va ushbu imtixonda 90 balldan yuqori ball to`plagan bitta o`quvchi keyingi oylik to`lovini qilmay o`qishi imkoniyatiga ega bo`ladi!\n\n"
        sarlavha += "* O`quvchilarni imtixonlarga tayyorlash bo`yicha yosh mehnatkash va tajribaga ega ustozlar.\n"
        sarlavha += "* Xo`jaobod tumanidagi yagon kuchli o`qitish tizimi.\n"
        sarlavha += "* Darsdan tashqari qo`shimcha dars tayyorlash uchun coworking zonalari.\n"
        sarlavha += "* O`quvchilarimizni bilim darajasini nazorat qilish va rag`batlantirish.\n"
        sarlavha += "* Bularning hammasi Aim school o`quv markazimizda!!!\n\n"
        sarlavha += "<b> Aim school\n For better days😎!</b>"
        with open("photo_2022-10-26_23-05-57.jpg", "rb") as file:
            await message.answer_photo(caption=sarlavha,photo=file, parse_mode="HTML")

    elif message.text == "📚Kurslar":
        await message.answer("Qaysi kurs haqida ma`lumot olmoqchisiz?\n"
                             "Quyidagilardan birini tanlang👇:",reply_markup=kurs)
    elif message.text == "Ingliz tili🇺🇸":
        sarlavha = "<b>Ingliz tili kursi</b>\n\n"
        sarlavha += "Ingliz tili kurslarimiz davomiyligi 120 minut, haftada 3 kun va bizda qo`shimcha darslar ham bor.\n"
        sarlavha += "Ya`ni yakshanba dam olish kunida ham qo`shimcha darslar o`tib boriladi.\n"
        sarlavha += "Siz kursga yozilganingizdan keyin sizdan imtixon olinadi va bilim darajangiz qaysi bosqichga to`g`ri keladigan bo`lsa " \
                        "ana shu bosqichdan davom ettirishingiz mumkin\n"
        sarlavha += "Sizga malakali o`qituvchilarimiz bilim berishda hech ham charchamaydi!\n"
        sarlavha += "Hoziroq ro`yxatdan o`ting📋👇!\n"
        await message.answer_photo(caption=sarlavha, photo="https://www.studiocambridge.co.uk/wp-content/uploads/2020/10/Learn-English-Word-Cloud-1024x677.png", parse_mode="HTML")

    elif message.text == "Matematika🧮":
        sarlavha = "<b>Matematika kursi</b>\n\n"
        sarlavha += "Matematika kurslarimiz davomiyligi 120 minut, haftada 3 kun va bizda qo`shimcha darslar ham bor.\n"
        sarlavha += "Ya`ni yakshanba dam olish kunida ham qo`shimcha darslar o`tib boriladi.\n"
        sarlavha += "Siz bu kurs orqali Davlat imtixonlariga va har qanday Olimpiadalar uchun ham tayyorlanishingiz mumkin.\n" \
                    "Nima uchun buni takidlab o`tyabmiz chunki bizning o`quvchilarimiz Olimpiada o`yinlarida yuqori natijalarni qo`lga kiritib kelmoqda.\n"
        sarlavha += "Hoziroq ro`yxatdan o`ting📋👇!\n"
        await message.answer_photo(caption=sarlavha, photo="https://i0.wp.com/www.additudemag.com/wp-content/uploads/2021/09/GettyImages-1044168372.jpg?resize=480%2C270px&ssl=1", parse_mode="HTML")

    elif message.text == "Rus tili🇷🇺":
        sarlavha = "<b>Rus tili kursi</b>\n\n"
        sarlavha += "Rus tili kurslarimiz davomiyligi 120 minut, haftada 3 kun va bizda qo`shimcha darslar ham bor.\n"
        sarlavha += "Ya`ni yakshanba dam olish kunida ham qo`shimcha darslar o`tib boriladi.\n"
        sarlavha += "Rus tili darslarimiz eng so`nggi zamonaviy uslublarda olib boriladi va siz bu uslublar orqali har qanday mavzularni oson tushunib olishinigiz mumkin\n"
        sarlavha += "Hoziroq ro`yxatdan o`ting📋!\n"
        await message.answer_photo(caption=sarlavha, photo="https://youlang.ru/storage/articles_img/HA2UdyA2dnFXiDJ49RY0M5LHanh9ZZyYFrDQmDWd.jpeg", parse_mode="HTML")

    elif message.text == "🌐Bizning ijtimoiy tarmoqlar":
        await message.answer("Bizning ijtimoiy tarmoqlarimiz👇:",reply_markup=ijtimoiy)

    elif message.text == "Bosh menyu🏠":
        await message.answer("Siz bosh menyu bo`limini tanladingiz✅!",reply_markup=bosh_menyu)

    elif message.text == "📍Manzil":
        await message.answer("Bizning manzil: Andijon viloyati,\nXo`jaobod tumani\nMo`ljal: Registon Fast Food ro`parasi. ")
        await message.answer_location(latitude=40.66587, longitude=72.56190)

    elif message.text == "⚙Til sozlamalari":
        await message.answer("O`zingizga qulay bo`lgan tilni tanlang👇:", reply_markup=um_til)

    elif message.text == "o`zbek tili🇺🇿":
        await message.answer("Siz o`zbek tilini muaffaqiyatli tanladingiz✅!")

    elif message.text == "русский язык🇷🇺":
        await message.answer("Вы успешно выбрали русский язык✅!",reply_markup=bosh_menyu_rus)

    elif message.text == "📋Ro`yxatdan o`tish":
        await message.answer("Siz haqiqatdan ham ro`yxatdan o`tishni istaysizmi?", reply_markup=ha_yoq)

    @dp.callback_query_handler(lambda c: c.data == "yoq")
    async def yoq(call: types.callback_query):
        await bot.answer_callback_query(call.id)
        await bot.send_message(call.message.chat.id, "Siz boshqa istalgan bo`limni tanlashingiz mumkin!", reply_markup=bosh_menyu)

    @dp.callback_query_handler(lambda c: c.data == "ha")
    async def ha(call: types.callback_query):
        await bot.answer_callback_query(call.id)
        await bot.send_message(call.message.chat.id,"To`liq ismingizni kiriting:")
        await PersonalData.next()

    @dp.message_handler(state=PersonalData.fullname)
    async def answer_fullname(message: types.Message, state: FSMContext):
        fullname = message.text
        await state.update_data(
            {"name": fullname}
        )
        await message.answer("Tug`ilgan sanangizni kiriting:\n(22.02.2022)")
        await PersonalData.next()

    @dp.message_handler(state=PersonalData.tugilgan_sana)
    async def answer_fullname(message: types.Message, state: FSMContext):
        tugilgan_sana = message.text
        await state.update_data(
            {"tugilgan_sana": tugilgan_sana}
        )
        await message.answer("Telefon raqamingizni kiriting:\n(+9989X 123-45-67)")
        await PersonalData.next()

    @dp.message_handler(state=PersonalData.phonenumber)
    async def answer_fullname(message: types.Message, state: FSMContext):
        phonenumber = message.text
        await state.update_data(
            {"phonenumber": phonenumber}
        )
        await message.answer("Manzilingizni kiriting:")
        await PersonalData.next()

    @dp.message_handler(state=PersonalData.manzil)
    async def answer_fullname(message: types.Message, state: FSMContext):
        manzil = message.text
        await state.update_data(
            {"yashash_manzili": manzil}
        )
        await message.answer("O`zingiz tanlanagan kurs nomimi kiriting:")
        await PersonalData.next()

    @dp.message_handler(state=PersonalData.kurslar)
    async def answer_fullname(message: types.Message, state: FSMContext):
        kurslar = message.text
        await state.update_data(
            {"kurslar": kurslar}
        )

        data = await state.get_data()
        name = data.get("name")
        tugilgan_sana = data.get("tugilgan_sana")
        phonenumber = data.get("phonenumber")
        yashash_manzil = data.get("yashash_manzili")
        kurslar = data.get("kurslar")

        msg = f"<b>Quyidagi ma`lumotlar qabul qilindi!</b>\n\n"
        msg += f"To`liq ismingiz - {name}\n\n"
        msg += f"Tug`ilgan sanangiz - {tugilgan_sana}\n\n"
        msg += f"Telefon raqamingiz - {phonenumber}\n\n"
        msg += f"Yashash manzilingiz - {yashash_manzil}\n\n"
        msg += f"Tanlagan kursingiz - {kurslar}\n\n"

        await message.answer(msg, parse_mode="HTML", reply_markup=royxatdan_otish)
        await state.finish()

        @dp.callback_query_handler(lambda c: c.data == "tasdiq")
        async def tasdiq(call: types.callback_query):
            await bot.answer_callback_query(call.id)
            await bot.send_message(call.message.chat.id, "Sizning ma`lumotlaringiz muaffaqiyatli saqlandi.Biz sizga o`zimiz aloqaga chiqamiz!")
        await bot.send_message(chat_id=ADMIN_CHAT_ID, text=msg, parse_mode="HTML")

        @dp.callback_query_handler(lambda c: c.data == "tahrir")
        async def tasdiq(call: types.callback_query):
            await bot.answer_callback_query(call.id)
            await message.answer("To`liq ismingizni kiriting:")
            await PersonalData.next()
        @dp.message_handler(state=PersonalData.fullname)
        async def tahrir(message: types.Message, state: FSMContext):
            fullname = message.text
            await state.update_data(
                {"name": fullname}
            )
            await message.answer("Tug`ilgan sanangizni kiriting:\n(22.02.2022)")
            await PersonalData.next()

        @dp.message_handler(state=PersonalData.tugilgan_sana)
        async def answer_fullname(message: types.Message, state: FSMContext):
            tugilgan_sana = message.text
            await state.update_data(
                {"tugilgan_sana": tugilgan_sana}
            )
            await message.answer("Telefon raqamingizni kiriting:\n(+9989X 123-45-67)")
            await PersonalData.next()

        @dp.message_handler(state=PersonalData.phonenumber)
        async def answer_fullname(message: types.Message, state: FSMContext):
            phonenumber = message.text
            await state.update_data(
                {"phonenumber": phonenumber}
            )
            await message.answer("Manzilingizni kiriting:")
            await PersonalData.next()

        @dp.message_handler(state=PersonalData.manzil)
        async def answer_fullname(message: types.Message, state: FSMContext):
            manzil = message.text
            await state.update_data(
                {"yashash_manzili": manzil}
            )
            await message.answer("O`zingiz tanlanagan kurs nomimi kiriting:")
            await PersonalData.next()

        @dp.message_handler(state=PersonalData.kurslar)
        async def answer_fullname(message: types.Message, state: FSMContext):
            kurslar = message.text
            await state.update_data(
                {"kurslar": kurslar}
            )

            data = await state.get_data()
            name = data.get("name")
            tugilgan_sana = data.get("tugilgan_sana")
            phonenumber = data.get("phonenumber")
            yashash_manzil = data.get("yashash_manzili")
            kurslar = data.get("kurslar")

            msg = f"<b>Quyidagi ma`lumotlar qabul qilindi!</b>\n"
            msg += f"To`liq ismingiz - {name}\n\n"
            msg += f"Tug`ilgan sanangiz - {tugilgan_sana}\n\n"
            msg += f"Telefon raqamingiz - {phonenumber}\n\n"
            msg += f"Yashash manzilingiz - {yashash_manzil}\n\n"
            msg += f"Tanlagan kursingiz - {kurslar}\n\n"

            await message.answer(msg, parse_mode="HTML", reply_markup=royxatdan_otish)
            await state.finish()

    if message.text == "📝О нас":
        sarlavha = "<b>Краткая информация об образовательном центре Aim school</b>\n\n"
        sarlavha += "Наш образовательный центр начал свою работу 22 февраля 2022 года.\n"
        sarlavha += "Наш образовательный центр до сих пор предоставляет образование многим студентам.\n"
        sarlavha += "И вы можете получить абсолютно бесплатное обучение в учебном центре. Как?! спросите вы.\n"
        sarlavha += "В конце каждого месяца будет проходить тест на 100 баллов, основанный на полученных вами знаниях. " \
                    "а один студент, набравший на этих экзаменах более 90 баллов, может обучаться без уплаты очередного ежемесячного платежа\n\n"
        sarlavha += "* Молодые трудолюбивые и опытные преподаватели для подготовки студентов к экзаменам.\n"
        sarlavha += "* Единственная в Ходжаабадском районе подобная образовательная система .\n"
        sarlavha += "* Коворкинги для подготовки дополнительных уроков вне занятий.\n"
        sarlavha += "* Мониторинг и поощрение уровня знаний наших студентов.\n"
        sarlavha += "* Все это есть в нашем образовательном центре Aim school!!!\n\n"
        sarlavha += "<b> Aim school For better days😎!</b>"
        with open("photo_2022-10-26_23-05-57.jpg", "rb") as file:
            await message.answer_photo(caption=sarlavha, photo=file, parse_mode="HTML")

    elif message.text == "📚Курсы":
        await message.answer("О каком курсе вы хотите получить информацию?\n"
                             "Выберите один из следующих👇:",reply_markup=kurs_rus)
    elif message.text == "Aнглийский язык🇺🇸":
        sarlavha = "<b>Курс английского языка</b>\n\n"
        sarlavha += "Продолжительность наших курсов английского языка 120 минут, 3 дня в неделю, а также у нас есть дополнительные уроки.\n"
        sarlavha += "То есть дополнительные занятия проводятся и по воскресеньям.\n"
        sarlavha += "После того, как вы запишитесь на курс, вы пройдете тестирование и оцените ваш уровень знаний. " \
                        "И вы сможете продолжить с полученного уровня\n"
        sarlavha += "Наши квалифицированные преподаватели никогда не устают учить вас!\n"
        sarlavha += "Зарегистрируйтесь сейчас📋!\n"
        await message.answer_photo(caption=sarlavha, photo="https://www.studiocambridge.co.uk/wp-content/uploads/2020/10/Learn-English-Word-Cloud-1024x677.png", parse_mode="HTML")

    elif message.text == "Математика🧮":
        sarlavha = "<b>Курс математики</b>\n\n"
        sarlavha += "Продолжительность наших курсов математики составляет 120 минут, 3 дня в неделю, а также у нас есть дополнительные занятия.\n"
        sarlavha += "То есть дополнительные занятия проводятся и по воскресеньям\n"
        sarlavha += "По этому курсу можно подготовиться к государственным экзаменам и к любой олимпиаде.\n" \
                    "Мы подчеркиваем это потому, что наши ученики добиваются высоких результатов на олимпиадах.\n"
        sarlavha += "Зарегистрируйтесь сейчас📋!\n"
        await message.answer_photo(caption=sarlavha, photo="https://i0.wp.com/www.additudemag.com/wp-content/uploads/2021/09/GettyImages-1044168372.jpg?resize=480%2C270px&ssl=1", parse_mode="HTML")


    elif message.text == "Русский язык🇷🇺":
        sarlavha = "<b>Курс русского языка</b>\n\n"
        sarlavha += "Продолжительность наших курсов русского языка составляет 120 минут, 3 дня в неделю, а также у нас есть дополнительные занятия.\n"
        sarlavha += "То есть дополнительные занятия проводятся и по воскресеньям\n"
        sarlavha += "Наши уроки русского языка проводятся по новейшим современным методикам, благодаря которым вы легко разберетесь в любой теме.\n"
        sarlavha += "Зарегистрируйтесь сейчас📋!\n"
        await message.answer_photo(caption=sarlavha, photo="https://youlang.ru/storage/articles_img/HA2UdyA2dnFXiDJ49RY0M5LHanh9ZZyYFrDQmDWd.jpeg", parse_mode="HTML")

    elif message.text == "Главное меню🏠":
        await message.answer("Вы выбрали раздел главного меню✅!",reply_markup=bosh_menyu_rus)

    elif message.text == "🌐Наши социальные сети":
        await message.answer("Наши социальные сети👇:",reply_markup=ijtimoiy_rus)

    elif message.text == "⚙Языковые настройки":
        await message.answer("Выберите язык, который вам удобен👇", reply_markup=um_til_rus)

    elif message.text == "o`zbek - tili🇺🇿":
        await message.answer("Siz o`zbek tilini muaffaqiyatli tanladingiz✅!", reply_markup=bosh_menyu)

    elif message.text == "русский - язык🇷🇺":
        await message.answer("Вы успешно выбрали русский язык✅")

    elif message.text == "📍Адрес":
        await message.answer("Наш адрес: Андижанская область,\nХоджаабадский район\nОриентир: напротив Registon Fast Food.")
        await message.answer_location( latitude=40.66587, longitude=72.56190)

    elif message.text == "📋Регистрация":
        await message.answer("Вы уверены, что хотите зарегистрироваться?", reply_markup=da_net)

    @dp.callback_query_handler(lambda c: c.data == "net")
    async def yoq(call: types.callback_query):
        await bot.answer_callback_query(call.id)
        await bot.send_message(call.message.chat.id, "Вы можете выбрать любой другой раздел!",
                                   reply_markup=bosh_menyu_rus)

    @dp.callback_query_handler(lambda c: c.data == "da")
    async def ha(call: types.callback_query):
            await bot.answer_callback_query(call.id)
            await bot.send_message(call.message.chat.id, "Введите ваше ФИО:")
            await PersonalData_rus.next()

    @dp.message_handler(state=PersonalData_rus.fullname_rus)
    async def answer_fullname_rus(message: types.Message, state: FSMContext):
        fullname_rus = message.text
        await state.update_data(
            {"name_rus": fullname_rus}
        )
        await message.answer("Введите дату вашего рождения:\n(22.02.2022)")
        await PersonalData_rus.next()

    @dp.message_handler(state=PersonalData_rus.tugilgan_sana_rus)
    async def answer_fullname_rus(message: types.Message, state: FSMContext):
        tugilgan_sana_rus = message.text
        await state.update_data(
            {"tugilgan_sana_rus": tugilgan_sana_rus}
        )
        await message.answer("Введите свой номер телефона:\n(+9989X 123-45-67)")
        await PersonalData_rus.next()

    @dp.message_handler(state=PersonalData_rus.phonenumber_rus)
    async def answer_fullname_rus(message: types.Message, state: FSMContext):
        phonenumber_rus = message.text
        await state.update_data(
            {"phonenumber_rus": phonenumber_rus}
        )
        await message.answer("Введите свой адрес:")
        await PersonalData_rus.next()

    @dp.message_handler(state=PersonalData_rus.manzil_russ)
    async def answer_fullname_rus(message: types.Message, state: FSMContext):
        manzil_rus = message.text
        await state.update_data(
            {"yashash_manzili_rus": manzil_rus}
        )
        await message.answer("Введите название курса, который вы выбрали:")
        await PersonalData_rus.next()

    @dp.message_handler(state=PersonalData_rus.kurslar_rus)
    async def answer_fullname_rus(message: types.Message, state: FSMContext):
        kurslar_rus = message.text
        await state.update_data(
            {"kurslar_rus": kurslar_rus}
        )

        data = await state.get_data()
        name = data.get("name_rus")
        tugilgan_sana = data.get("tugilgan_sana_rus")
        phonenumber = data.get("phonenumber_rus")
        yashash_manzil = data.get("yashash_manzili_rus")
        kurslar = data.get("kurslar_rus")

        msg = f"<b>Была получена следующая информация!</b>\n"
        msg += f"Ваше ФИО - {name}\n\n"
        msg += f"Ваша дата рождения - {tugilgan_sana}\n\n"
        msg += f"Ваш номер телефона - {phonenumber}\n\n"
        msg += f"Ваш адрес проживания - {yashash_manzil}\n\n"
        msg += f"Выбранный вами курс - {kurslar}\n\n"

        await message.answer(msg, parse_mode="HTML", reply_markup=royxatdan_otish_rus)
        await state.finish()


        @dp.callback_query_handler(lambda c: c.data == "tasdiq_rus")
        async def tasdiq_rus(call: types.callback_query):
            await bot.answer_callback_query(call.id)
            await bot.send_message(call.message.chat.id,"Ваша информация успешно сохранена Мы свяжемся с вами!")
        await bot.send_message(chat_id=ADMIN_CHAT_ID, text=msg, parse_mode="HTML")

        @dp.callback_query_handler(lambda c: c.data == "tahrir_rus")
        async def tahrir_rus(call: types.callback_query):
            await bot.answer_callback_query(call.id)
            await message.answer("Введите ФИО:")
            await PersonalData_rus.next()

        @dp.message_handler(state=PersonalData_rus.fullname_rus)
        async def answer_fullname_rus(message: types.Message, state: FSMContext):
            fullname_rus = message.text
            await state.update_data(
                {"name_rus": fullname_rus}
            )
            await message.answer("Введите вашу дату рождения:\n(22.02.2022)")
            await PersonalData_rus.next()

        @dp.message_handler(state=PersonalData_rus.tugilgan_sana_rus)
        async def answer_fullname_rus(message: types.Message, state: FSMContext):
            tugilgan_sana_rus = message.text
            await state.update_data(
                {"tugilgan_sana_rus": tugilgan_sana_rus}
            )
            await message.answer("Введите свой номер телефона:\n(+9989X 123-45-67)")
            await PersonalData_rus.next()

        @dp.message_handler(state=PersonalData_rus.phonenumber_rus)
        async def answer_fullname_rus(message: types.Message, state: FSMContext):
            phonenumber_rus = message.text
            await state.update_data(
                {"phonenumber_rus": phonenumber_rus}
            )
            await message.answer("Введите свой адрес:")
            await PersonalData_rus.next()

        @dp.message_handler(state=PersonalData_rus.manzil_russ)
        async def answer_fullname(message: types.Message, state: FSMContext):
            manzil_rus = message.text
            await state.update_data(
                {"yashash_manzili_rus": manzil_rus}
            )
            await message.answer("Введите название курса, который вы выбрали:")
            await PersonalData_rus.next()

        @dp.message_handler(state=PersonalData_rus.kurslar_rus)
        async def answer_fullname(message: types.Message, state: FSMContext):
            kurslar_rus = message.text
            await state.update_data(
                {"kurslar_rus": kurslar_rus}
            )

            data = await state.get_data()
            name = data.get("name_rus")
            tugilgan_sana = data.get("tugilgan_sana_rus")
            phonenumber = data.get("phonenumber_rus")
            yashash_manzil = data.get("yashash_manzili_rus")
            kurslar =    data.get("kurslar_rus")

            msg = f"<b>Была получена следующая информация!</b>\n"
            msg += f"Ваше ФИО - {name}\n\n"
            msg += f"Твоя дата рождения - {tugilgan_sana}\n\n"
            msg += f"Ваш номер телефона - {phonenumber}\n\n"
            msg += f"Ваш адрес проживания - {yashash_manzil}\n\n"
            msg += f"Выбранный вами курс - {kurslar}\n\n"

            await message.answer(msg, parse_mode="HTML", reply_markup=royxatdan_otish_rus)
            await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)





