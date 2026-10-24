# Especificación: Reservas académicas

## Propósito
Permitir que usuarios autenticados soliciten espacios académicos y consulten el estado de sus reservas.

## Requisitos
### Requisito: Crear una solicitud
El sistema DEBE permitir que un usuario autenticado solicite un espacio activo indicando fecha, hora inicial, hora final y motivo. La solicitud nueva DEBE quedar en estado pendiente.

#### Escenario: Solicitud válida
- DADO un usuario autenticado y un espacio activo
- CUANDO envía una fecha futura o actual y un intervalo válido sin conflicto
- ENTONCES se registra una reserva pendiente asociada al usuario

### Requisito: Evitar solapamientos
El sistema DEBE rechazar solicitudes cuyo intervalo se cruce con otra reserva pendiente o aprobada del mismo espacio y fecha. Los intervalos contiguos sin intersección DEBEN permitirse.

#### Escenario: Horario ocupado
- DADO una reserva pendiente o aprobada en el mismo espacio y fecha
- CUANDO otra solicitud se solapa con su horario
- ENTONCES la nueva solicitud es rechazada

### Requisito: Revisar solicitudes
El sistema DEBE permitir a un gestor aprobar o rechazar solicitudes pendientes. Los solicitantes comunes NO DEBEN ejecutar estas acciones.

### Requisito: Control de acceso
El sistema DEBE permitir a un solicitante consultar sus propias reservas y DEBE impedirle consultar reservas ajenas. Gestores y administradores pueden consultar las reservas para su gestión.

### Requisito: Cancelar reservas
El sistema DEBE permitir cancelar reservas pendientes o aprobadas al solicitante propietario o a un gestor autorizado.

### Requisito: Validar fechas y horas
El sistema DEBE rechazar fechas pasadas y horarios cuyo final sea igual o anterior al inicio.
