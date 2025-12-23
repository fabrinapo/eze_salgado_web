// Estructura sugerida para Vue I18n
// npm install vue-i18n
import { createI18n } from 'vue-i18n';
import es from './locales/es.json';
import en from './locales/en.json';

const i18n = createI18n({
  legacy: false, // Usar Composition API
  locale: 'es', // idioma por defecto
  fallbackLocale: 'en',
  messages: {
    es,
    en
  }
});

export default i18n;

/* Ejemplo de es.json:
{
  "hero": {
    "title": "El sonido del viento...",
    "cta": "Contactar"
  }
}
*/