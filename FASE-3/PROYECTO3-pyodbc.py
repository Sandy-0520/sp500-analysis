# PROYECTO3 Sandy Acosta

import pyodbc
import pandas as pd


# 1. Configuración de la conexión
server = '---'
database = '---'
username = '---'
password = '---'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Conexión a la base de datos
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# 2.Crear una tabla (si no existe)

cursor.execute('''
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='CompanyProfiles' AND xtype='U')
    CREATE TABLE CompanyProfiles (
        Symbol VARCHAR(50) NOT NULL,
        Company VARCHAR(50),
        Sector VARCHAR(50),
        Headquarters VARCHAR(50),
        FechaFundada VARCHAR(50),
     CONSTRAINT CompanyProfiles_pk PRIMARY KEY (Symbol)
    )
''')

cursor.execute('''
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Companies' AND xtype='U')
    CREATE TABLE Companies (
        Date DATE,
        Symbol VARCHAR(50),
        Clos FLOAT,
        PRIMARY KEY (Date, Symbol),
        FOREIGN KEY (Symbol) REFERENCES CompanyProfiles(Symbol)
    )
''')
conn.commit()

# Ruta a los archivos CSV

CompanyProfiles_csv= 'C:/Users/SANDY/Documents/SANDY/TIC/TALENTO-TECH/PROYECTO-ETL/PROYECTO-3/CSV/CompanyProfiles.csv'
Companies_csv= 'C:/Users/SANDY/Documents/SANDY/TIC/TALENTO-TECH/PROYECTO-ETL/PROYECTO-3/CSV/Companies.csv'

 # Lee los datos del archivo CSV en DataFrames
CompanyProfiles_df= pd.read_csv(CompanyProfiles_csv,sep=';', quotechar='"')
Companies_df= pd.read_csv(Companies_csv,sep=';', quotechar='"')


# Imprime los nombres de las columnas
print("Columnas en CompanyProfiles:")
print(CompanyProfiles_df.columns)

print("\nColumnas en Companies:")
print(Companies_df.columns)

# Cargar datos en la tabla CompanyProfiles
for index, row in CompanyProfiles_df.iterrows():
    cursor.execute('''
        INSERT INTO CompanyProfiles (Symbol, Company, Sector, Headquarters, FechaFundada)
        VALUES (?, ?, ?, ?, ?)
    ''', row['Symbol'], row['Company'], row['Sector'], row['Headquarters'], row['FechaFundada'])
conn.commit()

# Cargar datos en la tabla Companies
print("paso")
for index, row in Companies_df.iterrows():
    cursor.execute('''
        INSERT INTO Companies (Date, Symbol,  Clos)
        VALUES (?, ?, ?)
    ''', row['Date'], row['Symbol'], row['Clos'] )
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

print("Datos cargados exitosamente en SQL Server.")
