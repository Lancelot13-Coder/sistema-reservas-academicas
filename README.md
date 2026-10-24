# Sistema de reservas académicas

Aplicación web educativa con Django para gestionar espacios y solicitudes de reserva. Incluye autenticación, roles de solicitante/gestor, estados de reserva, prevención de solapamientos y límite máximo final de cuatro horas consecutivas.

## Requisitos
- Python 3.10 o superior compatible con Django 5.2.
- `pip`.

## Instalación en Windows (CMD)
Desde la carpeta que contiene `manage.py`:

```cmd
py -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py check
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abre http://127.0.0.1:8000/. Inicia sesión con el superusuario creado. El administrador puede registrar espacios desde http://127.0.0.1:8000/admin/. Para probar el rol gestor sin superusuario, crea un usuario y cambia su perfil a “Gestor de espacios” en el administrador.

## Ejecutar pruebas
```cmd
python manage.py test
```

## Verificación adicional
```cmd
python manage.py makemigrations --check --dry-run
python manage.py check --deploy
```

`check --deploy` advertirá sobre valores de desarrollo, como `DEBUG=True` y la clave de prueba; esas advertencias son esperables en local y deben corregirse antes de producción.

## Funcionalidades
- Login/logout con autenticación de Django.
- Catálogo de espacios activos.
- Creación de solicitudes con fecha, horario y motivo.
- Estados pendiente, aprobada, rechazada y cancelada.
- Gestión por usuario con rol de gestor o personal administrativo.
- Prevención de solapamientos en espacios y fechas iguales.
- Validación de fecha pasada, hora final y duración máxima de cuatro horas.
- Pruebas de reglas de negocio y permisos.

## Notas de seguridad y producción
Esta versión es para uso académico local. Cambia `SECRET_KEY`, establece `DEBUG=False`, configura `ALLOWED_HOSTS`, HTTPS, cookies seguras, respaldos y una base de datos de producción antes de desplegar. SQLite no debe considerarse garantía suficiente frente a solicitudes concurrentes de alta carga; evalúa PostgreSQL para producción.

## OpenSpec
Los artefactos están en `openspec/`. Las carpetas archivadas documentan la implementación inicial y el cambio formal del límite de cuatro horas. Revisa las especificaciones antes de extender el sistema.
