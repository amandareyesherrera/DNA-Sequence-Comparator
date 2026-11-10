# Estructura del proyecto

Este documento describe la organización de carpetas, módulos y documentos que componen el proyecto DNA Sequence Comparator.

## Carpetas

### data/
Contiene las secuencias genéticas utilizadas como entrada para el programa.

### src/
Contiene el código fuente principal del proyecto.

### docs/
Contiene la documentación técnica y organizativa del proyecto.

### tests/
Contiene los archivos utilizados para realizar pruebas y validaciones del sistema.

## Estructura de directorios

```text
dna-sequence-comparator/
│
├── data/
│   ├── reference_sequence.txt
│   └── sample_sequence.txt
│
├── src/
│   ├── main.py
│   ├── sequence_reader.py
│   ├── similarity_calculator.py
│   ├── mutation_detector.py
│   └── report_generator.py
│
├── tests/
│
├── docs/
│   ├── project_structure.md
│   ├── task_distribution.md
│   └── project_proposal.md
│
├── README.md
└── LICENSE
```

## Descripción de los módulos

### sequence_reader.py

Responsable de la lectura y validación de las secuencias genéticas proporcionadas por el usuario.

Funciones principales:

- Leer los archivos de entrada.
- Comprobar que las secuencias contienen únicamente nucleótidos válidos (A, T, C y G).
- Preparar los datos para su análisis posterior.

### similarity_calculator.py

Responsable de comparar ambas secuencias y calcular su grado de similitud.

Funciones principales:

- Comparar las secuencias nucleótido a nucleótido.
- Contabilizar coincidencias y diferencias.
- Calcular el porcentaje de similitud entre ambas secuencias.

### mutation_detector.py

Responsable de detectar y clasificar las diferencias encontradas.

Funciones principales:

- Identificar cambios entre las secuencias.
- Detectar sustituciones.
- Detectar inserciones.
- Detectar deleciones.
- Registrar la posición de cada mutación.

### report_generator.py

Responsable de generar el informe final de resultados.

Funciones principales:

- Mostrar el porcentaje de similitud.
- Listar las mutaciones detectadas.
- Presentar la posición y el tipo de cada cambio.
- Generar un resumen estadístico de resultados.

### main.py

Módulo principal del proyecto.

Funciones principales:

- Coordinar la ejecución de todos los módulos.
- Controlar el flujo general del programa.
- Invocar los distintos módulos en el orden adecuado.
- Recibir los resultados obtenidos por cada módulo.
- Centralizar la ejecución completa del programa.

## Documentación

### project_proposal.md

Contiene la descripción de la propuesta, la justificación de la elección del proyecto y sus aplicaciones en bioinformática.

### project_structure.md

Describe la organización de carpetas, archivos y módulos que componen el proyecto.

### task_distribution.md

Detalla el reparto de responsabilidades entre los integrantes del equipo y las tareas asignadas a cada miembro.

### README.md 

Documento principal del proyecto.

Contiene:

- Descripción general del proyecto.
- Objetivos.
- Guía de instalación y uso.
- Ejemplos de ejecución.
- Información sobre los autores.
- Información sobre la licencia.

### LICENSE

Archivo que define los términos legales bajo los cuales se distribuye el proyecto.
