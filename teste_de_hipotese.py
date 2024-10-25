import numpy as np 
import scipy.stats


 
sync = np.array([94, 84.9, 82.6, 69.5, 80.1, 79.6, 81.4, 77.8, 81.7, 78.8, 73.2, 87.9, 87.9, 93.5, 82.3, 79.3, 78.3, 71.6, 88.6, 74.6, 74.1, 80.6])
asyncr = np.array([77.1, 71.7, 91, 72.2, 74.8, 85.1, 67.6, 69.9, 75.3, 71.7, 65.7, 72.6, 71.5, 78.2])

def teste_normalidade(data):
    p_value = scipy.stats.shapiro(data)
    print(f"P value: {p_value}")
    
def teste_de_levene(sync, asyncr):
    test, pvalue_var = scipy.stats.levene(sync, asyncr)
    print(f"P Value var: {pvalue_var}")
    if pvalue_var < 0.05:
        print("Rejeita hipótese nula")
    else:
        print("Falha em rejeitar hipótese nula")

def tteste(sync, asyncr):
    test, pvalue = scipy.stats.ttest_ind(sync, asyncr)
    pvalue = pvalue / 2
    print(f"pvalue: {pvalue}")
    if pvalue < 0.05:
        print("Rejeita Hipotese nula")
    else:
        print("Falha em rejeitar hipotese nula")
# O sync e o async possuem distribuições normais, pois ambos tiveram pvalor acima de 0.05. Também tiveram varianças iguais

only_breast=np.array([794.1, 716.9, 993. , 724.7, 760.9, 908.2, 659.3 , 690.8, 768.7, 717.3 , 630.7, 729.5, 
             714.1, 810.3, 583.5, 679.9, 865.1])

only_formula=np.array([ 898.8, 881.2, 940.2, 966.2, 957.5, 1061.7, 1046.2, 980.4, 895.6, 919.7, 1074.1, 952.5, 
              796.3, 859.6, 871.1 , 1047.5, 919.1 , 1160.5, 996.9])

both=np.array([976.4, 656.4, 861.2, 706.8, 718.5, 717.1, 759.8, 894.6, 867.6, 805.6, 765.4, 800.3, 789.9, 875.3, 
      740. , 799.4, 790.3, 795.2 , 823.6, 818.7, 926.8, 791.7, 948.3])

teste_normalidade(only_breast)
teste_normalidade(only_formula)
teste_normalidade(both)
ttest
