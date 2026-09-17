#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

errors = []
warnings = []


def fail(message):
    errors.append(message)


def warn(message):
    warnings.append(message)


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.images = []
        self.districts = 0
        self.locations = 0
        self.title_depth = 0
        self.title_text = []
        self.meta = []
        self.html_lang = ""
        self.main_count = 0
        self.h1_count = 0

    @staticmethod
    def attrs_dict(attrs):
        return {k: (v or "") for k, v in attrs}

    def handle_starttag(self, tag, attrs):
        data = self.attrs_dict(attrs)
        if tag == "html":
            self.html_lang = data.get("lang", "")
        if data.get("id"):
            self.ids.append(data["id"])
        if tag == "a":
            self.links.append(data)
        elif tag == "img":
            self.images.append(data)
        elif tag == "meta":
            self.meta.append(data)
        elif tag == "main":
            self.main_count += 1
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "details":
            classes = set(data.get("class", "").split())
            if "district" in classes:
                self.districts += 1
            if "location" in classes:
                self.locations += 1
        elif tag == "title":
            self.title_depth += 1

    def handle_endtag(self, tag):
        if tag == "title" and self.title_depth:
            self.title_depth -= 1

    def handle_data(self, data):
        if self.title_depth:
            self.title_text.append(data.strip())


if not INDEX.exists():
    fail("Falta index.html")
else:
    text = INDEX.read_text(encoding="utf-8")
    parser = SiteParser()
    parser.feed(text)

    required_files = [
        "logo-dr-juan.png", "logo-dr-juan-web.webp", "favicon.png",
        "robots.txt", "sitemap.xml", "privacidad.html",
        "DOMAIN_CUTOVER_CHECKLIST.md", "ETAPA_3.md"
    ]
    for filename in required_files:
        if not (ROOT / filename).exists():
            fail(f"Falta {filename}")

    required_ids = {"contenido", "inicio", "servicios", "acompana", "nosotros", "locales", "contacto", "site-header"}
    missing_ids = sorted(required_ids.difference(parser.ids))
    if missing_ids:
        fail("Faltan IDs esenciales: " + ", ".join(missing_ids))

    duplicates = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
    if duplicates:
        fail("Hay IDs duplicados: " + ", ".join(duplicates))

    if parser.html_lang.lower() != "es":
        fail("El documento debe declarar lang='es'")
    if parser.main_count != 1:
        fail(f"Se esperaba un único elemento main y se encontraron {parser.main_count}")
    if parser.h1_count != 1:
        fail(f"Se esperaba un único H1 y se encontraron {parser.h1_count}")

    if parser.districts != 7:
        fail(f"Se esperaban 7 distritos y se encontraron {parser.districts}")
    if parser.locations != 18:
        fail(f"Se esperaban 18 boticas y se encontraron {parser.locations}")

    title = " ".join(part for part in parser.title_text if part).strip()
    if "BOTICAS DEL DR JUAN" not in title:
        fail("El título no contiene la marca BOTICAS DEL DR JUAN")

    descriptions = [m.get("content", "") for m in parser.meta if m.get("name", "").lower() == "description"]
    if not descriptions or len(descriptions[0].strip()) < 50:
        fail("Falta una meta descripción útil")

    viewports = [m.get("content", "") for m in parser.meta if m.get("name", "").lower() == "viewport"]
    if not viewports or "width=device-width" not in viewports[0]:
        fail("Falta viewport responsive")

    for image in parser.images:
        if not image.get("alt", "").strip():
            fail(f"Imagen sin texto alternativo: {image.get('src', '(sin src)')}")
        if not image.get("width") or not image.get("height"):
            warn(f"Imagen sin dimensiones explícitas: {image.get('src', '(sin src)')}")

    for link in parser.links:
        href = link.get("href", "").strip()
        if not href:
            fail("Hay un enlace sin href")
            continue
        if href == "#":
            fail("Hay un enlace con href='#'")
        if link.get("target") == "_blank":
            rel = set(link.get("rel", "").lower().split())
            if "noopener" not in rel:
                fail(f"Enlace externo sin noopener: {href}")
        if href.startswith("http"):
            scheme = urlparse(href).scheme
            if scheme != "https":
                fail(f"Enlace externo no HTTPS: {href}")

    required_fragments = [
        'class="skip-link"',
        ':focus-visible',
        'prefers-reduced-motion',
        'aria-label="Navegación principal"',
        'rel="canonical"',
        'application/ld+json',
        'privacidad.html'
    ]
    for fragment in required_fragments:
        if fragment not in text:
            fail(f"Falta control de experiencia/accesibilidad: {fragment}")

    if "color: ;" in text:
        fail("Se encontró una propiedad CSS vacía: color: ;")
    if "BOTICAS DEL DR. JUAN" in text:
        fail("Se encontró la marca con punto: BOTICAS DEL DR. JUAN")
    if "IDEAFAB S.A." not in text or "20606338806" not in text:
        fail("Faltan razón social o RUC en el contenido")
    if "51990993246" not in text:
        fail("Falta el WhatsApp de compras/cotizaciones/delivery")
    if "51990993247" not in text:
        fail("Falta el WhatsApp de orientación/acompañamiento")

    map_links = re.findall(r'https://maps\.app\.goo\.gl/[A-Za-z0-9_-]+', text)
    if len(set(map_links)) != 18:
        warn(f"Hay {len(set(map_links))} enlaces únicos de Google Maps; revisar que coincidan con las 18 boticas")

    tel_links = re.findall(r'href="tel:\+51\d{9}"', text)
    if len(tel_links) != 18:
        warn(f"Hay {len(tel_links)} enlaces de llamada; se esperaban 18")

print("VALIDACIÓN DEL SITIO")
for message in warnings:
    print(f"ADVERTENCIA: {message}")
for message in errors:
    print(f"ERROR: {message}")

if errors:
    print(f"\nResultado: {len(errors)} error(es) y {len(warnings)} advertencia(s).")
    sys.exit(1)

print(f"\nResultado: OK, {len(warnings)} advertencia(s).")
