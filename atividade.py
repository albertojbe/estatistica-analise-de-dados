import pandas
import numpy
import scipy.stats
import matplotlib.pyplot as plt
import seaborn


iris = pandas.read_csv('iris.csv')

irisSetosa = iris[iris["Species"] == "Iris-setosa"]
irisVirginica = iris[iris["Species"] == "Iris-virginica"]
irisVersicolor = iris[iris["Species"] == "Iris-versicolor"]

species = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

def maiorMedia():
    media = ['Type', 0]
    for specie in species:
        irisType = iris[iris["Species"] == specie]
        mediaType = numpy.mean(irisType['PetalLengthCm'])
        if mediaType > media[1]:
            media[0], media[1] = specie, mediaType
    return f"A maior média pertence à: {media[0]} - {mediaType:.2f}cm"


def correlacao():
    for specie in species:
        irisType = iris[iris["Species"] == specie]
        pearson = scipy.stats.pearsonr(x=irisType['PetalLengthCm'], y=irisType["SepalLengthCm"])
        print(pearson.statistic)
        seaborn.scatterplot(irisType, x='PetalLengthCm', y='SepalLengthCm')
        plt.show()

def distEspecies():
    distribuicaoEspecies = iris['Species'].value_counts().reset_index()
    distribuicaoEspecies.columns = ['especie', 'contagem']

    # Criar o gráfico de barras
    plt.figure(figsize=(10, 6))
    seaborn.barplot(data=distribuicaoEspecies, x='especie', y='contagem', palette='viridis')
    plt.title('Distribuição das Espécies')
    plt.xlabel('Espécie')
    plt.ylabel('Contagem')
    plt.xticks(rotation=45)
    plt.show()


def variabilidadeDosDados():
     for specie in species:
        irisType = iris[iris["Species"] == specie]
        print(f"Espécie: {specie}")
        print(f"Desvio padrão comprimento da sépala: {irisType["SepalLengthCm"].std(ddof=1) / irisType['SepalLengthCm'].mean()}")
        print(f"Desvio padrão largura da sépala: {irisType["SepalWidthCm"].std(ddof=1)/irisType["SepalWidthCm"].mean()}")
        print(f"Desvio padrão comprimento da pétala: {irisType["PetalLengthCm"].std(ddof=1)/irisType["PetalLengthCm"].mean()}")
        print(f"Desvio padrão largura da pétala: {irisType["PetalWidthCm"].std(ddof=1)/irisType["PetalWidthCm"].mean()}")
        print("")



