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
correlacao()

