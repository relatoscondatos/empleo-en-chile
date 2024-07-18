---
sql:
  ene: data/ene.parquet
---
# Empleo en Chile

```js
const añoReferencia = 2024;
const mesReferencia = 4;
const etiquetaMesReferencia = etiquetasTrimestres[mes];

```

<div class="card">
<h2>Distribución población</h2>
<h3>${añoReferencia} - Trimestre ${etiquetasTrimestres[mes]}</h3>

${ditribucionCifras(añoReferencia)}
</div>

<div class="card">
<h2>Evolución de cifras</h2>
<h3>Se indican cifras para trimestre ${etiquetasTrimestres[mes]} de cada año</h3>

${buildChart()}
</div>

<div class="card">
<h2>Distribución personas Ocupadas</h2>
<h3>${añoReferencia} - Trimestre ${etiquetasTrimestres[mes]}</h3>

${ditribucionOcupados(añoReferencia)}
</div>

<div class="card">
<h2>Cambios en ocupación</h2>
<h3>${añoReferencia} vs ${añoReferencia - 1}  - Trimestre ${etiquetasTrimestres[mes]}</h3>

${distribucionCambioOcupados({})}
</div>


```js
function buildChart() {
  const dataPlot = _.chain([...dataTrends])
    .map((d) => [
      {
        date: moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
        año: d.año,
        mes: d.mes,
        tipo: "Ocupadas",
        personas: d.O,
        topline: d.O
      },
      {
        date: moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
        año: d.año,
        mes: d.mes,
        tipo: "Desocupadas",
        personas: d.DO,
        topline: d.O + d.DO
      },
/*      {
        date: moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
        año: d.año,
        mes: d.mes,
        tipo: "Inactivas",
        personas: d.PET - d.O - d.DO,
        topline: d.PET
      },
      {
        date: moment(`${d.año}-${d.mes}`, "YYYY-M").toDate(),
        año: d.año,
        mes: d.mes,
        tipo: "Menores de 15 años",
        personas: d.personas - d.PET,
        topline: d.personas
      }*/
    ])
    .flatten()
    .value();

  const dataPlotLast = dataPlot.filter((d) => d.año == 2024 && d.mes == 4);

  const lineasTrimestre = _.chain(_.range(2019, 2025))
    .map((año) => moment(`${año}-${4}`, "YYYY-M").toDate())
    .value();

  //return dataPlotLast;
  return Plot.plot({
    width,
    marginLeft: 30,
    marginRight: 120,
    y: { grid: true, tickFormat: ".0s" },
    color: {
      range: [
        d3.schemeTableau10[0],
        d3.schemeTableau10[1],
        d3.schemeTableau10[2],
        "lightgrey"
      ]
    },
    marks: [
      Plot.ruleY([0]),

      Plot.areaY(
        dataPlot,
        Plot.stackY({
          y: "personas",
          x: "date",
          fill: "tipo"
        })
      ),
      Plot.ruleX(lineasTrimestre),

      Plot.text(
        dataPlot.filter((d) => d.mes == 4 && !d.tipo.match(/kupados/)),
        Plot.stackY({
          y: "personas",
          x: "date",
          fill: (d) => (d.tipo == "Ocupadas" ? "black" : "white"),
          text: (d) => d3.format(".3s")(d.personas),
          textAnchor: "end",
          dx: -1
        })
      ),
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

function ditribucionCifras(año) {
  const añoReferencia = año;
  const maxValue = _.chain(dataCambios)
    .map((d) => d.personas)
    .max()
    .value();
  const dataAñoReferencia = _.chain(dataCambios)
    .find((d) => d.año == añoReferencia)
    .value();

  const dataPlot = _.chain(dataAñoReferencia.metrics)
    .map((metric) => ({
      indicador: metric,
      valor: dataAñoReferencia[metric],
      cambio: dataAñoReferencia.cambioAnual[metric],
      cambioPct:
        dataAñoReferencia.cambioAnual[metric] /
        (dataAñoReferencia[metric] - dataAñoReferencia.cambioAnual[metric])
    }))
    .filter(
      (d) =>
        !d.indicador.match(
          /administracion|asalariados|extranjeros|ocupacion_informal|sector_informal/
        )
    )
    .value();

  return Plot.plot({
    //title: `Cifras de ocupación - ${añoReferencia} Trimestre ${etiquetasTrimestres[mes]}`,
    width,
    height: 300,
    marginLeft: 10,
    marginRight: 80,
    x: { tickFormat: "s", domain: [0, maxValue] },
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

function ditribucionOcupados(año) {
  const añoReferencia = año;
  const maxValue = _.chain(dataCambios)
    .map((d) => d.O)
    .max()
    .value();
  const dataAñoReferencia = _.chain(dataCambios)
    .find((d) => d.año == añoReferencia)
    .value();

  const dataPlot = _.chain(dataAñoReferencia.metrics)
    .map((metric) => ({
      indicador: metric,
      valor: dataAñoReferencia[metric],
      cambio: dataAñoReferencia.cambioAnual[metric],
      cambioPct:
        dataAñoReferencia.cambioAnual[metric] /
        (dataAñoReferencia[metric] - dataAñoReferencia.cambioAnual[metric])
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
    width,
    height: 300,
    marginLeft: 75,
    marginRight: 0,
    x: { tickFormat: "s", domain: [0, maxValue] },
    y: {
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
              fill: "#EEE",
              fontWeight: "bold",
              text: (d) => `${d["tipo"]}\n${d3.format(".3s")(d["personas"])}`
            })
          )
        ])
        .value()
    ]
  });
}

function distribucionCambioOcupados(options) {
  const añoReferencia = (options && options.año) || 2024;
  const mostrarPorcentaje = (options && options.mostrarPorcentaje) || false;
  const dataAñoReferencia = _.chain(dataCambios)
    .find((d) => d.año == añoReferencia)
    .value();

  const maxValue = dataAñoReferencia.cambioAnual.O;

  function getCambio(record, attrUniverso, attrFoco) {
    const cambio = attrUniverso
      ? record.cambioAnual[attrUniverso] - record.cambioAnual[attrFoco]
      : record.cambioAnual[attrFoco];

    return cambio;
  }

  function getCambioPct(record, attrUniverso, attrFoco) {
    const cambio = attrUniverso
      ? record.cambioAnual[attrUniverso] - record.cambioAnual[attrFoco]
      : record.cambioAnual[attrFoco];

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
        personas: dataAñoReferencia.cambioAnual.O,
        test: getCambio(dataAñoReferencia, null, "O"),
        porcentaje: getCambioPct(dataAñoReferencia, null, "O")
      }
    ],
    categoria: [
      {
        fila: "Categoria",
        tipo: "Asalariados Sector Público",
        personas: dataAñoReferencia.cambioAnual.asalariados_sector_publico,
        test: getCambio(dataAñoReferencia, null, "asalariados_sector_publico"),

        porcentaje_:
          dataAñoReferencia.cambioAnual.asalariados_sector_publico /
          (dataAñoReferencia.asalariados_sector_publico -
            dataAñoReferencia.cambioAnual.asalariados_sector_publico),
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
          dataAñoReferencia.cambioAnual.O -
          dataAñoReferencia.cambioAnual.asalariados_sector_publico,
        test: getCambio(dataAñoReferencia, "O", "asalariados_sector_publico"),
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
        personas: dataAñoReferencia.cambioAnual.ocupacion_informal,
        test: getCambio(dataAñoReferencia, null, "ocupacion_informal"),
        porcentaje: getCambioPct(dataAñoReferencia, null, "ocupacion_informal")
      },
      {
        fila: "Formalidad",
        tipo: "Ocupación Formal",
        personas:
          dataAñoReferencia.cambioAnual.O -
          dataAñoReferencia.cambioAnual.ocupacion_informal,
        test: getCambio(dataAñoReferencia, "O", "ocupacion_informal"),
        porcentaje: getCambioPct(dataAñoReferencia, "O", "ocupacion_informal")
      }
    ],
    actividad: [
      {
        fila: "Actividad",
        tipo: "Administración pública y defensa",
        personas: dataAñoReferencia.cambioAnual.administracion_publica,
        test: getCambio(dataAñoReferencia, null, "administracion_publica"),
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
          dataAñoReferencia.cambioAnual.O -
          dataAñoReferencia.cambioAnual.administracion_publica,
        test: getCambio(dataAñoReferencia, "O", "administracion_publica"),
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
        personas: dataAñoReferencia.cambioAnual.extranjeros,
        test: getCambio(dataAñoReferencia, null, "extranjeros"),
        porcentaje: getCambioPct(dataAñoReferencia, null, "extranjeros")
      },
      {
        fila: "Nacionalidad",
        tipo: "Chilena",
        personas:
          dataAñoReferencia.cambioAnual.O -
          dataAñoReferencia.cambioAnual.extranjeros,
        test: getCambio(dataAñoReferencia, "O", "extranjeros"),
        porcentaje: getCambioPct(dataAñoReferencia, "O", "extranjeros")
      }
    ],
    sexo: [
      {
        fila: "Sexo",
        tipo: "Hombres",
        personas: dataAñoReferencia.cambioAnual.hombres,
        test: getCambio(dataAñoReferencia, null, "hombres"),
        porcentaje: getCambioPct(dataAñoReferencia, null, "hombres")
      },
      {
        fila: "Sexo",
        tipo: "Mujeres",
        personas: dataAñoReferencia.cambioAnual.mujeres,
        test: getCambio(dataAñoReferencia, null, "mujeres"),
        porcentaje: getCambioPct(dataAñoReferencia, null, "mujeres")
      }
    ]
  };

  return Plot.plot({
    /*
    title: `Cambio en ocupación - ${añoReferencia} vs ${
      añoReferencia - 1
    } Trimestre ${etiquetasTrimestres[mes]}`,
    */

    width,
    height: 300,
    marginLeft: 75,
    marginRight: 0,
    x: { tickFormat: "s", domain: [0, maxValue] },
    y: {
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
              fill: "#EEE",
              fontWeight: "bold",
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


```js
const etiquetasTrimestres = {
  1: "Diciembre-Febrero",
  2: "Enero-Marzo",
  3: "Febrero-Abril",
  4: "Marzo-Mayo",
  5: "Abril-Junio",
  6: "Mayo-Julio",
  7: "Junio-Agosto",
  8: "Julio-Septimbre",
  9: "Agosto-Octubre",
  10: "Septiembre-Noviembre",
  11: "Octubre-Diciembre",
  12: "Noviembre-Enero"
}

const mes = 4;

function getCambios() {

  const dict = {};

  const minAño = _.chain(dataTrends)
    .map((d) => d.año)
    .min()
    .value();



  return _.chain(dataTrends)
    .filter((d) => d.mes == mes)
    .each((d) => {
      dict[d.año] = d;
    })
    .filter((d) => d.año > minAño)
    .map((d) => {
      const record = {
        año: d.año,
        mes: d.mes,
        metrics: [],
        cambioAnual: {}
      };
      _.keys(d)
        .filter((d) => !d.match(/año|mes/))
        .forEach((key) => {
          record.metrics.push(key);
          record[key] = d[key];
          record.cambioAnual[key] =
            d[key] - ((dict[d.año - 1] && dict[d.año - 1][key]) || null);
        });

      return record;
    })
    .value();
}

const dataCambios = getCambios()

```

```js
const dataTrends = [...dataTrends_]
```

```sql id=dataTrends_
SELECT *
FROM ene
LIMIT 100
```

```js 
import moment from 'npm:moment'
import { es_ES } from "./components/config.js";
d3.formatDefaultLocale(es_ES);
```