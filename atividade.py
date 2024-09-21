import pandas
import numpy

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
    return f"{media[0]}: {mediaType:.2f}cm"

print(maiorMedia())