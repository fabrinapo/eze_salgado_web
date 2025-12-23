/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        patagonia: '#0B1016', // Deep Patagonia
        mist: '#E2E2E2',      // Primary Text
        clay: '#CD5D36',      // Accent (CTA)
        brass: '#C5A065',     // Detail Accent
        surface: '#1C242E',   // Secondary BG
        western: ['"Rye"', 'serif'], 
        sans: ['"Manrope"', 'sans-serif'],
      },
      fontFamily: {
        serif: ['"Cormorant Garamond"', 'serif'],
        sans: ['"Manrope"', 'sans-serif'], // Cambiamos Lato por Manrope
      },
      backgroundImage: {
        'fog-gradient': 'radial-gradient(circle at 50% 50%, rgba(28, 36, 46, 0.4) 0%, rgba(11, 16, 22, 0) 70%)',
      },
      animation: {
        'fade-in-up': 'fadeInUp 0.8s ease-out forwards',
      },
      keyframes: {
        fadeInUp: {
          '0%': { opacity: '0', transform: 'translateY(30px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        }
      }
    },
  },
  plugins: [],
}