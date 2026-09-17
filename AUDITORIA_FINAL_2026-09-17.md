# Auditoría final institucional — BOTICAS DEL DR JUAN

Fecha: 17/09/2026  
Dominio auditado: https://boticasimilares.com/  
Repositorio: juancarrascomarin-cyber/boticasimilares.com  
Rama de auditoría: `auditoria-final-institucional`

## Resultado ejecutivo

La web institucional está técnicamente sólida y funcional. La auditoría confirma una base apta para producción, con mejoras aplicadas en accesibilidad y control de despliegue. Los puntos que no pueden cerrarse solo con código quedan identificados como validaciones empresariales o legales, sin inventar datos.

## 1. Marca e identidad

Verificado:
- La marca visible en `index.html` aparece como **BOTICAS DEL DR JUAN**.
- No se encontró la variante incorrecta **BOTICAS DEL DR. JUAN** en la página principal.
- Se identifica a **IDEAFAB S.A.** y el RUC **20606338806**.
- El dominio canónico institucional es `https://boticasimilares.com/`.
- La futura tienda `https://boticasdeldrjuan.com/` se mantiene separada de la web institucional.

## 2. Estructura y contenido

Verificado:
- Un único `<main>`.
- Un único `<h1>`.
- Navegación principal con Inicio, Nosotros, Servicios, Locales y Contacto.
- 7 distritos.
- 18 boticas.
- 18 enlaces únicos de Google Maps.
- 18 enlaces únicos de llamada.
- WhatsApp corporativo de compras/cotización/delivery: +51 990 993 246.
- WhatsApp de orientación/acompañamiento: +51 990 993 247.
- No hay formularios web ni cuentas de usuario.
- No hay pagos, catálogo, precios, stock ni carrito activos en la web institucional.

## 3. Accesibilidad

Verificado:
- Enlace “Saltar al contenido”.
- Estados `:focus-visible`.
- Soporte para `prefers-reduced-motion`.
- Botones principales con altura táctil suficiente.
- Texto base grande y diseño orientado a lectura sencilla.
- Navegación por `details/summary` para distritos y locales.

Correcciones aplicadas durante la auditoría:
- Se oscureció el color de acento para mejorar contraste sobre fondos claros.
- Se oscureció el verde de WhatsApp para mejorar contraste de texto blanco.
- Se aumentó el desplazamiento de anclas en móvil para evitar que la cabecera de dos filas tape títulos al navegar.

Pendiente de validación humana:
- Revisión visual final en dispositivos físicos o emuladores reales, especialmente 320–390 px y escritorio.
- Prueba manual completa con teclado y lector de pantalla.

## 4. SEO y buscadores

Verificado:
- `lang="es"`.
- `viewport` responsive.
- Meta descripción.
- `robots: index,follow`.
- Canonical a `https://boticasimilares.com/`.
- Open Graph y Twitter Card.
- Imagen social propia.
- Favicon.
- Marcado JSON-LD tipo `Organization`.
- `robots.txt` permite rastreo.
- `sitemap.xml` contiene la URL institucional principal.

Observación:
- La página de privacidad permanece con `noindex,follow`, por lo que no se incluye en el sitemap. Es consistente con su función actual.

## 5. Rendimiento

Inventario relevante:
- `index.html`: aproximadamente 67 KB.
- Logo web optimizado: aproximadamente 214 KB.
- Imagen social: aproximadamente 56 KB.
- Favicon: aproximadamente 29 KB.
- El PNG maestro de marca se conserva en el repositorio y no se usa como imagen principal visible.
- Solo se cargan dos instancias del logo en la página principal.
- No se cargan fotografías de 18 locales al inicio.

Resultado:
- No se detectó una carga de recursos innecesariamente pesada para una web institucional estática.

## 6. Seguridad y enlaces

Verificado:
- Los enlaces externos auditados usan HTTPS.
- Los enlaces con `target="_blank"` incluyen `noopener`.
- No hay formularios que envíen datos desde el sitio.
- No se almacenan claves, PIN, 2FA o credenciales en los archivos auditados.
- La tienda, chatbot, analítica, redes y asistente OTC permanecen desactivados por configuración.

Hallazgo de gobernanza:
- La rama `main` no tiene protección activa en GitHub.
- Esto no impide el funcionamiento del sitio, pero aumenta el riesgo de publicar cambios directos sin revisión.

## 7. CI/CD y publicación

Antes de la auditoría:
- La publicación a GitHub Pages se ejecutaba directamente al hacer `push` a `main`.
- La validación automática no cubría todos los pushes directos a `main`.

Corrección aplicada:
- El workflow de validación ahora incluye `main` y la rama de auditoría.
- El workflow de publicación ejecuta `scripts/validate_site.py` antes de desplegar.

Resultado:
- La validación automática de la rama de auditoría terminó correctamente.
- Con esta mejora, una publicación desde `main` deberá pasar por el validador antes de llegar a GitHub Pages.

## 8. Locales

La estructura actual contiene 18 boticas en:
- Ancón: 1
- Callao: 2
- Carabayllo: 1
- Comas: 7
- Los Olivos: 2
- Puente Piedra: 4
- San Martín de Porres: 1

Cada ficha contiene:
- dirección;
- referencia;
- horario;
- Google Maps;
- WhatsApp local;
- llamada;
- delivery corporativo.

Resultado técnico:
- La estructura está completa y consistente.

Validación empresarial pendiente:
- Confirmar que los 18 establecimientos siguen vigentes.
- Confirmar dirección, referencia, horario y teléfono de cada sede contra una fuente interna vigente.
- No se encontró en las fuentes internas conectadas un archivo maestro actualizado de locales.
- Fuentes públicas muestran variaciones históricas en nombres y algunas direcciones; no deben usarse para sobrescribir los datos del sitio sin confirmación interna.

## 9. Privacidad y datos personales

Estado actual:
- La web no recoge datos mediante formularios propios.
- El usuario puede salir a WhatsApp o Google Maps.
- La página de privacidad informa que recetas, fotografías o consultas farmacéuticas deben compartir solo la información necesaria.

Hallazgo:
- Para considerar la política de privacidad formalmente cerrada desde el punto de vista empresarial/legal, todavía deben definirse internamente:
  - canal oficial para ejercer derechos sobre datos personales;
  - finalidades documentadas del tratamiento por WhatsApp;
  - plazo o criterio de conservación;
  - responsables internos del tratamiento;
  - proveedores o transferencias que corresponda declarar;
  - procedimiento específico para información de salud/recetas.

Criterio de auditoría:
- No se inventaron estos datos ni se añadió un correo o responsable no autorizado.
- La página actual puede mantenerse como aviso informativo provisional, pero una política legal definitiva requiere validación interna.

## 10. Contenido farmacéutico

Verificado:
- La web evita interpretar recetas por aproximación cuando no son legibles.
- Separa el canal comercial del canal de orientación.
- No diagnostica ni prescribe dentro de la web.
- No activa el asistente OTC.
- No publica catálogo, precios o stock en la web institucional.
- La documentación futura del catálogo exige fuente oficial, identificación exacta del producto y revisión previa.

Resultado:
- La arquitectura actual reduce el riesgo de mezclar información institucional con información sanitaria o comercial no validada.

## 11. Fotografías y medios

Estado:
- La carpeta `media/` está preparada con convención de nombres, privacidad y criterios de optimización.
- Aún no contiene fotografías reales de locales.

Clasificación:
- No bloquea la operación de la web institucional.
- Sí limita el valor de SEO local, confianza visual y presentación de cada sede.

## 12. Páginas auxiliares

Verificado:
- `404.html` existe, está marcada `noindex` y permite volver al inicio.
- `privacidad.html` existe y permite volver al inicio.
- `robots.txt` y `sitemap.xml` están presentes.
- `CNAME` define `boticasimilares.com`.

## 13. Dominio y correo

La documentación del repositorio registra como completado:
- dominio personalizado;
- resolución del dominio raíz y `www`;
- HTTPS;
- continuidad de envío y recepción del correo corporativo;
- preservación de registros de correo durante el cambio.

Regla vigente:
- No modificar DNS, MX, SPF, DKIM, DMARC ni correo desde cambios de código del sitio.

## 14. Criterio de cierre de auditoría

### Cerrado técnicamente
- marca;
- estructura HTML;
- accesibilidad base;
- SEO técnico;
- mapas y enlaces estructurales;
- páginas auxiliares;
- rendimiento básico;
- seguridad de enlaces;
- separación institucional/tienda;
- controles de integración;
- validación automática;
- despliegue con validación previa.

### Requiere confirmación empresarial antes de llamarlo “cierre institucional definitivo”
1. Ficha maestra vigente de los 18 locales.
2. Política definitiva de privacidad y canal de ejercicio de derechos.
3. Revisión visual final en móvil/escritorio.
4. Decisión sobre protección de la rama `main`.
5. Incorporación de fotografías reales, si se desea elevar confianza y SEO local.

## Conclusión

**La auditoría técnica final está completada.**  
No se identificó un defecto técnico crítico que obligue a retirar la web. Los cambios de accesibilidad y control de despliegue preparados en esta rama son de bajo riesgo y deben integrarse tras pasar CI.

Los asuntos restantes son de validación empresarial, legal o editorial y no deben resolverse mediante suposiciones.
