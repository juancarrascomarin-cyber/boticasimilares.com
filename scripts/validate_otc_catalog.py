#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "otc-product.example.json"

errors = []
warnings = []


def fail(message):
    errors.append(message)


def warn(message):
    warnings.append(message)


def is_https(value):
    try:
        return urlparse(value).scheme == "https"
    except Exception:
        return False


if not CATALOG.exists():
    fail("Falta catalog/otc-product.example.json")
else:
    try:
        product = json.loads(CATALOG.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"JSON inválido: {exc}")
        product = {}

    required_top = [
        "sku", "name", "brand", "activeIngredient", "presentation",
        "category", "officialInfo", "commerce", "assistant"
    ]
    for field in required_top:
        if field not in product:
            fail(f"Falta campo obligatorio: {field}")

    if product.get("category") != "otc":
        fail("La plantilla OTC debe usar category='otc'")

    official = product.get("officialInfo", {})
    required_official = [
        "sourceName", "sourceUrl", "registrationId", "updatedAt",
        "indications", "warnings", "contraindications",
        "approvedUseInstructions", "storage"
    ]
    for field in required_official:
        if field not in official:
            fail(f"Falta officialInfo.{field}")

    source_url = official.get("sourceUrl", "").strip()
    if source_url and not is_https(source_url):
        fail("officialInfo.sourceUrl debe usar HTTPS")

    commerce = product.get("commerce", {})
    if commerce.get("priceManagedByStore") is not True:
        fail("El precio debe estar gestionado por la tienda")
    if commerce.get("stockManagedByStore") is not True:
        fail("El stock debe estar gestionado por la tienda")

    store_url = commerce.get("storeUrl", "").strip()
    if store_url and not is_https(store_url):
        fail("commerce.storeUrl debe usar HTTPS")

    assistant = product.get("assistant", {})
    if assistant.get("enabled") is not False:
        fail("La plantilla de ejemplo debe mantener el asistente desactivado")
    if assistant.get("requireExactProductId") is not True:
        fail("El asistente debe exigir identificación exacta del producto")
    if assistant.get("allowOnlyOfficialInfo") is not True:
        fail("El asistente OTC debe limitarse a información oficial")
    if assistant.get("humanEscalationAvailable") is not True:
        fail("Debe existir una vía de derivación humana")

    if not official.get("sourceName", "").strip():
        warn("La plantilla no tiene aún una fuente oficial concreta")
    if not official.get("registrationId", "").strip():
        warn("La plantilla no tiene aún registro/identificador regulatorio")
    if not official.get("updatedAt", "").strip():
        warn("La plantilla no tiene aún fecha de actualización oficial")

print("VALIDACIÓN DEL CATÁLOGO OTC")
for message in warnings:
    print(f"ADVERTENCIA: {message}")
for message in errors:
    print(f"ERROR: {message}")

if errors:
    print(f"\nResultado: {len(errors)} error(es) y {len(warnings)} advertencia(s).")
    sys.exit(1)

print(f"\nResultado: OK, {len(warnings)} advertencia(s).")
