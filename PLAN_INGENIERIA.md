# PLAN DE INGENIERÍA DE SOFTWARE
## Sistema de Gestión de Reservas de Espacios Académicos

**Proyecto:** Sistema de Gestión de Reservas Académicas  
**Asignatura:** Ingeniería de Software  
**Modalidad:** Individual  
**Estudiante:** [Nombre del estudiante]  
**Fecha:** [Fecha de elaboración]  
**Versión:** 1.0

---

## 1. Análisis del problema

### 1.1. Identificación de la problemática

Actualmente, la institución universitaria administra las reservas de laboratorios, auditorios y salas de cómputo mediante correos electrónicos y hojas de cálculo. Este procedimiento dificulta la centralización de la información y aumenta la posibilidad de errores durante la asignación de espacios.

Entre los principales problemas identificados se encuentran la duplicidad de solicitudes, los conflictos entre horarios, la falta de información actualizada sobre la disponibilidad de los espacios y las dificultades para consultar el historial de reservas.

Además, la aprobación de las solicitudes depende de procesos manuales que pueden ocasionar demoras y dificultades para realizar un seguimiento de las decisiones administrativas.

Por lo tanto, se propone desarrollar un sistema web que centralice la gestión de reservas y permita controlar la disponibilidad, las solicitudes, las aprobaciones y el historial de utilización de los espacios académicos.

### 1.2. Necesidades de la institución

El sistema deberá satisfacer las siguientes necesidades:

- Centralizar la información de los espacios académicos y las reservas.
- Permitir consultar la disponibilidad de los espacios por fecha y horario.
- Facilitar la creación, consulta y cancelación de solicitudes.
- Evitar conflictos entre reservas aprobadas.
- Permitir que los responsables administrativos aprueben o rechacen solicitudes.
- Gestionar usuarios, roles y permisos de acceso.
- Mantener un historial de las reservas y sus cambios de estado.
- Garantizar que las reglas de negocio se apliquen de manera consistente.
- Facilitar la verificación de requisitos mediante pruebas automatizadas.

### 1.3. Actores involucrados

**Usuario solicitante:** persona autorizada para consultar espacios y crear solicitudes de reserva. Puede consultar sus solicitudes, cancelar reservas según las reglas del sistema y revisar su historial.

**Administrador:** responsable de registrar, modificar, consultar y desactivar espacios académicos, así como administrar los usuarios y sus permisos.

**Responsable de aprobación:** persona autorizada para revisar las solicitudes pendientes y aprobarlas o rechazarlas, de acuerdo con la disponibilidad y las políticas institucionales.

**Institución universitaria:** entidad que establece las políticas de utilización de los espacios y los requisitos funcionales del sistema.

Para la primera versión, el administrador podrá tener también el permiso de aprobación, siempre que se defina así en la configuración de roles.

### 1.4. Alcance del sistema

La primera versión incluirá:

- Autenticación de usuarios.
- Administración de usuarios y roles.
- Gestión de laboratorios, auditorios y salas de cómputo.
- Consulta de disponibilidad por fecha y horario.
- Creación y seguimiento de solicitudes de reserva.
- Aprobación y rechazo de solicitudes.
- Cancelación de reservas.
- Historial de reservas.
- Prevención de conflictos de horarios.
- Restricción de máximo cuatro horas consecutivas por reserva.
- Pruebas automatizadas y documentación técnica.

### 1.5. Limitaciones

La primera versión será una aplicación web académica. No incluirá inicialmente aplicaciones móviles nativas, integración con sistemas institucionales externos, notificaciones por SMS, control físico de acceso a los espacios ni integración con calendarios institucionales.

Tampoco se implementarán algoritmos avanzados de optimización de horarios. La asignación se realizará mediante la consulta de disponibilidad y la aplicación de reglas de negocio definidas.

Las políticas institucionales no especificadas en el enunciado, como la anticipación máxima de las reservas o el tiempo límite para cancelarlas, deberán definirse explícitamente antes de su implementación.

---

## 2. Propuesta de solución

### 2.1. Descripción general

Se desarrollará una aplicación web que permita gestionar de manera centralizada las reservas de los espacios académicos.

Los usuarios podrán iniciar sesión, consultar espacios disponibles y enviar solicitudes con una fecha, una hora de inicio y una hora de finalización. El sistema validará los datos y comprobará que la solicitud cumpla las reglas de negocio.

Las solicitudes deberán pasar por un proceso de aprobación o rechazo. Una reserva aprobada no podrá entrar en conflicto horario con otra reserva aprobada del mismo espacio.

La aplicación también permitirá administrar espacios y usuarios, consultar historiales y mantener información organizada sobre el estado de cada solicitud.

### 2.2. Funcionalidades prioritarias

**Prioridad alta:**

1. Autenticación y autorización de usuarios.
2. Registro y administración de espacios académicos.
3. Consulta de disponibilidad.
4. Creación de solicitudes de reserva.
5. Validación de horarios y prevención de conflictos.
6. Aprobación y rechazo de solicitudes.

**Prioridad media:**

7. Cancelación de reservas.
8. Consulta del historial de reservas.
9. Administración de usuarios y roles.
10. Aplicación y verificación de la regla de máximo cuatro horas consecutivas.

**Prioridad de cierre:**

11. Pruebas automatizadas.
12. Documentación de instalación y ejecución.
13. Verificación de trazabilidad entre requisitos, código y pruebas.

La regla de cuatro horas se considera un requisito obligatorio de la entrega final. Su ubicación en la planificación no significa que pueda omitirse de la versión evaluada.

### 2.3. Organización del sistema en módulos

**Módulo de autenticación:** permite iniciar y cerrar sesión y controlar el acceso a las funcionalidades.

**Módulo de usuarios y roles:** administra las cuentas y determina las operaciones permitidas a cada usuario.

**Módulo de espacios:** registra los espacios académicos, su capacidad, su tipo y su estado de disponibilidad administrativa.

**Módulo de reservas:** gestiona las solicitudes, sus fechas, sus horarios y sus estados.

**Módulo de disponibilidad:** consulta las reservas existentes y detecta posibles conflictos de horarios.

**Módulo de aprobación:** permite aprobar o rechazar solicitudes y registrar la decisión correspondiente.

**Módulo de historial:** permite consultar las solicitudes y los cambios de estado de las reservas.

**Módulo de pruebas y calidad:** reúne las pruebas automatizadas para verificar las reglas de negocio y el funcionamiento de los módulos.

### 2.4. Desarrollo progresivo

El sistema se desarrollará mediante entregas incrementales:

- **Incremento 1:** estructura del proyecto, autenticación y permisos básicos.
- **Incremento 2:** modelos de datos y administración de espacios.
- **Incremento 3:** creación de solicitudes y consulta de disponibilidad.
- **Incremento 4:** aprobación, rechazo, cancelación e historial.
- **Incremento 5:** prevención de conflictos y validación del límite de cuatro horas.
- **Incremento 6:** pruebas integrales, documentación y cierre.

Antes de cada incremento se definirán y revisarán sus especificaciones. Ninguna funcionalidad se implementará únicamente a partir de una instrucción informal dirigida al agente de IA.

---

## 3. Decisiones de arquitectura y tecnología

### 3.1. Arquitectura seleccionada

Se utilizará una arquitectura monolítica modular con el patrón Modelo-Vista-Controlador, adaptado a la organización de Django mediante modelos, vistas y plantillas.

La aplicación se ejecutará como un único sistema web, con módulos separados por responsabilidad.

Esta arquitectura se selecciona porque reduce la complejidad de instalación y despliegue, facilita el desarrollo individual y permite mantener una separación clara entre la interfaz, la lógica de negocio y la persistencia de datos.

La estructura inicial será:

    sistema-reservas/
    ├── config/
    ├── usuarios/
    ├── espacios/
    ├── reservas/
    ├── templates/
    ├── static/
    ├── tests/
    ├── openspec/
    ├── PLAN_INGENIERIA.md
    ├── README.md
    ├── INFORME_FINAL.md
    ├── manage.py
    └── requirements.txt

La estructura definitiva podrá ajustarse según las convenciones del proyecto y las recomendaciones de OpenSpec.

### 3.2. Stack tecnológico

**Lenguaje:** Python. Se utilizará para implementar la lógica de negocio y las operaciones del backend.

**Framework:** Django. Proporciona autenticación, permisos, modelos, migraciones, formularios y herramientas de pruebas.

**Interfaz:** HTML, CSS y Django Templates. Permiten desarrollar una interfaz web sin incorporar un framework frontend adicional en la primera versión.

**Base de datos:** SQLite durante el desarrollo académico. Facilita la configuración local y permite persistir la información sin instalar un servidor de base de datos independiente.

**Control de versiones:** Git. Permitirá registrar los cambios, identificar su propósito y demostrar el orden de planificación, especificación e implementación.

**Repositorio remoto:** GitHub. Se utilizará para almacenar el código, la documentación y el historial de commits.

**Especificación:** OpenSpec. Se utilizará para definir requisitos, escenarios de aceptación, tareas y cambios funcionales.

**Pruebas:** framework de pruebas integrado de Django. Se utilizará para ejecutar pruebas unitarias, de integración y de regresión.

**Agente de IA:** una herramienta de programación asistida por IA compatible con el entorno de desarrollo. Su función será apoyar la generación de código, pruebas y documentación a partir de especificaciones revisadas.

Las versiones concretas de las dependencias se registrarán en el proyecto para favorecer la reproducibilidad del entorno.

### 3.3. Persistencia y modelo de datos

La información se almacenará en una base de datos relacional.

Se contemplan inicialmente las siguientes entidades:

- **Usuario:** identifica a cada usuario y sus permisos.
- **Espacio:** almacena el nombre, el tipo, la capacidad y el estado del espacio.
- **Reserva:** almacena el usuario solicitante, el espacio, la fecha, las horas de inicio y finalización y el estado.
- **Historial de reserva:** registra los cambios relevantes realizados sobre una solicitud.

Se utilizarán claves primarias, relaciones entre entidades, restricciones de integridad y validaciones para mantener la consistencia de los datos.

La autenticación aprovechará el sistema de usuarios de Django. Los roles podrán gestionarse mediante grupos y permisos, evitando desarrollar desde cero mecanismos de seguridad ya disponibles en el framework.

La validación de disponibilidad se implementará en la lógica de negocio. Se evaluarán mecanismos adicionales de integridad y concurrencia para impedir que dos solicitudes simultáneas terminen generando reservas incompatibles.

### 3.4. Comparación de decisiones técnicas

| Decisión | Alternativa seleccionada | Alternativa descartada | Justificación |
|---|---|---|---|
| Arquitectura | Monolítica modular | Microservicios | Reduce la complejidad de desarrollo, despliegue y depuración para un proyecto individual. |
| Backend | Django | Node.js con Express | Django incluye autenticación, ORM, permisos, administración y pruebas integradas. |
| Persistencia inicial | SQLite | PostgreSQL desde el inicio | Simplifica la configuración del entorno académico; se evaluará PostgreSQL para concurrencia y despliegues reales. |
| Interfaz | Django Templates | React con API independiente | Reduce la cantidad de tecnologías y la complejidad de integración. |
| Metodología de requisitos | SDD con OpenSpec | Desarrollo guiado solo por instrucciones directas a la IA | Facilita la trazabilidad y permite revisar los requisitos antes de implementar. |
| Control de cambios | Git con commits pequeños | Guardar únicamente la versión final | Permite demostrar la secuencia de trabajo y localizar errores introducidos durante el desarrollo. |

Estas decisiones son iniciales y deberán compararse con los resultados obtenidos durante la implementación. Cualquier modificación se documentará en el informe final.

---

## 4. Estrategia de desarrollo

### 4.1. Metodología de trabajo

Se aplicará Spec-Driven Development (SDD), una metodología en la que las especificaciones sirven como referencia principal para la implementación y la verificación del sistema.

El proceso seguirá esta secuencia:

1. Analizar el problema y documentar la planificación de ingeniería.
2. Registrar la planificación en Git mediante un commit independiente.
3. Inicializar OpenSpec y definir las especificaciones funcionales.
4. Revisar las especificaciones y corregir ambigüedades o contradicciones.
5. Definir las tareas de implementación.
6. Implementar cada funcionalidad con apoyo de un agente de IA.
7. Ejecutar las pruebas y revisar el código generado.
8. Gestionar las modificaciones mediante propuestas y especificaciones actualizadas.
9. Ejecutar las pruebas de regresión y documentar los resultados.

### 4.2. Etapas, dependencias y criterios de terminación

**Etapa 1. Planificación**

Dependencias: ninguna.

Criterio de terminación: documento de ingeniería completo, revisado y registrado en un commit independiente.

**Etapa 2. Especificaciones**

Dependencias: planificación terminada.

Criterio de terminación: requisitos claros, reglas de negocio documentadas, escenarios verificables, dependencias identificadas y revisión completada.

**Etapa 3. Estructura y usuarios**

Dependencias: especificaciones revisadas.

Criterio de terminación: proyecto ejecutable, autenticación funcional y permisos verificados.

**Etapa 4. Espacios académicos**

Dependencias: estructura y permisos básicos.

Criterio de terminación: operaciones de administración de espacios probadas y datos persistidos correctamente.

**Etapa 5. Reservas y disponibilidad**

Dependencias: usuarios, espacios y modelos de datos.

Criterio de terminación: solicitudes funcionales, conflictos detectados y decisiones de aprobación verificadas.

**Etapa 6. Gestión de cambios**

Dependencias: funcionalidades principales implementadas.

Criterio de terminación: propuesta de cambio revisada, especificaciones actualizadas, pruebas modificadas y límite de cuatro horas implementado y verificado.

**Etapa 7. Cierre**

Dependencias: implementación y pruebas completadas.

Criterio de terminación: pruebas ejecutadas, documentación completa, trazabilidad revisada y repositorio listo para su entrega.

### 4.3. Convenciones de Git

Se utilizarán commits pequeños y descriptivos para registrar las actividades del proyecto.

Ejemplos:

- `docs: agregar plan de ingeniería`
- `docs: definir especificaciones de reservas`
- `feat: implementar gestión de espacios`
- `feat: agregar validación de disponibilidad`
- `test: cubrir conflictos de horarios`
- `feat: limitar reservas a cuatro horas`
- `docs: completar informe final`

El primer commit deberá contener únicamente la planificación inicial y los archivos mínimos necesarios para documentarla.

Las especificaciones y el código se incorporarán en commits posteriores, respetando el orden exigido por la actividad.

---

## 5. Estrategia de calidad

### 5.1. Tipos de pruebas

**Pruebas unitarias:** verificarán reglas específicas, como validación de horarios, duración de reservas y permisos.

**Pruebas de integración:** comprobarán la interacción entre usuarios, espacios, reservas y persistencia de datos.

**Pruebas funcionales:** validarán los flujos completos de solicitud, aprobación, rechazo y cancelación.

**Pruebas de seguridad:** comprobarán que los usuarios no puedan ejecutar operaciones reservadas a otros roles ni modificar solicitudes ajenas sin autorización.

**Pruebas de concurrencia:** evaluarán solicitudes simultáneas para comprobar que no se produzcan reservas incompatibles sobre el mismo espacio.

**Pruebas de regresión:** verificarán que las nuevas modificaciones no dañen las funcionalidades existentes.

**Pruebas de aceptación:** comprobarán que los escenarios definidos en las especificaciones se cumplan desde la perspectiva de los usuarios.

### 5.2. Riesgos y estrategias de mitigación

| Riesgo | Impacto | Estrategia de mitigación |
|---|---|---|
| Reservas simultáneas incompatibles | Alto | Aplicar validaciones en la lógica de negocio y evaluar transacciones, restricciones e integración con PostgreSQL para escenarios concurrentes. |
| Errores en los permisos | Alto | Definir roles explícitos y probar accesos autorizados y no autorizados. |
| Requisitos ambiguos | Alto | Revisar las especificaciones antes de implementar y documentar las reglas no definidas por la institución. |
| Código incorrecto generado por IA | Alto | Revisar cada cambio, ejecutar pruebas y contrastar la implementación con los requisitos. |
| Pérdida o inconsistencia de datos | Alto | Utilizar migraciones, restricciones de integridad y copias de seguridad cuando corresponda al entorno. |
| Regresiones al introducir el límite de cuatro horas | Medio-alto | Crear pruebas de regresión y validar las funcionalidades de reservas existentes. |
| Configuración incorrecta del entorno | Medio | Documentar dependencias, versiones y pasos de instalación. |
| Falta de trazabilidad | Alto | Relacionar requisitos, tareas, cambios de código y pruebas, y mantener commits descriptivos. |

### 5.3. Mecanismos de verificación

El cumplimiento de requisitos se comprobará mediante una matriz de trazabilidad que relacione cada requisito con su especificación, implementación y prueba.

Cada requisito deberá contar con uno o varios escenarios de aceptación verificables. Las pruebas automatizadas proporcionarán evidencia de los resultados obtenidos.

Antes de considerar terminada una funcionalidad se comprobará que:

- La especificación haya sido revisada.
- El código respete la arquitectura definida.
- Las pruebas relacionadas se ejecuten correctamente.
- Los permisos y las reglas de negocio se cumplan.
- Los cambios estén registrados en Git.
- La documentación se encuentre actualizada.

Los resultados de las pruebas se registrarán para que puedan revisarse durante la sustentación.

---

## 6. Uso de SDD e inteligencia artificial

### 6.1. Utilización de OpenSpec

OpenSpec se utilizará para mantener las especificaciones del sistema y gestionar los cambios de manera controlada.

Después de aprobar el presente plan, se inicializará OpenSpec y se elaborarán las especificaciones correspondientes a usuarios, espacios, roles, reservas, disponibilidad, aprobación, cancelación e historial.

Cada especificación incluirá requisitos, restricciones y escenarios de aceptación que puedan comprobarse mediante pruebas.

Las propuestas de cambio permitirán documentar nuevas necesidades, analizar su impacto, definir tareas y actualizar las especificaciones antes de modificar el código.

### 6.2. Transformación del plan en especificaciones

El plan de ingeniería define el alcance, la arquitectura, las prioridades y la estrategia de calidad. A partir de él se construirán requisitos más precisos y verificables.

Por ejemplo, la necesidad de prevenir conflictos se convertirá en un requisito que establezca que dos reservas aprobadas del mismo espacio no pueden tener horarios superpuestos.

La regla de máximo cuatro horas consecutivas se incorporará posteriormente como un cambio formal, con sus propios escenarios de aceptación y pruebas.

La planificación no sustituye las especificaciones detalladas: establece la base sobre la cual estas se elaborarán.

### 6.3. Actividades delegadas al agente de IA

El agente de programación podrá apoyar en:

- Generación de estructuras iniciales de archivos.
- Implementación de modelos, vistas y formularios.
- Elaboración de pruebas automatizadas.
- Identificación de posibles errores y problemas de diseño.
- Revisión de la correspondencia entre código y especificaciones.
- Actualización de documentación técnica.
- Propuestas de mejora y refactorización.

El agente deberá trabajar sobre requisitos previamente revisados. Sus resultados se considerarán propuestas que necesitan verificación, no código correcto por defecto.

### 6.4. Verificación del código generado

Antes de aceptar una modificación se revisará:

1. Su correspondencia con los requisitos.
2. El cumplimiento de la arquitectura y las convenciones del proyecto.
3. La validación de permisos y reglas de negocio.
4. La ausencia de errores evidentes y dependencias innecesarias.
5. La ejecución satisfactoria de las pruebas relacionadas.
6. El impacto sobre funcionalidades previamente implementadas.

Los errores encontrados deberán corregirse y comprobarse antes de registrar la modificación como terminada.

### 6.5. Responsabilidades del estudiante

El estudiante conservará la responsabilidad de analizar el problema, definir el alcance, justificar las decisiones técnicas, revisar las especificaciones, aprobar los cambios, evaluar el código generado y verificar las pruebas.

También será responsable de mantener la trazabilidad, documentar las dificultades y explicar las decisiones tomadas durante la sustentación.

La inteligencia artificial se utilizará como herramienta de apoyo, sin sustituir el criterio técnico ni la comprensión del sistema por parte del estudiante.

---

## 7. Gestión del cambio: límite de cuatro horas

La solicitud de impedir reservas superiores a cuatro horas consecutivas se gestionará como un cambio formal posterior a la implementación inicial.

Antes de modificar el código se analizarán las especificaciones afectadas, se definirá el comportamiento esperado y se documentarán los nuevos escenarios de aceptación.

La regla deberá comprobar que una solicitud cuya duración sea superior a cuatro horas sea rechazada, mientras que una solicitud de cuatro horas exactas pueda aceptarse si cumple las demás condiciones.

También se verificarán los casos de horarios inválidos, conflictos con otras reservas y solicitudes que no excedan el límite.

Después de aprobar las especificaciones actualizadas, se implementará el cambio y se ejecutarán las pruebas nuevas y las pruebas de regresión.

La validación se realizará en el backend para evitar que la regla pueda eludirse mediante modificaciones de la interfaz.

---

## 8. Conclusión de la planificación

La solución propuesta busca construir un sistema de reservas confiable, mantenible y verificable, adecuado para las necesidades académicas definidas.

La combinación de una arquitectura monolítica modular, Django, persistencia relacional, Git y OpenSpec permitirá desarrollar progresivamente las funcionalidades y documentar las decisiones de ingeniería.

El uso de Spec-Driven Development ayudará a reducir las ambigüedades y a mantener una relación verificable entre los requisitos, el código y las pruebas.

La planificación inicial servirá como referencia para evaluar las decisiones tomadas durante la implementación y documentar cualquier modificación en el informe final.

Este documento constituye la base técnica del proyecto y deberá completarse y registrarse en Git antes de inicializar OpenSpec o desarrollar funcionalidades.
