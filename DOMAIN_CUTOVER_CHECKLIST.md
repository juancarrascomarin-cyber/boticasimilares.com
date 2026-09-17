# Protocolo de conexión de boticasimilares.com

Estado: completado y verificado el 17/09/2026.

## Antes del cambio

- [x] Acceder al administrador DNS legítimo del dominio.
- [x] Tomar una copia o captura completa de los registros actuales.
- [x] Identificar registros de correo y verificación existentes.
- [x] No eliminar ni sustituir MX, SPF, DKIM, DMARC o verificaciones de Google por el cambio de la web.
- [x] Confirmar que GitHub Pages continúa publicando correctamente la rama `main`.
- [x] Confirmar `boticasimilares.com` como dominio canónico.
- [x] Preparar tanto el dominio raíz como `www`.

## Cambio web

- [x] Configurar el dominio personalizado en GitHub Pages.
- [x] Modificar únicamente los registros necesarios para la web.
- [x] Mantener intactos los registros de correo.
- [x] Verificar DNS en GitHub Pages.
- [x] Activar HTTPS.

## Pruebas obligatorias

- [x] `https://boticasimilares.com` carga la web correcta.
- [x] `https://www.boticasimilares.com` resuelve y llega al dominio definido.
- [x] No aparece advertencia de certificado.
- [x] Se puede enviar correo desde una cuenta corporativa.
- [x] Se puede recibir un correo externo en una cuenta corporativa.
- [x] Los registros de correo permanecieron intactos durante el cambio.

## Controles que continúan vigentes

- No modificar registros DNS sin inventario previo.
- No almacenar contraseñas, PIN, códigos 2FA, claves privadas ni credenciales en el repositorio.
- Si una futura incidencia afecta solo a la web, no modificar el correo para resolverla.
- Mantener `boticasimilares.com` como dominio canónico mientras no exista una decisión empresarial distinta.
