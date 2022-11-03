@REM press enter after the CMD comes out
pause

@REM path
cd "E:\path-to-folder\folder-name>"

@REM if you want to change drive, if your cd above is C: you don't have to do this
E:

start "" python rollback-main.py
cmd /k
