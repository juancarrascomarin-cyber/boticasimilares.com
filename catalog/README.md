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

## Campos mínimos

- SKU
- nombre comercial
- marca
- principio activo
- presentación
- categoría
- imagen
- fuente oficial
- fecha de actualización
- registro o identificador regulatorio cuando corresponda
- indicaciones autorizadas
- advertencias
- contraindicaciones
- instrucciones de uso autorizadas
- conservación
- URL exacta de compra

## Reglas de seguridad

- No generar información sanitaria que no esté en la fuente validada.
- No usar el catálogo para diagnosticar.
- No convertir una consulta general en prescripción personalizada.
- No mostrar precio o stock duplicado si la tienda es la fuente comercial oficial.
- Mantener trazabilidad de la fuente usada para cada respuesta.

`otc-product.example.json` sirve únicamente como plantilla técnica y no representa un producto real.