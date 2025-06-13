import pandas as pd
print("nasheeeeeee")
data set:
objetivo:
import pandas as pd
Si trabajas con Google Colab, usa pandas para leer los archivos. Ejemplo:
import pandas as pd
# Para CSV
df = pd.read_csv('/path/a/tu/dataset.csv')
# Para XLS
df = pd.read_excel('/path/a/tu/dataset.xlsx')
Si estás trabajando con archivos .shp (shapefiles), usa geopandas:
import geopandas as gpd
gdf = gpd.read_file('/path/a/tu/dataset.shp')
Visualización:
Tablas: Usa df.head() para ver las primeras filas de tu dataset.
Gráficos:
Para gráficos simples usa matplotlib o seaborn:
import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(df)
plt.show()
Para análisis más complejos: Dependiendo del dataset, puedes hacer diagramas de barras, histogramas, gráficos de dispersión, etc.
Calidad y estadísticos
Usa df.describe() para ver estadísticas básicas como la media, mediana, desviación estándar, etc.
Usa df.isnull().sum() para comprobar si hay valores faltantes.
Si encuentras valores nulos, puedes decidir si eliminarlos o imputarlos.
4. Explotación de la Información
Combinación de dataframes:
Si tienes más de un dataframe, puedes combinarlos con:
merge(): Para hacer una combinación basada en una columna común.
join(): Para unir por índice.
concat(): Para concatenar datasets (por filas o por columnas).
df_merged = pd.merge(df1, df2, on="columna_común")
Aplicación de filtros:
Usa filtros condicionales para seleccionar los datos que te interesen:
df_filtrado = df[df['columna'] > valor]
Creación de indicadores:
Puedes crear nuevas columnas basadas en los datos existentes
df['nuevo_indicador'] = df['columna1'] / df['columna2']
Esto te permitirá generar nuevas métricas que ayuden en el análisis.
