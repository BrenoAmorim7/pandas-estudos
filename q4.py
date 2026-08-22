#mostrar a distribuição da variável Mortalidade infantil por região geográfica

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/DATAUNIRIO/Base_de_dados/master/Estados.csv"
df_dadosbrasil = pd.read_csv(url,sep=";",decimal=",")

sns.scatterplot(df_dadosbrasil,x = 'IDH',y = 'Mortalidade_infantil',hue = 'Regiao_Geografica')
plt.show() 