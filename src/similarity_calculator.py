#Descripción del concepto calculo de similitud

El cálculo de similitud entre secuencias de ADN se basa en algoritmos de alineamiento y modelos evolutivos. 
Se evalúan coincidencias de bases, inserciones o deleciones (indels) y la longitud del tramo comparado. 
Estos criterios permiten determinar qué tan parecidas son dos secuencias y si comparten un ancestro común (homología).

#Criterios para el calculo de similitud

##Coincidencias (Matches): 
Se otorga un puntaje positivo cuando ambas secuencias tienen exactamente el mismo nucleótido (A, T, C o G) en la misma posición.
  
##Desajustes (Mismatches): 
Se aplica una penalización cuando las bases no coinciden. 

##Penalización por huecos (Gaps): 
Se resta puntuación cuando se introducen espacios para compensar inserciones o deleciones (indels).
