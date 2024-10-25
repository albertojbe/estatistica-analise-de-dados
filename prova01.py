import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt


dietaA = np.array([5, 7, 6, 8, 5])
dietaB = np.array([4, 6, 5, 7, 6])
dietaC = np.array([6, 8, 7, 9, 7])

print(dietaA.mean())
print(dietaB.mean())
print(dietaC.mean())

def check_normality(data):
 test_stat_normality, p_value_normality=stats.shapiro(data)
 print("p value:%.4f" % p_value_normality)
 if p_value_normality <0.05:
    print("Reject null hypothesis >> The data is not normally distributed")
 else:
    print("Fail to reject null hypothesis >> The data is normally distributed")

def teste_de_levene(sync, asyncr, dietaC):
    test, pvalue_var = stats.levene(sync, asyncr, dietaC)
    print(f"P Value var: {pvalue_var}")
    if pvalue_var < 0.05:
        print("Rejeita hipótese nula")
    else:
        print("Falha em rejeitar hipótese nula")



def tteste(sync, asyncr, dietaC):
    test, pvalue = stats.ttest_ind(sync, asyncr, dietaC, equal_var=False)
    pvalue = pvalue
    print(f"pvalue: {pvalue}")
    if pvalue < 0.05:
        print("Rejeita Hipotese nula")
    else:
        print("Falha em rejeitar hipotese nula")

def oneway_test(sync, asyncr, dietaC):
    test, pvalue = stats.f_oneway(sync, asyncr, dietaC)
    pvalue = pvalue
    print(f"pvalue: {pvalue}")
    if pvalue < 0.05:
        print("Rejeita Hipotese nula")
    else:
        print("Falha em rejeitar hipotese nula")

print("Teste de Normalidade")
check_normality(dietaA)
check_normality(dietaB)
check_normality(dietaC)
print("")

print("Teste de Levene")
teste_de_levene(dietaA, dietaB, dietaC)
print("")


print("Teste Oneway")
oneway_test(dietaA, dietaB, dietaC)

plt.figure(figsize=(10, 6))
sns.kdeplot(dietaA, color='blue', label='Grupo 1', fill=True, alpha=0.5)
sns.kdeplot(dietaB, color='orange', label='Grupo 2', fill=True, alpha=0.5)
sns.kdeplot(dietaC, color='green', label='Grupo 2', fill=True, alpha=0.5)

# Configurando o gráfico
plt.title('KDE Plots de Dois Grupos')
plt.xlabel('Valor')
plt.ylabel('Densidade')
plt.legend()
plt.show()