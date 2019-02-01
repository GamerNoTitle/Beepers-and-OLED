@echo off
goto var
:sent
set /p file=Please Input Your File Place And its Name: 
python .\webrepl_cli.py %file% -p %pw% %ip%:%file%
goto sent
:var
set /p ip=Please Input Your Own(You Connected The device's WLAN)/Its(You And Your Device Connected the Same WLAN) Ip Address: 
set /p pw=Please Input Your Password: 
@echo Your Password is: %pw%
@echo Your Ip Address is: %ip%
set /p input=please confirm they are right, input yes to contiune or input no to change it: 
cls
if %input% == yes goto sent
if %input% == no goto var
exit