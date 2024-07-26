---
sql:
  ene_cambio_anual: data/ene_cambio_anual.parquet
---

```js
// Load the employment data from the SQL query result
const datosEmpleo = [...cifrasMensuales_]
```

```js
// Get unique years from the employment data and create a dropdown for selecting the reference year
const options_años = _.chain(datosEmpleo).map(d => d.año).uniq().value()
//const añoReferencia = view(Inputs.select(options_años, {value: _.max(options_años), label: "Año Referencia"}));
const añoReferencia = 2024
```

```js
// Get unique months for the selected reference year and create a dropdown for selecting the reference month
const options_meses = _.chain(datosEmpleo).filter(d => d.año == añoReferencia).map(d => d.mes).uniq().value()
//const mesReferencia = view(Inputs.select(options_meses, {value: 1, label: "Mes Referencia"}));
const mesReferencia = 4
```

```js
// Get the label for the selected reference month
const etiquetaMesReferencia = etiquetasTrimestres[mesReferencia];

const registroReferencia = datosEmpleo.find(d => d.año == añoReferencia && d.mes == mesReferencia)

```


----------------
# Empleo en Chile
## Datos para el trimestre móvil ${etiquetaMesReferencia} de ${añoReferencia}

### Introducción
En esta página, exploraremos la situación del empleo en Chile, con datos actualizados al trimestre móvil ${etiquetaMesReferencia} de ${añoReferencia}. Te invitamos a conocer cómo se compone la fuerza laboral, cómo han evolucionado las cifras y quiénes son las personas ocupadas en el país.

## ¿Qué es la Fuerza de Trabajo?
Cuando se mencionan los datos de empleo, se habla de personas ocupadas y desocupadas, pero eso no incluye a toda la población de Chile.

- De la población total en Chile (${d3.format(".3s")(registroReferencia.personas)}), las **Personas en Edad de Trabajar** son aquellas con 15 años o más (${d3.format(".3s")(registroReferencia.PET)}). 
- No todas estas personas se consideran ocupadas o desocupadas. Aquellas que sí lo hacen conforman la **Fuerza de Trabajo** (${d3.format(".3s")(registroReferencia.FT)}), mientras que las demás son consideradas **personas inactivas** (por razones de estudio, jubilación, falta de deseo de trabajar, entre otras).

En la Fuerza de Trabajo en Chile, durante el trimestre ${etiquetaMesReferencia} de ${añoReferencia}, había:

- **${d3.format(".3s")(registroReferencia.O)} personas ocupadas**
- **${d3.format(".3s")(registroReferencia.DO)} personas desocupadas**

Las personas desocupadas representan un ${d3.format(".1%")(registroReferencia.DO / registroReferencia.FT)} de la Fuerza de Trabajo.

<div class="card">
<h2>Distribución de la Población</h2>
<h3>${añoReferencia} - Trimestre ${etiquetasTrimestres[mesReferencia]}</h3>
<div>${distribucionCifras({data: datosEmpleo, añoReferencia: añoReferencia, mesReferencia: mesReferencia, width: 640})}</div>
</div><!--card-->

## Evolución en el Tiempo
Las cifras de empleo cambian con el tiempo. En el trimestre ${etiquetaMesReferencia} de ${añoReferencia}, hubo **${d3.format(".3s")(registroReferencia.O_diff)} ${registroReferencia.O_diff >= 0 ? "más" : "menos"} personas ocupadas** que en ${añoReferencia-1} y **${d3.format(".3s")(registroReferencia.DO_diff)} ${registroReferencia.DO_diff >= 0 ? "más" : "menos"} personas desocupadas** que en ${añoReferencia-1}.

El aumento en la cantidad de personas ocupadas no significa necesariamente que disminuirán las personas desocupadas. Es muy posible que exista un aumento en la Fuerza de Trabajo que implique un incremento tanto en las personas ocupadas como en las desocupadas.

<div class="card">
<h2>Evolución de las Cifras</h2>
<h3>Cifras para el trimestre ${etiquetasTrimestres[mesReferencia]} de cada año</h3>
<div>${buildChart_evolucionPorMes({data: datosEmpleo, añoReferencia: añoReferencia, mesReferencia: mesReferencia})}</div>
</div><!--card-->

## Composición de las Personas Ocupadas
Veamos cómo se compone el grupo de **personas ocupadas** en Chile.

De las ${d3.format(".3s")(registroReferencia.O)} personas ocupadas:
- **${d3.format(".3s")(registroReferencia.ocupacion_informal)} ocupaciones informales** (${d3.format(".1%")(registroReferencia.ocupacion_informal / registroReferencia.O)})
- **${d3.format(".3s")(registroReferencia.asalariados_sector_publico)} asalariados del sector público** (${d3.format(".1%")(registroReferencia.asalariados_sector_publico / registroReferencia.O)})
- **${d3.format(".3s")(registroReferencia.administracion_publica)} en Administración pública y defensa** (${d3.format(".1%")(registroReferencia.administracion_publica / registroReferencia.O)})
    - *Nota: No todos los asalariados del sector público se clasifican en esta actividad.*
- **${d3.format(".3s")(registroReferencia.extranjeros)} extranjeros** (${d3.format(".1%")(registroReferencia.extranjeros / registroReferencia.O)})
- **${d3.format(".3s")(registroReferencia.mujeres)} mujeres** (${d3.format(".1%")(registroReferencia.mujeres / registroReferencia.O)})

<div class="card">
<h2>Distribución de Personas Ocupadas</h2>
<h3>${añoReferencia} - Trimestre ${etiquetasTrimestres[mesReferencia]}</h3>
<div>${ditribucionOcupados({data: datosEmpleo, añoReferencia: añoReferencia, mesReferencia: mesReferencia})}</div>
</div><!--card-->

## Composición del Cambio en Personas Ocupadas
En comparación con el año anterior, hubo **${registroReferencia.O_diff >= 0 ? "un aumento" : "una disminución"} de ${d3.format(".3s")(registroReferencia.O_diff)} personas ocupadas**. Detallemos este cambio.

De estas ${d3.format(".3s")(registroReferencia.O_diff)} personas:
- **${d3.format(".3s")(registroReferencia.ocupacion_informal_diff)} en ocupaciones informales**
- **${d3.format(".3s")(registroReferencia.asalariados_sector_publico_diff)} asalariados del sector público**
- **${d3.format(".3s")(registroReferencia.administracion_publica_diff)} en Administración pública y defensa**
- **${d3.format(".3s")(registroReferencia.extranjeros_diff)} extranjeros**
- **${d3.format(".3s")(registroReferencia.mujeres_diff)} mujeres**

<div class="card"> 
<h2>Cambios en la Ocupación</h2>
<h3>${añoReferencia} vs ${añoReferencia - 1} - Trimestre ${etiquetasTrimestres[mesReferencia]}</h3>
<div>${distribucionCambioOcupados({data: datosEmpleo, añoReferencia: añoReferencia, mesReferencia: mesReferencia})}</div>
</div><!--card-->



```sql
SELECT *
FROM ene_cambio_anual
```


```js
const foco = ["Administracion pública", "Otras actividades"];

const dataPlot = _.chain([...cifrasMensuales_])
.map(d => ([
{
    date:moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
    personas: d.extranjeros,
    tipo:"Extranjeros"
},{
    date:moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
    personas: d.O,
    tipo:"Ocupados"
},
{
    date:moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
    personas: d.administracion_publica,
    tipo:"Administracion pública"

},
{
    date:moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
    personas: d.O-d.administracion_publica,
    tipo:"Otras actividades"

},
{
    date:moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
    personas: d.asalariados_sector_publico,
    tipo:"Asalariados Sector Público"

},
{
    date:moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
    personas: d.O-d.administracion_publica,
    tipo:"Otras actividades"

},
{
    date:moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
    personas: d.mujeres,
    tipo:"mujeres"

},
{
    date:moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
    personas: d.administracion_publica_diff,
    tipo:"Cambio - Administracion pública"

},
{
    date:moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
    personas: d.O_diff - d.administracion_publica_diff,
    tipo:"Cambio - Otras actividades"

}
]))
.flatten()
.sortBy(d => d.date)
.value()

const dataPlotPct = _.chain([...cifrasMensuales_])
.map(d => ([
{
    date:moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
    porcentaje: d.asalariados_sector_publico / d.O,
    tipo:"Asalariados Sector Público"
}
]))
.flatten()
.sortBy(d => d.date)
.value()

function plotTrendsPct({data = [], zero = true} = {}) {
    return Plot.plot({
    width,
    height: 300,
    marginLeft: 100,
    marginRight: 150,
    x: { 
    },
    y: {
        grid:true,
        zero:zero
    },
    marks: [
      // Bar for 'Población Total'
      Plot.lineX(data,
        {
            x: "date",
            y: "porcentaje",
            stroke:"tipo"
        }
      ),
      Plot.dot(data,
        {
          tip:true,
            x: "date",
            y: "porcentaje",
            fill:"tipo"
        }
      ),
     Plot.text(data,
        Plot.selectLast({
            x: "date",
            y: "porcentaje",
            z:"tipo",
            text:"tipo",
            textAnchor:"start",
            dx:5
        })
      )
    ]
})
}


function plotTrends({data = [], zero = true} = {}) {
    return Plot.plot({
    width,
    height: 300,
    marginLeft: 100,
    marginRight: 150,
    x: { 
    },
    y: {
        grid:true,
        zero:zero
    },
    marks: [
      // Bar for 'Población Total'
      Plot.lineX(data,
        {
            x: "date",
            y: "personas",
            stroke:"tipo"
        }
      ),
      Plot.dot(data,
        {
          tip:true,
            x: "date",
            y: "personas",
            fill:"tipo"
        }
      ),
     Plot.text(data,
        Plot.selectLast({
            x: "date",
            y: "personas",
            z:"tipo",
            text:"tipo",
            textAnchor:"start",
            dx:5
        })
      )
    ]
})
}

display(plotTrends({data: dataPlot}))

display(plotTrends({data:dataPlot.filter(d => ["Administracion pública"].includes(d.tipo))}))

display(plotTrends({
  data:dataPlot.filter(d => ["Administracion pública"].includes(d.tipo)),
  zero:false
  }))


display(plotTrends({
  data:dataPlot.filter(d => ["Cambio - Administracion pública", "Cambio - Otras actividades"].includes(d.tipo)),
  zero:false
  }))

display(plotTrends({
  data:dataPlot.filter(d => ["Asalariados Sector Público", "Ocupados"].includes(d.tipo)),
  zero:false
  }))


display(plotTrendsPct({
  data:dataPlotPct,
  zero:false
  }))

dataPlotPct
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
function distribucionCifras({data=[], añoReferencia=2024, mesReferencia=1, width=640} = {}) {

  // Calculate the maximum value for the x-axis domain
  const maxValue = _.chain(data)
    .filter(d => d.año == añoReferencia && d.mes == mesReferencia)
    .map((d) => d.personas)
    .max()
    .value();

  // Get the data for the reference year and month
  const dataAñoReferencia = _.chain(data)
    .find((d) => d.año == añoReferencia && d.mes == mesReferencia)
    .value();

  // Build the plot configuration
  return Plot.plot({
    width,
    height: 300,
    marginLeft: 10,
    marginRight: 10,
    x: { 
      tickFormat: "s", 
      domain: [0, maxValue],       
      label:"Personas"
    },
    y: {
      tickSize: 0,
      tickFormat: (d) => "",
      domain: [
        "Ocupados",
        "Fuerza de Trabajo",
        "Personas en Edad de Trabajar",
        "Población Total"
      ]
    },
    marks: [
      // Bar for 'Población Total'
      Plot.barX(
        [{ tipo: "Población Total", personas: dataAñoReferencia.personas }],
        {
          x: "personas",
          y: (d) => "Población Total",
          fill: "tipo"
        }
      ),
      // Text label for 'Población Total'
      Plot.text(
        [{ tipo: "Población Total", personas: dataAñoReferencia.personas }],
        Plot.stackX({
          x: "personas",
          y: (d) => "Población Total",
          z: "tipo",
          fill: "#EEE",
          fontWeight: "bold",
          text: (d) => `${d["tipo"]}\n${d3.format(".3s")(d["personas"])}`
        })
      ),
      // Bar and text labels for 'Personas en Edad de Trabajar'
      Plot.barX(
        [
          {
            tipo: "Personas en Edad de Trabajar",
            personas: dataAñoReferencia.PET
          },
          {
            tipo: "Menores de 15 años",
            personas: dataAñoReferencia.personas - dataAñoReferencia.PET
          }
        ],
        {
          x: "personas",
          y: (d) => "Personas en Edad de Trabajar",
          fill: "tipo"
        }
      ),
      Plot.text(
        [
          {
            tipo: "Personas en Edad de Trabajar",
            personas: dataAñoReferencia.PET
          },
          {
            tipo: "Menores de 15 años",
            personas: dataAñoReferencia.personas - dataAñoReferencia.PET
          }
        ],
        Plot.stackX({
          x: "personas",
          y: (d) => "Personas en Edad de Trabajar",
          z: "tipo",
          fill: "#EEE",
          fontWeight: "bold",
          text: (d) => `${d["tipo"]}\n${d3.format(".3s")(d["personas"])}`
        })
      ),
      // Bar and text labels for 'Fuerza de Trabajo'
      Plot.barX(
        [
          { tipo: "Fuerza de Trabajo", personas: dataAñoReferencia.FT },
          {
            tipo: "Inactivas",
            personas: dataAñoReferencia.PET - dataAñoReferencia.FT
          }
        ],
        {
          x: "personas",
          y: (d) => "Fuerza de Trabajo",
          fill: "tipo"
        }
      ),
      Plot.text(
        [
          { tipo: "Fuerza de Trabajo", personas: dataAñoReferencia.FT },
          {
            tipo: "Inactivas",
            personas: dataAñoReferencia.PET - dataAñoReferencia.FT
          }
        ],
        Plot.stackX({
          x: "personas",
          y: (d) => "Fuerza de Trabajo",
          z: "tipo",
          fill: "#EEE",
          fontWeight: "bold",
          text: (d) => `${d["tipo"]}\n${d3.format(".3s")(d["personas"])}`
        })
      ),
      // Bar and text labels for 'Ocupados'
      Plot.barX(
        [
          { tipo: "Ocupados", personas: dataAñoReferencia.O },
          { tipo: "Desocupados", personas: dataAñoReferencia.DO }
        ],
        {
          x: "personas",
          y: (d) => "Ocupados",
          fill: "tipo"
        }
      ),
      Plot.text(
        [
          { tipo: "Ocupados", personas: dataAñoReferencia.O },
          { tipo: "Desocupados", personas: dataAñoReferencia.DO }
        ],
        Plot.stackX({
          x: "personas",
          y: (d) => "Ocupados",
          z: "tipo",
          fill: "#EEE",
          fontWeight: "bold",
          text: (d) => `${d["tipo"]}\n${d3.format(".3s")(d["personas"])}`
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
function buildChart_evolucionPorMes({ data = [], añoReferencia = 2024, mesReferencia = 1 } = {}) {
  
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
      /*      
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
      }*/
    ])
    .flatten() // Flatten the array of arrays
    .sortBy(d => d.mes) // Sort by month
    .sortBy(d => d.año) // Sort by year
    .value(); // Extract the value from the chain

  // Filter data for the last month of the reference year
  const dataPlotLast = _.chain(dataPlot).filter((d) => d.mes == mesReferencia && d.año == añoReferencia).value();

  // Create a list of dates for each unique year at the reference month
  const lineasTrimestre = _.chain(dataPlot)
    .map(d => d.año)
    .uniq() // Get unique years
    .map((año) => moment(`${año}-${mesReferencia}`, "YYYY-M").toDate()) // Create a date object for each year at the reference month
    .value();

  // Build the plot configuration
  return Plot.plot({
    // width,
    marginLeft: 30,
    marginRight: 80,
    y: { 
      grid: true, 
      tickFormat: ".0s",
      label:"Personas"
    },
    color: {
      range: [
        d3.schemeTableau10[0],
        d3.schemeTableau10[1],
        d3.schemeTableau10[2],
        "lightgrey"
      ]
    },
    marks: [
      // Add a horizontal line at y=0
      Plot.ruleY([0]),

      // Create an area plot with stacking for the data
      Plot.areaY(
        dataPlot,
        Plot.stackY({
          y: "personas",
          x: "date",
          fill: "tipo"
        })
      ),
      
      // Add vertical lines for each unique year at the reference month
      Plot.ruleX(lineasTrimestre),

      // Add text labels for the data points of the reference month
      Plot.text(
        dataPlot.filter((d) => d.mes == mesReferencia),
        Plot.stackY({
          y: "personas",
          x: "date",
          fill: (d) => (d.tipo == "Ocupadas" ? "black" : "white"),
          text: (d) => d3.format(".3s")(d.personas),
          textAnchor: "end",
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
          dx: 10
        })
      )
    ]
  });
}

```

```js
/**
 * Builds a chart to show the distribution of employed persons.
 * 
 * @param {Object} options - The options for building the chart.
 * @param {Array} options.data - The employment data.
 * @param {number} [options.añoReferencia=2024] - The reference year.
 * @param {number} [options.mesReferencia=1] - The reference month.
 * @returns {Object} - The chart configuration.
 */
function ditribucionOcupados({data=[], añoReferencia=2024, mesReferencia=1} = {}) {

  // Calculate the maximum value for the x-axis domain
  const maxValue = _.chain(data)
    .filter(d => d.mes == mesReferencia && d.año == añoReferencia)
    .map((d) => d.O)
    .max()
    .value();

  // Get the data for the reference year and month
  const dataAñoReferencia = _.chain(data)
    .find((d) => d.año == añoReferencia && d.mes == mesReferencia)
    .value();

  // Define metrics and filter out unnecessary ones
  const metrics = _.keys(dataAñoReferencia).filter(d => !d.match(/año|mes|diff|__index_level/))

  // Prepare the data for plotting
  const dataPlot = _.chain(metrics)
    .map((metric) => ({
      indicador: metric,
      valor: dataAñoReferencia[metric],
      cambio: dataAñoReferencia[metric+"_diff"],
      cambioPct:
        dataAñoReferencia[metric+"_diff"] /
        (dataAñoReferencia[metric] - dataAñoReferencia[[metric+"_diff"]])
    }))
    .filter((d) => !d.indicador.match(/DO|personas|FT|PET|sector_informal/))
    .value();

  // Define datasets for different categories
  const dataSets = {
    ocupados: [
      { fila: "Ocupados", tipo: "Ocupados", personas: dataAñoReferencia.O }
    ],
    categoria: [
      {
        fila: "Categoria",
        tipo: "Asalariados Sector Público",
        personas: dataAñoReferencia.asalariados_sector_publico
      },
      {
        fila: "Categoria",
        tipo: "Otras categorías",
        personas:
          dataAñoReferencia.O - dataAñoReferencia.asalariados_sector_publico
      }
    ],
    formalidad: [
      {
        fila: "Formalidad",
        tipo: "Ocupación Informal",
        personas: dataAñoReferencia.ocupacion_informal
      },
      {
        fila: "Formalidad",
        tipo: "Ocupación Formal",
        personas: dataAñoReferencia.O - dataAñoReferencia.ocupacion_informal
      }
    ],
    actividad: [
      {
        fila: "Actividad",
        tipo: "Administración pública y defensa",
        personas: dataAñoReferencia.administracion_publica
      },
      {
        fila: "Actividad",
        tipo: "Otras actividades",
        personas: dataAñoReferencia.O - dataAñoReferencia.administracion_publica
      }
    ],
    nacionalidad: [
      {
        fila: "Nacionalidad",
        tipo: "Extranjera",
        personas: dataAñoReferencia.extranjeros
      },
      {
        fila: "Nacionalidad",
        tipo: "Chilena",
        personas: dataAñoReferencia.O - dataAñoReferencia.extranjeros
      }
    ],
    sexo: [
      {
        fila: "Sexo",
        tipo: "Hombres",
        personas: dataAñoReferencia.hombres
      },
      {
        fila: "Sexo",
        tipo: "Mujeres",
        personas: dataAñoReferencia.mujeres
      }
    ]
  };

  // Build the plot configuration
  return Plot.plot({
    height: 300,
    marginLeft: 70,
    marginRight: 75,
    x: { 
      tickFormat: "s", 
      domain: [0, maxValue],
      label:"Personas"
    },
    y: {
      axis:"right",
      tickFormat: (d) => d,
      domain: [
        "Ocupados",
        "Formalidad",
        "Categoria",
        "Actividad",
        "Nacionalidad",
        "Sexo"
      ],
      label: ""
    },
    marks: [
      _.chain(dataSets)
        .map((set, key) => [
          Plot.barX(set, {
            x: "personas",
            y: "fila",
            fill: "tipo"
          }),
          Plot.text(
            set,
            Plot.stackX({
              x: "personas",
              y: "fila",
              z: "tipo",
              fill: "#000",
              text: (d) => `${d["tipo"]}\n${d3.format(".3s")(d["personas"])}`
            })
          )
        ])
        .value()
    ]
  });
}


```






```js
/**
 * Builds a chart to show the changes in occupation.
 * 
 * @param {Object} options - The options for building the chart.
 * @param {Array} options.data - The employment data.
 * @param {number} [options.añoReferencia=2024] - The reference year.
 * @param {number} [options.mesReferencia=1] - The reference month.
 * @param {boolean} [options.mostrarPorcentaje=true] - Whether to show percentage changes.
 * @returns {Object} - The chart configuration.
 */
function distribucionCambioOcupados({ data = [], añoReferencia = 2024, mesReferencia = 1, mostrarPorcentaje=true  } = {}) {

  // Get the data for the reference year and month
  const dataAñoReferencia = _.chain(data)
    .find((d) => d.año == añoReferencia && d.mes == mesReferencia)
    .value();

  // Calculate the maximum value for the x-axis domain
  const maxValue = dataAñoReferencia.O_diff;

  // Helper function to calculate the change
  function getCambio(record, attrUniverso, attrFoco) {
    const cambio = attrUniverso
      ? record[attrUniverso+"_diff"] - record[attrFoco+"_diff"]
      : record[attrFoco+"_diff"];
    return cambio;
  }

  // Helper function to calculate the percentage change
  function getCambioPct(record, attrUniverso, attrFoco) {
    const cambio = attrUniverso
      ? record[attrUniverso+"_diff"] - record[attrFoco+"_diff"]
      : record[attrFoco+"_diff"];
    const valorActual = attrUniverso
      ? record[attrUniverso] - record[attrFoco]
      : record[attrFoco];
    return cambio / (valorActual - cambio);
  }

  // Helper function to build the label for the chart
  function buildLabel(d) {
    const core = `${d["tipo"]}\n${d["personas"] > 0 ? "+" : ""}${d3.format(".3s")(d["personas"])}`;
    const change = ` (${d["personas"] > 0 ? "+" : ""}${d3.format(".1%")(d["porcentaje"])})`;
    return mostrarPorcentaje ? core + change : core;
  }

  // Define datasets for different categories
  const dataSets = {
    ocupados: [
      {
        fila: "Ocupados",
        tipo: "Ocupados",
        personas: dataAñoReferencia.O_diff,
        porcentaje: getCambioPct(dataAñoReferencia, null, "O")
      }
    ],
    categoria: [
      {
        fila: "Categoria",
        tipo: "Asalariados Sector Público",
        personas: dataAñoReferencia.asalariados_sector_publico_diff,
        porcentaje: getCambioPct(dataAñoReferencia, null, "asalariados_sector_publico")
      },
      {
        fila: "Categoria",
        tipo: "Otras categorías",
        personas: dataAñoReferencia.O_diff - dataAñoReferencia.asalariados_sector_publico_diff,
        porcentaje: getCambioPct(dataAñoReferencia, "O", "asalariados_sector_publico")
      }
    ],
    formalidad: [
      {
        fila: "Formalidad",
        tipo: "Ocupación Informal",
        personas: dataAñoReferencia.ocupacion_informal_diff,
        porcentaje: getCambioPct(dataAñoReferencia, null, "ocupacion_informal")
      },
      {
        fila: "Formalidad",
        tipo: "Ocupación Formal",
        personas: dataAñoReferencia.O_diff - dataAñoReferencia.ocupacion_informal_diff,
        porcentaje: getCambioPct(dataAñoReferencia, "O", "ocupacion_informal")
      }
    ],
    actividad: [
      {
        fila: "Actividad",
        tipo: "Administración pública y defensa",
        personas: dataAñoReferencia.administracion_publica_diff,
        porcentaje: getCambioPct(dataAñoReferencia, null, "administracion_publica")
      },
      {
        fila: "Actividad",
        tipo: "Otras actividades",
        personas: dataAñoReferencia.O_diff - dataAñoReferencia.administracion_publica_diff,
        porcentaje: getCambioPct(dataAñoReferencia, "O", "administracion_publica")
      }
    ],
    nacionalidad: [
      {
        fila: "Nacionalidad",
        tipo: "Extranjera",
        personas: dataAñoReferencia.extranjeros_diff,
        porcentaje: getCambioPct(dataAñoReferencia, null, "extranjeros")
      },
      {
        fila: "Nacionalidad",
        tipo: "Chilena",
        personas: dataAñoReferencia.O_diff - dataAñoReferencia.extranjeros_diff,
        porcentaje: getCambioPct(dataAñoReferencia, "O", "extranjeros")
      }
    ],
    sexo: [
      {
        fila: "Sexo",
        tipo: "Hombres",
        personas: dataAñoReferencia.hombres_diff,
        porcentaje: getCambioPct(dataAñoReferencia, null, "hombres")
      },
      {
        fila: "Sexo",
        tipo: "Mujeres",
        personas: dataAñoReferencia.mujeres_diff,
        porcentaje: getCambioPct(dataAñoReferencia, null, "mujeres")
      }
    ]
  };

  // Build the plot configuration
  return Plot.plot({
    height: 300,
    marginLeft: 70,
    marginRight: 75,
    x: { 
      tickFormat: "s", 
      domain: [0, maxValue],
      label:"Personas"
    },
    y: {
      axis:"right",
      tickFormat: (d) => d,
      domain: [
        "Ocupados",
        "Formalidad",
        "Categoria",
        "Actividad",
        "Nacionalidad",
        "Sexo"
      ],
      label: ""
    },
    marks: [
      _.chain(dataSets)
        .map((set, key) => [
          Plot.barX(set, {
            x: "personas",
            y: "fila",
            fill: "tipo"
          }),
          Plot.text(
            set,
            Plot.stackX({
              x: "personas",
              y: "fila",
              z: "tipo",
              fill: "#000",
              fontWeight: "none",
              text: (d) => buildLabel(d),
              text_: (d) => `${d["tipo"]}\n${d["personas"] > 0 ? "+" : ""}${d3.format(".3s")(d["personas"])} (${d["personas"] > 0 ? "+" : ""}${d3.format(".1%")(d["porcentaje"])})`
            })
          )
        ])
        .value()
    ]
  });
}

```



```sql id=cifrasMensuales_
SELECT *
FROM ene_cambio_anual
```

```js 
// Import required modules and configurations
import moment from 'npm:moment'
import { es_ES , etiquetasTrimestres} from "./components/config.js";

// Set the default locale for D3 formatting
d3.formatDefaultLocale(es_ES);

```