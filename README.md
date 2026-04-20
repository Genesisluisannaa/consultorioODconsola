
---

# 🦷 Sistema de Gestión Odontológica (Python CLI)

<p align="center">
  Aplicación de consola robusta para la administración de pacientes, citas y facturación de un consultorio dental, desarrollada bajo estándares de algoritmia pura.
</p>

<p align="center"> 
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"> 
  <img src="https://img.shields.io/badge/Data_Persistence-JSON-f5da55?style=for-the-badge&logo=json&logoColor=black" alt="JSON">
  <img src="https://img.shields.io/badge/Algorithm-Custom-orange?style=for-the-badge" alt="Custom Algorithms">
</p>

---

### 👤 Sobre el Proyecto

Este proyecto es una herramienta de gestión para consultorios odontológicos que permite registrar pacientes bajo diferentes modalidades (Particular, EPS, Prepagada). El software automatiza el cálculo de costos según el tipo de atención, prioriza la integridad de los datos y ofrece análisis estadísticos en tiempo real, todo mediante una interfaz de línea de comandos (CLI) intuitiva.

### ✨ Características Técnicas

* **💾 Persistencia de Datos:** Implementación de lectura y escritura de archivos en formato `.txt` (JSON) para asegurar que la información se mantenga tras cerrar la sesión.
* **⚙️ Lógica Algorítmica Pura:** El sistema no depende de funciones integradas como `len()` o `.append()`, utilizando en su lugar algoritmos de conteo y expansión de memoria manuales.
* **📊 Análisis de Datos:** * **Bubble Sort:** Algoritmo de ordenamiento personalizado para clasificar clientes por valor de pago de forma descendente.
    * **Búsqueda Lineal:** Localización eficiente de registros mediante el número de cédula.
* **🛡️ Validación Robusta:** Control de excepciones con `try/except` para prevenir errores de entrada y normalización de texto (insensibilidad a mayúsculas/minúsculas y manejo de tildes).

### 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x.
* **Persistencia:** Módulo `json` nativo.
* **Entorno:** Terminal / Consola de comandos.
* **Paradigma:** Programación Estructurada y Modular.

### 🚀 Instalación y Ejecución

Para ejecutar el sistema en tu entorno local:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/MarioSuero/odontologia-cli.git
   ```

2. **Navegar a la carpeta:**
   ```bash
   cd odontologia-cli
   ```

3. **Ejecutar la aplicación:**
   ```bash
   python main.py
   ```

### 📁 Estructura del Proyecto

```text
├── main.py             # Código fuente principal con toda la lógica
├── consultorio.txt     # Base de datos en formato JSON (se crea al primer registro)
└── README.md           # Documentación del proyecto
```

---

### 📘 Guía Técnica para Desarrolladores

Este programa fue construido bajo **restricciones técnicas específicas** para demostrar el manejo de algoritmos fundamentales sin depender de abstracciones de alto nivel de Python.

#### 1. Gestión de Memoria y Listas
Para suplir la ausencia de métodos nativos, se desarrollaron funciones auxiliares:
* **`get_length()`**: Calcula el tamaño de cualquier estructura iterable mediante un ciclo y un acumulador manual.
* **`Notes()`**: Emplea la concatenación de listas (`lista + [elemento]`) para gestionar el crecimiento dinámico de la base de datos en memoria.

#### 2. Reglas de Negocio
El sistema cruza dinámicamente dos variables para determinar el precio final:
* **Valor Base:** Definido por el convenio del cliente (EPS, Particular o Prepagada).
* **Valor Operativo:** Costo de la atención (Limpieza, Calzas, etc.) multiplicado por la cantidad, validando que ciertos procedimientos tengan cantidades fijas (ej. Diagnóstico siempre es 1).

#### 3. Normalización de Datos
Para mejorar la experiencia de usuario (UX) en consola, el sistema procesa las entradas:
* Transforma entradas como `"eps"`, `"EPS"` o `"Eps"` en un token válido.
* Corrige automáticamente la ausencia de tildes en palabras clave como `"extraccion"` o `"diagnostico"` para asegurar la coincidencia con los diccionarios de costos.

---

### 📈 Estado del Proyecto

* **Estado:** ✅ Funcional y Estable.
* **Próximas mejoras:** Implementación de generación de facturas en PDF y módulo de agenda de citas por horas.

