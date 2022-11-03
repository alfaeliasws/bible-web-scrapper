# BIBLE WEB SCRAPPER WITH PYTHON.

## GETTING BIBLE FROM "https://www.bible.com/id/bible/306/{bible_book}.{bible_chapter}.{bible_version}"

* Change bible version in each python file, here I am using Terjemahan Baru (Indonesia)
* If you want you can assign the command to bat file and you can click-to-run after some editing
* If you want to see my example of simple bat you can check in /bat file
* Install python requirement (requirement.txt)
* You can push keyboard button and run it after assigning your AHK fle and run it (Install AHK first) - it will trigger the bat file, so you need to edit those example.ahk and bat file
* bibletracker.sql is the SQL file, import it to your database and you can connect
* Delete db_pass_env row and replace it with your own password in line 11 in each python file to match your db password and make sure that your database name is bible and your user in database is bible, or you can change the code in each python file
* Or you can use .env with python-dotenv with variable name DB_PASSWORD
* The result will be in .md file in the root of this folder
* Close the opened notepad to stop the code from running