# 📋 Guía de Clases CSS Disponibles para Generadores de IA

Esta guía describe todas las clases CSS predefinidas en `global.css` que puedes usar al generar nuevas herramientas.

## ✅ Clases Base (Usa siempre estas)

### Contenedores
- **`.tool-container`** - Contenedor principal de la herramienta
  - Incluye: padding, border, border-radius, background, animación fade-in
  - Uso: `<div class="tool-container">`

### Títulos y Descripción
- **`.tool-container h1`** - Título h1 dentro del contenedor
  - Incluye: Gradiente de colores, font-size 2.5rem, font-weight 900
  - Uso: `<h1>Mi Herramienta</h1>`

- **`.tool-container > p`** - Párrafo de descripción
  - Incluye: Color secundario, margin-bottom, font-size 1.1rem, line-height
  - Uso: `<p>Descripción de la herramienta</p>`

### Layout
- **`.tool-wrapper`** - Contenedor de dos columnas (formulario + resultados)
  - Incluye: `grid-template-columns: 1fr 1fr`, gap: 3rem
  - Uso: `<div class="tool-wrapper">`

- **`.form-container`** - Columna izquierda para formularios
  - Incluye: `flex-direction: column`, gap: 1.5rem
  - Uso: `<div class="form-container">`

- **`.results-container`** - Columna derecha para resultados
  - Incluye: `flex-direction: column`, gap: 1.5rem
  - Uso: `<div class="results-container">`

### Navegación
- **`.back-link`** - Link para volver a la página principal
  - Incluye: Font-weight 700, opacity 0.8, hover effect
  - Uso: `<a href={import.meta.env.BASE_URL} class="back-link">&larr; Volver</a>`

---

## 📝 Formularios

### Inputs
- **`.input-field`** - Clase para inputs y textareas
  - Incluye: Padding 0.8rem, border, background transparente, focus effects
  - Uso: `<input class="input-field" id="miInput">`

### Grupos de Input
- **`.input-group`** - Contenedor para label + input
  - Incluye: `flex-direction: column`, gap: 0.5rem
  - Uso:
    ```html
    <div class="input-group">
      <label>Mi Label</label>
      <input class="input-field" id="miInput">
    </div>
    ```

- **`.input-group label`** - Label dentro del input-group
  - Incluye: Font-weight 600, font-size 1rem
  - Uso: `<label>Mi Label</label>`

---

## 🔘 Botones

- **`.btn`** - Clase base para botones
  - Incluye: Padding 1rem 2rem, font-size 1.1rem, border-radius 8px, cursor pointer
  - Uso: `<button class="btn">Mi Botón</button>`

- **`.btn-primary`** - Botón de acción principal
  - Incluye: Gradiente de colores, color white, box-shadow, hover effect
  - Uso: `<button class="btn btn-primary" id="miBoton">Calcular</button>`

---

## 📊 Resultados

- **`.summary`** - Contenedor de resultados
  - Incluye: Gradiente background, border, padding 2rem, border-radius 12px
  - Uso: `<div class="summary">`

- **`.summary-item`** - Item individual dentro del summary
  - Incluye: `flex-direction: column`, gap: 0.5rem
  - Uso:
    ```html
    <div class="summary-item">
      <h4>Label del Resultado</h4>
      <p>$100.00</p>
    </div>
    ```

- **`.summary-item h4`** - Label del resultado
  - Incluye: Font-size 0.95rem, text-transform uppercase, letter-spacing
  - Uso: `<h4>Mi Resultado</h4>`

- **`.summary-item p`** - Valor del resultado
  - Incluye: Font-size 2rem, font-weight 900, color accent
  - Uso: `<p>$100.00</p>`

---

## 🎨 Clases Específicas (Agregadas por la IA si es necesario)

Si tu herramienta necesita estilos únicos que no están en global.css, puedes agregar un `<style>` scoped.

### Ejemplos de cuándo agregar estilos específicos:

1. **Layouts especiales** 
   - Ejemplo: `.calculator-wrapper { grid-template-columns: 300px 1fr; }`
   - Uso: Para un layout de calculadora (formulario estrecho + resultados amplios)

2. **Componentes únicos**
   - Ejemplo: `.palette-container`, `.color-swatch`, `.hex-code`
   - Uso: Para herramientas con paletas de colores o componentes especiales

3. **Estilos de contenido renderizado**
   - Ejemplo: `.prose h1`, `.prose code`, `.prose blockquote`
   - Uso: Para herramientas que renderizan HTML (markdown converters)

---

## 📱 Responsive

Todos los estilos base incluyen media queries para dispositivos móviles (`max-width: 768px`):
- `.tool-wrapper` → `grid-template-columns: 1fr`
- `.tool-container` → `padding: 1.5rem`
- Otros ajustes automáticos

---

## 📌 Estructura Típica de una Herramienta

```astro
---
import Layout from '../../layouts/Layout.astro';

export const frontmatter = {
  title: 'Mi Nueva Herramienta',
  description: 'Descripción de la herramienta',
  tags: ['tag1', 'tag2']
};
---

<Layout title={frontmatter.title}>
  <a href={import.meta.env.BASE_URL} class="back-link">&larr; Volver</a>
  
  <div class="tool-container">
    <h1>{frontmatter.title}</h1>
    <p>{frontmatter.description}</p>
    
    <div class="tool-wrapper">
      <div class="form-container">
        <div class="input-group">
          <label>Mi Input</label>
          <input class="input-field" id="miInput">
        </div>
        <button class="btn btn-primary" id="miBoton">Calcular</button>
      </div>
      
      <div class="results-container">
        <div class="summary">
          <div class="summary-item">
            <h4>Resultado</h4>
            <p id="resultado">-</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</Layout>

<script>
  // Tu JavaScript aquí
  document.getElementById('miBoton').addEventListener('click', () => {
    const valor = document.getElementById('miInput').value;
    // ... tu lógica
    document.getElementById('resultado').textContent = valor;
  });
</script>

<!-- OPCIONAL: Solo si necesitas estilos específicos -->
<style>
  /* Tus estilos únicos aquí */
</style>
```

---

## 🎯 Resumen

- ✅ **Usa las clases de `global.css` siempre**
- ✅ **No dupliques CSS**
- ✅ **Si necesitas algo nuevo, agrégalo en `<style>`**
- ✅ **Mantén los archivos limpios: HTML + JS + estilos específicos**
