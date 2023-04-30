# Импорт библиотеки
import sqlite3

# Подключение к БД
con = sqlite3.connect("akinator.db")

# Создание курсора
cur = con.cursor()


# Выполнение запроса и запись всех результатов
def inp(name, primary_attr, attack_type, legs):
    result = cur.execute(
        f"""INSERT INTO hero(name, primary_attr, attack_type, legs) VALUES("{name}", "{primary_attr}", "{attack_type}", "{legs}")""").fetchall()
    con.commit()


def take():
    result = cur.execute(
        f"""SELECT name, primary_attr, attack_type, legs FROM hero""").fetchall()
    return result


def take_gender_fmale():
    result = cur.execute(
        f"""SELECT name, primary_attr, attack_type, legs FROM hero WHERE gender =='fmale'""").fetchall()
    return result


def take_gender_male():
    result = cur.execute(
        f"""SELECT name, primary_attr, attack_type, legs FROM hero WHERE gender =='male'""").fetchall()
    return result


def search(ans12, ans22, ans32, ans42):
    result = cur.execute(
        f"""SELECT name FROM hero WHERE gender == '{ans12}' and (primary_attr == '{ans22}' or 'all') and 
        attack_type == '{ans32}' and legs == '{ans42}' """).fetchall()
    return result


def take_all():
    result = cur.execute(
        f"""SELECT * FROM hero""").fetchall()
    return result


def take_name():
    result = cur.execute(
        f"""SELECT name FROM hero""").fetchall()
    return result


def normal_name():
    name = take_name()
    ls = []
    for i in range(len(name)):
        ls.append(name[i][0])
    return ls


def naming(update, context):
    result = cur.execute(
        f"""SELECT primary_attr, attack_type, legs FROM hero WHERE name == {update.message.text}""").fetchall()
    return result


def take_info():
    result = cur.execute(
        f"""SELECT information FROM hero""").fetchall()
    return result


def take_info_hero(hero):
    result = cur.execute(
        f"""SELECT information FROM hero WHERE name == '{hero}'""").fetchone()
    return result
