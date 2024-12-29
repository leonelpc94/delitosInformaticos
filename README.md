Procesamiento de Datos
Se utilizó  la tecnología  JupyterLab (v2024.10.0) mediante una extensión en el editor de código Visual Studio Code, para
realizar la conformación y depuración del dataset. Se utilizó el lenguaje de programación python (v3.12.3) además de las 
bibliotecas pandas (v2.2.3) y numpy(v2.1.3). Después, se cargó el dataset en el editor para ser modificado utilizando pandas.

A continuación, se separaron los datos por el año en que ocurrieron los hechos del delito el cual es una columna del dataset, 
luego se eliminaron las columnas con datos que no serán relevantes para el estudio y por último se crearon cuatro dataset 
separándolos por año  

Luego, se cargó el dataset del año 2023 que es al cual se le va hacer el estudio, se seleccionaron los delitos con único 
ya que estos se repetían en el dataset original, se aplicó el mismo método para el nombre del departamento y el año. con el 
nombre de los delitos se crearon nuevas columnas y el nombre de los departamentos fueron agregados a una nueva columna para 
crear un nuevo dataset rectangular con dimensiones R32x69 y utilizando los datos de la columna  número de incidentes se 
agregaron los valores de la nueva tabla 

Posteriormente se realizó una sumatoria por columna (tipo de delito) y una sumatoria total de todos los datos, esto para sacar
un promedio de todos los delitos y los delitos que no superan el 1% de de ocurrencia del total fueron descartados y sus columnas fueron eliminadas y se creó una nueva para agruparlos a todos la sumatoria de esto es el 3.5 % del total 

Finalmente, se calcularon los porcentajes de los datos utilizando la ecuación X=DTD*100 (D = delito por departamento; 
TD = total delitos por departamento ) por departamento se reemplazaron los valores en el dataset por los porcentajes, se 
redondearon las cifras a 2 decimales  y se creó un nuevo archivo csv.

Por último se muestra en la figura 6, el dataset ya conformado para su posterior análisis mediantes las herramientas y 
técnicas de análisis de espacial de datos. Adicionalmente se adjunta en el apartado de Anexos, el archivo final de JupyterLab
