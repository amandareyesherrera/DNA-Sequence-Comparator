# DNA Sequence Comparator

## Índice del proyecto

1. Descripción
2. Objetivos
3. Funcionamiento
4. Tipos de mutaciones detectadas
5. Instalación
6. Uso
7. Autores
   
## Descripción

Este proyecto tiene como objetivo comparar dos secuencias genéticas para identificar diferencias entre ellas y detectar posibles mutaciones.

La herramienta analiza una secuencia de referencia y una secuencia de muestra, calculando el porcentaje de similitud entre ambas e identificando las posiciones donde existen cambios genéticos.

Las diferencias detectadas se clasifican en:

- Sustituciones
- Inserciones
- Deleciones

La comparación de secuencias es una de las técnicas más utilizadas en bioinformática y genómica. Permite estudiar la evolución de organismos, detectar variantes genéticas y analizar mutaciones presentes en muestras biológicas.

## Objetivos

- Comparar dos secuencias de ADN.
- Calcular el porcentaje de similitud.
- Detectar diferencias entre secuencias.
- Identificar la posición de cada cambio.
- Clasificar las mutaciones encontradas.
- Generar un informe de los resultados.

## Funcionamiento

El programa recibe dos secuencias:

1. Secuencia de referencia.
2. Secuencia de muestra.

Posteriormente realiza los siguientes pasos:

1. Validación de las secuencias.
2. Comparación nucleótido a nucleótido.
3. Cálculo del porcentaje de similitud.
4. Detección de diferencias.
5. Clasificación de mutaciones.
6. Generación de informe.

## Tipos de mutaciones detectadas

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

## Instalación

### Requisitos previos

Antes de ejecutar el proyecto es necesario disponer de:

- Python 3.10 o superior
- Git

### Clonar el repositorio

```bash
git clone https://github.com/amandareyesherrera/DNA-Sequence-Comparator.git
```

### Acceder al directorio del proyecto

```bash
cd dna-sequence-comparator
```

## Uso

### Preparar los archivos de entrada

Guardar las secuencias a comparar en la carpeta `data/`:

**reference_sequence.txt**

```text
ATGCGATACGATCGATCGAT
```

**sample_sequence.txt**

```text
ATGCTATACGATCGATCGAT
```

### Ejecutar el programa

Desde la carpeta principal del proyecto:

```bash
python src/main.py
```

### Resultado esperado

El programa mostrará:

- Porcentaje de similitud.
- Posiciones donde existen diferencias.
- Tipo de mutación detectada.
- Resumen final de cambios encontrados.

### Ejemplo de salida

```text
--------------------------------
ANÁLISIS DE SECUENCIAS
--------------------------------

Similitud: 98.5 %

Mutaciones detectadas:

Posición 152
Tipo: Sustitución
A → G

Posición 367
Tipo: Deleción
T eliminada

Resumen:

Sustituciones: 1
Inserciones: 0
Deleciones: 1

Total de cambios: 2
```

## Autores

Proyecto desarrollado por:

- Amaia Astrain López
- Amanda Reyes Herrera
- Ana Belén Liébana Vilches
- Ana Martín Sánchez

## Licencia

Este proyecto se distribuye bajo la licencia MIT.

Consulta el archivo `LICENSE` para obtener más información.
