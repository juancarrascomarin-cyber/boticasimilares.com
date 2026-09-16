# Catálogo OTC — estructura futura

Esta carpeta define cómo se conectará un producto OTC con información oficial, el asistente informativo y la futura tienda online.

## Flujo previsto

1. El producto se identifica por un `sku` único.
2. La ficha institucional conserva solo información objetiva y validada.
3. La información sanitaria debe indicar su fuente oficial y fecha de actualización.
4. Precio y stock permanecen bajo control de la tienda, no de la página institucional.
5. El botón de compra enlaza a la ficha exacta del producto en la tienda.
6. El asistente OTC recibe el `sku` exacto y responde únicamente con la información oficial asociada.
7. Si la pregunta excede ese alcance o requiere valoración clínica, se deriva a atención humana/profesional.

## Estados de control

Cada producto comienza como `draft`. Cargar una ficha no significa publicarla.

Para pasar a `approved` deben estar verificados tanto la fuente como el contenido, y deben constar el responsable y la fecha de revisión. Un producto no puede hacerse visible ni habilitarse para el asistente mientras no esté aprobado.

Si cambia la fuente oficial o la información autorizada, la ficha debe volver a revisión antes de continuar disponible para el asistente.

## Campos mínimos

- SKU
- nombre comercial
- marca
- principio activo
- presentación
- categoría
- imagen
- fuente oficial
- URL o referencia verificable de la fuente
- fecha de actualización
- registro o identificador regulatorio cuando corresponda
- indicaciones autorizadas
- advertencias
- contraindicaciones
- instrucciones de uso autorizadas
- conservación
- responsable y fecha de revisión
- URL exacta de compra cuando exista

## Reglas de seguridad

- No inferir que un producto es OTC: esa condición debe verificarse antes de su activación.
- No generar información sanitaria que no esté en la fuente validada.
- No mezclar información entre presentaciones, concentraciones o productos diferentes.
- No usar el catálogo para diagnosticar.
- No convertir una consulta general en prescripción personalizada.
- No recomendar iniciar, suspender o modificar un tratamiento prescrito.
- No mostrar precio o stock duplicado si la tienda es la fuente comercial oficial.
- Mantener trazabilidad de la fuente usada para cada respuesta.
- Ante dudas clínicas, señales de alarma o información insuficiente, derivar a atención humana/profesional.

## Puerta de activación

Antes de habilitar un producto real debe completarse `OTC_ACTIVATION_CHECKLIST.md` y las validaciones automáticas deben finalizar correctamente.

`otc-product.example.json` sirve únicamente como plantilla técnica y no representa un producto real.