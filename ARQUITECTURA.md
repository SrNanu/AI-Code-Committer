# 🏗️ Arquitectura Final del Proyecto

## 📋 Estructura del Proyecto

```
AI-Code-Committer/
├── src/
│   ├── styles/
│   │   └── global.css                    # ✅ CSS CENTRALIZADO (Base)
│   ├── layouts/
│   │   └── Layout.astro                  # ✅ Layout con importación de global.css
│   ├── components/
│   │   └── ToolCard.astro                # ✅ Componente reutilizable
│   └── pages/
│       ├── index.astro                   # ✅ Página principal
│       ├── about.astro                   # ✅ Página de información
│       └── tools/
│           ├── calculadora-propinas.astro    # ✅ HTML + JS (0 CSS)
│           ├── calculadora-interes.astro     # ✅ HTML + JS (0 CSS)
│           ├── conversor-markdown.astro      # ✅ HTML + JS (0 CSS)
│           ├── generador-paletas.astro       # ✅ HTML + JS (0 CSS)
│           └── contador-texto.astro          # ✅ HTML + JS (0 CSS)
├── CLASES_DISPONIBLES.md                 # 📖 Guía para la IA
├── astro.config.mjs
├── tsconfig.json
└── package.json
```

---

## 🎯 Filosofía de Diseño

### ✅ Lo que hace cada archivo

| Archivo | Responsabilidad | Contiene CSS |
|---------|-----------------|--------------|
| `Layout.astro` | Estructura HTML base + importa global.css | Solo `<style is:global>` |
| `global.css` | Clases CSS reutilizables y genéricas | ✅ TODO el CSS base |
| `pages/tools/*.astro` | HTML + JavaScript específico | ❌ NO (solo si es muy específico) |

### 🔄 Flujo de Generación de Herramientas por la IA

```
1. IA genera archivo .astro
   ├─ Importa Layout
   ├─ Define frontmatter (title, description, tags)
   └─ Escribe HTML usando clases de global.css

2. Usa clases disponibles
   ├─ .tool-container
   ├─ .tool-wrapper
   ├─ .form-container
   ├─ .input-field
   ├─ .btn .btn-primary
   ├─ .summary .summary-item
   └─ etc...

3. Agrega JavaScript para lógica
   └─ Sin nada de CSS

4. Si necesita estilos muy específicos
   └─ Crea <style> scoped (ejemplo: paleta de colores)
```

---

## 📚 Clases CSS Base Disponibles en `global.css`

### Contenedores
- `.tool-container` - Contenedor principal
- `.tool-wrapper` - Layout 2 columnas
- `.form-container` - Formularios
- `.results-container` - Resultados

### Formularios
- `.input-group` - Grupo label + input
- `.input-field` - Inputs y textareas
- `.input-group label` - Labels

### Botones
- `.btn` - Botón base
- `.btn-primary` - Botón principal

### Resultados
- `.summary` - Contenedor de resultados
- `.summary-item` - Items individuales
- `.summary-item h4` - Labels
- `.summary-item p` - Valores

### Navegación
- `.back-link` - Link para volver

---

## 🤖 Instrucciones para la IA Generadora

### Template Estándar para Nueva Herramienta

```astro
---
import Layout from '../../layouts/Layout.astro';

export const frontmatter = {
  title: 'Nombre de la Herramienta',
  description: 'Descripción breve de qué hace',
  tags: ['tag1', 'tag2', 'tag3']
};
---

<Layout title={frontmatter.title}>
  <a href={import.meta.env.BASE_URL} class="back-link">&larr; Volver</a>
  
  <div class="tool-container">
    <h1>{frontmatter.title}</h1>
    <p>{frontmatter.description}</p>
    
    <div class="tool-wrapper">
      <div class="form-container">
        <!-- Inputs aquí -->
      </div>
      <div class="results-container">
        <!-- Resultados aquí -->
      </div>
    </div>
  </div>
</Layout>

<script>
  // Tu JavaScript aquí
</script>
```

### ✅ DO (Correcto)

```astro
<div class="input-group">
  <label>Mi Input</label>
  <input class="input-field" id="miInput">
</div>

<button class="btn btn-primary" id="miBoton">Calcular</button>

<div class="summary">
  <div class="summary-item">
    <h4>Resultado</h4>
    <p id="resultado">$0.00</p>
  </div>
</div>
```

### ❌ DON'T (Incorrecto)

```astro
<!-- NO agregues CSS aquí -->
<style>
  .input-field {
    padding: 0.8rem 1rem;
    /* Esto ya está en global.css */
  }
</style>

<!-- NO uses colores directos -->
<div style="background: rgb(99, 102, 241); color: white;">
  <!-- Usa clases en su lugar -->
</div>
```

### 📌 Si Necesitas Estilos Específicos

Solo si tu herramienta es muy diferente a las otras, agrégalos en un `<style>` scoped:

```astro
<style>
  /* Solo estilos ESPECÍFICOS de esta herramienta */
  .palette-container {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    height: 400px;
  }
  
  .color-swatch {
    cursor: pointer;
  }
</style>
```

---

## 🎨 Clases CSS Disponibles - Resumen Rápido

| Clase | Propósito | Disponible |
|-------|-----------|-----------|
| `.tool-container` | Contenedor principal | ✅ |
| `.tool-wrapper` | Layout 2 cols | ✅ |
| `.form-container` | Columna formulario | ✅ |
| `.results-container` | Columna resultados | ✅ |
| `.input-group` | Grupo label+input | ✅ |
| `.input-field` | Input/textarea | ✅ |
| `.btn` | Botón base | ✅ |
| `.btn-primary` | Botón principal | ✅ |
| `.summary` | Contenedor resultados | ✅ |
| `.summary-item` | Item resultado | ✅ |
| `.back-link` | Link atrás | ✅ |

---

## 🌈 Variables CSS Disponibles

En `Layout.astro` se definen variables CSS globales:

```css
/* Colores */
--accent              /* Color primario (Indigo) */
--accent-secondary    /* Color secundario (Purple) */
--accent-tertiary     /* Color terciario (Pink) */

/* Fuentes */
--font-family-sans    /* Inter */
--font-family-mono    /* IBM Plex Mono */

/* Temas */
--bg                  /* Background */
--text-color          /* Color de texto */
--text-secondary      /* Color de texto secundario */
--card-bg             /* Background de cards */
--card-border         /* Border de cards */
```

Úsalas en estilos específicos:
```css
.mi-elemento {
  color: rgb(var(--accent));
  background: var(--card-bg);
}
```

---

## 📱 Responsive Automático

Todos los estilos base incluyen media queries (`@media (max-width: 768px)`):
- **No necesitas hacer nada**
- Las herramientas se adaptan automáticamente a móvil
- `.tool-wrapper` se convierte en 1 columna en móvil

---

## ✨ Cómo Escalamos

### Agregar Nueva Herramienta

1. **IA genera** `src/pages/tools/mi-herramienta.astro`
2. **Usa solo clases** de `global.css`
3. **Agrega estilos específicos** solo si es necesario
4. **Propósito**: Reutilizar, no duplicar CSS

### Agregar Nueva Clase CSS Global

1. **Edita** `src/styles/global.css`
2. **Agrega la clase** con toda su lógica
3. **Documenta** en `CLASES_DISPONIBLES.md`
4. **Usa en IA** para futuras herramientas

---

## 📊 Beneficios de Esta Arquitectura

✅ **DRY (Don't Repeat Yourself)** - CSS centralizado
✅ **Mantenible** - Cambios globales en un lugar
✅ **Escalable** - La IA no escribe CSS
✅ **Consistente** - Todas las herramientas usan el mismo estilo
✅ **Ligero** - Menos código en cada archivo
✅ **Responsive** - Automático en todos los dispositivos
✅ **Flexible** - Permite estilos específicos cuando sea necesario

---

## 🚀 Próximos Pasos

1. **Capacita la IA** con `CLASES_DISPONIBLES.md`
2. **Genera herramientas** sin CSS
3. **Monitorea** si hay estilos repetidos
4. **Centraliza** estilos comunes en `global.css`
5. **Mantén limpio** el CSS específico (solo cuando sea realmente necesario)
