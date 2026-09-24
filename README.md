# BOTICAS DEL DR JUAN — sitio web

Sitio institucional y de atención para BOTICAS DEL DR JUAN, nombre comercial de los establecimientos operados por IDEAFAB S.A.

## Lineamientos que no deben romperse

- La marca debe escribirse siempre como **BOTICAS DEL DR JUAN**.
- El público principal incluye personas mayores de 50 años y familiares/cuidadores.
- La experiencia debe priorizar lectura clara, botones grandes, lenguaje sencillo y pocos pasos.
- El sitio no debe obligar a registrarse ni a descargar una aplicación para recibir atención.
- Compras, cotizaciones y delivery: WhatsApp `+51 990 993 246`.
- Orientación y acompañamiento: WhatsApp `+51 990 993 247`.
- No interpretar recetas por aproximación cuando una indicación no pueda identificarse con seguridad.
- Mantener la separación entre información comercial y orientación farmacéutica.
- No modificar DNS, correo corporativo ni configuración del dominio desde este repositorio.

## Estructura

- `index.html`: sitio principal.
- `404.html`: página de error amigable.
- `privacidad.html`: información sencilla sobre privacidad y servicios externos.
- `adesy-connect.html`: página pública de ADESY CONNECT usada como página principal de la aplicación OAuth.
- `privacidad-adesy-connect.html`: política de privacidad específica de ADESY CONNECT y su acceso a Google Drive.
- `robots.txt`: directivas para buscadores.
- `sitemap.xml`: mapa del sitio.
- `logo-dr-juan.png`: archivo original de la marca.
- `logo-dr-juan-web.webp`: versión optimizada para carga web.
- `favicon.png`: icono del sitio.
- `social-boticas-del-dr-juan.jpg`: imagen de vista previa para compartir la web.
- `scripts/validate_site.py`: validación automatizada de contenido y datos esenciales.
- `.github/workflows/validate-site.yml`: ejecuta la validación en GitHub Actions.

## ADESY CONNECT y OAuth

La configuración pública de OAuth de ADESY CONNECT utiliza páginas alojadas en este mismo dominio:

- Página principal: `https://boticasimilares.com/adesy-connect.html`
- Política de privacidad: `https://boticasimilares.com/privacidad-adesy-connect.html`
- Dominio autorizado: `boticasimilares.com`

La política describe el uso del alcance limitado de Google Drive `drive.file`. No ampliar los permisos OAuth ni modificar esa descripción sin revisar previamente la arquitectura real de ADESY CONNECT.

## Validación

Antes de publicar, GitHub Actions debe terminar correctamente. La validación comprueba, entre otros puntos:

- 7 distritos y 18 boticas.
- marca escrita correctamente.
- presencia de razón social y RUC.
- canales principales de WhatsApp.
- enlaces externos seguros.
- imágenes con texto alternativo.
- ausencia de errores básicos definidos en el script.

## Publicación

La rama `main` debe mantenerse estable. Los cambios grandes se preparan en una rama separada y se integran mediante Pull Request una vez aprobados visual y funcionalmente.
