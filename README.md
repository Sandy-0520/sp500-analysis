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

-FASE-3: Almacenamiento de Datos en SQL Server con Python
  - **Archivo Python (PROYECTO3-pyodbc.py)**: Script para conectar a SQL Server y cargar datos desde archivos CSV.
  - **Archivo .env**: Contiene variables de entorno para la conexión a SQL Server (servidor, base de datos, usuario, contraseña).
  - **Carpeta .vscode**: Configuraciones de Visual Studio Code para el desarrollo.
  - **Archivos CSV**: Datos que se cargarán en SQL Server.

-FASE-4: Esta carpeta contiene el dashboard en Power BI para realizar un análisis descriptivo de las acciones del S&P 500 y sus precios. El tablero de control debe incluir KPIs en tarjetas, tooltips y bookmarks para una mejor visualización y navegación.

-FASE-5: Esta carpeta incluye los archivos necesarios para clasificar las acciones del S&P 500 en grupos basados en indicadores de volatilidad.
  -**Archivo Python (ETL_y_Clusterización_de_Empresas_del_S&P_500.ipynb)**: Notebook de Jupyter para realizar ETL y aplicar técnicas de clustering a las acciones del S&P 500 según su volatilidad.
  -**Archivo CSV**: Datos utilizados para el análisis de volatilidad y agrupamiento.
