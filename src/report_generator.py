# Descripción 
Este archivo contiene el script para la generación de informes a partir de la comparación de las secuencias analizadas.
El informe deberá incluir: 

## Tipos de mutaciones detectadas y su posición

### Sustitución

Ocurre cuando un nucleótido es reemplazado por otro.

**Ejemplo**

Referencia:

```text
ATGCGA
```

Muestra:

```text
ATGTGA
```

Resultado:

```text
Posición 4: C → T
```

### Inserción

Ocurre cuando aparecen nucleótidos adicionales en la secuencia de muestra.

**Ejemplo**

Referencia:

```text
ATGCA
```

Muestra:

```text
ATGGCA
```

Resultado:

```text
Inserción de G en la posición 4.
```

### Deleción

Ocurre cuando un nucleótido presente en la referencia desaparece en la muestra.

**Ejemplo**

Referencia:

```text
ATGGCA
```

Muestra:

```text
ATGCA
```

Resultado:

```text
Deleción de G en la posición 4.
```

##Implicaciones de las mutaciones detectadas
Esta información deberá contrastarse con publicaciones 

##Conclusión
Conclusiones extraidas del análisis 
          
##Bibliografía
Listado completo de las referencias bibliográficas y fuentes de información empleadas


