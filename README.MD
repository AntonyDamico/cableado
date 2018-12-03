# Cableado

## Habitaciones

Para crear nuevos objetos tipo Habitacion se necesitan los siguientes argumentos
- int computadoras: número de computadoras en la habitación
- int x: posición en x de la habitación en el plano
- int y: posición en y de la habitación en el plano
- int ancho: valor del tamaño horizontal de la habitación
- int alto: valor del tamaño vertical de la habitación
- Habitacion hab_anterior: objeto Habitación al que está conectado la habitación actual
- int CONST_MTS: constante para calcular el cableado de bajadas

En main y pruebas hay ejemplos de la creación y el guardado de estos objetos en un array para representar un piso

Cuando se crea la primera habitación, la cual va a ser la principal se necesita usar el método para agregar la caja principal
```
habitacion_principal = Habitacion(0, 0, 0, 4, 4)
# En este método se pone la posición de la caja en la habitación principal
habitacion_principal.agregar_caja_principal(0,0)
```
Luego cada vez que se cree una habitación solo se debe especificar cuál es su habitación anterior para que se ubiquen las cajas
solas
```
habitacion_1 = Habitacion(2, 4, 0, 4, 4, habitacion_principal)
```

## Cableados

Los objetos Habitacion calculan su cantidad de cableado aereo y de bajada al ser creados, así que se puede simplemente
acceder al valor de cada uno a partir del objeto
```
print('cableado aereo:', habitacion_1.cableado_aereo)
```
Para el calculo del cableado de bajada se puede pasar una nueva constante o se puede dejar el predeterminado(8)
```
habitacion_2 = Habitacion(1, 8, 0, 4, 4, habitacion_1, 10)
print('cableado de bajada:', habitacion_2.cableado_bajadas
# Imprime el cableado de bajada calculado con la constante 10
```

## Plano
Para dibujar el plano solo se debe usar la función dibujar y se le debe pasar un array de objetos Habitacion
```
habitaciones = [habitacion_principal, habitacion_1, habitacion_2]
plano.dibujar(habitaciones)
```