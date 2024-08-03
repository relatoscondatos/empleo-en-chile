---
sql:
  ene_cambio_anual: data/ene_cambio_anual.parquet
  ene_actividad: data/ene_actividad.parquet
  ilo_sector_gdppc: data/ilo_sector_gdppc.parquet
  ilo_ocupacion_informal: data/ilo_ocupacion_informal.parquet
  mpd: data/mpd2023_full_data.parquet
  ilo_sex_gpdpc: data/ilo_sex_gdppc.parquet
  ene_sintetica: data/ene_sintetica.parquet
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
const mesReferencia = 5
```

```js
// Get the label for the selected reference month
const etiquetaMesReferencia = etiquetasTrimestres[mesReferencia];

const registroReferencia = datosEmpleo.find(d => d.año == añoReferencia && d.mes == mesReferencia)
const registroReferenciaPrevio = datosEmpleo.find(d => d.año == añoReferencia-1 && d.mes == mesReferencia)
const registro2017 = datosEmpleo.find(d => d.año == 2017 && d.mes == mesReferencia)
const registro2019 = datosEmpleo.find(d => d.año == 2019 && d.mes == mesReferencia)
const registro2020 = datosEmpleo.find(d => d.año == 2020 && d.mes == mesReferencia)
const registro2021 = datosEmpleo.find(d => d.año == 2021 && d.mes == mesReferencia)
```

# Empleo en Chile
## Datos para trimestre móvil ${etiquetaMesReferencia} de ${añoReferencia}



## Clasificación de la población

```js
const data2023 = FileAttachment("data/resumen2023.json").json();
``` 

Al reportar cifras de empleo se habla de conceptos tales como la **Fuerza de trabajo**. A continuación hablaremos de estos conceptos utilizando como ejemplo los datos de empleo en Chile en 2023. 

<div class="card">
<h2>Distribución población</h2>
<h3>Año 2023</h3>
<div>${distribucionCifras3({data:data2023, width:640, stage:0})}</div>
</div><!--card-->

El 2023 en Chile había una población total de (${d3.format(".3s")(data2023.TOTAL)}), pero se considera a quienes tienen 15 años o más como **Personas en Edad de Trabajar**.  En 2023 en Chile eran (${d3.format(".3s")(data2023.PET)}), un ${d3.format(".1%")(data2023.PET/data2023.TOTAL)} de la población total.


<div class="card">
<h2>Distribución población</h2>
<h3>Año 2023</h3>
<div>${distribucionCifras3({data:data2023, width:640, stage:1})}</div>

</div><!--card-->


En las Personas en Edad de Trabajar existe un grupo que se clasifica como **Personas Inactivas**.  

Son personas que que no están buscando trabajo, como estudiantes, jubilados, o personas dedicadas a labores del hogar de forma exclusiva. En 2023 en Chile eran ${d3.format(".3s")(data2023.PET- data2023.FT)} personas.

El resto, la **Fuerza de Trabajo**, incluye a todas las personas en edad y capacidad de trabajar que están disponibles para trabajar, es decir, las que están empleadas o en busca de empleo. En 2023 en Chile eran ${d3.format(".3s")(data2023.FT)}, un ${d3.format(".1%")(data2023.FT/data2023.PET)} de las Personas en Edad de Trabajar.

<div class="card">
<h2>Distribución población</h2>
<h3>Año 2023</h3>
<div>${distribucionCifras3({data:data2023, width:640, stage:2})}</div>
</div><!--card-->


En la Fuerza de Trabajo hay **personas ocupadas** y **personas desocupadas**.

Las **personas ocupadas** son aquellas que están trabajando y en 2023 en Chile eran **${d3.format(".3s")(data2023.O)}**, un **${d3.format(".1%")(data2023.O/data2023.PET)} de las personas en edad de trabajar**.  Esta es la cifra que se reporta como **tasa de ocupación**.

Las **personas desocupadas** son aquellas que no están trabajando pero están disponibles y buscando empleo activamente. En 2023 en Chile eran **${d3.format(".3s")(data2023.DO)}**, un **${d3.format(".1%")(data2023.DO/data2023.FT)} de las fuerza de trabajo**. Esta es la cifra que se reporta como **tasa de desocupación**.

<div class="card">
<h2>Distribución población</h2>
<h3>Año 2023</h3>
<div>${distribucionCifras3({data:data2023, width:640, stage:3})}</div>
</div><!--card-->

## Evolución en el tiempo

Las cifras de empleo evolucionan con el tiempo. La población total crece, pero los distintos grupos varian sus tamaños absolutos y relativos. El siguiente gráfico muestra cifras para el trimestre ${etiquetasTrimestres[mesReferencia]} entre 2017 y ${añoReferencia}.

La pandemia en 2020 generó una importante reducción en las personas ocupadas. La tasa de ocupación en el trimestre ${etiquetasTrimestres[mesReferencia]} llegó a un **${d3.format(".1%")(registro2020.O / registro2020.PET)} en 2020** vs un **${d3.format(".1%")(registro2019.O / registro2019.PET) } en 2019**.

El empleo ha aumentado progresivamente desde la pandemia, llegando  a una tasa de ocupación de un **${d3.format(".1%")(registroReferencia.O / registroReferencia.PET) } en ${añoReferencia}**


```js
const statsCambio = (function() {
  const ocupadosActuales = registroReferencia.O
  const ocupadosPrevios = registroReferencia.O - registroReferencia.O_diff

  const desocupadosActuales = registroReferencia.DO
  const desocupadosPrevios = registroReferencia.DO - registroReferencia.DO_diff

  const ftActual = registroReferencia.FT
  const ftPrevia = registroReferencia.FT - registroReferencia.FT_diff

  const desocupacionActual = desocupadosActuales / ftActual
  const desocupacionPrevia = desocupadosPrevios / ftPrevia

  const aumentoOcupados = ocupadosActuales/ocupadosPrevios -1
  const aumentoDesocupados = desocupadosActuales/desocupadosPrevios -1
  const aumentoFT = ftActual/ftPrevia -1

  return {
    aumentoOcupados: aumentoOcupados,
    aumentoDesocupados:aumentoDesocupados,
    aumentoFT:aumentoFT,
    desocupacionActual:desocupacionActual,
    desocupacionPrevia:desocupacionPrevia
  }
})()

```


<div class="card">
<h2>Evolución de cifras</h2>
<h3>Se indican cifras para trimestre ${etiquetasTrimestres[mesReferencia]} de cada año</h3>
<div>${buildChart_evolucionPorMes_bars({data:datosEmpleo, añoReferencia:añoReferencia, mesReferencia: mesReferencia})}</div>
</div><!--card-->


## Composición de las personas ocupadas

El total de **personas ocupadas** varía en el tiempo. Para el trimestre ${etiquetasTrimestres[mesReferencia]} antes de la pandemia, **en 2019, había ${d3.format(".3s")(registro2019.O)}** de personas ocupadas y en **${añoReferencia} se reportan ${d3.format(".3s")(registroReferencia.O)}**. 

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

La proporción de personas extranjeras entre los ocupados aumento de manera importante de un **${d3.format(".1%")(registro2017.extranjeros / registro2017.O)} en 2017** a un **${d3.format(".1%")(registro2021.extranjeros / registro2021.O)} en 2021**.

A partir de 2021 la proporción de extranjeros muestra cierta estabilidad, llegando a un **${d3.format(".1%")(registroReferencia.extranjeros / registroReferencia.O)} en ${añoReferencia}**

<div class="card">
<h2>Evolución de cifras</h2>
<h3>Se indican cifras para trimestre ${etiquetasTrimestres[mesReferencia]} de cada año</h3>
<div>${buildChart_evolucionPorMes_subgrupos_bars({dataPlot:dataPlotEvolucionExtranjeros, añoReferencia:añoReferencia, mesReferencia: mesReferencia})}</div>
</div><!--card-->

La mayoría de las personas ocupadas son hombres.

La **proporción de mujeres** en el empleo disminuyó en la pandemia a un **${d3.format(".1%")(registro2020.mujeres / registro2020.O)} en 2020** y ha aumentado desde esa fecha. Pero la cifra en **${añoReferencia} (${d3.format(".1%")(registroReferencia.mujeres / registroReferencia.O)})** no es muy superior a la que se observaba en **2019 (${d3.format(".1%")(registro2019.mujeres / registro2019.O)})**


<div class="card">
<h2>Evolución de cifras</h2>
<h3>Se indican cifras para trimestre ${etiquetasTrimestres[mesReferencia]} de cada año</h3>
<div>${buildChart_evolucionPorMes_subgrupos_bars({dataPlot:dataPlotEvolucionSexo, añoReferencia:añoReferencia, mesReferencia: mesReferencia})}</div>
</div><!--card-->



## ¿Cómo son las cifras de Chile al comparar con otros países?
## Porcentaje de empleo informal

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



## Porcentaje de empleo público 

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




## Porcentaje de empleo femenino

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
const grupoPaisesView = Inputs.select(["Alto ingreso", "América Latina y el Caribe"], { label: "Grupo de paises"});
const grupoPaises = view(grupoPaisesView)
```

<div class="card"> 
<h2>Porcentaje de empleos en el sector público</h2>
<h3>${display(Inputs.bind(Inputs.select(["Alto ingreso", "América Latina y el Caribe"], { label: "Grupo de países"}), grupoPaisesView))}</h3>
<h3>Paises de ${grupoPaises} según clasificación del Banco Mundial que cuentan con los respectivos datos de empleo en datos públicos de la OIT</h3><div>${rankingSectorPublico}</div>
</div><!--card-->


<div class="card"> 
<h2>Porcentaje de ocupación informal</h2>
<h3>${display(Inputs.bind(Inputs.select(["Alto ingreso", "América Latina y el Caribe"], { label: "Grupo de países"}), grupoPaisesView))}</h3>
<h3>Paises de ${grupoPaises} según clasificación del Banco Mundial que cuentan con los respectivos datos de empleo en datos públicos de la OIT</h3><div>${rankingOcupacionInformal}</div>
</div><!--card-->



<div class="card"> 
<h2>Porcentaje de ocupación femenina</h2>

<h3>${display(Inputs.bind(Inputs.select(["Alto ingreso", "América Latina y el Caribe"], { label: "Grupo de países"}), grupoPaisesView))}</h3>
<h3>Paises de ${grupoPaises} según clasificación del Banco Mundial que cuentan con los respectivos datos de empleo en datos públicos de la OIT</h3>
<div>${rankingSexo}</div>
</div><!--card-->


<div class="card"> 
<h2>Porcentaje de empleo público vs PIB per capita</h2>
<h3>${display(Inputs.bind(Inputs.select(["Alto ingreso", "América Latina y el Caribe"], { label: "Grupo de países"}), grupoPaisesView))}</h3>
<h3>Paises de ${grupoPaises} según clasificación del Banco Mundial que cuentan con los respectivos datos de empleo en datos públicos de la OIT</h3><div>${scateredPlotEmpleoInformalGDPPC}</div>
</div><!--card-->



```js
const umbralIngresoPaises = 15000;
const fuenteINE= `Fuente de datos: Encuesta Nacional de Empleo, INE, Chile`;


```

```js
display([...dataPaises_sexo])
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
const rankingSexo  = (function() {
  const dataPlot = [...dataPaises_sexo].filter(d => 
    (grupoPaises == "Alto ingreso" 
    ? d.incomeGroup == "High income"
    : d.region == "Latin America & Caribbean") 
    && d.femalePercentage
  )

  return Plot.plot({
      height: 800,
      marginLeft: 150,
      marginRight: 90,

      x:{
        label:"Porcentaje de empleo femenino",
        tickFormat: d => d3.format(".0%")(d)
      },

      y:{label:"País"},

      marks: [
        // Bar for 'Población Total'
        Plot.barX(
          dataPlot,
          {
            x: "femalePercentage",
            y: "country",
            fill: d => d.country == 'Chile' ? "orange" : "grey",
            sort:{y:"x", reverse:true}
          }
        ),
      Plot.text(
          dataPlot,
          {
            x: "femalePercentage",
            y: "country",
            text: d => `${d3.format(".1%")(d.femalePercentage)} (${d.time})`,
            dx:5,
            textAnchor:"start"
          }
        ),
    
      ]
  })

})()

```



```js
const rankingSectorPublico = (function() {
  const dataPlot = [...dataPaises_sector].filter(d => 
    (grupoPaises == "Alto ingreso" 
    ? d.incomeGroup == "High income"
    : d.region == "Latin America & Caribbean") 
    && d.publicPercentage
  )

  return  Plot.plot({
      height: 800,
      marginLeft: 150,
      marginRight: 70,
      x:{
        label:"Porcentaje de empleo público",
        tickFormat: d => d3.format(".0%")(d)
        },
      y:{label:"País", },
      marks: [
        // Bar for 'Población Total'
        Plot.barX(
          dataPlot,
          {
            x: "publicPercentage",
            y: "country",
            fill: d => d.country == 'Chile' ? "orange" : "grey",
            sort:{y:"x", reverse:true}
          }
        ),
      Plot.text(
          dataPlot,
          {
            x: "publicPercentage",
            y: "country",
            text: d => `${d3.format(".1%")(d.publicPercentage)} (${d.time})`,
            dx:5,
            textAnchor:"start"
          }
        ),
    
      ]
  })
})();
```


```js
const rankingOcupacionInformal = (function() {
  const dataPlot = [...dataPaises_ocupacion_informal].filter(d => 
    (grupoPaises == "Alto ingreso" 
    ? d.incomeGroup == "High income"
    : d.region == "Latin America & Caribbean") 
    && d.value
  )

  return Plot.plot({
    height: 800,
    marginLeft: 150,
    marginRight: 70,

    x:{
      label:"Porcentaje de ocupación informal",
      tickFormat: d => d3.format(".0%")(d/100)
    },
    y:{label:"País"},

    marks: [
      // Bar for 'Población Total'
      Plot.barX(
        dataPlot,
        {
          x: "value",
          y: "country",
          fill: d => d.country == 'Chile' ? "orange" : "grey",
          sort:{y:"x", reverse:true}
        }
      ),
     Plot.text(
        dataPlot,
        {
          x: "value",
          y: "country",
          text: d => `${d3.format(".1%")(d.value/100)} (${d.time})`,
          dx:5,
          textAnchor:"start"
        }
      ),
  
    ]
  })
})();


```



```js
const scateredPlotEmpleoInformalGDPPC = (function() {
  const countriesWithVisibleName = [
    "Chile","Norway", "Ireland", "Luxembourg", "Switzerland", "Denmark", "Belgium", "US", "Israel", "Panama", "Japan", "South Korea", "Austria", "France", "Poland", "Finland", "Hungary", "Spain", "Greece", "UK", "Australia", "Argentina", "Costa Rica", "Brazil", "Mexico", "Paraguay", "Peru", "Ecuador", "El Salvador", "Bolivia", "Honduras", "Nicaragua", "Guatemala", "Uruguay", "Haiti", "Bahamas", "Barbados", "Surinam", "Trinidad", "Guyana", "Jamaica", "Grenada", "Seychelles", "Palau", "Nauru", "Lithuania"
  ]

  const regexp = new RegExp(countriesWithVisibleName.map(d => d).join("|"))

  const dataPlot = [...dataPaises_sector].filter(d => 
    (grupoPaises == "Alto ingreso" 
    ? d.incomeGroup == "High income"
    : d.region == "Latin America & Caribbean") 
    && d.publicPercentage
  )

  //return Inputs.table(dataPlot)

  return Plot.plot({

    marginLeft: 150,
    marginRight: 70,

    x:{
      type:"log",
      grid:true
    },

    y:{
      type:"linear",
      tickFormat:(d => d3.format(".0%")(d)),
      grid:true
    },

    marks: [
      Plot.dot(
        dataPlot,
        {
          x: "gdppc",
          y: "publicPercentage",
          fill: d => d.country == "Chile" ? "orange" : "grey",
          tip:true,
          channels: {country: "country"},
        }
      ),
       Plot.text(
        dataPlot.filter(d => d.country.match(regexp)),
        {
          x: "gdppc",
          y: "publicPercentage",
          text: d => d.country ,
          dy:-10
        }
      )
  
    ]
  })
})();


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
const dataPlotEvolucionOcupados = _.chain(datosEmpleo)
    .filter(d => d.año == añoReferencia ? d.mes <= mesReferencia : d.año < añoReferencia && d.año > 2017)
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
        //topline: d.ocupacion_informal
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
        //topline: d.ocupacion_informal
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
        //topline: d.O + d.ocupacion_informal
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
        //topline: d.O + d.ocupacion_informal
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
        //topline: d.O + d.ocupacion_informal
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
        //topline: d.O + d.ocupacion_informal
      },
      // Uncomment the following blocks if you need 'Inactivas' and 'Menores de 15 años' categories
           
    ])
    .flatten() // Flatten the array of arrays
    .sortBy(d => d.order) // Sort by month
    .sortBy(d => d.mes) // Sort by month
    .sortBy(d => d.año) // Sort by year
    .filter(d => d.mes == mesReferencia)
    .value(); // Extract the value from the chain


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
  
  const labels = _.chain(dataPlot)
    .uniqBy(d => d.tipo)
    .sortBy(d => d.order)
    .reverse()
    .map(d => d.tipo)
    .value()

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
      domain: labels
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
          fill: (d) => (d.tipo == labels[0] ? "white" : "black"),
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

```sql
SELECT *
FROM ilo_ocupacion_informal
WHERE value < 10
```


```sql id=cifrasInformalidad
SELECT año, mes, O, ocupacion_informal, ocupacion_informal/O as tasaInformalidad
FROM ene_cambio_anual
WHERE mes = 4
ORDER BY año,mes
```

```js

Plot.plot({
    caption: fuenteINE,

    height: 300,
    marginLeft: 70,
    marginRight: 100,
    y: { 
    },
    x: {
    },
    color:{
    },
 
    marks: [
      
      Plot.lineY(
        cifrasInformalidad,
        {
          x: d => moment(`${d.año}-${d.mes}`, `YYYY-M`).toDate(),
          y: "ocupacion_informal",
        })

    ]
  })
```


```js

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


