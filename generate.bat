@echo off
set /p name=Please Input Your File's Name(.png): 
py generate.py %name%
pause