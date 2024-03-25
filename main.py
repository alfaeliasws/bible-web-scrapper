from bs4 import BeautifulSoup
from dotenv import load_dotenv, find_dotenv
import mysql.connector
import requests
import subprocess
import os
import re

load_dotenv(find_dotenv())

db_pass_env = os.environ.get("DB_PASSWORD")

connection = mysql.connector.connect(
    host="localhost", database="bible", user="root", password=""
)
cursor = connection.cursor()

bible_chapter_mysql = (
    """SELECT bible_chapter, bible_book FROM bible where data = "main" """
)

cursor.execute(bible_chapter_mysql)

result = cursor.fetchall()

bible_chapter_result = result[0][0]
bible_book_result = result[0][1]

list = [
    ["Genesis", 50],
    ["Exodus", 40],
    ["Leviticus", 27],
    ["Numbers", 36],
    ["Deuteronomy", 34],
    ["Joshua", 24],
    ["Judges", 21],
    ["Ruth", 4],
    ["1 Samuel", 31],
    ["2 Samuel", 24],
    ["1 Kings", 22],
    ["2 Kings", 25],
    ["1 Chronicles", 29],
    ["2 Chronicles", 36],
    ["Ezra", 10],
    ["Nehemiah", 13],
    ["Esther", 10],
    ["Job", 42],
    ["Psalm", 150],
    ["Proverbs", 31],
    ["Ecclesiastes", 12],
    ["Song of Solomon", 8],
    ["Isaiah", 66],
    ["Jeremiah", 52],
    ["Lamentations", 5],
    ["Ezekiel", 48],
    ["Daniel", 12],
    ["Hosea", 14],
    ["Joel", 3],
    ["Amos", 9],
    ["Obadiah", 1],
    ["Jonah", 4],
    ["Micah", 7],
    ["Nahum", 3],
    ["Habakkuk", 3],
    ["Zephaniah", 3],
    ["Haggai", 2],
    ["Zechariah", 14],
    ["Malachi", 4],
    ["Matthew", 28],
    ["Mark", 16],
    ["Luke", 24],
    ["John", 21],
    ["Acts", 28],
    ["Romans", 16],
    ["1 Corinthians", 16],
    ["2 Corinthians", 13],
    ["Galatians", 6],
    ["Ephesians", 6],
    ["Philippians", 4],
    ["Colossians", 4],
    ["1 Thessalonians", 5],
    ["2 Thessalonians", 3],
    ["1 Timothy", 6],
    ["2 Timothy", 4],
    ["Titus", 3],
    ["Philemon", 1],
    ["Hebrews", 13],
    ["James", 5],
    ["1 Peter", 5],
    ["2 Peter", 3],
    ["1 John", 5],
    ["2 John", 1],
    ["3 John", 1],
    ["Jude", 1],
    ["Revelation", 22],
]

i = bible_book_result if bible_book_result < 67 else 1

title = list[i - 1][0]


def chapter():
    if bible_chapter_result == 22 and title == "Revelation":
        return 23
    elif bible_chapter_result + 1 == list[i - 1][1] + 1 and title != "Revelation":
        return 1
    else:
        return bible_chapter_result + 1


bible_chapter_result = chapter()


def book():
    global bible_chapter_result
    if bible_chapter_result == 23 and title == "Revelation":
        bible_chapter_result = 1
        return 1
    elif bible_chapter_result == 1:
        return i + 1
    else:
        return i


i = book()

title = list[i - 1][0]

update_mysql = f"""update bible set bible_book = {i}, bible_chapter = {bible_chapter_result} where data = "main" """

cursor.execute(update_mysql)
connection.commit()
cursor.close()
connection.close()


def bible_book_function():
    if i == 62 or i == 63 or i == 64:
        check = list[i - 1][0].replace(" ", "")[0:1]
        return f"{check}JN"
    elif i == 43:
        return "JHN"
    elif i == 22:
        return "SNG"
    elif i == 26:
        return "EZK"
    elif i:
        return list[i - 1][0].replace(" ", "")[0:3]
    else:
        return list[i - 1][0][0:3]


bible_book = bible_book_function()
bible_chapter = bible_chapter_result

# change bible version
bible_version = "TB"

# LINK = f"https://www.bible.com/bible/306/{bible_book}.{bible_chapter}.{bible_version}"
LINK = f"https://alkitab.sabda.org/bible.php?book={i}&chapter={bible_chapter}&tab=text&mode=print"
print(LINK)

r = requests.get(LINK)
page_parse = BeautifulSoup(r.text, "html.parser")
# search_results = page_parse.find("div",{"class":"ChapterContent_reader__UZc2K"}).find_all("span",{"class":["ChapterContent_heading__RjEme","ChapterContent_verse__jS6jM","ChapterContent_label__S_AvV"]})
search_results = page_parse.find("div", {"class": "texts"})
content = []
continuation = "false"

verse = 0

CLEANR = re.compile("<.*?>")


def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, "", raw_html)
    return cleantext


for i in search_results:
    temp = str(i)
    # if'<span class="ChapterContent_heading__RjEme">(' in temp:
    #     continuation = "true"
    #     continue
    # if'<span class="ChapterContent_heading__RjEme">)' in temp:
    #     continuation = "false"
    #     continue
    item = cleanhtml(str(i))
    item = item.replace("	", "")
    item = item.replace(
        "                                                                                                                                                                             ",
        "",
    )
    item = item.replace(
        "                                                                                                                ",
        "",
    )
    item = item.replace("                         ", "")
    # if '<span class="ChapterContent_verse__jS6jM v"' in temp:
    #     item = temp.replace('<span class="ChapterContent_verse__jS6jM v',"").replace('</span>',"")
    # if '<span class="ChapterContent_heading__RjEme">Tuhan' in temp:
    #     item = temp.replace('<span class="ChapterContent_heading__RjEme">',"").replace('</span>',"")
    # if ('<span class="ChapterContent_heading__RjEme">' in temp and '<span class="ChapterContent_heading__RjEme">Tuhan' not in temp):
    #     item = temp.replace('<span class="ChapterContent_heading__RjEme">',"\n### ").replace('</span>',"")
    # if 'v' in temp:
    #     verse = 1

    # if ('<span class="ChapterContent_verse__jS6jM"' in temp and '<span class="ChapterContent_verse__jS6jM"> ' not in temp ):
    #     item = temp.replace('<span class="ChapterContent_verse__jS6jM',"").replace('</span>',"")
    # if '<span class="label">' in temp:
    #     item = temp.replace('<span class="ChapterContent_heading__RjEme"',"\n \n").replace('</span>'," ")
    # if '<span class="ChapterContent_label__S_AvV">#</span>' in temp:
    #     continue

    # if item == " ":
    #     continue
    # if continuation == "true":
    #     continue
    # if continuation == "false":
    print(item)
    if "item" in vars():
        content.append(item)

f = open(f"{bible_book} {bible_chapter}.md", "w+")

f.write(f"# {title} {bible_chapter}")

for i in content:
    if i != "\n":
        f.write(str(i))
    elif i == "\n":
        f.write(i)

f.close()

subprocess.call(["notepad.exe", f"{bible_book} {bible_chapter}.md"])
