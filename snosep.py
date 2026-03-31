#https://t.me/+O1F14zN8HPM0N2Fh
import random
import time
import os
import urllib.parse
import pycurl
from io import BytesIO
from colorama import init, Fore, Style

init(autoreset=True)

FIO = [
"Иванов Иван Иванович", "Сидоров Петр Алексеевич", "Смирнов Алексей Дмитриевич", "Волков Дмитрий Сергеевич", "Кузнецов Сергей Андреевич",
"Попов Андрей Михайлович", "Васильев Максим Петрович", "Соколов Артем Игоревич", "Михайлов Кирилл Владимирович", "Федоров Роман Александрович",
"Морозов Николай Викторович", "Егоров Игорь Павлович", "Козлов Олег Николаевич", "Павлов Павел Романович", "Степанов Вадим Денисович",
"Николаев Юрий Олегович", "Орлов Руслан Евгеньевич", "Андреев Антон Сергеевич", "Макаров Денис Ильич", "Никитин Виктор Борисович",
"Захаров Станислав Григорьевич", "Зайцев Михаил Федорович", "Соловьев Егор Юрьевич", "Борисов Арсений Андреевич", "Яковлев Лев Максимович",
"Поляков Марк Александрович", "Воронин Владислав Дмитриевич", "Семенов Данил Кириллович", "Григорьев Леонид Владиславович", "Аксенов Глеб Петрович",
"Тимофеев Тимур Алексеевич", "Романов Артур Игоревич", "Филиппов Григорий Олегович", "Щербаков Евгений Николаевич", "Титов Олег Вячеславович",
"Абрамов Ярослав Витальевич", "Калинин Семен Романович", "Кириллов Кирилл Даниилович", "Быков Анатолий Егорович", "Куликов Борис Артемович",
"Маслов Константин Ильич", "Плотников Илья Максимович", "Некрасов Аркадий Тимофеевич", "Жуков Геннадий Сергеевич", "Рубцов Савва Андреевич",
"Комаров Матвей Алексеевич", "Коновалов Захар Денисович", "Сафонов Игнат Павлович", "Белов Назар Владимирович", "Тарасов Егор Михайлович",
"Кудрявцев Артем Сергеевич", "Баранов Ян Александрович", "Кукушкин Юхим Петрович", "Чернов Аким Игоревич", "Шевцов Богдан Владимирович",
"Фролов Вацлав Дмитриевич", "Матвеев Герасим Андреевич", "Пономарев Демид Сергеевич", "Устинов Ефим Николаевич", "Мельников Заур Рамилевич",
"Денисов Ибрагим Русланович", "Гаврилов Клим Алексеевич", "Тихонов Лаврентий Борисович", "Князев Моисей Григорьевич", "Марков Нил Александрович",
"Якушев Остап Игоревич", "Кузьмин Даниил Павлович", "Ермаков Руслан Денисович", "Галкин Степан Викторович", "Лукин Аркадий Сергеевич",
"Наумов Виктор Андреевич", "Шарапов Валентин Олегович", "Белоусов Эдуард Кириллович", "Потапов Виталий Максимович", "Сорокин Альберт Романович",
"Журавлев Родион Федорович", "Богданов Святослав Ильич", "Колесников Платон Валерьевич", "Сергеев Всеволод Алексеевич", "Алексеев Марат Дмитриевич",
"Лебедев Арсен Константинович", "Козлов Ростислав Евгеньевич", "Новиков Филипп Андреевич", "Медведев Карен Артурович", "Беляев Давид Александрович",
"Рябов Иосиф Михайлович", "Власов Еремей Петрович", "Тарасов Лука Николаевич", "Емельянов Мирон Игоревич", "Гордеев Степан Владимирович",
"Никифоров Тарас Олегович", "Симонов Эльдар Равильевич", "Кудрявцев Ян Сергеевич", "Баранов Юхим Витальевич", "Кукушкин Аким Борисович",
"Чернов Данила Андреевич", "Шевцов Роман Петрович", "Фролов Денис Сергеевич", "Матвеев Виктор Александрович", "Пономарев Александр Владимирович"
]

PHONES = [
"+79011234567", "+79021234568", "+79031234569", "+79041234570", "+79051234571", "+79061234572", "+79071234573", "+79081234574", "+79091234575", "+79101234576",
"+79111234577", "+79121234578", "+79131234579", "+79141234580", "+79151234581", "+79161234582", "+79171234583", "+79181234584", "+79191234585", "+79201234586",
"+79211234587", "+79221234588", "+79231234589", "+79241234590", "+79251234591", "+79261234592", "+79271234593", "+79281234594", "+79291234595", "+79301234596",
"+79311234597", "+79321234598", "+79331234599", "+79341234600", "+79351234601", "+79361234602", "+79371234603", "+79381234604", "+79391234605", "+79401234606",
"+79411234607", "+79421234608", "+79431234609", "+79441234610", "+79451234611", "+79461234612", "+79471234613", "+79481234614", "+79491234615", "+79501234616",
"+79511234617", "+79521234618", "+79531234619", "+79541234620", "+79551234621", "+79561234622", "+79571234623", "+79581234624", "+79591234625", "+79601234626",
"+79611234627", "+79621234628", "+79631234629", "+79641234630", "+79651234631", "+79661234632", "+79671234633", "+79681234634", "+79691234635", "+79701234636",
"+79711234637", "+79721234638", "+79731234639", "+79741234640", "+79751234641", "+79761234642", "+79771234643", "+79781234644", "+79791234645", "+79801234646",
"+79811234647", "+79821234648", "+79831234649", "+79841234650", "+79851234651", "+79861234652", "+79871234653", "+79881234654", "+79891234655", "+79901234656",
"+79911234657", "+79921234658", "+79931234659", "+79941234660", "+79951234661", "+79961234662", "+79971234663", "+79981234664", "+79991234665", "+79001234666",
"+79011234667", "+79021234668", "+79031234669", "+79041234670", "+79051234671", "+79061234672", "+79071234673", "+79081234674", "+79091234675", "+79101234676",
"+79111234677", "+79121234678", "+79131234679", "+79141234680", "+79151234681", "+79161234682", "+79171234683", "+79181234684", "+79191234685", "+79201234686",
"+79211234687", "+79221234688", "+79231234689", "+79241234690", "+79251234691", "+79261234692", "+79271234693", "+79281234694", "+79291234695", "+79301234696",
"+79311234697", "+79321234698", "+79331234699", "+79341234700", "+79351234701", "+79361234702", "+79371234703", "+79381234704", "+79391234705", "+79401234706",
"+79411234707", "+79421234708", "+79431234709", "+79441234710", "+79451234711", "+79461234712", "+79471234713", "+79481234714", "+79491234715", "+79501234716",
"+79511234717", "+79521234718", "+79531234719", "+79541234720", "+79551234721", "+79561234722", "+79571234723", "+79581234724", "+79591234725", "+79601234726",
"+79611234727", "+79621234728", "+79631234729", "+79641234730", "+79651234731", "+79661234732", "+79671234733", "+79681234734", "+79691234735", "+79701234736",
"+79711234737", "+79721234738", "+79731234739", "+79741234740", "+79751234741", "+79761234742", "+79771234743", "+79781234744", "+79791234745", "+79801234746",
"+79811234747", "+79821234748", "+79831234749", "+79841234750", "+79851234751", "+79861234752", "+79871234753", "+79881234754", "+79891234755", "+79901234756",
"+79911234757", "+79921234758", "+79931234759", "+79941234760", "+79951234761", "+79961234762", "+79971234763", "+79981234764", "+79991234765", "+79001234766",
"+79011234767", "+79021234768", "+79031234769", "+79041234770", "+79051234771", "+79061234772", "+79071234773", "+79081234774", "+79091234775", "+79101234776",
"+79111234777", "+79121234778", "+79131234779", "+79141234780", "+79151234781", "+79161234782", "+79171234783", "+79181234784", "+79191234785", "+79201234786",
"+79211234787", "+79221234788", "+79231234789", "+79241234790", "+79251234791", "+79261234792", "+79271234793", "+79281234794", "+79291234795", "+79301234796",
"+79311234797", "+79321234798", "+79331234799", "+79341234800", "+79351234801", "+79361234802", "+79371234803", "+79381234804", "+79391234805", "+79401234806",
"+79411234807", "+79421234808", "+79431234809", "+79441234810", "+79451234811", "+79461234812", "+79471234813", "+79481234814", "+79491234815", "+79501234816"
]

EMAILS = [
"ivanov1@mail.ru", "sidorov2@yandex.ru", "smirnov3@gmail.com", "volkov4@bk.ru", "kuznetsov5@list.ru", "popov6@inbox.ru", "vasiliev7@protonmail.com", "sokolov8@yahoo.com", "mikhailov9@outlook.com", "fedorov10@rambler.ru",
"morozov11@mail.ru", "egorov12@yandex.ru", "kozlov13@gmail.com", "pavlov14@bk.ru", "stepanov15@list.ru", "orlov16@inbox.ru", "andreev17@protonmail.com", "makarov18@yahoo.com", "nikitin19@outlook.com", "zakharov20@rambler.ru",
"zaitsev21@mail.ru", "soloviev22@yandex.ru", "borisov23@gmail.com", "yakovlev24@bk.ru", "polyakov25@list.ru", "voronov26@inbox.ru", "semenov27@protonmail.com", "grigoriev28@yahoo.com", "aksenov29@outlook.com", "timofeev30@rambler.ru",
"romanov31@mail.ru", "voronin32@yandex.ru", "filippov33@gmail.com", "scherbakov34@bk.ru", "titov35@list.ru", "abramov36@inbox.ru", "kalinin37@protonmail.com", "kirillov38@yahoo.com", "bykov39@outlook.com", "kulikov40@rambler.ru",
"maslov41@mail.ru", "plotnikov42@yandex.ru", "nekrasov43@gmail.com", "zhukov44@bk.ru", "rubtsov45@list.ru", "komarov46@inbox.ru", "konovalov47@protonmail.com", "safonov48@yahoo.com", "belov49@outlook.com", "sobolev50@rambler.ru",
"karpov51@mail.ru", "lvov52@yandex.ru", "gusev53@gmail.com", "zverev54@bk.ru", "pastukhov55@list.ru", "lazarev56@inbox.ru", "fokin57@protonmail.com", "samsonov58@yahoo.com", "mironov59@outlook.com", "mukhin60@rambler.ru",
"dyachkov61@mail.ru", "konstantinov62@yandex.ru", "korolev63@gmail.com", "medvedev64@bk.ru", "belyaev65@list.ru", "ryabov66@inbox.ru", "vlasov67@protonmail.com", "tarasov68@yahoo.com", "emelyanov69@outlook.com", "gordeev70@rambler.ru",
"nikiforov71@mail.ru", "simonov72@yandex.ru", "kudryavtsev73@gmail.com", "baranov74@bk.ru", "kukushkin75@list.ru", "chernov76@inbox.ru", "shevtsov77@protonmail.com", "frolov78@yahoo.com", "matveev79@outlook.com", "ponomarev80@rambler.ru",
"ustinov81@mail.ru", "melnikov82@yandex.ru", "denisov83@gmail.com", "gavrilov84@bk.ru", "tihonov85@list.ru", "knyazev86@inbox.ru", "markov87@protonmail.com", "yakushev88@yahoo.com", "kuzmin89@outlook.com", "ermakov90@rambler.ru",
"galkin91@mail.ru", "lukin92@yandex.ru", "naumov93@gmail.com", "sharapov94@bk.ru", "belousov95@list.ru", "potapov96@inbox.ru", "sorokin97@protonmail.com", "zhuravlev98@yahoo.com", "bogdanov99@outlook.com", "kolesnikov100@rambler.ru",
"sergeev101@mail.ru", "alekseev102@yandex.ru", "lebedev103@gmail.com", "kozlov104@bk.ru", "novikov105@list.ru", "medvedev106@inbox.ru", "belyaev107@protonmail.com", "ryabov108@yahoo.com", "vlasov109@outlook.com", "tarasov110@rambler.ru",
"emelyanov111@mail.ru", "gordeev112@yandex.ru", "nikiforov113@gmail.com", "simonov114@bk.ru", "kudryavtsev115@list.ru", "baranov116@inbox.ru", "kukushkin117@protonmail.com", "chernov118@yahoo.com", "shevtsov119@outlook.com", "frolov120@rambler.ru",
"matveev121@mail.ru", "ponomarev122@yandex.ru", "ustinov123@gmail.com", "melnikov124@bk.ru", "denisov125@list.ru", "gavrilov126@inbox.ru", "tihonov127@protonmail.com", "knyazev128@yahoo.com", "markov129@outlook.com", "yakushev130@rambler.ru",
"kuzmin131@mail.ru", "ermakov132@yandex.ru", "galkin133@gmail.com", "lukin134@bk.ru", "naumov135@list.ru", "sharapov136@inbox.ru", "belousov137@protonmail.com", "potapov138@yahoo.com", "sorokin139@outlook.com", "zhuravlev140@rambler.ru",
"bogdanov141@mail.ru", "kolesnikov142@yandex.ru", "sergeev143@gmail.com", "alekseev144@bk.ru", "lebedev145@list.ru", "kozlov146@inbox.ru", "novikov147@protonmail.com", "medvedev148@yahoo.com", "belyaev149@outlook.com", "ryabov150@rambler.ru",
"vlasov151@mail.ru", "tarasov152@yandex.ru", "emelyanov153@gmail.com", "gordeev154@bk.ru", "nikiforov155@list.ru", "simonov156@inbox.ru", "kudryavtsev157@protonmail.com", "baranov158@yahoo.com", "kukushkin159@outlook.com", "chernov160@rambler.ru",
"shevtsov161@mail.ru", "frolov162@yandex.ru", "matveev163@gmail.com", "ponomarev164@bk.ru", "ustinov165@list.ru", "melnikov166@inbox.ru", "denisov167@protonmail.com", "gavrilov168@yahoo.com", "tihonov169@outlook.com", "knyazev170@rambler.ru",
"markov171@mail.ru", "yakushev172@yandex.ru", "kuzmin173@gmail.com", "ermakov174@bk.ru", "galkin175@list.ru", "lukin176@inbox.ru", "naumov177@protonmail.com", "sharapov178@yahoo.com", "belousov179@outlook.com", "potapov180@rambler.ru",
"sorokin181@mail.ru", "zhuravlev182@yandex.ru", "bogdanov183@gmail.com", "kolesnikov184@bk.ru", "sergeev185@list.ru", "alekseev186@inbox.ru", "lebedev187@protonmail.com", "kozlov188@yahoo.com", "novikov189@outlook.com", "medvedev190@rambler.ru",
"belyaev191@mail.ru", "ryabov192@yandex.ru", "vlasov193@gmail.com", "tarasov194@bk.ru", "emelyanov195@list.ru", "gordeev196@inbox.ru", "nikiforov197@protonmail.com", "simonov198@yahoo.com", "kudryavtsev199@outlook.com", "baranov200@rambler.ru",
"kukushkin201@mail.ru", "chernov202@yandex.ru", "shevtsov203@gmail.com", "frolov204@bk.ru", "matveev205@list.ru", "ponomarev206@inbox.ru", "ustinov207@protonmail.com", "melnikov208@yahoo.com", "denisov209@outlook.com", "gavrilov210@rambler.ru",
"tihonov211@mail.ru", "knyazev212@yandex.ru", "markov213@gmail.com", "yakushev214@bk.ru", "kuzmin215@list.ru", "ermakov216@inbox.ru", "galkin217@protonmail.com", "lukin218@yahoo.com", "naumov219@outlook.com", "sharapov220@rambler.ru",
"belousov221@mail.ru", "potapov222@yandex.ru", "sorokin223@gmail.com", "zhuravlev224@bk.ru", "bogdanov225@list.ru", "kolesnikov226@inbox.ru", "sergeev227@protonmail.com", "alekseev228@yahoo.com", "lebedev229@outlook.com", "kozlov230@rambler.ru",
"novikov231@mail.ru", "medvedev232@yandex.ru", "belyaev233@gmail.com", "ryabov234@bk.ru", "vlasov235@list.ru", "tarasov236@inbox.ru", "emelyanov237@protonmail.com", "gordeev238@yahoo.com", "nikiforov239@outlook.com", "simonov240@rambler.ru",
"kudryavtsev241@mail.ru", "baranov242@yandex.ru", "kukushkin243@gmail.com", "chernov244@bk.ru", "shevtsov245@list.ru", "frolov246@inbox.ru", "matveev247@protonmail.com", "ponomarev248@yahoo.com", "ustinov249@outlook.com", "melnikov250@rambler.ru"
]

def generate_violation_link(username, target_id):
    link_id = ''.join([random.choice('abcdef0123456789') for _ in range(8)])
    return f"t.me/telegram_reports/{link_id}?q={username}_{target_id}"

def get_complaint_text(username, target_id, template_type):
    link = generate_violation_link(username, target_id)
    
    templates = {
        "akc_doks": f"User @{username} (ID: {target_id}) is publishing doxing materials.\nHe posted my home address and passport photos.\nViolation link: {link}\nI ask to ban him immediately for violating privacy laws.",
        "akc_spam": f"User @{username} (ID: {target_id}) is sending massive spam every day.\nHe flooded my channel with ads and phishing links.\nViolation link: {link}\nThis is a violation of Telegram rules. Please block him.",
        "akc_scam": f"Account @{username} (ID: {target_id}) is a scammer.\nHe promised to sell me an iPhone but took my money and disappeared.\nViolation link: {link}\nI have screenshots. Many people complain about him.",
        "akc_narko": f"User @{username} (ID: {target_id}) runs a drug shop in Telegram.\nHe sells mephedrone and cocaine via private messages.\nViolation link: {link}\nHis channel promotes illegal substances. Ban this account.",
        "akc_prodazha": f"User @{username} (ID: {target_id}) sells stolen Telegram accounts and hacked data.\nHe offers stolen credit cards and PayPal logins.\nViolation link: {link}\nThis is clearly against Telegram ToS. Please suspend him.",
        "tgk_doks": f"Channel @{username} (ID: {target_id}) publishes personal data of people.\nThey posted my full name, address and workplace without consent.\nViolation link: {link}\nThis is doxing and harassment. Close this channel.",
        "tgk_narko": f"Channel @{username} (ID: {target_id}) is a drug marketplace.\nThey have links to darknet shops and contact for buying narcotics.\nViolation link: {link}\nViolation of Telegram rules and federal law. Please delete.",
        "tgk_prodazha": f"Channel @{username} (ID: {target_id}) sells illegal goods.\nThey offer fake passports, driving licenses and university diplomas.\nViolation link: {link}\nThis is fraud. Ban this channel immediately.",
        "bot_narko": f"Bot @{username} (ID: {target_id}) sells drugs via auto-reply.\nAnyone can order cocaine, LSD or marijuana through this bot.\nIt is a clear violation. Please block this bot.",
        "bot_glaz": f"Bot @{username} (ID: {target_id}) is a doxing tool called Eye of God.\nIt leaks personal data: passport, car number, phone, address.\nViolation link: {link}\nThis bot violates privacy laws. Remove it from Telegram.",
        "bot_spam": f"Bot @{username} (ID: {target_id}) sends spam to all users who start it.\nIt promotes crypto scams and fake giveaways.\nViolation link: {link}\nThousands of complaints. Delete this bot.",
        "bot_prodazha": f"Bot @{username} (ID: {target_id}) sells stolen data and hacked accounts.\nIt offers credit card dumps and access to mailboxes.\nViolation link: {link}\nThis is illegal. Ban this bot right now."
    }
    return templates.get(template_type, templates["akc_spam"])

def send_complaint(username, target_id, template_type, name, email, phone):
    msg = get_complaint_text(username, target_id, template_type)
    
    user_agents = [
        "Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 Chrome/124.0.6367.82 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 Chrome/123.0.6312.99 Mobile Safari/537.36",
        "Mozilla/5.0 (Android 14; Mobile; rv:120.0) Gecko/120.0 Firefox/120.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
    ]
    
    payload = urllib.parse.urlencode({
        'text': msg, 'name': name, 'email': email, 'phone': phone, 'setl': 'en'
    }).encode()
    
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, 'https://telegram.org/support')
    c.setopt(c.POSTFIELDS, payload)
    c.setopt(c.HTTPHEADER, [
        'User-Agent: ' + random.choice(user_agents),
        'Content-Type: application/x-www-form-urlencoded',
        'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language: en-US,en;q=0.9',
        'Origin: https://telegram.org',
        'Referer: https://telegram.org/support'
    ])
    c.setopt(c.SSL_VERIFYPEER, 1)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.TIMEOUT, 20)
    c.setopt(c.CONNECTTIMEOUT, 15)
    
    try:
        c.perform()
        status = c.getinfo(c.RESPONSE_CODE)
        c.close()
        return status == 200
    except:
        c.close()
        return False

def mass_report(username, target_id, template_type, count=250):
    print(f"\n{Fore.CYAN}Запуск {count} жалоб на {username} ({target_id})...")
    success = 0
    for i in range(count):
        name = FIO[i % len(FIO)]
        email = EMAILS[i % len(EMAILS)]
        phone = PHONES[i % len(PHONES)]
        if send_complaint(username, target_id, template_type, name, email, phone):
            success += 1
        print(f"[{i+1}/{count}] Успешно: {success}", end='\r')
        time.sleep(random.uniform(4, 8))
    print(f"\n{Fore.CYAN}Готово! Отправлено {success} из {count} жалоб.")
    input("Нажмите Enter...")

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def main():
    while True:
        clear()
        print(f"{Fore.GREEN}Бесплатный сносера - https://t.me/+O1F14zN8HPM0N2Fh")
        print("1. снос акк")
        print("2. снос тгк")
        print("3. снос ботов")
        print("4. сьебатся нахуй")
        
        choice = input("> ").strip()
        
        if choice == "1":
            username = input("Укажите @username цели: ").strip()
            target_id = input("Укажите ID цели: ").strip()
            clear()
            print("1. Докс\n2. Спам\n3. Скам\n4. Реклама наркошопа\n5. Продажа")
            choice2 = input("Выберите тему (1-5): ").strip()
            type_map = {"1":"akc_doks","2":"akc_spam","3":"akc_scam","4":"akc_narko","5":"akc_prodazha"}
            template_type = type_map.get(choice2, "akc_spam")
            mass_report(username, target_id, template_type, 250)
        elif choice == "2":
            username = input("Укажите @username канала: ").strip()
            target_id = input("Укажите ID канала: ").strip()
            clear()
            print("1. Докс\n2. Наркошоп\n3. Продажа")
            choice2 = input("Выберите тему (1-3): ").strip()
            type_map = {"1":"tgk_doks","2":"tgk_narko","3":"tgk_prodazha"}
            template_type = type_map.get(choice2, "tgk_doks")
            mass_report(username, target_id, template_type, 250)
        elif choice == "3":
            username = input("Укажите @username бота: ").strip()
            target_id = input("Укажите ID бота: ").strip()
            clear()
            print("1. Наркошоп (без ссылки)\n2. Глаз Бога (докс-бот)\n3. Спам\n4. Продажа краденого")
            choice2 = input("Выберите тему (1-4): ").strip()
            type_map = {"1":"bot_narko","2":"bot_glaz","3":"bot_spam","4":"bot_prodazha"}
            template_type = type_map.get(choice2, "bot_spam")
            mass_report(username, target_id, template_type, 250)
        elif choice == "4":
            print("Сьебывай.")
            break
        else:
            print(f"{Fore.RED}Неверный выбор. Введите 1, 2, 3 или 4.")
            time.sleep(1.5)

if __name__ == "__main__":
    main()