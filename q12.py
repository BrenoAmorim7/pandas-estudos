import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/DATAUNIRIO/Base_de_dados/master/Estados.csv"
df_dadosbrasil = pd.read_csv(url,sep=";",decimal=",")

df_dadosbrasil[(df_dadosbrasil['Gini'] < 0.55)] 