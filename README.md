[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![Coverage](https://img.shields.io/badge/coverage-pytest%20--cov-green)]()
# **Simulador de Dudo**

Un simulador en Python del clásico juego de dados chileno, Dudo. Este proyecto ofrece una implementación central de la lógica del juego, con pruebas exhaustivas y análisis de cobertura de código.

El Dudo es un juego de dados estratégico y de engaños donde los jugadores tiran sus dados en secreto y hacen apuestas sobre el resultado total. El desafío consiste en mentir, predecir y decidir si creer o dudar de lo que dicen los oponentes. Los jugadores pierden o recuperan dados hasta que solo queda un ganador. Este simulador permite probar la mecánica y las reglas del juego.

Más información: [Aprende a jugar Dudo](https://www.donpichuncho.cl/aprende-a-jugar-dudo-en-cacho)
### **Características**

* **Implementación de la Lógica del Juego**: Las reglas principales del juego están implementadas en Python.  
* **Pruebas Unitarias Completas**: Un conjunto completo de pruebas con pytest para asegurar que la lógica del juego funcione como se espera.  
* **Reporte de Cobertura de Código**: Herramientas para analizar la cobertura de código de la fuente.


### Sigue estos pasos para configurar el proyecto y ejecutar las pruebas:

#### **🛠️ Instalación**

1. Clona este repositorio en tu máquina local.  
2. Navega al directorio del proyecto y abre una terminal.  
3. Instala las dependencias requeridas usando el archivo requirements.txt. Se recomienda usar un entorno virtual para evitar conflictos con los paquetes globales.

Para instalar los requrimientos use el siguente comando:
````
pip install -r requirements.txt
````
#### **✅ Ejecutar Pruebas**

Utiliza los siguientes comandos para ejecutar el conjunto de pruebas y verificar la funcionalidad del proyecto.
````
pytest
````
o
````
python3 -m pytest
````
#### **📊 Cobertura de Pruebas**

Para verificar la cobertura de código e identificar cualquier caso de prueba faltante, ejecuta uno de los siguientes comandos.
````
pytest --cov=src --cov-report=term-missing
````
o
````
python3 -m pytest --cov=src --cov-report=term-missing
````
