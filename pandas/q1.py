#mostrar a contagem de cada região geográfica do Brasil em um gráfico de barras

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/DATAUNIRIO/Base_de_dados/master/Estados.csv"
df_dadosbrasil = pd.read_csv(url,sep=";",decimal=",")


sns.countplot(data = df_dadosbrasil,x = 'Regiao_Geografica')
plt.show()