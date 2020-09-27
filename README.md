# Quiz Examen Listas

Escribe un programa que se llame **combina_listas.py**

#### Su programa deberá tener el pseudocódigo generado por code2flow (10 pts)

#### Su programa deberá tener docstring. (10 pts)

*El programa No debe tener ninguna instrucción de input ni de print*

Define un método que se llame **combina** que recibe dos listas.

1. Si cualquiera de los parámetros *NO* es de <u>tipo</u> lista debe de regresar un **string** con la frase **Error tipo**. (20 pts)
2. Si la longitud de ambas listas NO es igual debe de regresar un **string** con la frase **Error longitud** (20 pts)

El método en dado caso de que ambos parámetros sean listas deberá de regresar una **lista** que contenga los elementos combinados de ambas listas. (40 pts)

Por ejemplo

`combina([1 , 2 , 3] , ["Hola", "es ", "Examen"])` regresará:  `[1 , "Hola" , 2, "es" , 3 , "Examen"]`

Usa para probar tu método el archivo **test1.py** proporcionado