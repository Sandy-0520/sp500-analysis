# sp500-analysis
## Descripción del Proyecto
El proyecto analiza las empresas del S&P 500 mediante la recolección y almacenamiento de datos en SQL Server, el desarrollo de dashboards en Power BI para visualizar métricas clave, y la aplicación de técnicas de clusterización para agrupar acciones según su volatilidad, ofreciendo una comprensión más profunda del comportamiento del mercado.
## Requisitos
- Python 3.x
- Librerías: `pandas`, `sqlalchemy`, `pyodbc`, `scikit-learn`
- Power BI Desktop
- SQL Server
## Estructura del Proyecto
- FASE-1: Esta carpeta contiene todos los elementos necesarios para la ** ETL (extracción, transformación y carga de datos)** del proyecto. Incluye:
  - **Archivo Python (`Proyecto1.py`)**: Script principal que realiza el proceso completo de ETL (Extracción, Transformación y Carga) para los datos de las empresas del S&P 500. 
  - **Archivo `.env`**: Contiene las variables de entorno necesarias para el script Python, como credenciales de acceso y configuraciones específicas para la conexión a las fuentes de datos.
  - **Carpeta `data/`**: Incluye los datos en formato CSV y otros archivos relacionados que se utilizan para el análisis y la preparación de datos.
  - **Carpeta `log/`**:  Archivos de registro con detalles sobre el progreso del script y errores.
  - **Tablas de Empresas-table_empresas.csv**: Archivos con información de las empresas del S&P 500.

- FASE-3: Almacenamiento de Datos en SQL Server con Python
  - **Archivo Python (PROYECTO3-pyodbc.py)**: Script para conectar a SQL Server y cargar datos desde archivos CSV.
  - **Archivo .env**: Contiene variables de entorno para la conexión a SQL Server (servidor, base de datos, usuario, contraseña).
  - **Carpeta .vscode**: Configuraciones de Visual Studio Code para el desarrollo.
  - **Archivos CSV**: Datos que se cargarán en SQL Server.

- FASE-4: Esta carpeta contiene el dashboard en Power BI para realizar un análisis descriptivo de las acciones del S&P 500 y sus precios. El tablero de control debe incluir KPIs en tarjetas, tooltips y bookmarks para una mejor visualización y navegación.

- FASE-5: Esta carpeta incluye los archivos necesarios para clasificar las acciones del S&P 500 en grupos basados en indicadores de volatilidad.
  - **Archivo Python (ETL_y_Clusterización_de_Empresas_del_S&P_500.ipynb)**: Notebook de Jupyter para realizar ETL y aplicar técnicas de clustering a las acciones del S&P 500 según su volatilidad.
  - **Archivo CSV**: Datos utilizados para el análisis de volatilidad y agrupamiento.

## Instrucciones de Instalación y Uso
- Clonar el repositorio:
Se debe clonar el repositorio del proyecto desde GitHub y acceder al directorio del proyecto.

- Instalar las dependencias:
Asegúrarse de tener pip instalado y actualizado. Luego, instale las dependencias necesarias utilizando el archivo requirements.txt proporcionado.

- Configurar el entorno:
  - Archivo .env:Crear un archivo llamado .env en el directorio raíz del proyecto.
  - Agregar las credenciales necesarias para la conexión a SQL Server en el archivo .env.
  - Ajustar los scripts:
Revisar y actualizar los scripts de las fases correspondientes para asegurar que la configuración de conexión a SQL Server sea correcta.

- Ejecutar los scripts en el orden correspondiente para realizar un analisis completo.
  
- Revisa los resultados:
  - Verificar que los datos se hayan cargado correctamente en la base de datos.
  - Revisar el dashboard creado en Power BI.
  - Consultar los resultados del clustering en el notebook de Jupyter.
 
## Fases de Proyecto
- Fase 1: Obtención de Datos
  - Recolección de información financiera de las empresas del S&P 500 desde una fuente de datos en línea y recopilación de datos históricos sobre el rendimiento de las acciones durante el último año.
    
- Fase 3: Almacenamiento en SQL Server
  - Importación de los datos procesados y validados a una base de datos en SQL Server para su almacenamiento y gestión eficiente.
 
- Fase 4: Análisis y Dashboard en Power BI
  - Desarrollo de un dashboard interactivo en Power BI que incluye KPIs, tooltips y bookmarks. Este dashboard incorpora un análisis descriptivo e inferencial de los precios de las acciones, proporcionando una visión detallada de las tendencias y patrones en los datos.

- Fase 5: Clusterización de las Acciones
  - Implementación de técnicas de clustering para clasificar las acciones en grupos basados en sus características de volatilidad y rendimiento.
 
- Fase 6: Publicación en GitHub
  - Subida del proyecto al repositorio de GitHub, con la inclusión del código, los datos y una guía detallada en el archivo README.md para facilitar la comprensión y uso del proyecto.

