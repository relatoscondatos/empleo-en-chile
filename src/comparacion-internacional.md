---
sql:
  ene_cambio_anual: data/ene_cambio_anual.parquet
  ene_actividad: data/ene_actividad.parquet
  ilo_sector_gdppc: data/ilo_sector_gdppc.parquet
  ilo_ocupacion_informal: data/ilo_ocupacion_informal.parquet
  mpd: data/mpd2023_full_data.parquet
  ilo_sex_gpdpc: data/ilo_sex_gdppc.parquet
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

# Empleo en Chile


## ¿Cómo son las cifras de Chile al comparar con otros países?
### Porcentaje de empleo informal

```js

(function() {
  const dataPlot = _.chain([...dataPaises_ocupacion_informal])
  .map(d => {
    const record = {
      country:d.country,
      countryCode:d.countryCode,
      value:d.value/100
    }

    return record
  })
  .filter(d => d.countryCode && d.country.match(/Chile|UK|Brazil|Argentina|Haiti|Russia|Peru|Nicaragua|Barbados/))
  .value()

  return beeSwarm({data:dataPlot, r:25, showLabel:true, showXAxis:false, height:150})
})()
```

```js

(function() {
  const dataPlot = _.chain([...dataPaises_ocupacion_informal])
  .map(d => {
    const record = {
      country:d.country,
      countryCode:d.countryCode,
      value:d.value/100
    }
    return record
  })
  .filter(d => d.countryCode)
  .value()

  return beeSwarm({data:dataPlot, r:7})
})()
```

```js

(function() {
  const dataPlot = _.chain([...dataPaises_ocupacion_informal])
  .filter(d => d.countryCode && d.incomeGroup == "High income" )
  .map(d => {
    const record = {
      country:d.country,
      countryCode:d.countryCode,
      value:d.value/100
    }
    return record
  })
  .filter(d => d.countryCode)
  .value()

  return beeSwarm({data:dataPlot, r:10, height:600})
})()
```



### Porcentaje de empleo público 

```js
(function() {
  const dataPlot = _.chain([...dataPaises_sector])
  .map(d => {
    const record = {
      country:d.country,
      countryCode:d.countryCode,
      value:d.publicPercentage
    }
    return record
  })
  .filter(d => d.countryCode && d.country.match(/Chile|Djibouti|Cuba|Seychelles|Tuvalu|Norway|UK|Uganda/))
  .value()


  return beeSwarm({data:dataPlot, r:25, showLabel:true, showXAxis:false, height:150})
})()
```

```js

(function() {
  const dataPlot = _.chain([...dataPaises_sector])
  .map(d => {
    const record = {
      country:d.country,
      countryCode:d.countryCode,
      value:d.publicPercentage
    }
    return record
  })
  .filter(d => d.countryCode)
  .value()

  return beeSwarm({data:dataPlot, r:7})
})()
```

```js

(function() {
  const dataPlot = _.chain([...dataPaises_sector])
  .filter(d => d.countryCode && d.incomeGroup == "High income" )
  .map(d => {
    const record = {
      country:d.country,
      countryCode:d.countryCode,
      value:d.publicPercentage
    }
    return record
  })
  .filter(d => d.countryCode)
  .value()

  return beeSwarm({data:dataPlot, r:14})
})()
```




### Porcentaje de empleo femenino

```js
(function() {
  const dataPlot = _.chain([...dataPaises_sexo])
  .map(d => {
    const record = {
      country:d.country,
      countryCode:d.countryCode,
      value:d.femalePercentage
    }
    return record
  })
  .filter(d => d.countryCode && d.country.match(/Chile|Yemen|Iraq|Qatar|Morocco|India|Somalia|Costa Rica|Canada|Mozambique/))
  .value()


  return beeSwarm({data:dataPlot, r:25, showLabel:true, showXAxis:false, xScale:[0.05,0.55], height:150})
})()
```

```js
(function() {
  const dataPlot = _.chain([...dataPaises_sexo])
  .map(d => {
    const record = {
      country:d.country,
      countryCode:d.countryCode,
      value:d.femalePercentage
    }
    return record
  })
  .value()


  return beeSwarm({data:dataPlot, r:7,xScale:[0.05,0.55], height:500})
})()
```


```js
(function() {
  const dataPlot = _.chain([...dataPaises_sexo])
  .filter(d => d.countryCode && d.incomeGroup == "High income" )
  .map(d => {
    const record = {
      country:d.country,
      countryCode:d.countryCode,
      value:d.femalePercentage
    }
    return record
  })
  .value()

  return beeSwarm({data:dataPlot, r:10,xScale:[0.05,0.55]})
})()
```




```js
const umbralIngresoPaises = 15000;
const fuenteINE= `Fuente de datos: Encuesta Nacional de Empleo, INE, Chile`;


```


```sql id=dataPaises_sexo
SELECT *
FROM ilo_sex_gpdpc
```

```sql id=dataPaises_sector
SELECT *
FROM ilo_sector_gdppc
```

```sql id=dataPaises_ocupacion_informal
SELECT *
FROM ilo_ocupacion_informal
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
function distribucionCifras({data=[], añoReferencia=2024, mesReferencia=1, width=640, level=3} = {}) {

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

  const fontColor = "#111"

  const marksByLevel = {
    4: [
 ],

      3: [ 
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
          fill: fontColor,
          fontWeight: "normnal",
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
          fill: fontColor,
          fontWeight: "normal",
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
          fill: fontColor,
          fontWeight: "normal",
          text: (d) => `${d["tipo"]}\n${d3.format(".3s")(d["personas"])}`
        })
      ),
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
          fill: fontColor,
          fontWeight: "normal",
          text: (d) => `${d["tipo"]}\n${d3.format(".3s")(d["personas"])}`
        })
      )],
      2:[ 
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
          fill: fontColor,
          fontWeight: "normnal",
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
          fill: fontColor,
          fontWeight: "normal",
          text: (d) => `${d["tipo"]}\n${d3.format(".3s")(d["personas"])}`
        })
      ),
            Plot.barX(
        [
          {
            tipo: "Personas en Edad de Trabajar",
            personas: dataAñoReferencia.PET
          },

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

        ],
        Plot.stackX({
          x: "personas",
          y: (d) => "Personas en Edad de Trabajar",
          z: "tipo",
          fill: fontColor,
          fontWeight: "normal",
          text: (d) => `${d["tipo"]}\n${d3.format(".3s")(d["personas"])}`
        })
      )
      ],


      1:[      // Bar and text labels for 'Ocupados'
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
          fill: fontColor,
          fontWeight: "normnal",
          text: (d) => `${d["tipo"]}\n${d3.format(".3s")(d["personas"])}`
        })
      ),
           Plot.barX(
        [
          { tipo: "Fuerza de Trabajo", personas: dataAñoReferencia.FT },
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
 
        ],
        Plot.stackX({
          x: "personas",
          y: (d) => "Fuerza de Trabajo",
          z: "tipo",
          fill: fontColor,
          fontWeight: "normal",
          text: (d) => `${d["tipo"]}\n${d3.format(".3s")(d["personas"])}`
        })
      )
      
      
      ]
  }
  


  // Build the plot configuration
  return Plot.plot({
    caption: fuenteINE,
    width,
    height: 300,
    marginLeft: 10,
    marginRight: 20,
    marginBottom: 40,
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
    style :{fontSize:12},
    marks: [
      _.concat([level].map(i => marksByLevel[i]))
    ]
  });
}

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
function distribucionCifras2({data=[], añoReferencia=2024, mesReferencia=1, width=640, stage=3} = {}) {

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
            personas: dataAñoReferencia.personas - dataAñoReferencia.PET,
            level:2
          },
          { tipo: "Población Total", personas: dataAñoReferencia.personas , level:1}
        ]

  const dataGroups = {
   1: data_all.filter(d => d.tipo.match(/En Edad de Trabajar|Menores de 15 años|Población Tota/)),
   2: data_all.filter(d => d.tipo.match(/Fuerza de Trabajo|Inactivas|En Edad de Trabajar/)),
   3: data_all.filter(d => d.tipo.match(/Ocupados|Desocupados|Fuerza de Trabajo/))

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
      domain: [
        "Ocupados",
        "Desocupados",
        "Fuerza de Trabajo",
        "Inactivas",
        "En Edad de Trabajar",
        "Menores de 15 años",
        "Población Total"
      ]
    },
    y: { 
      tickFormat: "s", 
      //domain: [0, maxValue],       
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
          fill: d => d.tipo.match(/Ocupados/) ? "white" : "black"
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
    caption: fuenteINE,
    // width,
    marginLeft: 40,
    marginRight: 130,
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
        style :{fontSize:12},

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
      /*ange: [
        d3.schemeTableau10[0],
        d3.schemeTableau10[1],
        d3.schemeTableau10[2],
        "lightgrey"
      ]*/
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
 * Builds a chart to show the distribution of employed persons.
 * 
 * @param {Object} options - The options for building the chart.
 * @param {Array} options.data - The employment data.
 * @param {number} [options.añoReferencia=2024] - The reference year.
 * @param {number} [options.mesReferencia=1] - The reference month.
 * @returns {Object} - The chart configuration.
 */
function ditribucionOcupadosVert({data=[], añoReferencia=2024, mesReferencia=1, foco="formalidad"} = {}) {

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
  const dataSets_all = {
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
/*    actividad: [
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
    ],*/
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

  const totalOcupados = dataSets_all["ocupados"][0]["personas"]

  const dataSets = [dataSets_all["ocupados"], dataSets_all[foco]]

  // Build the plot configuration
  return Plot.plot({
    caption: fuenteINE,

    height: 300,
    marginLeft: 70,
    marginRight: 100,
    y: { 
      tickFormat: "s", 
      domain: [0, maxValue],
      label:"Personas"
    },
    x: {
      //axis:"right",
      tickFormat: (d) => d,
      domain: [
        "Ocupados",
        _.first(dataSets_all[foco]).fila,
      ],
      label: ""
    },
    color:{
      domain:_.concat(dataSets_all[foco].map(d => d.tipo),["Ocupados"], )
    },
    style :{fontSize:12},

    marks: [
      _.chain(dataSets)
        .map((set, key) => [
          Plot.barY(set, {
            x: "fila",
            y: "personas",
            fill: "tipo"
          }),
          Plot.text(
            set,
            Plot.stackY({
              x: "fila",
              y: "personas",
              z: "tipo",
              fill: d => d.tipo == _.first(dataSets_all[foco]).tipo ? "white": "#000",
              text: (d) => `${d["tipo"]}\n${d3.format(".3s")(d["personas"])} (${d3.format(".1%")(d["personas"]/totalOcupados)})`
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
/*    actividad: [
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
    ],*/
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

  const totalOcupados = dataSets["ocupados"][0]["personas"]


  // Build the plot configuration
  return Plot.plot({
    caption: fuenteINE,

    height: 300,
    marginLeft: 70,
    marginRight: 100,
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
        "Nacionalidad",
        "Sexo"
      ],
      label: ""
    },
        style :{fontSize:12},

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
              text: (d) => `${d["tipo"]}\n${d3.format(".3s")(d["personas"])} (${d3.format(".1%")(d["personas"]/totalOcupados)})`
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
/*    actividad: [
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
    ],*/
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

  const totalOcupados = dataSets["ocupados"][0]["personas"]

    // Helper function to build the label for the chart
  function buildLabel(d) {
    const core = `${d["tipo"]}\n${d["personas"] > 0 ? "+" : ""}${d3.format(".3s")(d["personas"])}`;
    const change = ` (${d["personas"] > 0 ? "+" : ""}${d3.format(".1%")(d["porcentaje"])})`;
    const proporción = ` (${d["personas"] > 0 ? "" : ""}${d3.format(".1%")(d["personas"]/totalOcupados)})`;

    
    return mostrarPorcentaje ? core + proporción : core;
  }


  // Build the plot configuration
  return Plot.plot({
    caption: fuenteINE,

    height: 300,
    marginLeft: 70,
    marginRight:100,
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
        "Nacionalidad",
        "Sexo"
      ],
      label: ""
    },
            style :{fontSize:12},

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
function ditribucionCambioOcupadosVert({data=[], añoReferencia=2024, mesReferencia=1, mostrarPorcentaje=true, foco="formalidad"} = {}) {

  // Calculate the maximum value for the x-axis domain
  const maxValue = _.chain(data)
    .filter(d => d.mes == mesReferencia && d.año == añoReferencia)
    .map((d) => d.O_diff)
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
  const dataSets_all = {
    ocupados: [
      { fila: "Ocupados", tipo: "Ocupados", personas: dataAñoReferencia.O_diff }
    ],
    categoria: [
      {
        fila: "Categoria",
        tipo: "Asalariados Sector Público",
        personas: dataAñoReferencia.asalariados_sector_publico_diff
      },
      {
        fila: "Categoria",
        tipo: "Otras categorías",
        personas:
          dataAñoReferencia.O_diff - dataAñoReferencia.asalariados_sector_publico_diff
      }
    ],
    formalidad: [
      {
        fila: "Formalidad",
        tipo: "Ocupación Informal",
        personas: dataAñoReferencia.ocupacion_informal_diff
      },
      {
        fila: "Formalidad",
        tipo: "Ocupación Formal",
        personas: dataAñoReferencia.O_diff - dataAñoReferencia.ocupacion_informal_diff
      }
    ],
/*    actividad: [
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
    ],*/
    nacionalidad: [
      {
        fila: "Nacionalidad",
        tipo: "Extranjera",
        personas: dataAñoReferencia.extranjeros_diff
      },
      {
        fila: "Nacionalidad",
        tipo: "Chilena",
        personas: dataAñoReferencia.O_diff - dataAñoReferencia.extranjeros_diff
      }
    ],
    sexo: [
      {
        fila: "Sexo",
        tipo: "Hombres",
        personas: dataAñoReferencia.hombres_diff
      },
      {
        fila: "Sexo",
        tipo: "Mujeres",
        personas: dataAñoReferencia.mujeres_diff
      }
    ]
  };

  const totalOcupados = dataSets_all["ocupados"][0]["personas"]

  const dataSets = [dataSets_all["ocupados"], dataSets_all[foco]]

      // Helper function to build the label for the chart
  function buildLabel(d) {
    const core = `${d["tipo"]}\n${d["personas"] > 0 ? "+" : ""}${d3.format(".3s")(d["personas"])}`;
    const change = ` (${d["personas"] > 0 ? "+" : ""}${d3.format(".1%")(d["porcentaje"])})`;
    const proporción = ` (${d["personas"] > 0 ? "" : ""}${d3.format(".1%")(d["personas"]/totalOcupados)})`;

    
    return mostrarPorcentaje ? core + proporción : core;
  }

  // Build the plot configuration
  return Plot.plot({
    caption: fuenteINE,

    height: 300,
    marginLeft: 70,
    marginRight: 100,
    y: { 
      tickFormat: "s", 
      domain: [0, maxValue],
      label:"Personas"
    },
    x: {
      //axis:"right",
      tickFormat: (d) => d,
      domain: [
        "Ocupados",
        _.first(dataSets_all[foco]).fila,
      ],
      label: ""
    },
    color:{
      domain:_.concat(dataSets_all[foco].map(d => d.tipo),["Ocupados"], )
    },
    style :{fontSize:12},

    marks: [
      _.chain(dataSets)
        .map((set, key) => [
          Plot.barY(set, {
            x: "fila",
            y: "personas",
            fill: "tipo"
          }),
          Plot.text(
            set,
            Plot.stackY({
              x: "fila",
              y: "personas",
              z: "tipo",
              fill: d => d.tipo == _.first(dataSets_all[foco]).tipo ? "white": "#000",
              text: (d) => buildLabel(d),

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



```sql id=cifrasInformalidad
SELECT año, mes, O, ocupacion_informal, ocupacion_informal/O as tasaInformalidad
FROM ene_cambio_anual
WHERE mes = 4
ORDER BY año,mes
```


```js
const country_codes = await FileAttachment("./data/country_codes.csv").csv();
const countryCodeDict3to2 = {}
country_codes.forEach((d) => {
  countryCodeDict3to2[d["alpha-3"]] = d["alpha-2"];
});

function getFlagImageURL(code3) {
  return `https://cdnjs.cloudflare.com/ajax/libs/flag-icon-css/3.3.0/flags/1x1/${
              countryCodeDict3to2[code3] && countryCodeDict3to2[code3].toLowerCase()
            }.svg`
}

function beeSwarm({
    data = [], 
    r=10,
    formatter = d3.format(".1%"),
    showLabel = false,
    showXAxis = true,
    xScale=[0,1],
    height=400
    } = {}) {
  return Plot.plot({
    height: height,
    x:{
      tickFormat: d => showXAxis ? formatter(d) : "",
      tickSize:showXAxis ? 5 : 0,
      domain:xScale
    },
    marks: [
      Plot.image(
        data,
        Plot.dodgeY({
          x: "value",
          width: 2 * r, 
          r: r,
          src: (d) => getFlagImageURL(d.countryCode),
          tip: true,
          channels: { pais: "country", "Porcentaje (%)":"value"}
        })
      ),
      showLabel ? Plot.text(
        data,
        Plot.dodgeY({
          x: "value",
          width: 2 * r, 
          r: r,
          text: d => `${d["country"]}\n${formatter(d["value"])}`,
          dy:-45,
          channels: { pais: "country", "Empleo informal (%)":"value"}
        })
      ) : []
    ]
  })
}
```


```js 
// Import required modules and configurations
import moment from 'npm:moment'
import { es_ES , etiquetasTrimestres} from "./components/config.js";

// Set the default locale for D3 formatting
d3.formatDefaultLocale(es_ES);

```


