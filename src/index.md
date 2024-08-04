---
sql:
  ene_cambio_anual: data/ene_cambio_anual.parquet
---

# Empleo en Chile - Actualización Trimestral (Abril-Mayo-Junio) ${añoReferencia}

Las cifras de empleo evolucionan con el tiempo. La población total crece, pero los distintos grupos varian sus tamaños absolutos y relativos. El siguiente gráfico muestra cifras para el trimestre ${etiquetasTrimestres[mesReferencia]} entre 2017 y ${añoReferencia}.

Dado que hay variaciones estacionales durante el año, para analizar los cambios comparamos el mismo trimestre de distintos años. 

<div class="card">
<h2>Evolución de cifras</h2>
<h3>Se indican cifras para trimestre ${etiquetasTrimestres[mesReferencia]} de cada año</h3>
<div>${buildChart_evolucionPorMes_bars({data:datosEmpleo, añoReferencia:añoReferencia, mesReferencia: mesReferencia})}</div>
</div><!--card-->

La pandemia en 2020 generó una importante reducción en las personas ocupadas.  

La tasa de ocupación (proporción de Ocupados dentro de Personas en Edad de Trabajar) en el trimestre ${etiquetasTrimestres[mesReferencia]} bajó de un **${d3.format(".1%")(registro2019.O / registro2019.PET) } en 2019** a un **${d3.format(".1%")(registro2020.O / registro2020.PET)} en 2020**.

Desde 2020 ha aumentado progresivamente llegando a un **${d3.format(".1%")(registroReferencia.O / registroReferencia.PET) } en ${añoReferencia}**, pero aún no se llega a los niveles previos a la pandemia.

```js
graficoOcupacion
```


## Composición de las personas ocupadas

El total de **personas ocupadas** varía en el tiempo. Para el trimestre ${etiquetasTrimestres[mesReferencia]} de **2019, antes de la pandemia, había ${d3.format(".2s")(registro2019.O)}** de personas ocupadas y en **${añoReferencia} se reportan ${d3.format(".2s")(registroReferencia.O)}**. 

A continuación veremos cómo se descompone ese total de ocupados en distintos sub grupos utilizando como referencia los datos del trimestre ${etiquetasTrimestres[mesReferencia]} en los respectivos años.

<div class="card">
<h2>Evolución de cifras</h2>
<h3>Se indican cifras para trimestre ${etiquetasTrimestres[mesReferencia]} de cada año</h3>
<div>${buildChart_evolucionPorMes_subgrupos_bars({dataPlot:dataPlotEvolucionOcupados, añoReferencia:añoReferencia, mesReferencia: mesReferencia})}</div>
</div><!--card-->

Dentro del total de ocupados, el grupo que corresponde a **ocupación informal** son quienes carecen de protección social y laboral adecuada.

La proporción de ocupación informal **en 2019 era un ${d3.format(".1%")(registro2019.ocupacion_informal / registro2019.O)}**.  

Esta proporción disminuyó en la pandemia bajando a un **${d3.format(".1%")(registro2020.ocupacion_informal / registro2020.O)} en 2020** ya que muchos trabajadores informales pasaron a ser inactivos.  

La cifra ha ido aumentando progresivamente llegando a un **${d3.format(".1%")(registroReferencia.ocupacion_informal / registroReferencia.O)} en ${añoReferencia}**

<div class="card">
<h2>Evolución de cifras</h2>
<h3>Se indican cifras para trimestre ${etiquetasTrimestres[mesReferencia]} de cada año</h3>
<div>${buildChart_evolucionPorMes_subgrupos_bars({dataPlot:dataPlotEvolucionInformalidad, añoReferencia:añoReferencia, mesReferencia: mesReferencia})}</div>
</div><!--card-->

Las personas ocupadas se pueden clasificar en distintas categorías dentro de las cuales están los **asalariados del sector público** que son aquellos trabajadores que están empleados por el gobierno o por entidades estatales.

La proporcíón de asalariados del sector público aumentó de un **${d3.format(".1%")(registro2019.asalariados_sector_publico / registro2019.O)} en 2019** a un **${d3.format(".1%")(registro2020.asalariados_sector_publico / registro2020.O)} en 2020** ya que la cantidad absoluta de ocupados en este sector no fue mayormente afectada por la pandemia. 

Entre **${añoReferencia-1} y ${añoReferencia}** se observa una variacion de **${d3.format(".1%")(registroReferenciaPrevio.asalariados_sector_publico / registroReferenciaPrevio.O)}** a un **${d3.format(".1%")(registroReferencia.asalariados_sector_publico / registroReferencia.O)}**. 

Cabe hacer notar que en 2024 se desarrolló el CENSO Nacional y las cifras de empleo en el sector público pueden verse transitoriamente afectadas por empleos temporales en esta actividad.


<div class="card">
<h2>Evolución de cifras</h2>
<h3>Se indican cifras para trimestre ${etiquetasTrimestres[mesReferencia]} de cada año</h3>
<div>${buildChart_evolucionPorMes_subgrupos_bars({dataPlot:dataPlotEvolucionSectorPublico, añoReferencia:añoReferencia, mesReferencia: mesReferencia})}</div>
</div><!--card-->

Las cifras de empleo también se ven afectadas por cambios en la **población extranjera** en Chile.

La proporción de personas extranjeras entre los ocupados aumentó de manera importante de un **${d3.format(".1%")(registro2017.extranjeros / registro2017.O)} en 2017** a un **${d3.format(".1%")(registro2021.extranjeros / registro2021.O)} en 2021**.

A partir de 2021 la proporción de extranjeros no aumenta, llegando a un **${d3.format(".1%")(registroReferencia.extranjeros / registroReferencia.O)} en ${añoReferencia}**.

<div class="card">
<h2>Evolución de cifras</h2>
<h3>Se indican cifras para trimestre ${etiquetasTrimestres[mesReferencia]} de cada año</h3>
<div>${buildChart_evolucionPorMes_subgrupos_bars({dataPlot:dataPlotEvolucionExtranjeros, añoReferencia:añoReferencia, mesReferencia: mesReferencia})}</div>
</div><!--card-->

La mayoría de las personas ocupadas son hombres.

La **proporción de mujeres** en el empleo disminuyó en la pandemia, llegando a un **${d3.format(".1%")(registro2020.mujeres / registro2020.O)} en 2020** y ha aumentado desde esa fecha. Pero la cifra en **${añoReferencia} (${d3.format(".1%")(registroReferencia.mujeres / registroReferencia.O)})** no es muy superior a la que se observaba en **2019 (${d3.format(".1%")(registro2019.mujeres / registro2019.O)})**


<div class="card">
<h2>Evolución de cifras</h2>
<h3>Se indican cifras para trimestre ${etiquetasTrimestres[mesReferencia]} de cada año</h3>
<div>${buildChart_evolucionPorMes_subgrupos_bars({dataPlot:dataPlotEvolucionSexo, añoReferencia:añoReferencia, mesReferencia: mesReferencia})}</div>
</div><!--card-->

```sql id=cifrasMensuales
SELECT *
FROM ene_cambio_anual
```

```js
const añoReferencia = 2024
const mesReferencia = 5

const fuenteINE= `Fuente de datos: Encuesta Nacional de Empleo, INE, Chile`;

// Get the label for the selected reference month
const etiquetaMesReferencia = etiquetasTrimestres[mesReferencia];

const registroReferencia = datosEmpleo.find(d => d.año == añoReferencia && d.mes == mesReferencia)
const registroReferenciaPrevio = datosEmpleo.find(d => d.año == añoReferencia-1 && d.mes == mesReferencia)
const registro2017 = datosEmpleo.find(d => d.año == 2017 && d.mes == mesReferencia)
const registro2019 = datosEmpleo.find(d => d.año == 2019 && d.mes == mesReferencia)
const registro2020 = datosEmpleo.find(d => d.año == 2020 && d.mes == mesReferencia)
const registro2021 = datosEmpleo.find(d => d.año == 2021 && d.mes == mesReferencia)
```

```js
// Load the employment data from the SQL query result
const datosEmpleo = [...cifrasMensuales]
```

```js
const dataPlotEvolucionOcupados = _.chain(datosEmpleo)
    .filter(d => d.año == añoReferencia ? d.mes <= mesReferencia : d.año < añoReferencia && d.año >= 2017)
    .map((d) => [
      {
        // Create data point for 'Ocupadas' (Employed)
        date: moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
        año: d.año,
        mes: d.mes,
        tipo: "Ocupados",
        personas: d.O,
        percentage: d.O/d.O,
        order:1,
      }
           
    ])
    .flatten() // Flatten the array of arrays
    .sortBy(d => d.mes) // Sort by month
    .sortBy(d => d.año) // Sort by year
    .filter(d => d.mes == mesReferencia)
    .value(); // Extract the value from the chain

const dataPlotEvolucionInformalidad = _.chain(datosEmpleo)
    .filter(d => d.año == añoReferencia ? d.mes <= mesReferencia : d.año < añoReferencia && d.año > 2017)
    .map((d) => [
      {
        // Create data point for 'Ocupadas' (Employed)
        date: moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
        año: d.año,
        mes: d.mes,
        tipo: "Informales",
        personas: d.ocupacion_informal,
        percentage: d.ocupacion_informal/d.O,
        order:1,
      },
      {
        // Create data point for 'Desocupadas' (Unemployed)
        date: moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
        año: d.año,
        mes: d.mes,
        tipo: "Formales",
        personas: d.O-d.ocupacion_informal,
        percentage: 1-d.ocupacion_informal/d.O,
        order:2,
      },
      // Uncomment the following blocks if you need 'Inactivas' and 'Menores de 15 años' categories
           
    ])
    .flatten() // Flatten the array of arrays
    .sortBy(d => d.mes) // Sort by month
    .sortBy(d => d.año) // Sort by year
    .filter(d => d.mes == mesReferencia)
    .value(); // Extract the value from the chain

const dataPlotEvolucionSectorPublico = _.chain(datosEmpleo)
    .filter(d => d.año == añoReferencia ? d.mes <= mesReferencia : d.año < añoReferencia)
    .map((d) => [
      {
        // Create data point for 'Ocupadas' (Employed)
        date: moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
        año: d.año,
        mes: d.mes,
        tipo: "Sector Público",
        personas: d.asalariados_sector_publico,
        percentage: d.asalariados_sector_publico/d.O,
        order:1,

      },
      {
        // Create data point for 'Desocupadas' (Unemployed)
        date: moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
        año: d.año,
        mes: d.mes,
        tipo: "Otros",
        personas: d.O-d.asalariados_sector_publico,
        percentage: 1-d.asalariados_sector_publico/d.O,
        order:2,
      },
      // Uncomment the following blocks if you need 'Inactivas' and 'Menores de 15 años' categories
           
    ])
    .flatten() // Flatten the array of arrays
    .sortBy(d => d.mes) // Sort by month
    .sortBy(d => d.año) // Sort by year
    .filter(d => d.mes == mesReferencia)
    .value(); // Extract the value from the chain

const dataPlotEvolucionExtranjeros = _.chain(datosEmpleo)
    .filter(d => d.año == añoReferencia ? d.mes <= mesReferencia : d.año < añoReferencia)
    .map((d) => [
      {
        // Create data point for 'Ocupadas' (Employed)
        date: moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
        año: d.año,
        mes: d.mes,
        tipo: "Extranjeros",
        personas: d.extranjeros,
        percentage: d.extranjeros/d.O,
        order:1,

      },
      {
        // Create data point for 'Desocupadas' (Unemployed)
        date: moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
        año: d.año,
        mes: d.mes,
        tipo: "Chilenos",
        personas: d.O-d.extranjeros,
        percentage: 1-d.extranjeros/d.O,
        order:2,
      },
      // Uncomment the following blocks if you need 'Inactivas' and 'Menores de 15 años' categories
           
    ])
    .flatten() // Flatten the array of arrays
    .sortBy(d => d.mes) // Sort by month
    .sortBy(d => d.año) // Sort by year
    .filter(d => d.mes == mesReferencia)
    .value(); // Extract the value from the chain


const dataPlotEvolucionSexo = _.chain(datosEmpleo)
    .filter(d => d.año == añoReferencia ? d.mes <= mesReferencia : d.año < añoReferencia)
    .map((d) => [
      {
        // Create data point for 'Ocupadas' (Employed)
        date: moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
        año: d.año,
        mes: d.mes,
        tipo: "Hombres",
        personas: d.hombres,
        percentage: d.hombres/d.O,
        order:2,

      },
      {
        // Create data point for 'Desocupadas' (Unemployed)
        date: moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
        año: d.año,
        mes: d.mes,
        tipo: "Mujeres",
        personas: d.mujeres,
        percentage: d.mujeres/d.O,
        order:1,
      },
           
    ])
    .flatten() // Flatten the array of arrays
    .sortBy(d => d.order) // Sort by month
    .sortBy(d => d.mes) // Sort by month
    .sortBy(d => d.año) // Sort by year
    .filter(d => d.mes == mesReferencia)
    .value(); // Extract the value from the chain
```

```js
/**
 * Builds a chart to show the evolution of employment data by month.
 * 
 * @param {Object} options - The options for building the chart.
 * @param {Array} options.data - The employment data.
 * @param {number} [options.añoReferencia=2024] - The reference year.
 * @param {number} [options.mesReferencia=1] - The reference month.
 * @returns {Object} - The chart configuration.
 */
function buildChart_evolucionPorMes_bars({ data = [], añoReferencia = 2024, mesReferencia = 1 } = {}) {
  
  // Process the data to generate the data points for the plot
  const dataPlot = _.chain(data)
    .filter(d => d.año == añoReferencia ? d.mes <= mesReferencia : d.año < añoReferencia)
    .map((d) => [
      {
        // Create data point for 'Ocupadas' (Employed)
        date: moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
        año: d.año,
        mes: d.mes,
        tipo: "Ocupadas",
        personas: d.O,
        topline: d.O
      },
      {
        // Create data point for 'Desocupadas' (Unemployed)
        date: moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
        año: d.año,
        mes: d.mes,
        tipo: "Desocupadas",
        personas: d.DO,
        topline: d.O + d.DO
      },
      // Uncomment the following blocks if you need 'Inactivas' and 'Menores de 15 años' categories
           
      {
        // Create data point for 'Inactivas' (Inactive)
        date: moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
        año: d.año,
        mes: d.mes,
        tipo: "Inactivas",
        personas: d.PET - d.O - d.DO,
        topline: d.PET
      },
      {
        // Create data point for 'Menores de 15 años' (Under 15 years)
        date: moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
        año: d.año,
        mes: d.mes,
        tipo: "Menores de 15 años",
        personas: d.personas - d.PET,
        topline: d.personas
      }
    ])
    .flatten() // Flatten the array of arrays
    .sortBy(d => d.mes) // Sort by month
    .sortBy(d => d.año) // Sort by year
    .filter(d => d.mes == mesReferencia)
    .value(); // Extract the value from the chain

  // Filter data for the last month of the reference year
  const dataPlotLast = _.chain(dataPlot).filter((d) => d.mes == mesReferencia && d.año == añoReferencia).value();

  // Build the plot configuration
  return Plot.plot({
    caption: fuenteINE,
    // width,
    marginLeft: 40,
    marginRight: 130,
    marginBottom: 40,
    x: { 
      tickFormat: d => `${moment(d).format('YYYY')}`,
      type:"band"
    },    
    y: { 
      grid: true, 
      tickFormat: ".0s",
      label:"Personas"
    },
    color: {
      domain: [
        "Ocupadas",
        "Desocupadas",
        "Inactivas",
        "Menores de 15 años"
      ]
    },
        style :{fontSize:12},

    marks: [
      // Add a horizontal line at y=0
      Plot.ruleY([0]),

      // Create an area plot with stacking for the data
      Plot.barY(
        dataPlot,
        Plot.stackY({
          y: "personas",
          x: "date",
          fill: "tipo"
        })
      ),

      // Add text labels for the data points of the reference month
      Plot.text(
        dataPlot.filter((d) => d.mes == mesReferencia),
        Plot.stackY({
          y: "personas",
          x: "date",
          fill: (d) => (d.tipo == "Ocupadas" ? "white" : "black"),
          text: (d) => d3.format(".3s")(d.personas),
          textAnchor: "middle",
          dx: -1
        })
      ),
      
      // Add text labels for the data points of the last month in the reference year
      Plot.text(
        dataPlotLast,
        Plot.stackY({
          y: "personas",
          x: "date",
          fill: (d) => (d.tipo == "Ocupadas" ? "black" : "black"),
          text: "tipo",
          textAnchor: "start",
          dx: 50
        })
      )
      
    ]
  });
}
```

```js
/**
 * Builds a chart to show the evolution of employment data by month.
 * 
 * @param {Object} options - The options for building the chart.
 * @param {Array} options.data - The employment data.
 * @param {number} [options.añoReferencia=2024] - The reference year.
 * @param {number} [options.mesReferencia=1] - The reference month.
 * @returns {Object} - The chart configuration.
 */
function buildChart_evolucionPorMes_subgrupos_bars({ dataPlot = [], añoReferencia = 2024, mesReferencia = 1 } = {}) {
  
  const colorRange = d3.schemeObservable10;

  const labels = _.chain(dataPlot)
    .uniqBy(d => d.tipo)
    .sortBy(d => d.order)
    .reverse()
    .map(d => d.tipo)
    .value()

  function textColor(label) {
    const pos = labels.indexOf(label);
    const color = colorRange[pos];
    const {r, g, b} = d3.rgb(color);
    const yiq = (r * 299 + g * 587 + b * 114) / 1000 / 255; // returns values between 0 and 1

    return yiq >= 0.6 ? "#111" : "white"
  }

  // Filter data for the last month of the reference year
  const dataPlotLast = _.chain(dataPlot).filter((d) => d.mes == mesReferencia && d.año == añoReferencia).value();

  // Build the plot configuration
  return Plot.plot({
    caption: fuenteINE,
    // width,
    marginLeft: 40,
    marginRight: 130,
    marginBottom: 40,
    x: { 
      tickFormat: d => `${moment(d).format('YYYY')}`,
      type:"band"
    },    
    y: { 
      grid: true, 
      tickFormat: ".0s",
      label:"Personas"
    },
    color: {
      domain: labels,
      range: colorRange
    },
        style :{fontSize:12},

    marks: [
      // Add a horizontal line at y=0
      Plot.ruleY([0]),

      // Create an area plot with stacking for the data
      Plot.barY(
        dataPlot,
        Plot.stackY({
          y: "personas",
          x: "date",
          fill: "tipo"
        })
      ),

      // Add text labels for the data points of the reference month
      Plot.text(
        dataPlot.filter((d) => d.mes == mesReferencia),
        Plot.stackY({
          y: "personas",
          x: "date",
          // fill: (d) => (d.tipo == labels[0] ? "white" : "black"),
          fill: d => textColor(d.tipo),
          text: (d) => `${d3.format(".3s")(d.personas)}\n${d3.format(".1%")(d.percentage)}`,
          textAnchor: "middle",
          dx: -1
        })
      ),
      
      // Add text labels for the data points of the last month in the reference year
      Plot.text(
        dataPlotLast,
        Plot.stackY({
          y: "personas",
          x: "date",
          fill: (d) => (d.tipo == "Ocupadas" ? "black" : "black"),
          text: "tipo",
          textAnchor: "start",
          dx: 50
        })
      )
      
    ]
  });
}
```

```js
const graficoOcupacion = (function() {

  const datosOcupacion = _.chain(datosEmpleo)
  .filter(d => d.mes == mesReferencia)
  .map(d => ({
    año: d.año,
    tasaOcupacion: d.O / d.PET
  }))
  .value()

  const maxOcupacion = _.chain(datosOcupacion)
    .map(d => d.tasaOcupacion)
    .max()
    .value() 

  const minOcupacion = _.chain(datosOcupacion)
    .map(d => d.tasaOcupacion)
    .min()
    .value()

  return Plot.plot({
    caption: fuenteINE,
    marginLeft: 40,
    marginTop: 40,

    x:{
      inset:40,
      grid:true
    },

    y:{
      zero:false,
      tickFormat: d => d3.format(".1%")(d),
      domain:[
        minOcupacion -0.1 < 0 ? 0 : minOcupacion -0.1, 
        maxOcupacion +0.1 > 1 ? 1 : maxOcupacion +0.1
      ],
      label: "Tasa de Ocupación",
      grid:true
    },

    marks: [
      // Create an area plot with stacking for the data
      Plot.lineY(
        datosOcupacion,
        {
          y: "tasaOcupacion",
          x: "año",
          stroke: d => "ocupación",
          strokeWidth:3
        }
      ),
      Plot.dot(
        datosOcupacion,
        {
          y: "tasaOcupacion",
          x: "año",
          stroke: d => "ocupación",
          strokeWidth:3
        }
      ),
      Plot.text(
        datosOcupacion,
        {
          y: "tasaOcupacion",
          x: "año",
          text: d => d3.format(".1%")(d.tasaOcupacion),
          dy:-15,
          fontSize:14,
          fontWeight:"bold"
        }
      )
    ]
  })

})()

```




```js
// Import required modules and configurations
import moment from 'npm:moment'
import { es_ES , etiquetasTrimestres} from "./components/config.js";

// Set the default locale for D3 formatting
d3.formatDefaultLocale(es_ES);
```