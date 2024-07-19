---
sql:
  ene_cambio_anual: data/ene_cambio_anual.parquet
---
# Empleo en Chile

```js
const datosEmpleo = [...cifrasMensuales_]
```

```js
const options_años = _.chain(datosEmpleo).map(d => d.año).uniq().value()
const añoReferencia = view(Inputs.select(options_años, {value: _.max(options_años), label: "Año Referencia"}));
```

```js
const options_meses = _.chain(datosEmpleo).filter(d => d.año == añoReferencia).map(d => d.mes).uniq().value()
const mesReferencia = view(Inputs.select(options_meses, {value: 1, label: "Mes Referencia"}));
```

```js
const etiquetaMesReferencia = etiquetasTrimestres[mesReferencia];
```


<div class="card">
<h2>Distribución población</h2>
<h3>${añoReferencia} - Trimestre ${etiquetasTrimestres[mesReferencia]}</h3>
<div>${distribucionCifras({data:datosEmpleo,añoReferencia:añoReferencia,mesReferencia:mesReferencia, width:640})}</div>
</div><!--card-->


<div class="card">
<h2>Evolución de cifras</h2>
<h3>Se indican cifras para trimestre ${etiquetasTrimestres[mesReferencia]} de cada año</h3>
<div>${buildChart_evolucionPorMes({data:datosEmpleo, añoReferencia:añoReferencia, mesReferencia: mesReferencia})}</div>
</div><!--card-->

<div class="card">
<h2>Distribución personas Ocupadas</h2>
<h3>${añoReferencia} - Trimestre ${etiquetasTrimestres[mesReferencia]}</h3>
<div>${ditribucionOcupados({data:datosEmpleo, añoReferencia:añoReferencia,mesReferencia: mesReferencia})}</div>
</div><!--card-->

<div class="card"> 
<h2>Cambios en ocupación</h2>
<h3>${añoReferencia} vs ${añoReferencia - 1}  - Trimestre ${etiquetasTrimestres[mesReferencia]}</h3>
<div>${distribucionCambioOcupados({data:datosEmpleo, añoReferencia:añoReferencia,mesReferencia: mesReferencia})}</div>
</div><!--card-->


```js
/**
 * Processes data with the given options.
 * 
 * @param {Object} options - The options for processing data.
 * @param {number} [options.dataCambioAnual=[]] - Arreglo con los cambios anuales.
 * @param {boolean} [options.verbose=false] - Whether to log detailed information.
 * @param {string} [options.mode='default'] - The mode of operation.
 */
function distribucionCifras({data=[], añoReferencia=2024,mesReferencia=1, width:width} = {}) {

  const maxValue = _.chain(data)
    .filter(d => d.año == añoReferencia && d.mes == mesReferencia)
    .map((d) => d.personas)
    .max()
    .value();

  const dataAñoReferencia = _.chain(data)
    .find((d) => d.año == añoReferencia && d.mes == mesReferencia)
    .value();

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
      Plot.barX(
        [{ tipo: "Población Total", personas: dataAñoReferencia.personas }],
        {
          x: "personas",
          y: (d) => "Población Total",
          fill: "tipo"
        }
      ),
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
      ,
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
function ditribucionOcupados({data=[],añoReferencia=2024, mesReferencia = 1} = {}) {


  const maxValue = _.chain(data)
    .filter(d => d.mes == mesReferencia && d.año == añoReferencia)
    .map((d) => d.O)
    .max()
    .value();


  const dataAñoReferencia = _.chain(data)
    .find((d) => d.año == añoReferencia && d.mes == mesReferencia)
    .value();


  const metrics = _.keys(dataAñoReferencia).filter(d => !d.match(/año|mes|diff|__index_level/))

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

  return Plot.plot({
    //title: `Cifras detalle de ocupación - ${añoReferencia} Trimestre ${etiquetasTrimestres[mes]}`,
    //width,
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
function distribucionCambioOcupados({ data = [], añoReferencia = 2024,mesReferencia = 1, mostrarPorcentaje=true  } = {}) {


  const dataAñoReferencia = _.chain(data)
    .find((d) => d.año == añoReferencia && d.mes == mesReferencia)
    .value();

  const maxValue = dataAñoReferencia.O_diff;


  function getCambio(record, attrUniverso, attrFoco) {
    const cambio = attrUniverso
      ? record[attrUniverso+"_diff"] - record[attrFoco+"_diff"]
      : record[attrFoco+"_diff"];

    return cambio;
  }

  function getCambioPct(record, attrUniverso, attrFoco) {
    const cambio = attrUniverso
      ? record[attrUniverso+"_diff"] - record[attrFoco+"_diff"]
      : record[attrFoco+"_diff"];

    const valorActual = attrUniverso
      ? record[attrUniverso] - record[attrFoco]
      : record[attrFoco];

    return cambio / (valorActual - cambio);
  }

  function buildLabel(d) {
    const core = `${d["tipo"]}\n${d["personas"] > 0 ? "+" : ""}${d3.format(
      ".3s"
    )(d["personas"])}`;
    const change = ` (${d["personas"] > 0 ? "+" : ""}${d3.format(".1%")(
      d["porcentaje"]
    )})`;
    return mostrarPorcentaje ? core + change : core;
  }

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
        porcentaje: getCambioPct(
          dataAñoReferencia,
          null,
          "asalariados_sector_publico"
        )
      },
      {
        fila: "Categoria",
        tipo: "Otras categorías",
        personas:
          dataAñoReferencia.O_diff -
          dataAñoReferencia.asalariados_sector_publico_diff,
        porcentaje: getCambioPct(
          dataAñoReferencia,
          "O",
          "asalariados_sector_publico"
        )
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
        personas:
          dataAñoReferencia.O_diff -
          dataAñoReferencia.ocupacion_informal_diff,
        porcentaje: getCambioPct(dataAñoReferencia, "O", "ocupacion_informal")
      }
    ],
    actividad: [
      {
        fila: "Actividad",
        tipo: "Administración pública y defensa",
        personas: dataAñoReferencia.administracion_publica_diff,
        porcentaje: getCambioPct(
          dataAñoReferencia,
          null,
          "administracion_publica"
        )
      },
      {
        fila: "Actividad",
        tipo: "Otras actividades",
        personas:
          dataAñoReferencia.O_diff -
          dataAñoReferencia.administracion_publica_diff,
        porcentaje: getCambioPct(
          dataAñoReferencia,
          "O",
          "administracion_publica"
        )
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
        personas:
          dataAñoReferencia.O_diff -
          dataAñoReferencia.extranjeros_diff,
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


  return Plot.plot({
    //width,
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

              text_: (d) =>
                `${d["tipo"]}\n${d["personas"] > 0 ? "+" : ""}${d3.format(
                  ".3s"
                )(d["personas"])}` +
                ` (${d["personas"] > 0 ? "+" : ""}${d3.format(".1%")(
                  d["porcentaje"]
                )})`
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
LIMIT 100
```

```js 
import moment from 'npm:moment'
import { es_ES , etiquetasTrimestres} from "./components/config.js";
d3.formatDefaultLocale(es_ES);
```