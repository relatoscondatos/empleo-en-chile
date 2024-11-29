// See https://observablehq.com/framework/config for documentation.
export default {
  // The project’s title; used in the sidebar and webpage titles.
  title: "Empleo en Chile",

  // The pages and sections in the sidebar. If you don’t specify this option,
  // all pages will be listed in alphabetical order. Listing pages explicitly
  // lets you organize them into sections and have unlisted pages.
  
  home: {},
 
  pages: [
    {
      name: "Actualizaciones trimestrales",
      pages: [
        {name: "Abril-Mayo-Junio 2024", path: "/empleo-en-chile-05-AMJ"},
        {name: "Mayo-Junio-Julio 2024", path: "/empleo-en-chile-06-MJJ"},
        {name: "Junio-Julio-Agosto 2024", path: "/empleo-en-chile-07-JJA"},
        {name: "Julio-Agosto-Septiembre 2024", path: "/empleo-en-chile-08-JAS"},
        {name: "Agosto-Septiembre-Octubre 2024", path: "/"},
      ]
    },
    {
      name: "Conceptos y panorama global",
      pages: [
         {name: "Conceptos claves", path: "/empleo-conceptos-claves"},
        {name: "Comparación internacional", path: "/comparacion-internacional"}
      ]
    }
  ],

  // Content to add to the head of the page, e.g. for a favicon:
  head: `
  <link rel="icon" href="favicon.ico" type="image/png" sizes="32x32">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
  <!--
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  -->
  `,

  // The path to the source root.
  root: "src",

  // Some additional configuration options and their defaults:
  theme: "default", // try "light", "dark", "slate", etc.
  header: 'Un relato con datos <img src="./favicon.ico" height="20px"> <a href="https://www.relatoscondatos.cl" target="_blank">www.relatoscondatos.cl</a> ', // what to show in the header (HTML)
  footer: 'Relatos con datos <i class="fas fa-envelope"></i> <a href="mailto:contacto@relatoscondatos.cl">contacto@relatoscondatos.cl</a>', // what to show in the footer (HTML)
  sidebar: true, // whether to show the sidebar
  toc: {show:true, label:"Contenido"}, // whether to show the table of contents
  pager: true, // whether to show previous & next links in the footer
  // output: "dist", // path to the output root for build
  // search: true, // activate search
  // linkify: true, // convert URLs in Markdown to links
  typographer: true, // smart quotes and other typographic improvements
  // cleanUrls: true, // drop .html from URLs
};
