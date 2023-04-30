import telebot
import glob

import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup
import random
from config import BOT_TOKEN

from date_b import take, search, take_info, normal_name, take_info_hero

# Логгирование пользователей и тд
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

# Все клавиатуры, которые используются
reply_keyboard = [['/akinator', '/victory'],
                  ['/information', '/memes']]
ans_keyboard = [['Да', 'Нет'], ['/stop'], ['/start']]
victory_keyboard = [['1', '2'], ['/stop']]
victory2_keyboard = [['1', '2'], ['3', '4'], ['/stop']]
victory3_keyboard = [['1', '2'], ['3', '4'], ['5', '6'], ['/stop']]
victory4_keyboard = [['1', '2'], ['3', '4', '5'], ['/stop']]
akinator1_keyboard = [['Мужчина', 'Женщина'], ['/start']]
stop_keyboard = [['/stop']]
info_keyboard = [['ID', 'Name'], ['/stop']]
mem_keyboard = [['Давай'], ['/stop']]
start_kb = [['/start']]

# Привязка клавиатур
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
markup2 = ReplyKeyboardMarkup(ans_keyboard, one_time_keyboard=False)
victory_markup = ReplyKeyboardMarkup(victory_keyboard, one_time_keyboard=False)
victory_markup2 = ReplyKeyboardMarkup(victory2_keyboard, one_time_keyboard=False)
victory_markup3 = ReplyKeyboardMarkup(victory3_keyboard, one_time_keyboard=False)
victory_markup4 = ReplyKeyboardMarkup(victory4_keyboard, one_time_keyboard=False)
stop_markup = ReplyKeyboardMarkup(stop_keyboard, one_time_keyboard=False)
start_markup = ReplyKeyboardMarkup(start_kb, one_time_keyboard=False)
question1 = ReplyKeyboardMarkup(akinator1_keyboard, one_time_keyboard=False)
id_name_keyboard = ReplyKeyboardMarkup(info_keyboard, one_time_keyboard=False)
memes_markup = ReplyKeyboardMarkup(mem_keyboard, one_time_keyboard=False)


# глобальные переменные
heroic = []
heroic2 = take()
info = take_info()
ans1 = ''
ans2 = ''
ans3 = ''
ans4 = ''
pers = ''
bot = telebot.TeleBot(BOT_TOKEN)


# Функция старта и экстренного возврата
async def start(update, context):
    user = update.effective_user
    await update.message.reply_html(
        rf"Приветствую, {user.mention_html()}! Я ДотаНатор - экскурсовод", reply_markup=markup)
    await update.message.reply_text("Давайте я Вас проведу по всем функциям\n"
                                    "/victory - это мини-игра где ты можешь узнать какой персонаж тебе больше подходит\n "
                                    "/memes - это мемы по дота-тематике (только попробуй не засмеяться!)\n "
                                    "/akinator - я не знаю кто это такой лучше спросите у него или разработчика\n"
                                    " /informations - найдет любого перса по имени или ID\n Дерзайте пробовать!!!")
    await update.message.reply_text("Чуть не забыл:\n НЕ ИСПОЛЬЗУЙТЕ\n /start где есть /stop просто доверьтесь мне")


# функция остановки действия
async def stop(update, context):
    user = update.effective_user
    await update.message.reply_html(
        rf"Приветствую, {user.mention_html()}! Я ДотаНатор - экскурсовод", reply_markup=markup)
    await update.message.reply_text("Давайте я Вас проведу по всем функциям\n"
                                    "/victory - это мини-игра где ты можешь узнать какой персонаж тебе больше подходит\n "
                                    "/memes - это мемы по дота-тематике (только попробуй не засмеяться!)\n "
                                    "/akinator - я не знаю кто это такой лучше спросите у него или разработчика\n"
                                    " /informations - найдет любого перса по имени или ID\n Дерзайте пробовать!!!")
    await update.message.reply_text("Чуть не забыл:\n НЕ ИСПОЛЬЗУЙТЕ\n /start где есть /stop просто доверьтесь мне")
    return ConversationHandler.END


# функция закрытия клавиатуры
async def close_keyboard(update, context):
    await update.message.reply_text("OK", reply_markup=ReplyKeyboardRemove())


# акинатор
async def akinator(update, context):
    user = update.effective_user
    await update.message.reply_html(
        rf"Приветствую, {user.mention_html()}, я акинатор! Я знаю всех персонажей доты! Не веришь? Проверяй скорее!!!",
        reply_markup=start_markup)
    await update.message.reply_text(
        "К сожалению мой разработчик немного кривор... Ладно не буду про него плохо говорить\n"
        "Но он еще не наделил меня сильным разумом и не показал мое обличие")
    await update.message.reply_text(
        "Насколько мне известно предрелиз меня же 2.06.2023\n"
        "Пока воспользуйитесь другими интересными функциями")
    # await update.message.reply_text("Какого пола Ваш персонаж?", reply_markup=question1)


# Функция подсказки по персонажу
async def victory(update, context):
    user = update.effective_user
    await update.message.reply_html(
        rf"Приветствую, {user.mention_html()}! Я ДотаПикер - помогу выбрать персонажа для следующей катки")
    await update.message.reply_text("Давайте посмотрим какой персонаж из игры Dota2 Вам больше всего подойдет?")
    await update.message.reply_text("Вы мальчик или девочка\n 1. Мальчик \n 2. Девочка", reply_markup=victory_markup)

    return 2


# Вопрос
async def question(update):
    await update.message.reply_text(
        "Какой жанр фильма Вы бы выбрали?\n 1.Боевик\n 2. Документальный\n 3. Ужасы\n 4. Фантастика\n 5.Криминал\n 6.Военный ",
        reply_markup=victory_markup3)


# обработка ответов
async def victory1(update, context):
    global ans1

    if update.message.text == '1':
        ans1 = 'male'
        await question(update)
        return 3

    elif update.message.text == '2':
        ans1 = 'fmale'
        await question(update)
        print(heroic)
        return 3
    else:
        await update.message.reply_text("Некорректный ответ! Попробуйте еще раз!")
        await update.message.reply_text("Вы мальчик или девочка\n 1. Мальчик \n 2. Девочка", reply_markup=victory_markup)
        return 2


# Вопрос
async def question2(update):
    await update.message.reply_text(
        "Какой вид спорта Вы больше предпочитаете?\n 1. Хоккей\n 2. Волейбол\n 3. Баскетбол\n 4. Большой/настольный тенис",
        reply_markup=victory_markup2)


# обработка ответов
async def victory2(update, context):
    global ans2

    if update.message.text == '1':
        ans2 = 'str'
        await question2(update)
        return 4

    elif update.message.text == '2':
        ans2 = 'int'
        await question2(update)
        return 4

    elif update.message.text == '3':
        ans2 = 'agi'
        await question2(update)
        return 4

    elif update.message.text == '4':
        ans2 = 'int'

        await question2(update)
        return 4

    elif update.message.text == '5':
        ans2 = 'agi'
        await question2(update)
        return 4

    elif update.message.text == '6':
        ans2 = 'str'
        await question2(update)
        return 4
    else:
        await update.message.reply_text("Некорректный ответ! Попробуйте еще раз!")
        await update.message.reply_text(
            "Какой жанр фильма Вы бы выбрали?\n 1.Боевик\n 2. Документальный\n 3. Ужасы\n 4. Фантастика\n 5.Криминал\n 6.Военный ",
            reply_markup=victory_markup3)
        return 3


# Вопрос
async def question3(update):
    await update.message.reply_text(
        "Кого бы Вы выбрали?:\n 1. Бабочка\n 2. Собака\n 3. Страус\n 4. Паук\n 5. Червяк",
        reply_markup=victory_markup4)


# обработка ответов
async def victory3(update, context):
    global ans3

    if update.message.text == '1':
        ans3 = 'Melee'
        await question3(update)
        return 5

    elif update.message.text == '2':
        ans3 = 'Ranged'

        await question3(update)
        return 5

    elif update.message.text == '3':
        ans3 = 'Melee'

        await question3(update)
        return 5

    elif update.message.text == '4':
        ans3 = 'Ranged'

        await question3(update)
        return 5

    else:
        await update.message.reply_text(
            "Какой вид спорта Вы больше предпочитаете?\n 1. Хоккей\n 2. Волейбол\n 3. Баскетбол\n 4. Большой/настольный тенис",
            reply_markup=victory_markup2)
        return 4


# Вывод персонажа если есть по параметрам
async def out_heroic(update):
    await update.message.reply_text(f"Ваш персонаж:\n {search(ans1, ans2, ans3, ans4)[0][0]}",
                                    reply_markup=stop_markup)
    chatId = update.message.chat.id
    pict = open(f'data/{search(ans1, ans2, ans3, ans4)[0][0]}.gif', 'rb')
    bot.send_photo(chatId, photo=pict)


# Вывод персонажа самого близкого по параметрам (в случае если нет точного персонажа)
async def another_heroic(update):
    num = random.randint(0, len(heroic2))
    await update.message.reply_text(f"Ваш персонаж:\n {heroic2[num][0]}",
                                    reply_markup=stop_markup)
    chatId = update.message.chat.id
    pict = open(f'data/{heroic2[num][0]}.gif', 'rb')
    bot.send_photo(chatId, photo=pict)
    await update.message.reply_text(f"{info[num][0]}\n")


# обработка ответов
async def victory4(update, context):
    global ans4
    global heroic2
    if update.message.text == '1':
        ans4 = '6'
        if len(search(ans1, ans2, ans3, ans4)) == 0:
            await another_heroic(update)
        else:
            await out_heroic(update)

        # return ConversationHandler.END

    elif update.message.text == '2':
        ans4 = '4'
        if len(search(ans1, ans2, ans3, ans4)) == 0:
            await another_heroic(update)
        else:
            await out_heroic(update)

        # return ConversationHandler.END

    elif update.message.text == '3':
        ans4 = '2'

        if search(ans1, ans2, ans3, ans4):
            await another_heroic(update)
        else:
            await out_heroic(update)

        # return ConversationHandler.END

    elif update.message.text == '4':
        ans4 = '8'
        if len(search(ans1, ans2, ans3, ans4)) == 0:
            await another_heroic(update)
        else:
            await out_heroic(update)

        # return ConversationHandler.END

    elif update.message.text == '5':
        ans4 = '0'

        if len(search(ans1, ans2, ans3, ans4)) == 0:

            await another_heroic(update)
        else:
            await out_heroic(update)

        # return ConversationHandler.END

    else:
        await update.message.reply_text("Некорректный ответ! Попробуйте еще раз!")
        await update.message.reply_text(
            "Кого бы Вы выбрали?:\n 1. Бабочка\n 2. Собака\n 3. Страус\n 4. Паук\n 5. Червяк",
            reply_markup=victory_markup4)
        return 5


# обработка ответов
async def victory_end(update, context):
    await update.message.reply_text("Кнопки были убранны не просто так :)")
    return ConversationHandler.END


# функция поиска персонажа
async def information(update, context):
    user = update.effective_user
    await update.message.reply_html(rf"Приветствую, {user.mention_html()}! Я бот ДотаФайндер!")
    await update.message.reply_text("Я найду по ID или имени любого персонажа и расскажу все что знаю")
    await update.message.reply_text("Поиск по ID или имени?", reply_markup=id_name_keyboard)
    return 2


async def information2(update, context):
    if update.message.text == 'ID' or update.message.text == 'id' or update.message.text == 'Id':
        await update.message.reply_text("Введите ID(от 1 до 124)", reply_markup=stop_markup)
        return 3

    elif update.message.text == 'Name':
        await update.message.reply_text("Введите имя", reply_markup=ReplyKeyboardRemove())
        return 4

    else:
        await update.message.reply_text("Хм...")
        await update.message.reply_text("По-моему Вы вводите что-то не то...")
        return 2


@bot.message_handler(content_types=['text'])
async def information3(update, context):
    chatId = update.message.chat.id
    if not (update.message.text.isalpha()) and 0 < int(update.message.text) < 125:
        await update.message.reply_text("Вот что я нашёл:", reply_markup=stop_markup)
        await update.message.reply_text(f"{heroic2[int(update.message.text) - 1][0]}\n")
        await update.message.reply_text(f"{info[int(update.message.text) - 1][0]}\n")
        pict = open(f'data/{heroic2[int(update.message.text) - 1][0]}.gif', 'rb')
        bot.send_photo(chatId, photo=pict)

    else:
        await update.message.reply_text("Хм...")
        await update.message.reply_text("По-моему Вы вводите что-то не то...")
        # return ConversationHandler.END


@bot.message_handler(content_types=['text'])
async def information4(update, context):
    chatId = update.message.chat.id
    if update.message.text in normal_name():
        await update.message.reply_text("Вот что я нашёл:", reply_markup=stop_markup)
        # await update.message.reply_text(f"{heroic2[int(update.message.text) - 1][0]}\n")
        await update.message.reply_text(f"{take_info_hero(update.message.text)[0]}\n")
        pict = open(f'data/{update.message.text}.gif', 'rb')
        bot.send_photo(chatId, photo=pict)


    else:
        await update.message.reply_text("Хм...")
        await update.message.reply_text("По-моему Вы вводите что-то не то...")


# функция вывода мемов
async def memes(update, context):
    await update.message.reply_text("Я могу показать тебе смешные картинки по Дота-тематике", reply_markup=memes_markup)
    return 2


async def memes2(update, context):
    if update.message.text == 'Давай':
        chatId = update.message.chat.id
        pict = open(random.choice(glob.glob('Mems/*.jpg')), 'rb')
        bot.send_photo(chatId, photo=pict)
        # return ConversationHandler.END


# главная функция
def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("akinator", akinator))
    application.add_handler(CommandHandler("close", close_keyboard))

    # сценарий для викторины
    conv_handler = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /start. Она задаёт первый вопрос.
        entry_points=[CommandHandler('victory', victory)],

        # Состояние внутри диалога.
        # Вариант с двумя обработчиками, фильтрующими текстовые сообщения.
        states={
            # Функция читает ответ на первый вопрос и задаёт второй.
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, victory)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, victory1)],
            # Функция читает ответ на второй вопрос и завершает диалог.
            3: [MessageHandler(filters.TEXT & ~filters.COMMAND, victory2)],
            4: [MessageHandler(filters.TEXT & ~filters.COMMAND, victory3)],
            5: [MessageHandler(filters.TEXT & ~filters.COMMAND, victory4)],
            6: [MessageHandler(filters.TEXT & ~filters.COMMAND, victory_end)]
        },
        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )
    application.add_handler(conv_handler)

    # сценарий для
    conv_handler_info = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /start. Она задаёт первый вопрос.
        entry_points=[CommandHandler("information", information)],

        # Состояние внутри диалога.
        # Вариант с двумя обработчиками, фильтрующими текстовые сообщения.
        states={
            # Функция читает ответ на первый вопрос и задаёт второй.
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, information)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, information2)],
            # Функция читает ответ на вопрос и завершает диалог.
            3: [MessageHandler(filters.TEXT & ~filters.COMMAND, information3)],
            4: [MessageHandler(filters.TEXT & ~filters.COMMAND, information4)]
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )

    application.add_handler(conv_handler_info)

    conv_handler_mem = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /start. Она задаёт первый вопрос.
        entry_points=[CommandHandler("memes", memes)],

        # Состояние внутри диалога.
        # Вариант с двумя обработчиками, фильтрующими текстовые сообщения.
        states={
            # Функция читает ответ на первый вопрос и задаёт второй.
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, memes)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, memes2)],
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )

    application.add_handler(conv_handler_mem)
    application.run_polling()


if __name__ == '__main__':
    main()
