@echo off
setlocal
echo === Comprobacion de Django ===
python manage.py check
if errorlevel 1 goto error
echo === Migraciones ===
python manage.py migrate
if errorlevel 1 goto error
echo === Pruebas automatizadas ===
python manage.py test
if errorlevel 1 goto error
echo === Verificacion terminada sin errores reportados por los comandos ===
pause
exit /b 0
:error
echo La verificacion reporto un error. Lee el mensaje anterior.
pause
exit /b 1
