import statistics
import numpy

 
sync = numpy.array([94, 84.9, 82.6, 69.5, 80.1, 79.6, 81.4, 77.8, 81.7, 78.8, 73.2, 87.9, 87.9, 93.5, 82.3, 79.3, 78.3, 71.6, 88.6, 74.6, 74.1, 80.6])
asyncr = numpy.array([77.1, 77.1, 91, 77.2, 74.8, 85.1, 67.6, 69.9, 75.3, 71.7, 71.7, 65.7, 72.6, 71.5, 78.2])

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