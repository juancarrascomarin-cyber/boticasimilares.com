# Ruta de integraciones futuras

La web institucional de BOTICAS DEL DR JUAN se mantiene separada de los servicios transaccionales y de asistencia automatizada.

## Tienda online

La configuración se centraliza en `integrations.config.js`. La tienda permanece desactivada hasta contar con una URL definitiva y una plataforma aprobada.

Arquitectura prevista:

Web institucional -> Tienda online -> catálogo, precios, disponibilidad, carrito, compra, recojo o delivery.

La tienda puede alojarse en un servicio externo o, más adelante, en un subdominio dedicado. Cualquier cambio DNS debe preservar la configuración del correo corporativo.

Antes de activar la tienda se debe validar inventario, precios, condiciones de venta, privacidad, pagos, entrega, restricciones aplicables a medicamentos y experiencia móvil.

## Chatbot

La configuración del chatbot también se centraliza en `integrations.config.js` y permanece desactivada hasta seleccionar proveedor.

El asistente podrá ayudar con navegación, locales, horarios, preguntas frecuentes, acceso a la tienda y derivación a canales humanos.

No deberá diagnosticar, prescribir, modificar tratamientos ni interpretar por aproximación una receta o indicación que no pueda identificarse con seguridad. Debe ofrecer derivación a una persona cuando la consulta lo requiera.

## Principio de implementación

Las integraciones deben poder activarse o reemplazarse sin reconstruir la página institucional. La experiencia principal debe seguir siendo simple, accesible y con una salida clara hacia atención humana.
