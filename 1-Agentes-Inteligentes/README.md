![](ia.png)
# Desarrollo de entornos y agentes
**Evaluación de competencias 1**

## Desarrollo de entornos y agentes

### Objetivo de la tarea

Esta tarea tiene como objetivo revisar y dejar claro el desarrollo de las técnicas que se 
estudiarán en el curso como el desarrollo de programas de agentes racionales, y se revisará
en forma superficial el desarrollo de agentes *reactivos* y *reactivos basados en modelo*, así
como las peculiaridades de diferentes tipos de entornos. 

Igualmente, esta tarea es un primer acercamiento a `python` y a la forma en la que vamos a
trabajar el resto del curso. Es por esta razón que la mayoría del código ya viene programado.


### Trabajo a realizar

**Importante:** Todo el desarrollo que se realice para la tarea debe de ser
incluido en el archivo `tarea_1.py`. Recuerda que los commits que hagas de tus
avances son importantes para que como profesor pueda medir lo que vas haciendo.

En esta tarea realiza las siguiente acciones:

1. Desarrolla un entorno similar al de los dos cuartos (el cual se
   encuentra en el módulo doscuartos_o.py), pero con tres cuartos en
   el primer piso, tres cuartos en el segundo piso y tres cuartos en el 3er piso.
   
   El entorno se llamará `NueveCuartos`.

   Las acciones totales serán
   
   ```
   ["ir_Derecha", "ir_Izquierda", "subir", "bajar", "limpiar", "nada"]
   ``` 
    
   La acción de `"subir"` solo es legal en los primeros dos pisos, en los cuartos de la derecha, 
   mientras que la acción de `"bajar"` solo es legal en los dos pisos de arriba de arriba y en 
   el cuarto de la izquierda.

   Las acciones de subir y bajar son mas costosas en término de
   energía que ir a la derecha y a la izquierda, por lo que la función
   de desempeño debe de ser de tener limpios todos los cuartos, con el
   menor numero de acciones posibles, y minimizando subir y bajar en
   relación a ir a los lados. El costo de limpiar es menor a los costos
   de cualquier acción.

2. Diseña un Agente reactivo basado en modelo para este entorno y
   compara su desempeño con un agente aleatorio despues de 200 pasos
   de simulación.

3. A este modelo de `NueveCuartos`, modificalo de manera que el
   agente solo pueda saber en que cuarto se encuentra pero no sabe si
   está limpio o sucio. Utiliza la herencia entre clases para no escribir código redundante.

   A este nuevo entorno llamalo `NueveCuartosCiego`.

   Diseña un agente racional para este problema, pruebalo y comparalo
   con el agente aleatorio.

4. Al modelo original de `NueveCuartos` 
   modificalo para que cuando el agente decida aspirar, el 80% de las
   veces limpie pero el 20% (aleatorio) deje sucio el cuarto. Igualmente, 
   cuando el agente decida cambiar de cuarto, se cambie correctamente de cuarto el 80% de la veces,
   el 10% de la veces se queda en su lugar y el 10% de las veces realiza una acción legal aleatoria. Diseña
   un agente racional para este problema, pruebalo y comparalo con el
   agente aleatorio.

   A este entorno llámalo `NueveCuartosEstocástico`.

Todos los incisos tienen un valor de 25 puntos sobre la calificación de
la tarea.

