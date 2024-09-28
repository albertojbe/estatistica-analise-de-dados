from cmath import sqrt
from ensurepip import bootstrap
from os import system
import numpy as np
import math


dados = np.array([41.60, 41.48, 42.34, 41.95, 41.86, 42.18, 41.72, 42.26, 41.81, 42.04])
dados2 = np.array([24.1514, 27.4145, 20.4000, 22.5151, 28.5152, 28.5611, 21.2489, 20.9983, 24.9840, 22.6245])

def calcErroPadrao(dados):
    erroPadrao = dados.std(ddof=1) / (math.sqrt(len(dados)))
    return(erroPadrao)

def calcMedia(dados):
    return dados.mean()

def intervaloMediaPopulacional(dados):
    media = calcMedia(dados)
    erroPadrao = calcErroPadrao(dados)
    return [media - 3*erroPadrao, media + 3 * erroPadrao]

def bootstrap(dados):
    mediasBoot = []
    for _ in range (0, 1000):
        bootsample = np.random.choice(dados, size=10, replace=True)
        media = bootsample.mean()
        mediasBoot.append(media)
        stdMediasBoot = np.std(mediasBoot)
        
    print(f"Intervalo Bootsrap: {[media-(3*stdMediasBoot), media+(3*stdMediasBoot)]}")

system('cls')
print(f"\nErro padrão nos dados: {calcErroPadrao(dados2)}")
print(f"Média nos dados: {calcMedia(dados2)}")
print(f"Intervalo da média populacional: {intervaloMediaPopulacional(dados2)}")
bootstrap(dados2)
input()


