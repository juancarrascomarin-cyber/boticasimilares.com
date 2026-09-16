# Etapa 3 — Experiencia, crecimiento y preparación de dominio

## Objetivo

Convertir la base técnica de BOTICAS DEL DR JUAN en una experiencia digital simple, confiable y preparada para crecer, priorizando a personas mayores de 50 años, familiares/cuidadores y usuarios móviles.

## Principios

- Menos pasos y decisiones por pantalla.
- WhatsApp y atención humana siempre visibles.
- Texto legible, objetivos táctiles amplios y navegación comprensible.
- Nada de diagnósticos, prescripción automatizada ni interpretación aproximada de recetas.
- Rendimiento móvil antes que efectos visuales pesados.
- Fotografías reales y optimizadas antes que imágenes genéricas cuando estén disponibles.
- Integraciones externas desacopladas de la web institucional.
- Privacidad por defecto: analítica y píxeles desactivados hasta definir consentimiento y proveedor.

## Trabajo completado o preparado

### Experiencia y accesibilidad

La web ya incorpora navegación semántica, enlace para saltar al contenido, foco visible, controles amplios, diseño responsive y reducción de movimiento según preferencia del dispositivo. La tercera etapa conserva esos criterios y evita introducir interfaces complejas solo por tendencia.

### Conversión útil

Las acciones principales permanecen centradas en necesidades concretas: cotizar receta, orientación, medicamentos habituales, ubicación de boticas y contacto humano. La futura tienda debe ser una capa adicional, no un requisito para recibir ayuda.

### Contenido visual

`media/README.md` define la incorporación posterior de fotografías reales de locales, personal y atención. Las imágenes deben optimizarse para web, conservar originales por separado, tener texto alternativo útil y respetar autorización de personas fotografiadas.

### OTC y asistente

El catálogo OTC incluye estados de validación/publicación, fuente oficial, trazabilidad, revisión y bloqueo del asistente hasta aprobación. `catalog/OTC_ACTIVATION_CHECKLIST.md` es obligatorio antes de habilitar un producto real.

### Tienda, chatbot y redes

`integrations.config.js` mantiene estas capacidades desactivadas hasta disponer de proveedores, URLs, pruebas de privacidad y validación operativa. Precio y stock pertenecen a la tienda y no deben duplicarse en la web institucional sin sincronización confiable.

## Preparación para dominio

La web puede seguir funcionando en GitHub Pages mientras se prepara el dominio personalizado. El cambio de DNS se hará únicamente después de inventariar la zona DNS existente.

Reglas para el cambio:

1. No modificar MX ni registros asociados al correo corporativo.
2. Identificar y preservar SPF, DKIM, DMARC y verificaciones existentes.
3. Cambiar únicamente los registros necesarios para servir la web.
4. Configurar el dominio personalizado en GitHub Pages.
5. Verificar dominio raíz y `www`.
6. Activar HTTPS cuando GitHub confirme el certificado.
7. Probar web y correo antes de considerar cerrado el cambio.
8. Conservar un registro de los valores DNS anteriores para reversión.

## Tendencias adoptadas con criterio

- Diseño mobile-first y orientado a tareas.
- Progressive disclosure: mostrar primero lo esencial y ampliar detalles cuando el usuario lo solicita.
- Atención conversacional con salida humana clara.
- Contenido auténtico y local mediante fotografías reales.
- IA limitada por fuentes verificadas y contexto exacto del producto.
- Arquitectura desacoplada para comercio, redes y chatbot.
- Accesibilidad y reducción de carga cognitiva como parte del diseño, no como complemento.

## Tendencias que no se incorporan por defecto

No se añaden animaciones decorativas intensas, carruseles automáticos, pop-ups invasivos, registro obligatorio, reproducción automática, interfaces experimentales que oculten acciones principales ni IA clínica autónoma.

## Pendientes que requieren información externa o acceso administrativo

- Fotografías reales de los locales y equipo.
- Proveedor/URL de la futura tienda.
- Proveedor del chatbot si se decide activarlo.
- URLs oficiales de redes sociales.
- Productos OTC reales con fuentes oficiales validadas.
- Inventario DNS actual y acceso administrativo para anexar `boticasimilares.com` sin afectar el correo.

Estos pendientes no impiden cerrar la preparación técnica de la etapa 3; son datos o activaciones posteriores que requieren insumos reales.