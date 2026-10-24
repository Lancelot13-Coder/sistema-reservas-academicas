# Informe final — Sistema de reservas académicas

## 1. Objetivo
Construir una aplicación web para consultar espacios académicos, solicitar reservas y gestionar su aprobación, rechazo o cancelación.

## 2. Resultado implementado en el paquete
- Autenticación mediante Django.
- Roles de solicitante y gestor de espacios.
- Catálogo de espacios académicos.
- Solicitudes con fecha, horario y motivo.
- Estados y registro del responsable de revisión.
- Validación de solapamientos, fechas pasadas y horas válidas.
- Límite formal de cuatro horas consecutivas.
- Pruebas automatizadas de modelos, permisos y flujos principales.

## 3. Tecnologías
Python, Django, HTML/CSS, SQLite, Git y OpenSpec.

## 4. Verificación
**Estado de ejecución en el entorno de generación:** las pruebas Django no se ejecutaron aquí porque Django no estaba instalado y este entorno no pudo acceder a Internet para instalar dependencias. El proyecto incluye la suite para ejecutarla localmente. No se afirma que todas las pruebas hayan pasado hasta ejecutar `python manage.py test` en un entorno con las dependencias instaladas.

| Comprobación | Estado | Comando recomendado |
|---|---|---|
| Instalación de dependencias | Pendiente en PC destino | `pip install -r requirements.txt` |
| Comprobación Django | Pendiente | `python manage.py check` |
| Migraciones | Pendiente | `python manage.py migrate` |
| Pruebas automatizadas | Pendiente de ejecución local | `python manage.py test` |
| Prueba manual de login y roles | Pendiente | Seguir README.md |
| Revisión de seguridad para despliegue | Pendiente | `python manage.py check --deploy` |

## 5. Limitaciones conocidas
- Proyecto educativo, no endurecido para producción.
- SQLite se utiliza para desarrollo local; para uso concurrente productivo se recomienda evaluar PostgreSQL y mecanismos adicionales de integridad transaccional.
- El registro de espacios se realiza desde el administrador de Django.
- El flujo de aprobación es básico y no incorpora notificaciones por correo.

## 6. Conclusión
El paquete contiene la implementación y los artefactos necesarios para realizar la verificación final. La aceptación definitiva depende de instalar dependencias y ejecutar la batería de pruebas y los escenarios manuales en el computador de destino.
