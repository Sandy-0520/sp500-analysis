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
