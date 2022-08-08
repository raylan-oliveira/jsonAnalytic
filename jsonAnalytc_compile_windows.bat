pyinstaller jsonAnalytic.py --onefile
rmdir build /q /s
del jsonAnalytic.spec /f /q /s
copy dist\jsonAnalytic.exe dist\jA.exe /y