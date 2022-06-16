# Ripio
Mejoras:
  - Agregar un login para los usuarios. Esto facilitaria el manejo de autorizacion con respecto a acceso a los datos de los usuarios. 
     En estos momemtos se maneja con un if, y el usuario 'logueado' esta hardcodiado.
  - Mejorar un poco lo que es la validacion de datos cuando llegan a las views. Por ahi tener una clase validator que automaticamente analize lo que uno precise del objeto que entra
  - La ui tiene mucho por mejorar, no pude dedicarle mucho tiempo a eso
  - Agregar mas tests, sobretodo edge cases
  - Por ahi limpiar un poco el codigo y ver si se pueden dividir funciones largas en otras mas chicas que tengan una sola responsabilidad.

Tengo algunas dudas de si esta bien que el codigo que haga el guardado de datos este dentro de views.
