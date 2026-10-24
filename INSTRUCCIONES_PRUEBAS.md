# Guía de pruebas y verificación final

## Preparar entorno
1. Crear entorno virtual e instalar `requirements.txt` siguiendo `README.md`.
2. Ejecutar `python manage.py check`.
3. Ejecutar `python manage.py migrate`.
4. Ejecutar `python manage.py test`.
5. Revisar las salidas y anotar los resultados reales en `INFORME_FINAL.md`.

## Pruebas manuales sugeridas
1. Crear superusuario y entrar al administrador.
2. Registrar dos espacios activos con códigos distintos.
3. Crear un usuario solicitante y un usuario gestor; asignar al segundo el rol “Gestor de espacios”.
4. Iniciar sesión como solicitante y crear una reserva futura de 60 minutos. Verificar estado pendiente.
5. Crear otra reserva que se solape en el mismo espacio/fecha; verificar que se rechaza.
6. Crear una reserva contigua al horario anterior; verificar que se permite.
7. Probar duración de 4 h exactas y después 4 h 1 min; la primera debe poder aceptarse y la segunda rechazarse.
8. Iniciar sesión como gestor y aprobar una solicitud pendiente.
9. Verificar que el solicitante no puede aprobar solicitudes ni consultar reservas de otro usuario.
10. Cancelar una reserva y verificar que el horario vuelve a estar disponible.

## Evidencia
Capturar la salida completa de `python manage.py test` y registrar número de pruebas, errores y fecha en `INFORME_FINAL.md`. No marcar pruebas como aprobadas antes de ejecutarlas.
