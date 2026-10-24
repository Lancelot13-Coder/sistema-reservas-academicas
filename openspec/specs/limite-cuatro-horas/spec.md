# Especificación: Límite de cuatro horas

## Propósito
Limitar la duración consecutiva de una reserva académica.

## Requisitos
### Requisito: Duración máxima
El sistema DEBE rechazar reservas cuya duración sea superior a cuatro horas consecutivas y DEBE permitir una duración exacta de cuatro horas si el resto de las validaciones se cumple.

#### Escenario: Duración superior al máximo
- DADO un solicitante que registra un espacio libre
- CUANDO solicita una reserva de más de cuatro horas consecutivas
- ENTONCES el sistema rechaza la solicitud e informa la causa

#### Escenario: Duración exacta permitida
- DADO un solicitante que registra un espacio libre
- CUANDO solicita una reserva de exactamente cuatro horas
- ENTONCES la solicitud puede guardarse como pendiente
