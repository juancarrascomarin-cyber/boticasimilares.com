# Checklist de activación — Asistente OTC

Este checklist debe completarse antes de habilitar el asistente OTC para un producto real.

## 1. Identidad del producto

- [ ] SKU interno único.
- [ ] Nombre comercial confirmado.
- [ ] Marca confirmada.
- [ ] Principio activo confirmado.
- [ ] Presentación exacta confirmada.
- [ ] Registro o identificador regulatorio consignado cuando corresponda.

## 2. Fuente oficial

- [ ] Fuente oficial identificada.
- [ ] URL HTTPS verificable.
- [ ] Fecha de consulta/actualización registrada.
- [ ] Información asociada exactamente a la presentación publicada.
- [ ] No se ha mezclado información de otra concentración o presentación.

## 3. Contenido permitido

- [ ] Indicaciones autorizadas cargadas.
- [ ] Instrucciones de uso autorizadas cargadas.
- [ ] Advertencias cargadas.
- [ ] Contraindicaciones cargadas.
- [ ] Condiciones de conservación cargadas.
- [ ] No existen afirmaciones promocionales presentadas como información sanitaria.
- [ ] No se añadieron usos no respaldados por la fuente validada.

## 4. Revisión

- [ ] `sourceVerified` = true.
- [ ] `contentVerified` = true.
- [ ] Responsable de revisión registrado.
- [ ] Fecha de revisión registrada.
- [ ] `validation.status` = `approved` solo después de completar lo anterior.

## 5. Asistente

- [ ] El asistente recibe el SKU exacto del producto.
- [ ] Responde únicamente con información validada de ese SKU.
- [ ] No diagnostica.
- [ ] No prescribe.
- [ ] No cambia tratamientos indicados por profesionales.
- [ ] Existe salida visible hacia atención humana/profesional.
- [ ] Se han probado preguntas ambiguas y casos de escalamiento.

## 6. Tienda

- [ ] La URL lleva a la ficha exacta del producto.
- [ ] La URL usa HTTPS.
- [ ] Precio y stock se gestionan en la tienda.
- [ ] La web institucional no duplica precio o stock si no existe sincronización confiable.

## 7. Publicación

- [ ] Producto aprobado.
- [ ] `publication.visible` solo se activa después de aprobación.
- [ ] `publication.assistantAvailable` solo se activa después de aprobación y pruebas.
- [ ] `publication.storeLinkAvailable` solo se activa si existe una URL de tienda válida.
- [ ] Validaciones automáticas terminan correctamente.

## 8. Mantenimiento

- [ ] Se definió cada cuánto revisar la fuente oficial.
- [ ] Se definió cómo retirar temporalmente una ficha si la información cambia.
- [ ] Se conserva historial de revisión y fecha de última actualización.

Este documento es un control técnico y operativo. La habilitación pública de un producto debe seguir también los procedimientos regulatorios y profesionales que correspondan.