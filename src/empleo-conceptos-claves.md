---
sql:
---

# Empleo - Conceptos clave 


Al reportar cifras de empleo se habla de conceptos tales como **Personas en Edad de Trabajar**,  **Fuerza de trabajo**, **Ocupados** y **Desocupados**. A continuación hablaremos de estos conceptos utilizando como ejemplo los datos de empleo en Chile en 2023. 

<div class="card">
<h2>Distribución población</h2>
<h3>Año 2023</h3>
<div>${distribucionCifras3({data:data2023, width:640, stage:0})}</div>
</div><!--card-->

El 2023 en Chile había una población total de (${d3.format(".2s")(data2023.TOTAL)}), pero se considera a quienes tienen 15 años o más como **Personas en Edad de Trabajar**.  En 2023 en Chile eran (${d3.format(".2s")(data2023.PET)}), un ${d3.format(".1%")(data2023.PET/data2023.TOTAL)} de la población total.


<div class="card">
<h2>Distribución población</h2>
<h3>Año 2023</h3>
<div>${distribucionCifras3({data:data2023, width:640, stage:1})}</div>

</div><!--card-->


En las Personas en Edad de Trabajar existe un grupo que se clasifica como **Personas Inactivas**.  

Son personas que que no están buscando trabajo, como estudiantes, jubilados, o personas dedicadas a labores del hogar de forma exclusiva. En 2023 en Chile eran ${d3.format(".2s")(data2023.PET- data2023.FT)} personas.

El resto, la **Fuerza de Trabajo**, incluye a todas las personas en edad y capacidad de trabajar que están disponibles para trabajar, es decir, las que están empleadas o en busca de empleo. En 2023 en Chile eran ${d3.format(".2s")(data2023.FT)}, un ${d3.format(".1%")(data2023.FT/data2023.PET)} de las Personas en Edad de Trabajar.

<div class="card">
<h2>Distribución población</h2>
<h3>Año 2023</h3>
<div>${distribucionCifras3({data:data2023, width:640, stage:2})}</div>
</div><!--card-->


En la Fuerza de Trabajo hay **personas ocupadas** y **personas desocupadas**.

Las **personas ocupadas** son aquellas que están trabajando y en 2023 en Chile eran **${d3.format(".2s")(data2023.O)}**, un **${d3.format(".1%")(data2023.O/data2023.PET)} de las personas en edad de trabajar**.  Esta es la cifra que se reporta como **tasa de ocupación**.

<div class="card">
<h2>Distribución población</h2>
<h3>Año 2023</h3>
<div>${distribucionCifras3({data:data2023, width:640, stage:3})}</div>
</div><!--card-->


Las **personas desocupadas** son aquellas que no están trabajando pero están disponibles y buscando empleo activamente. En 2023 en Chile eran **${d3.format(".2s")(data2023.DO)}**, un **${d3.format(".1%")(data2023.DO/data2023.FT)} de las fuerza de trabajo**. Esta es la cifra que se reporta como **tasa de desocupación**.

<div class="card">
<h2>Distribución población</h2>
<h3>Año 2023</h3>
<div>${distribucionCifras3({data:data2023, width:640, stage:4})}</div>
</div><!--card-->


```js
const data2023 = FileAttachment("data/resumen2023.json").json();
const fuenteINE= `Fuente de datos: Encuesta Nacional de Empleo, INE, Chile`;
``` 

```js
/**
 * Processes data with the given options and builds a bar chart showing the distribution of the population.
 * 
 * @param {Object} options - The options for processing data.
 * @param {Array} options.data - The employment data.
 * @param {number} [options.añoReferencia=2024] - The reference year.
 * @param {number} [options.mesReferencia=1] - The reference month.
 * @param {number} [options.width=640] - The width of the chart.
 * @returns {Object} - The chart configuration.
 */
function distribucionCifras3({data={}, width=640, stage=3} = {}) {

  const colorRange = d3.schemeObservable10;

  const labels = [
    "Ocupados",
    "Desocupados",
    "Fuerza de Trabajo",
    "Inactivas",
    "En Edad de Trabajar",
    "Menores de 15 años",
    "Población Total"
  ]

  function textColor(label) {
    const pos = labels.indexOf(label);
    const color = colorRange[pos];
    const {r, g, b} = d3.rgb(color);
    const yiq = (r * 299 + g * 587 + b * 114) / 1000 / 255; // returns values between 0 and 1

    return yiq >= 0.6 ? "#111" : "white"
  }

  // Calculate the maximum value for the x-axis domain
  const maxValue = data.TOTAL

  // Get the data for the reference year and month
  const dataAñoReferencia = data

  const fontColor = "#111"

  const data_all =  [
          { tipo: "Ocupados", personas: dataAñoReferencia.O, level: 4},
          { tipo: "Desocupados", personas: dataAñoReferencia.DO, level: 4 },
          { tipo: "Fuerza de Trabajo", personas: dataAñoReferencia.FT, level:3 },
          {
            tipo: "Inactivas",
            personas: dataAñoReferencia.PET - dataAñoReferencia.FT,
            level:3
          },
          {
            tipo: "En Edad de Trabajar",
            personas: dataAñoReferencia.PET,
            level:2
          },
          {
            tipo: "Menores de 15 años",
            personas: dataAñoReferencia.TOTAL - dataAñoReferencia.PET,
            level:2
          },
          { tipo: "Población Total", personas: dataAñoReferencia.TOTAL , level:1}
        ]

  const dataGroups = {
    
   0: data_all.filter(d => d.tipo.match(/En Edad de Trabajar|Menores de 15 años|Población Tota|Fuerza de Trabajo|Inactivas|Ocupados|Desocupados/)),
   1: data_all.filter(d => d.tipo.match(/En Edad de Trabajar|Menores de 15 años|Población Tota/)),
   2: data_all.filter(d => d.tipo.match(/Fuerza de Trabajo|Inactivas|En Edad de Trabajar/)),
   3: data_all.filter(d => d.tipo.match(/En Edad de Trabajar|Ocupados|Desocupados|Fuerza de Trabajo/)),
   4: data_all.filter(d => d.tipo.match(/Ocupados|Desocupados|Fuerza de Trabajo/))

  }

   const dataGroups_ = {
   1: data_all.filter(d => d.tipo.match(/Ocupados|Desocupados|Fuerza de Trabajo/)),
   2: data_all.filter(d => d.tipo.match(/Ocupados|Desocupados|Fuerza de Trabajo|Inactivas|En Edad de Trabajar/)),
  3: data_all.filter(d => d.tipo.match(/Ocupados|Desocupados|Fuerza de Trabajo|Inactivas|En Edad de Trabajar|Menores de 15 años|Población Total/))
  }

  const dataPlot = dataGroups[stage]

  // Build the plot configuration
  return Plot.plot({
    caption: fuenteINE,
    width,
    marginLeft: 40,
    marginRight: 0,
    color:{
      domain: labels,
      range: colorRange
    },
    y: { 
      tickFormat: "s", 
      label:"Personas"
    },
    x: {
      tickSize: 0,
      tickFormat: (d) => "",
      domain: [
        1,2,3,4
      ],
      label:""
    },
    style :{fontSize:12},
    marks: [
      Plot.barY(
        dataPlot,
        {
          x: "level",
          y: "personas",
          fill: "tipo"
        }
      ),
      Plot.text(
        dataPlot,
        Plot.stackY({
          x: "level",
          y: "personas",
          z: "tipo",
          text:d => `${d.tipo}\n${d3.format(".3s")(d.personas)}`,
          fill: d => textColor(d.tipo),
        })
      )
    ]
  });
}

```

```js
// Import required modules and configurations
import { es_ES} from "./components/config.js";

// Set the default locale for D3 formatting
d3.formatDefaultLocale(es_ES);
```