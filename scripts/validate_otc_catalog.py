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
        "category", "officialInfo", "validation", "publication",
        "commerce", "assistant"
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

    validation = product.get("validation", {})
    allowed_statuses = {"draft", "review", "approved", "rejected"}
    if validation.get("status") not in allowed_statuses:
        fail("validation.status debe ser draft, review, approved o rejected")

    source_verified = validation.get("sourceVerified") is True
    content_verified = validation.get("contentVerified") is True
    if validation.get("status") == "approved":
        if not source_verified or not content_verified:
            fail("Un producto aprobado requiere fuente y contenido verificados")
        if not validation.get("reviewedBy", "").strip():
            fail("Un producto aprobado requiere reviewedBy")
        if not validation.get("reviewedAt", "").strip():
            fail("Un producto aprobado requiere reviewedAt")
        if not official.get("sourceUrl", "").strip():
            fail("Un producto aprobado requiere URL de fuente oficial")
        if not official.get("registrationId", "").strip():
            fail("Un producto aprobado requiere registro/identificador regulatorio")
        if not official.get("updatedAt", "").strip():
            fail("Un producto aprobado requiere fecha de actualización oficial")

    publication = product.get("publication", {})
    for field in ("visible", "assistantAvailable", "storeLinkAvailable"):
        if field not in publication or not isinstance(publication.get(field), bool):
            fail(f"publication.{field} debe existir y ser booleano")

    if publication.get("visible") and validation.get("status") != "approved":
        fail("Un producto visible debe estar aprobado")
    if publication.get("assistantAvailable"):
        if validation.get("status") != "approved":
            fail("El asistente solo puede estar disponible para productos aprobados")
        if not source_verified or not content_verified:
            fail("El asistente requiere fuente y contenido verificados")
    if publication.get("storeLinkAvailable") and not product.get("commerce", {}).get("storeUrl", "").strip():
        fail("storeLinkAvailable requiere commerce.storeUrl")

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
