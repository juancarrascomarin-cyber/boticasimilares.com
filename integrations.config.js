window.BOTICAS_INTEGRATIONS = {
  store: {
    enabled: false,
    url: "",
    openInNewTab: true,
    buttonLabel: "Comprar online",
    description: "Consulta precios, disponibilidad y realiza tu compra en nuestra tienda online.",
    productRouteTemplate: "",
    categoryRouteTemplate: "",
    availabilityMode: "store-controlled"
  },
  catalog: {
    enabled: false,
    source: "",
    currency: "PEN",
    country: "PE",
    productIdField: "sku",
    allowPricesOnInstitutionalSite: false,
    allowStockOnInstitutionalSite: false,
    otcCategoryKey: "otc",
    productFields: [
      "sku",
      "name",
      "brand",
      "activeIngredient",
      "presentation",
      "category",
      "image",
      "officialInfoSource",
      "officialInfoUpdatedAt",
      "storeUrl"
    ]
  },
  chatbot: {
    enabled: false,
    provider: "",
    scriptUrl: "",
    widgetId: "",
    position: "bottom-right",
    fallbackWhatsApp: "https://wa.me/51990993247?text=Hola%2C%20necesito%20ayuda"
  },
  otcAssistant: {
    enabled: false,
    knowledgeMode: "official-sources-only",
    primarySource: "DIGEMID",
    requireExactProductId: true,
    showSourceAndUpdateDate: true,
    allowProductInformation: true,
    allowLabelIndications: true,
    allowApprovedWarnings: true,
    allowApprovedDosageInformation: true,
    allowPersonalizedDiagnosis: false,
    allowPrescriptionAdvice: false,
    allowTreatmentChanges: false,
    requireHumanEscalationForRedFlags: true,
    requireHumanEscalationForPregnancy: true,
    requireHumanEscalationForChildren: true,
    requireHumanEscalationForComplexComorbidities: true,
    fallbackWhatsApp: "https://wa.me/51990993247?text=Hola%2C%20quiero%20consultar%20sobre%20un%20producto%20de%20venta%20sin%20receta"
  },
  social: {
    enabled: false,
    facebook: "",
    instagram: "",
    tiktok: "",
    youtube: "",
    linkedin: "",
    x: "",
    threads: "",
    whatsappChannel: ""
  },
  socialCommerce: {
    enabled: false,
    facebookShopUrl: "",
    instagramShopUrl: "",
    tiktokShopUrl: "",
    campaignLandingBaseUrl: ""
  },
  tracking: {
    enabled: false,
    metaPixelId: "",
    tiktokPixelId: "",
    googleTagId: "",
    consentRequired: true
  }
};