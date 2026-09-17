# Etapa 4 — Crecimiento digital y futura tienda online

## Visión

BOTICAS DEL DR JUAN operará con dos activos digitales complementarios:

- `https://boticasimilares.com/` será la web institucional principal: marca, locales, servicios, preparados magistrales, orientación, contacto y contenidos corporativos.
- `https://boticasdeldrjuan.com/` se reservará como futura web store: catálogo, precios, stock, promociones, carrito y compra online.

Ambas propiedades deben enlazarse entre sí de forma clara, manteniendo responsabilidades distintas para evitar duplicidad de información y errores de precio o stock.

## Estrategia temporal para boticasdeldrjuan.com

Mientras la tienda aún no esté operativa, no se recomienda una redirección 301 permanente. El dominio debe conservarse disponible para su futura función comercial.

La solución temporal recomendada es una landing mínima con:

- marca BOTICAS DEL DR JUAN;
- mensaje breve indicando que la tienda online está en preparación;
- botón principal hacia `https://boticasimilares.com/`;
- sin precios, stock ni catálogo simulado;
- sin formularios complejos ni captura de datos innecesaria.

## Estrategia de navegación entre ambas webs

### Desde la web institucional

Cuando la tienda esté lista y validada, se activará un botón visible "Comprar online" que abra `https://boticasdeldrjuan.com/`.

### Desde la futura tienda

La tienda deberá incluir un acceso claro a la web institucional, por ejemplo:

- "Conoce BOTICAS DEL DR JUAN"
- "Nuestros locales y servicios"
- "Información institucional"

Todos estos accesos apuntarán a `https://boticasimilares.com/`.

## Regla de arquitectura

La web institucional no debe convertirse en fuente primaria de precio o stock. Estos datos deberán pertenecer a la tienda o a un backend comercial sincronizado. Esto reduce inconsistencias y facilita futuras integraciones con inventario, POS, delivery y campañas.

## Próximos frentes de trabajo

1. Preparar landing temporal para `boticasdeldrjuan.com` cuando se identifique su hosting actual.
2. Incorporar fotografías reales optimizadas de locales y equipo en la web institucional.
3. Reforzar SEO local por sede con datos verificados.
4. Definir arquitectura de tienda, catálogo, carrito y pagos.
5. Mantener chatbot, analítica, redes y asistente OTC desacoplados hasta su validación operativa y regulatoria.

## Criterio de seguridad

No activar funciones comerciales simuladas, no publicar stock o precios sin fuente confiable y no modificar dominios, DNS, correo o integraciones externas sin identificar primero el proveedor y la configuración vigente.