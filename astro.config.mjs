// astro.config.mjs
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
   // Configuración condicional para el despliegue
  site: process.env.NODE_ENV === 'production'
    ? 'https://srnanu.github.io/AI-Code-Committer/' // URL en producción
    : 'http://localhost:4321',  // URL en desarrollo local

  base: process.env.NODE_ENV === 'production'
    ? '/AI-Code-Committer' // El subdirectorio del repositorio
    : '/', // La raíz para el desarrollo local
});
