window.BOTICAS_INTEGRATIONS = {
  store: {
    enabled: false,
    url: "https://boticasdeldrjuan.com/",
    institutionalUrl: "https://boticasimilares.com/",
    launchStatus: "prelaunch",
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
    requireApprovedProductBeforePublication: true,
    requireVerifiedSourceBeforeApproval: true,
    productFields: [
      "sku",
      "name",
      "brand",
      "activeIngredient",
      "presentation",
      "category",
      "image",
      "officialInfo",
      "validation",
      "publication",
      "commerce"
    ]
  },
  productExperience: {
    enabled: false,
    requireValidatedProductBeforeAssistant: true,
    requireApprovedProductBeforeVisibility: true,
    showOfficialSource: true,
    showOfficialInfoUpdatedAt: true,
    actions: {
      askAssistant: false,
      openStore: false,
      askHuman: true
    },
    humanSupportWhatsApp: "https://wa.me/51990993247?text=Hola%2C%20necesito%20orientaci%C3%B3n%20sobre%20un%20producto"
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
    requireApprovedProduct: true,
    requireVerifiedSource: true,
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
    enabled: true,
    facebook: "https://www.facebook.com/boticasdeldrjuan",
    instagram: "",
    tiktok: "https://www.tiktok.com/@boticasdeldrjuan",
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