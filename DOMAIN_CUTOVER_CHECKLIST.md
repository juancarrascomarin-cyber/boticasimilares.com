# Protocolo de conexión de boticasimilares.com

Este documento prepara el cambio de la web al dominio propio sin modificar todavía la zona DNS.

## Antes del cambio

- [ ] Acceder al administrador DNS legítimo del dominio.
- [ ] Tomar una copia o captura completa de los registros actuales.
- [ ] Identificar registros de correo y verificación existentes.
- [ ] No eliminar ni sustituir MX, SPF, DKIM, DMARC o verificaciones de Google por el cambio de la web.
- [ ] Confirmar que GitHub Pages continúa publicando correctamente la rama `main`.
- [ ] Confirmar que `boticasimilares.com` será el dominio canónico.
- [ ] Preparar tanto el dominio raíz como `www`.

## Cambio web

Los valores DNS concretos deben obtenerse de la configuración vigente de GitHub Pages en el momento del cambio. No deben copiarse valores antiguos o supuestos.

- [ ] Configurar el dominio personalizado en GitHub Pages.
- [ ] Añadir/modificar únicamente los registros necesarios para la web.
- [ ] Mantener intactos los registros de correo.
- [ ] Esperar la verificación DNS de GitHub.
- [ ] Activar HTTPS cuando GitHub confirme que el certificado está disponible.

## Pruebas obligatorias

- [ ] `https://boticasimilares.com` carga la web correcta.
- [ ] `https://www.boticasimilares.com` resuelve y llega al destino definido.
- [ ] No aparece advertencia de certificado.
- [ ] Navegación móvil funciona.
- [ ] WhatsApp de compras funciona.
- [ ] WhatsApp de orientación funciona.
- [ ] Mapas y teléfonos de locales funcionan.
- [ ] Se puede enviar correo desde una cuenta corporativa.
- [ ] Se puede recibir un correo externo en una cuenta corporativa.
- [ ] SPF/DKIM/DMARC no se modificaron accidentalmente.

## Reversión

Si la web falla pero el correo funciona, se revierte únicamente el cambio web usando la copia previa de los registros. No se modifica el correo para resolver un problema de publicación web.

## Regla de seguridad

Nunca solicitar ni almacenar en este repositorio contraseñas, PIN, códigos 2FA, claves privadas o credenciales del administrador del dominio.