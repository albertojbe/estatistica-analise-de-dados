import asyncore
from ctypes import alignment
import statistics
from time import time
from turtle import pd, ycor
import numpy
import matplotlib.dates as mdate
import matplotlib.pyplot as plt
import seaborn
import scipy.stats
import pandas


 
sync = numpy.array([94, 84.9, 82.6, 69.5, 80.1, 79.6, 81.4, 77.8, 81.7, 78.8, 73.2, 87.9, 87.9, 93.5, 82.3, 79.3, 78.3, 71.6, 88.6, 74.6, 74.1, 80.6])
asyncr = numpy.array([77.1, 71.7, 91, 72.2, 74.8, 85.1, 67.6, 69.9, 75.3, 71.7, 65.7, 72.6, 71.5, 78.2])

x = sync.mean()
x2 = asyncr.mean()
print("Média Sync: " + str(x))
print("Média ASync: " + str(x2))

me = numpy.median(sync)
me2 = numpy.median(asyncr)
print(f"Mediana Sync: {me}")
print(f"Mediana ASync: {me2}")
q1s = numpy.percentile(sync, 25)
q3s = numpy.percentile(sync, 75)
print(f"Primeiro Quartil Sync: {q1s}")
print(f"Terceiro Quartil Sync: {q3s}")
q1a = numpy.percentile(asyncr, 25)
q3a = numpy.percentile(asyncr, 75)
print(f"Primeiro Quartil ASync: {q1a}")
print(f"Terceiro Quartil Async: {q3a}")   

modas = statistics.quantiles(sync)
modaa = statistics.quantiles(asyncr, n=10)
print(f"Moda Sync: {modas}")
print(f"Moda ASync: {modaa}")

maxS = (max(sync))
minS = (min(sync))
rangeS = (maxS - minS)
print(f"Amplitude Sync: {rangeS}")

maxA = (max(asyncr))
minA = (min(asyncr))
rangeA = (maxA - minA)
print(f"Amplitude ASync: {rangeA}")

amplitudeInterquartilS = q3s - q1s
print(f"Amplitude Interquartílica Sync: {amplitudeInterquartilS}")
amplitudeInterquartilA = q3a - q1a
print(f"Amplitude Interquartílica Sync: {amplitudeInterquartilA}")

varS = sync.var(ddof=1)
varA = asyncr.var(ddof=1)
print(f"Variância Sync: {varS}")
print(f"Variância ASync: {varA}")

desvPadraoS = sync.std(ddof=1)
desvPadraoA = asyncr.std(ddof=1)
print(f"Desvio padrão Sync: {desvPadraoS}")
print(f"Desvio padrão ASync: {desvPadraoA}")

cofVarS = desvPadraoS / x
cofVarA = desvPadraoA / x2
print(f"Coeficiente de variação Sync: {cofVarS}")
print(f"Coeficiente de variação ASync: {cofVarA}")

#HISTOGRAMA
"""plt.hist(sync)"""

#BOXPLOT
"""plt.xlabel('Work Type')
seaborn.boxplot([sync, asyncr], orient="h")
plt.yticks([0, 1], ['Dados 1', 'Dados 2'])
plt.xlabel('Hours')"""

stockdata = pandas.read_csv('stock_data.csv')
iris = pandas.read_csv('iris.csv')

#OUTLIERS
"""open = stockdata['Open']
xStock = open.mean()
pontoDeCorte = asyncr.std(ddof=1) * 3
inferior, superior = x2 - pontoDeCorte, x2 + pontoDeCorte
outliers = asyncr[(asyncr < inferior) | (asyncr > superior)]
print(stockdata)
print(outliers)

seaborn.boxplot(stockdata['Open'], orient='h')
plt.show()"""

"""
Regra empiríca: distribuição normal 
    - 68% dos intervalos devem estar em um intervalo entre ['x - 5, 'x + 5]
    - 95% dos intervalos devem estar em um intervalo entre ['x -2s, 'x + 2s]
"""

# TIME SERIES
'''stockdata['Date'] = pandas.to_datetime(stockdata["Date"])
print(stockdata.head())
seaborn.lineplot(data=stockdata, x="Date", y="High")
seaborn.lineplot(data=stockdata, x="Date", y="Low")
plt.show()'''


'''print(scipy.stats.spearmanr(x, y))
print(scipy.stats.pearsonr(x, y))
# seaborn.scatterplot(data=iris, x=x, y=y)
# seaborn.boxplot([x, y], orient='h')'''

# plt.show()
species = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
for specie in species:
    x = "SepalLengthCm"
    y = "SepalWidthCm"
    irisSpecie = iris[iris["Species"] == specie].drop(columns=["Species"])
    irisSpecie = irisSpecie.drop(columns=["Id"])
    corrMatrix = irisSpecie.corr()
    print(f"\n{corrMatrix}")
    print(f"Spearman {specie}: {scipy.stats.spearmanr(irisSpecie[x], irisSpecie[y])}")
    print(f"Pearson {specie}: {scipy.stats.pearsonr(irisSpecie[x], irisSpecie[y])}")
    # seaborn.scatterplot(data=irisSpecie, x=irisSpecie[x], y=irisSpecie[y])
    seaborn.heatmap(corrMatrix, annot=True)
    plt.show()
    break

for specie in species:
    x = "PetalLengthCm"
    y = "PetalWidthCm"
    irisSpecie = iris[iris["Species"] == specie].drop(columns=["Id", "Species"])
    corrMatrix = irisSpecie.corr()
    print(f"Corr Matrix: {corrMatrix}")
    print(f"\nSpearman {specie}: {scipy.stats.spearmanr(irisSpecie[x], irisSpecie[y])}")
    print(f"Pearson {specie}: {scipy.stats.pearsonr(irisSpecie[x], irisSpecie[y])}")
    seaborn.scatterplot(data=irisSpecie, x=irisSpecie[x], y=irisSpecie[y])
    plt.show()
    break


