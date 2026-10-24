# Plan de ingeniería — Sistema de reservas académicas

## 1. Objetivo
Desarrollar una aplicación web para consultar espacios académicos y gestionar solicitudes de reserva, con revisión por un gestor, control de conflictos horarios e historial.

## 2. Tecnologías
- Python y Django 5.2 LTS.
- Plantillas Django, HTML y CSS.
- SQLite para desarrollo y pruebas locales.
- Git/GitHub para control de versiones.
- OpenSpec con flujo `spec-driven` para especificaciones, diseño y tareas.
- Pruebas automatizadas con `django.test`.

## 3. Alcance funcional inicial
- Autenticación y roles solicitante/gestor.
- Catálogo de espacios académicos activos.
- Creación de solicitudes de reserva.
- Prevención de reservas solapadas para el mismo espacio y fecha.
- Estados pendiente, aprobada, rechazada y cancelada.
- Aprobación/rechazo por gestores y cancelación autorizada.
- Consulta del detalle e historial de reservas.

## 4. Cambio formal posterior
El límite máximo de cuatro horas consecutivas se trata como un cambio formal separado: se documenta, se actualizan especificaciones y después se incorpora a la implementación y las pruebas. La entrega final integra este cambio y debe rechazar duraciones superiores a cuatro horas, permitiendo cuatro horas exactas si no existe otro conflicto.

## 5. Arquitectura
Monolito modular Django. `config/` contiene la configuración del proyecto y `reservas/` concentra modelos, formularios, vistas, administración y pruebas. La autenticación utiliza el sistema integrado de Django.

## 6. Riesgos y límites
SQLite es adecuado para ejecución académica local, pero no se recomienda asumir que garantiza por sí solo todas las garantías de concurrencia de una instalación productiva. Para producción, evaluar PostgreSQL, transacciones y restricciones apropiadas. Configurar `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, HTTPS y respaldos antes de desplegar.

## 7. Criterios de aceptación
- Un usuario autenticado puede crear y consultar sus solicitudes.
- Un usuario no puede consultar reservas ajenas.
- Solo gestores pueden aprobar o rechazar.
- No se aceptan fechas pasadas, horas inválidas, conflictos ni reservas superiores a cuatro horas.
- Las pruebas automatizadas cubren reglas de negocio, permisos y flujos principales.
