# Análisis de datos de la NASA
## Descubriendo asteroides cercanos a la Tierra y otros planetas
<em>Analisis de datos y extraccion desde API </em>

Existen proyectos que nos permiten explorar el vasto universo y descubrir información fascinante. En este proyecto de análisis de datos, nos sumergimos en la API de la NASA para extraer datos sobre asteroides y detalles de acercamiento. Utilizando Python con Pandas, realizamos la extracción y creación de diferentes tablas, centrándonos en los asteroides cercanos a la Tierra y otros tres planetas del sistema solar. Además, creamos visualizaciones en Tableau Public, mostrando gráficos que diferencian los asteroides según su diámetro en kilómetros y el año de su acercamiento aproximado. También exploramos datos sobre la peligrosidad de estos asteroides en cada uno de los cuerpos celestes, proporcionando información clave sobre su conteo, características y distancias de error.

![Dashboard 2](https://github.com/javierahartog/Portafolio/assets/134547879/2d17b948-e405-4fe5-bef1-c898dedd0e65)

El proyecto de análisis de datos de la API NeoWs (Near Earth Object Web service) de la NASA comienza con la extracción de datos utilizando Python y la biblioteca Pandas. Nos enfocamos en obtener información sobre asteroides cercanos a la Tierra y otros tres planetas seleccionados. Creamos dos dataframe diferentes, el primero llamado Asteroids para los datos generales y un segundo dataframe para los datos de close approach. Utilizando las capacidades de extracción y manipulación de datos de Pandas, dimos formato a las variables, subdividimos y reordenamos la forma en que nos entregaba información la API y dejamos lista nuestra base de datos para poder conectarla a través de Tableau. Como estamos utilizando Tableau Public, no es posible conectarla directamente con el código Python, por lo que tuvimos que crear un enlace a través de archivos Excel. En caso de usar Tableau Desktop solo deberíamos subir nuestro código a través de Tabpy y conectarnos a la API en tiempo real

[Codigo Python](https://github.com/javierahartog/Portafolio/blob/09f902909f04b8cb8aad32d45377e4ff70b446a1/Nasa_NEOWS/Preparacion_datos.py)

![NEOWS python](https://github.com/javierahartog/Portafolio/assets/134547879/cf78a051-ccfe-47f1-9075-f7720fee24a8)

A continuación, utilizamos Tableau Public para crear visualizaciones interactivas. En nuestro análisis, presentamos dos gráficos iniciales para destacar los asteroides cercanos y potencialmente peligrosos. Estos gráficos nos permiten diferenciar los asteroides según su diámetro en kilómetros y el año de su acercamiento aproximado. De esta manera, podemos visualizar la distribución y la relación entre estos dos factores clave.

[Dashboard interactivo Tableau Public](https://public.tableau.com/views/Neows/Dashboard2?:language=en-US&:display_count=n&:origin=viz_share_link)


![NEOWS1](https://github.com/javierahartog/Portafolio/assets/134547879/d67ad305-8efa-4754-b549-25129e89f25b)

Además, nos sumergimos en los datos sobre la peligrosidad de los asteroides en relación con cada uno de los cuerpos celestes analizados. Analizamos el conteo de asteroides cercanos en cada cuerpo celeste y destacamos las características de los asteroides más peligrosos. Estos datos incluyen la distancia de error en kilómetros y la velocidad relativa de los asteroides, lo que nos proporciona información esencial para evaluar el riesgo potencial y tomar medidas preventivas.

![NEOWS2](https://github.com/javierahartog/Portafolio/assets/134547879/f66573c1-0e3d-42a4-aff2-be3efc614dff)

Gracias a las visualizaciones interactivas en Tableau Public, pudimos observar patrones y tendencias relacionados con el diámetro de los asteroides y su acercamiento aproximado en diferentes años. Estas visualizaciones nos proporcionan una visión clara y comprensible de la distribución de los asteroides y nos ayudan a identificar aquellos que representan un mayor potencial de peligro.

Además, al analizar los datos sobre la peligrosidad de los asteroides en relación con los cuerpos celestes específicos, hemos obtenido información valiosa sobre el conteo de asteroides cercanos y las características de los más peligrosos, como la distancia de error en kilómetros y la velocidad relativa. Estos datos son fundamentales para evaluar el riesgo potencial y tomar medidas preventivas en cuanto a posibles impactos.

El proyecto demuestra la importancia del análisis de datos en el campo de la astronomía y la exploración espacial. Gracias a la API de la NASA y las herramientas de análisis utilizadas, hemos podido adentrarnos en el estudio de los asteroides y comprender mejor su comportamiento y su potencial impacto en nuestro planeta y otros cuerpos celestes.

El análisis de datos nos brinda una perspectiva más clara y precisa sobre el universo que nos rodea, permitiéndonos tomar decisiones informadas y desarrollar estrategias para la mitigación de riesgos. Con proyectos como este, continuaremos expandiendo nuestro conocimiento y nuestra capacidad para comprender y proteger nuestro entorno espacial.
