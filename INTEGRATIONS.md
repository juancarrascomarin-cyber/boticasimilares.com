# Integraciones futuras de BOTICAS DEL DR JUAN

Este documento define cómo incorporar una tienda online externa y un chatbot sin acoplarlos al contenido principal del sitio.

## Tienda online

La web institucional seguirá siendo el punto de entrada de BOTICAS DEL DR JUAN. La tienda podrá vivir en una plataforma o aplicación diferente y se enlazará desde botones de compra mediante una URL configurable.

La configuración está centralizada en `integrations.config.js`.

Antes de activar la tienda se debe definir y validar:

- URL definitiva y dominio o subdominio.
- Catálogo, precios y disponibilidad mostrados al cliente.
- Flujo de carrito, pago, recojo y/o delivery.
- Identificación clara de quién realiza la venta.
- Condiciones, privacidad y tratamiento de datos aplicables.
- Medicamentos o productos que no deban incorporarse a un flujo de autoservicio.
- Mecanismo de atención humana cuando el cliente necesite ayuda.

La tienda no debe depender de cambios en el DNS del correo corporativo. Cualquier futuro subdominio debe planificarse sin alterar MX u otros registros críticos de correo.

## Chatbot

El chatbot se integrará como una capa independiente y desactivable. `integrations.config.js` reserva los datos del proveedor, script/widget y un canal de WhatsApp de respaldo.

Antes de activarlo se debe definir:

- Proveedor y tratamiento de datos.
- Objetivos permitidos: navegación, locales, horarios, estado o derivación de compra, preguntas frecuentes y orientación general.
- Escalamiento visible a una persona.
- Registro y revisión de conversaciones cuando legalmente corresponda.
- Mensajes de privacidad y límites de uso.

### Límite farmacéutico

El chatbot no debe diagnosticar, prescribir, modificar tratamientos ni adivinar información ilegible de una receta. Ante incertidumbre clínica, receta no identificable o situación que requiera juicio profesional, debe derivar a atención humana/profesional.

## Principio de arquitectura

La página institucional, la tienda y el chatbot deben poder evolucionar por separado. Una falla o cambio de proveedor de tienda/chatbot no debe impedir que el usuario encuentre locales, teléfonos, WhatsApp y la información institucional básica.
