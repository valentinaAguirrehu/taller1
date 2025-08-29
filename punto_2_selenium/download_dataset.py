import os
import requests
import pandas as pd

# Carpeta donde guardar los archivos
os.makedirs("datasets", exist_ok=True)

# URL del dataset en CSV (API Socrata)
CSV_URL = "https://www.datos.gov.co/api/views/xbwb-yz9d/rows.csv?accessType=DOWNLOAD"

# Rutas de salida
csv_path = "datasets/atenciones_salud_migrante.csv"
excel_path = "datasets/atenciones_salud_migrante.xlsx"

# Descargar CSV
print("Descargando CSV...")
r = requests.get(CSV_URL)
r.raise_for_status()
with open(csv_path, "wb") as f:
    f.write(r.content)
print(f"CSV descargado en: {os.path.abspath(csv_path)}")

# Convertir CSV a Excel con pandas
print("Convirtiendo CSV a Excel...")
df = pd.read_csv(csv_path)
df.to_excel(excel_path, index=False)
print(f"Excel generado en: {os.path.abspath(excel_path)}")
