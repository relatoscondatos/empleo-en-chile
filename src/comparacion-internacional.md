---
sql:
  ilo_sector_gdppc: data/ilo_sector_gdppc.parquet
  ilo_ocupacion_informal: data/ilo_ocupacion_informal.parquet
  ilo_sex_gpdpc: data/ilo_sex_gdppc.parquet
---

# Empleo en Chile vs el mundo

## ¿Cómo son las cifras de Chile al comparar con otros países?

La Organización Internacional del Trabajo (OIT) pública datos relacionados con la composición del empleo en distintos países.  Utilizaremos estos datos para comparar las cifras de Chile con las de otros países según los últimos datos disponibles de la OIT en Julio de 2024 para:

* Porcentaje de empleo informal
* Porcentaje de empleo en el sector público
* Porcentaje de empleo femenino

## Porcentaje de empleo informal

Aquellas personas ocupadas con una **ocupación informal** carecen de protección social y laboral adecuada.

Si bien el porcentaje de ocupación informal en Chile (${d3.format(".1%")(dictPaises["Chile"].value_informalidad)}) es menor que otros países de la región (ej Perú ${d3.format(".1%")(dictPaises["Peru"].value_informalidad)}), las cifras son mucho mayores que gran parte de los países de alto ingreso (ej España ${d3.format(".1%")(dictPaises["Spain"].value_informalidad)}).

```js
(function() {
  const dataPlot = _.chain([...dataPaises_ocupacion_informal])
  .map(d => {
    const record = {
      country:d.country,
      countryCode:d.countryCode,
      value:d.value/100,
      year:d.time
    }

    return record
  })
  .filter(d => d.countryCode && d.country.match(/Chile|UK|Brazil|Argentina|Haiti|Spain|Peru|Uruguay|Norway/))
  .sortBy(d => d.value)
  .value()

  return ranking({
    data:dataPlot, 
    r:25, 
    showLabel:true, 
    showXAxis:false, 
    height:150
  })
})()
```

En la siguiente imagen se visualizan las cifras de países considerados de Alto Ingreso por el Banco Mundial. La gran mayoría de estos países tiene cifras relativamente bajas (<5%), pero existen unos pocos con cifras cercanas a las de Chile (Uruguay, Corea del Sur, Australia, Brunei)
```js

(function() {
  const dataPlot = _.chain([...dataPaises_ocupacion_informal])
  .filter(d => d.countryCode && d.incomeGroup == "High income" )
  .map(d => {
    const record = {
      country:d.country,
      countryCode:d.countryCode,
      value:d.value/100,
      year:d.time
    }
    return record
  })
  .filter(d => d.countryCode)
  .value()

  return beeSwarm({
    data:dataPlot,
    r:11, 
    height:500,
    xScale:[0.0,0.65], 
    xLabel:"Proporción de ocupación informal (%)"
    })
})()
```

En la siguiente imagen se visualizan las cifras de países en la región de "América Latina y El Caribe" según clasificación del Banco Mundial. Chile está entre los países con menor proporción de empleo informal en este grupo.


```js

(function() {
  const dataPlot = _.chain([...dataPaises_ocupacion_informal])
  .filter(d => d.countryCode && d.region == "Latin America & Caribbean" )
  .map(d => {
    const record = {
      country:d.country,
      countryCode:d.countryCode,
      value:d.value/100,
      year:d.time
    }
    return record
  })
  .filter(d => d.countryCode)
  .value()

  return beeSwarm({
    data:dataPlot, 
    r:20, 
    height:300,
    xScale:[0.25,0.95],
    xLabel:"Proporción de ocupación informal (%)"
  })
})()
```


La siguiente visualización ilustra las cifras de empleo informal para todos los países con datos publicados por la OIT.
```js

(function() {
  const dataPlot = _.chain([...dataPaises_ocupacion_informal])
  .map(d => {
    const record = {
      country:d.country,
      countryCode:d.countryCode,
      value:d.value/100,
      year:d.time
    }
    return record
  })
  .filter(d => d.countryCode)
  .value()

  return beeSwarm({
    data:dataPlot, 
    r:7, 
    height:350,
    xLabel:"Proporción de ocupación informal (%)"
  })
})()

```




## Porcentaje de empleo público 

Las personas ocupadas clasificadas en la categoría de **asalariados del sector público** que son aquellás que están empleados por el gobierno o por entidades estatales.

Chile tiene un porcentaje de empleo público - **${d3.format(".1%")(dictPaises["Chile"].value_sector)}** - mayor a otros países de la región (ej **Perú ${d3.format(".1%")(dictPaises["Peru"].value_sector)}**), pero las cifras son menores que gran parte de los países de alto ingreso (ej **Reino Unido ${d3.format(".1%")(dictPaises["UK"].value_sector)}**).


```js

(function() {
  const dataPlot = _.chain([...dataPaises_sector])
  .map(d => {
    const record = {
      country:d.country,
      countryCode:d.countryCode,
      value:d.publicPercentage,
      year:d.time
    }
    return record
  })
  .filter(d => d.countryCode && d.country.match(/Chile|UK|Brazil|US|Spain|Peru|Uruguay|Norway|Sweden|Ecuador|Mexico/))
  .sortBy(d => d.value)  
  .value()


  return ranking({
    data:dataPlot, 
    r:25, 
    showLabel:true, 
    showXAxis:false, 
    height:150
  })
})()
```

En la siguiente imagen se visualizan las cifras de países considerados de Alto Ingreso por el Banco Mundial. La  mayoría de estos países tiene cifras relativamente altas (> 20%), pero también hay algunos con cifras cercanas a las de Chile (ej Uruguay, Estados Unidos, Holanda).

Son menos aquellos con cifras menores a Chile (ej Austria, Japón, Singapur)
```js
(function() {
  const dataPlot = _.chain([...dataPaises_sector])
  .filter(d => d.countryCode && d.incomeGroup == "High income" )
  .map(d => {
    const record = {
      country:d.country,
      countryCode:d.countryCode,
      value:d.publicPercentage,
      year:d.time
    }
    return record
  })
  .filter(d => d.countryCode)
  .value()

  return beeSwarm({
    data:dataPlot, 
    r:15, 
    height:350,
    xScale:[0.05,0.70],
    xLabel:"Proporción de empleo en sector público (%)"
  })
})()
```

En la siguiente imagen se visualizan las cifras de países en la región de "América Latina y El Caribe" según clasificación del Banco Mundial. 

Chile se encuentra en una posición intermedia.  Muchos países latinoamericanos tienen cifras más bajas (ej Ecuador, Guatemala, Honduras), y en entre los países del Caribe se observan cifras mayores (ej Bahamas, Trinidad y Tobago, Grenada)

```js

(function() {
  const dataPlot = _.chain([...dataPaises_sector])
  .filter(d => d.countryCode && d.region == "Latin America & Caribbean" )
  .map(d => {
    const record = {
      country:d.country,
      countryCode:d.countryCode,
      value:d.publicPercentage,
      year:d.time
    }
    return record
  })
  .filter(d => d.countryCode)
  .value()

  return beeSwarm({
    data:dataPlot, 
    r:18, 
    height:220,
    xScale:[0.03,0.35],
    xLabel:"Proporción de empleo en sector público (%)"
  })
})()
```

La siguiente visualización ilustra las cifras de empleo público para todos los países con datos publicados por la OIT.

```js

(function() {
  const dataPlot = _.chain([...dataPaises_sector])
  .map(d => {
    const record = {
      country:d.country,
      countryCode:d.countryCode,
      value:d.publicPercentage,
      year:d.time
    }
    return record
  })
  .filter(d => d.countryCode)
  .value()

  return beeSwarm({
    data:dataPlot, 
    r:7,
    height:350,
    xScale:[0.00,0.90],
    xLabel:"Proporción de empleo en sector público (%)"
  })
})()
```


## Porcentaje de empleo femenino

En el mundo hay algunos países que tienen cifras muy bajas de empleo femenino (ej **Irak ${d3.format(".1%")(dictPaises["Iraq"].value_female)}**) pero ellos son una exepción (y probablemente responde a temas culturales). La mayoría de los países tiene cifras entre un 35% y 55%.

Las cifras de Chile - **${d3.format(".1%")(dictPaises["Chile"].value_female)}** - no son las más bajas, pero son bajas comparado con otros países que se acercan al 50% (ej **Reino Unido ${d3.format(".1%")(dictPaises["UK"].value_female)}**)
```js
(function() {
  const dataPlot = _.chain([...dataPaises_sexo])
  .map(d => {
    const record = {
      country:d.country,
      countryCode:d.countryCode,
      value:d.femalePercentage,
      year:d.time
    }
    return record
  })
  .filter(d => d.countryCode && d.country.match(/Chile|Egypt|Iraq|India|Costa Rica|UK|Canada|Argentina|Brazil|Denmark/))
    .sortBy(d => d.value) 

  .value()


  return ranking({
    data:dataPlot, 
    r:25, 
    showLabel:true, 
    showXAxis:false, 
    xScale:[0.05,0.55], 
    height:150
  })
})()
```

En la siguiente imagen se visualizan las cifras de países considerados de Alto Ingreso por el Banco Mundial. Unos pocos tienen cifras bajas de empleo femenino (ej Emiratos Árabes Unidos), pero la mayoría tiene cifras entre 40% y 50%.  En este rango Chile tiene cifras relativamente bajas.

Entre aquellos con cifras más altas (cercanas al 50%) se encuentra, por ejemplo, a Barbados, Lituania y Letonia
```js
(function() {
  const dataPlot = _.chain([...dataPaises_sexo])
  .filter(d => d.countryCode && d.incomeGroup == "High income" )
  .map(d => {
    const record = {
      country:d.country,
      countryCode:d.countryCode,
      value:d.femalePercentage,
      year:d.time
    }
    return record
  })
  .filter(d => d.countryCode)
  .value()

  return beeSwarm({
    data:dataPlot, 
    r:12, 
    height:450,
    xScale:[0.12,0.53],
    xLabel:"Proporción de empleo femenino (%)"
  })
})()
```


Los países de "América Latina y El Caribe" Chile se concentran entre un 35% y un 50%, con Chile en una posición intermedia, similar a países como Brazil y Ecuador.

Entre los países con cifras más bajas está Costa Rica y Honduras, y por la parte alta Barbados, Bahamas y Bolivia.

```js

(function() {
  const dataPlot = _.chain([...dataPaises_sexo])
  .filter(d => d.countryCode && d.region == "Latin America & Caribbean" )
  .map(d => {
    const record = {
      country:d.country,
      countryCode:d.countryCode,
      value:d.femalePercentage,
      year:d.time
    }
    return record
  })
  .filter(d => d.countryCode)
  .value()

  return beeSwarm({
    data:dataPlot, 
    r:18, 
    height:250,
    xScale:[0.36,0.51],
    xLabel:"Proporción de empleo femenino (%)"
  })
})()

```

La siguiente visualización ilustra las cifras de empleo informal para todos los países con datos publicados por la OIT.

```js
(function() {
  const dataPlot = _.chain([...dataPaises_sexo])
  .map(d => {
    const record = {
      country:d.country,
      countryCode:d.countryCode,
      value:d.femalePercentage,
      year:d.time
    }
    return record
  })
  .value()


  return beeSwarm({
    data:dataPlot, 
    r:7,
    xScale:[0.05,0.55], 
    height:500,
    xLabel:"Proporción de empleo femenino (%)"
  })
})()
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
const country_codes = await FileAttachment("./data/country_codes.csv").csv();
const countryCodeDict3to2 = {}
country_codes.forEach((d) => {
  countryCodeDict3to2[d["alpha-3"]] = d["alpha-2"];
});

const dictPaises = {};

[...dataPaises_sexo].forEach(d => {
  dictPaises[d.country] = dictPaises[d.country] || {
    año:d.time,
  }

  dictPaises[d.country]["value_female"]= d.femalePercentage
});

[...dataPaises_sector].forEach(d => {
  dictPaises[d.country] = dictPaises[d.country] || {
    año:d.time,
  }
  dictPaises[d.country]["value_sector"]= d.publicPercentage
})

_.each([...dataPaises_ocupacion_informal], d => {
  dictPaises[d.country] = dictPaises[d.country] || {
    año:d.time,
  }
  dictPaises[d.country]["value_informalidad"]= d.value/100

})

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
    height=400,
    xLabel="Porcentaje"
    } = {}) {
  return Plot.plot({
    height: height,
    x:{
      tickFormat: d => showXAxis ? formatter(d) : "",
      tickSize:showXAxis ? 5 : 0,
      domain:xScale,
      label:xLabel
    },
    marks: [
      Plot.image(
        data,
        Plot.dodgeY({
          x: "value",
          width: 2 * r, 
          r: r,
          src: (d) => getFlagImageURL(d.countryCode),
          title: d => `${d["country"]}\n${formatter(d["value"])} (${d["year"]})`,
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


function ranking({
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
      inset:20
      //domain:xScale
    },
    marks: [
      Plot.image(
        data,
        Plot.dodgeY({
          x: (d,i) => i,
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
          x: (d,i) => i,
          width: 2 * r, 
          r: r,
          text: d => `${d["country"]}\n${formatter(d["value"])}\n(${d["year"]})`,
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
import { es_ES} from "./components/config.js";

// Set the default locale for D3 formatting
d3.formatDefaultLocale(es_ES);
```