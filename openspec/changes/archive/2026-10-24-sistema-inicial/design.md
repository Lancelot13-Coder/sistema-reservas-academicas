# Diseño: Sistema inicial de reservas académicas

- Monolito modular Django.
- Autenticación integrada de Django.
- Modelos `PerfilUsuario`, `Espacio` y `Reserva`.
- Formularios Django validan entrada; el modelo mantiene reglas de negocio.
- Vistas protegidas por autenticación y verificación de rol.
- SQLite para desarrollo y pruebas locales.
- Las reservas pendientes y aprobadas ocupan el horario; rechazadas y canceladas no lo bloquean.
