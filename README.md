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
- `robots.txt`: directivas para buscadores.
- `sitemap.xml`: mapa del sitio.
- `scripts/validate_site.py`: validación automatizada de contenido y datos esenciales.
- `.github/workflows/validate-site.yml`: ejecuta la validación en GitHub Actions.

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
