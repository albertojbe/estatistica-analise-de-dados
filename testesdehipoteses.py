#!/usr/bin/env python
# coding: utf-8

# # EXEMPLO 1 (ESTUDO SÍNCRONO E ASSÍNCRONO)

# In[6]:


import numpy as np
import statistics
#import scipy as scp

sync = np.array([94. , 84.9, 82.6, 69.5, 80.1, 79.6, 81.4, 77.8, 81.7, 78.8, 73.2,
       87.9, 87.9, 93.5, 82.3, 79.3, 78.3, 71.6, 88.6, 74.6, 74.1, 80.6])
asyncr = np.array([77.1, 71.7, 91. , 72.2, 74.8, 85.1, 67.6, 69.9, 75.3, 71.7, 65.7, 72.6, 71.5, 78.2])


# In[7]:


sync.std()


# In[8]:


sync.ptp()


# In[9]:


print(sync.mean())
print(asyncr.mean())


# In[10]:


# TESTE DE NORMALIDADE!

# VERIFICAR SE OS DADOS SEGUEM UMA DISTRIBUIÇÃO NORMAL!

# teste de hipótese de Shapiro-Wilk

# H0:Os dados têm distribuição normal;
# H1:Os dados não têm distribuição normal.

# Conclusões:
# Se p-valor (valor de prova) <= 0.05, rejeita H0 (H0 é falso) e assume H1 (H1 é verdadeiro);
# Se p-valor (valor de prova) > 0.05 não deve rejeitar H0 (H0 é verdadeiro).

# 0.05 = 5% é a cauda do intervalo de confiança de 95%.

from scipy.stats import shapiro
from scipy import stats

def check_normality(data):
    test_stat_normality, p_value_normality=stats.shapiro(data)
    print("p value:%.4f" % p_value_normality)
    if p_value_normality <0.05:
        print("Reject null hypothesis >> The data is not normally distributed")
    else:
        print("Fail to reject null hypothesis >> The data is normally distributed")


# In[11]:


check_normality(sync)
check_normality(asyncr)


# In[32]:


print(sync.mean())
print(statistics.median(sync))


# In[33]:


import seaborn as sns
import matplotlib.pyplot as  plt

sns.distplot(sync)
plt.show()


# In[34]:


# TESTANDO A VARIABILIDADE DOS DADOS

# Aplicando o teste de homogeneidade de Levene

# H0:As varâncias são iguais;
# H1:As variâncias são diferentes.

# Conclusões:
# Se pvalue <= 0.05, rejeita H0 e assume H1;
# Se pvalue > 0.05 não deve rejeitar H0.

from scipy.stats import levene

test_stat_var, p_value_var= stats.levene(sync, asyncr)
print("p value:%.4f" % p_value_var)
if p_value_var <0.05:
    print("Reject null hypothesis >> The variances of the samples are different.")
else:
    print("Fail to reject null hypothesis >> The variances of the samples are same.")


# In[35]:


# PARÂMETROS:
# PRÉ-REQUISITOS
# DUAS AMOSTRAS NÃO PAREADAS
# SÃO NORMALMENTE DISTRIBUIDAS
# MESMA VARIÂNCIA

# APLICANDO T-TEST (TESTE PARAMÉTRICO)

# Hipóteses
# H0: as médias são iguais
# H1: as médias são diferentes

# Conclusões:
# Se pvalue <= 0.05, rejeita H0 e assume H1;
# Se pvalue > 0.05 não deve rejeitar H0.

ttest,p_value = stats.ttest_ind(sync,asyncr)
print("p value:%.8f" % p_value)
print("since the hypothesis is one sided >> use p_value/2 >> p_value_one_sided:%.4f" %(p_value/2))
if p_value/2 <0.05:
    print("Reject null hypothesis")
else:
    print("Fail to reject null hypothesis")


# In[9]:


# Conclusão: As médias das notas da população dos alunos que estudaram de forma síncrona e assíncrona são diferentes e 
# a média dos alunos com estudo síncrono é maior que a dos alunos com estudo assíncrono.


# # EXEMPLO 2 (ALIMENTAÇÃO COM LEITE MATERNO, FÓRMULA OU OS DOIS)

# In[44]:


only_breast=np.array([794.1, 716.9, 993. , 724.7, 760.9, 908.2, 659.3 , 690.8, 768.7, 717.3 , 630.7, 729.5, 
             714.1, 810.3, 583.5, 679.9, 865.1])

only_formula=np.array([ 898.8, 881.2, 940.2, 966.2, 957.5, 1061.7, 1046.2, 980.4, 895.6, 919.7, 1074.1, 952.5, 
              796.3, 859.6, 871.1 , 1047.5, 919.1 , 1160.5, 996.9])

both=np.array([976.4, 656.4, 861.2, 706.8, 718.5, 717.1, 759.8, 894.6, 867.6, 805.6, 765.4, 800.3, 789.9, 875.3, 
      740. , 799.4, 790.3, 795.2 , 823.6, 818.7, 926.8, 791.7, 948.3])


# In[45]:


check_normality(only_breast)
check_normality(only_formula)
check_normality(both)


# In[46]:


sns.distplot(only_formula)
plt.show()


# In[47]:


stat, pvalue_levene= stats.levene(only_breast,only_formula,both)
print("p value:%.4f" % pvalue_levene)
if pvalue_levene <0.05:
    print("Reject null hypothesis >> The variances of the samples are different.")
else:
    print("Fail to reject null hypothesis >> The variances of the samples are same.")


# In[48]:


# PARÂMETROS:
# PRÉ-REQUISITOS
# MAIS DE DUAS AMOSTRAS NÃO PAREADAS
# SÃO NORMALMENTE DISTRIBUIDAS
# MESMA VARIÂNCIA

# APLICANDO ANOVA - ANÁLISE DE VARIÂNCIA (TESTE PARAMÉTRICO)

#H0: as médias são iguais;
#H1: pelo menos uma das médias é diferente.

# Conclusões:
# Se pvalue <= 0.05, rejeita H0 e assume H1;
# Se pvalue > 0.05 não deve rejeitar H0.

F, p_value = stats.f_oneway(only_breast,only_formula,both)
print("p value:%.6f" % p_value)
if p_value <0.05:
    print("Reject null hypothesis")
else:
    print("Fail to reject null hypothesis")


# In[15]:


#Conclusão: Pelo menos uma das médias da população é diferente.


# In[16]:


# PARÂMETROS:
# DUAS AMOSTRAS NÃO PAREADAS
# SÃO NORMALMENTE DISTRIBUIDAS
# MESMA VARIÂNCIA

# APLICANDO T-TEST

#H0: as médias são iguais
#H1: as médias são diferentes

# Conclusões:
# Se pvalue <= 0.05, rejeita H0 e assume H1;
# Se pvalue > 0.05 não deve rejeitar H0.

import scikit_posthocs as sp
posthoc_df= sp.posthoc_ttest([only_breast,only_formula,both], equal_var=True, p_adjust="bonferroni")

group_names= ["only breast", "only formula","both"]
posthoc_df.columns= group_names
posthoc_df.index= group_names
posthoc_df.style.applymap(lambda x: "background-color:violet" if x<0.05 else "background-color: white")


# In[17]:


print(only_breast.mean())
print(only_formula.mean())
print(both.mean())


# In[18]:


# only_formula e only_breast p-valor = 0, as médias das populações são diferentes;
# only_formula e both p-valor = 0, as médias das populações são diferentes;
# only_breast e both p-valor = 0.129, as médias das populações são iguais;

#Conclusão 1: alimentar os bebês com leite materno ou intercalando leite materno e fórmula tem o mesmo aumento médio de peso.
#Conclusão 2: o aumento médio de peso dos bebês que são alimentados com leite artificial (fórmula) será maior que os bebês 
#alimentados com leite materno ou com os dois intercalados.


# # EXEMPLO 3 (HORAS EXTRAS POR EQUIPES DE DESENVOLVIMENTO DE SOFTWARE E EQUIPE DE TESTE)

# In[20]:


test_team=np.array([6.2, 7.1, 1.5, 2,3 , 2, 1.5, 6.1, 2.4, 2.3, 12.4, 1.8, 5.3, 3.1, 9.4, 2.3, 4.1])
developer_team=np.array([2.3, 2.1, 1.4, 2.0, 8.7, 2.2, 3.1, 4.2, 3.6, 2.5, 3.1, 6.2, 12.1, 3.9, 2.2, 1.2 ,3.4])


# In[21]:


check_normality(test_team)
check_normality(developer_team)


# In[22]:


sns.distplot(developer_team)
plt.show()


# In[23]:


stat, pvalue_levene= stats.levene(test_team, developer_team)
print("p value:%.4f" % pvalue_levene)
if pvalue_levene <0.05:
    print("Reject null hypothesis >> The variances of the samples are different.")
else:
    print("Fail to reject null hypothesis >> The variances of the samples are same.")


# In[24]:


# PARÂMETROS:
# PRÉ-REQUISITOS
# DUAS AMOSTRAS NÃO PAREADAS
# MESMA VARIÂNCIA

# CONSTATAÇÃO
# NÃO SÃO NORMALMENTE DISTRIBUIDOS (NORMALIDADE NÃO INFLUENCIA NO TESTE)


#  APLICANDO MANN-WHITNEY U TEST (NÃO PARAMÉTRICO)

# Hipóteses
#H0: as médias são iguais
#H1: as médias são diferentes

# Conclusões:
# Se pvalue <= 0.05, rejeita H0 e assume H1;
# Se pvalue > 0.05 não deve rejeitar H0.

ttest,pvalue = stats.mannwhitneyu(test_team,developer_team, alternative="two-sided")
print("p-value:%.4f" % pvalue)
if pvalue <0.05:
    print("Reject null hypothesis")
else:
    print("Fail to recejt null hypothesis")


# In[26]:


print(developer_team.mean())
print(test_team.mean())


# In[ ]:


# Conclusão: As médias das horas extras trabalhadas por semana da população de teste é igual a média da 
# população de desenvolvimento.


# # EXEMPLO 4 (CONSUMIDORES ATRAIDOS PELAS PLATAFORMAS YOUTUBE, INSTAGRAM E FACEBOOK POR DIA)

# In[37]:


youtube = np.array([1913, 1879, 1939, 2146, 2040, 2127, 2122, 2156, 2036, 1974, 1956, 2146, 2151, 1943, 2125])

instagram = np.array([2305., 2355., 2203., 2231., 2185., 2420., 2386., 2410., 2340., 2349., 2241., 2396., 2244., 2267., 2281.])

facebook = np.array([2133., 2522., 2124., 2551., 2293., 2367., 2460., 2311., 2178., 2113., 2048., 2443., 2265., 2095., 2528.])


# In[38]:


check_normality(youtube)
check_normality(instagram)
check_normality(facebook)


# In[39]:


stat, pvalue_levene= stats.levene(youtube, instagram, facebook)

print("p value:%.4f" % pvalue_levene)
if pvalue_levene <0.05:
    print("Reject null hypothesis >> The variances of the samples are different.")
else:
    print("Fail to reject null hypothesis >> The variances of the samples are same.")


# In[40]:


# PARÂMETROS:
# PRÉ-REQUISITOS
# MAIS DE DUAS AMOSTRAS NÃO PAREADAS


# CONSTATAÇÃO
# NÃO SÃO NORMALMENTE DISTRIBUIDOS (NORMALIDADE NÃO INFLUENCIA NO TESTE)
# VARIÂNCIAS DIFERENTES (VARIABILIDADE NÃO INFLUENCIA NO TESTE)

# APLICANDO KRUSKAL-WALLIS ANOVA (NÃO PARAMÉTRICO)

#H0: as médias são iguais
#H1: pelo menos uma das médias é diferente

# Conclusões:
# Se pvalue <= 0.05, rejeita H0 e assume H1;
# Se pvalue > 0.05 não deve rejeitar H0.

F, p_value = stats.kruskal(youtube, instagram, facebook)
print("p value:%.6f" % p_value)
if p_value <0.05:
    print("Reject null hypothesis")
else:
    print("Fail to reject null hypothesis")


# In[ ]:


# Conclusão: Existe significância suficiente para afirmar que pelo menos uma das médias da população é diferente.


# In[41]:


# APLICANDO MANN-WHITNEY U TEST

#H0: as médias são iguais
#H1: as médias são diferentes

# Conclusões:
# Se pvalue <= 0.05, rejeita H0 e assume H1;
# Se pvalue > 0.05 não deve rejeitar H0.

posthoc_df = sp.posthoc_mannwhitney([youtube,instagram, facebook], p_adjust = 'bonferroni')
group_names= ["youtube", "instagram","facebook"]
posthoc_df.columns= group_names
posthoc_df.index= group_names
posthoc_df.style.applymap(lambda x: "background-color:violet" if x<0.05 else "background-color: white")


# In[42]:


print(youtube.mean())
print(instagram.mean())
print(facebook.mean())


# In[43]:


# Nível de confiança 95%
# Conclusão 1: Podemos afirmar que a população do facebook e Instagram tem a mesma média de consumidores atraidos diariamente.
# Conclusão 2: Podemos afirmar que a população do Youtube tem média de consumidores atraidos diariamente, menor que a população 
# do facebook e do instagram.


# # EXEMPLO 5 (NÍVEL DE COLESTEROL ANTES DA DIETA E DEPOIS DA DIETA)

# In[51]:


before_diet=np.array([224, 235, 223, 253, 253, 224, 244, 225, 259, 220, 242, 240, 239, 229, 276, 254, 237, 227])
after_diet=np.array([198, 195, 213, 190, 246, 206, 225, 199, 214, 210, 188, 205, 200, 220, 190, 199, 191, 218])


# In[52]:


check_normality(before_diet)
check_normality(after_diet)


# In[53]:


# T-TEST PARA AMOSTRAS PAREADAS (PARAMÉTRICO)

# PRÉ-REQUISITO
# DISTRIBUIÇÃO NORMAL

#H0: as médias são iguais
#H1: as médias são diferentes

# Conclusões:
# Se pvalue <= 0.05, rejeita H0 e assume H1;
# Se pvalue > 0.05 não deve rejeitar H0.

test_stat, p_value_paired = stats.ttest_rel(before_diet,after_diet)
print("p value:%.6f" % p_value_paired , "one tailed p value:%.6f" %(p_value_paired/2))
if p_value_paired <0.05:
    print("Reject null hypothesis")
else:
    print("Fail to reject null hypothesis")


# In[ ]:


# Conclusção: Existe significância suficiente para afirmar que a média de colesterol na população antes da dieta e depois 
# da dieta são diferentes, e podemos observar que a média de colesterol na população após a dieta é menor que antes da dieta.


# # EXEMPLO 6 (SCORE DE DESEMPENHO DE EMPRESAS)

# In[54]:


piedpiper=np.array([4.57, 4.55, 5.47, 4.67, 5.41, 5.55, 5.53, 5.63, 3.86, 3.97, 5.44, 3.93, 5.31, 5.17, 4.39, 4.28, 5.25])
endframe = np.array([4.27, 3.93, 4.01, 4.07, 3.87, 4. , 4. , 3.72, 4.16, 4.1 , 3.9 , 3.97, 4.08, 3.96, 3.96, 3.77, 4.09])


# In[55]:


check_normality(piedpiper)
check_normality(endframe)


# In[56]:


# APLICANDO WILCOXON SIGNED RANK (NÃO PARAMÉTRICO) PARA AMOSTRAS PAREADAS

# Hipóteses
#H0: as médias são iguais
#H1: as médias são diferentes

# Conclusões:
# Se pvalue <= 0.05, rejeita H0 e assume H1;
# Se pvalue > 0.05 não deve rejeitar H0.

test,pvalue = stats.wilcoxon(endframe,piedpiper) ##alternative default two sided
print("p-value:%.6f" %pvalue, ">> one_tailed_pval:%.6f" %(pvalue/2))

test,one_sided_pvalue = stats.wilcoxon(endframe,piedpiper, alternative="less")
print("one sided pvalue:%.6f" %(one_sided_pvalue))
if pvalue <0.05:
    print("Reject null hypothesis")
else:
    print("Fail to recejt null hypothesis")


# In[ ]:


# Conclusção: Existe significância suficiente para afirmar que a média do score na população da empresa endframe e piedpiper 
# são diferentes, e podemos observar que a média do score da empresa piedpiper é maior que o da empresa endframe.

