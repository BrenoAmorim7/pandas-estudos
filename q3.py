#mostrar a distribuição da variável Mortalidade infantil por região geográfica
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/DATAUNIRIO/Base_de_dados/master/Estados.csv"
df_dadosbrasil = pd.read_csv(url,sep=";",decimal=",")
sns.histplot(data=df_dadosbrasil, x = 'Mortalidade_infantil',hue  = 'Regiao_Geografica',multiple = 'dodge')
plt.show() 