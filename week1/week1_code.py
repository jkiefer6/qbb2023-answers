#!/usr/bin/env python
import pandas as pd 
dnm = pd.read_csv('aau1043_dnm.csv')
#print(dnm)

#keys_ID = dnm.Proband_id.unique() #specifying only one indv per key

#look line by line and for indv count how many time you see father and mother
#when key occurs if not new append versus create new key
#Andrew showed us how to do this earlier in the week witha  codon dict


#check_my_data = dnm[['Proband_id', 'Phase_combined']].copy()
#print(check_my_data)
#roi = (check_my_data.loc['Proband_id', :] == 675)
#df_adelie = df.loc[roi, :]
#print(df_adelie)


deNovoCount = dnm.groupby('Proband_id')['Phase_combined'].apply(list).to_dict()
#print(deNovoCount)




for i in deNovoCount.keys():
    #print(deNovoCount.get(i))
    the_sum_mom = 0
    the_sum_dad = 0
    for values in deNovoCount.get(i):
        if values == 'mother':
            the_sum_mom += 1
    for valued in deNovoCount.get(i):
        if valued == 'father':
            the_sum_dad += 1
    deNovoCount[i] = [the_sum_mom, the_sum_dad]


#print(deNovoCount)

#this worked I think!!

deNovoCountDF = pd.DataFrame.from_dict(deNovoCount, orient = 'index', columns = ['maternal_dnm', 'paternal_dnm'])

#print(deNovoCountDF)
new_deNovoCountDF = deNovoCountDF.reset_index() #need to reset row numbers
new2 = new_deNovoCountDF.drop('index', axis = 'columns') #created an index column by accident, so removing that
#print(new2)
age = pd.read_csv('aau1043_parental_age.csv')
#print(age)


df3 = pd.concat([age, new2], axis = 1, join = 'outer')
#print(df3)

#This works! now its ID, F age, M age, Mdnm, Pdnm

#Exercise 2:

import statsmodels.formula.api as smf

# the count of maternal de novo mutations vs. maternal age (upload as ex2_a.png in your submission directory)
#the count of paternal de novo mutations vs. paternal age (upload as ex2_b.png in your submission directory)

import matplotlib.pyplot as plt

fig, (ax) = plt.subplots()
ax.set_title( "Maternal Mutations and Age" )
ax.scatter(df3["Mother_age"], df3["maternal_dnm"])
ax.set_xlabel("Maternal Age")
ax.set_ylabel("Maternal DeNovo Mutations")


plt.tight_layout()
#plt.show()
#fig.savefig( "ex2_a" )
#plt.close(fig)

fig, (ax) = plt.subplots()
ax.set_title( "Paternal Mutations and Age" )
ax.scatter(df3["Father_age"], df3["paternal_dnm"])
ax.set_xlabel("Paternal Age")
ax.set_ylabel("Paternal DeNovo Mutations")


plt.tight_layout()
#plt.show()
#fig.savefig( "ex2_b" )
#plt.close(fig)


model_female = smf.ols(formula = "maternal_dnm ~ Mother_age", data = df3).fit()
#print(model_female.summary())

#print(model_female.pvalues[1])


model_male = smf.ols(formula = "paternal_dnm ~ Father_age", data = df3).fit()
#print(model_male.summary())

#print(model_male.pvalues[0])
#print(model_male.pvalues[1])


#fig, ax = plt.subplots()
#ax.hist(df3["maternal_dnm"][df3["Mother_age"]], label = "maternal", bins = 30, alpha = 0.5)
#ax.hist(df3["paternal_dnm"][df3["Father_age"]], label = "paternal", bins = 30, alpha = 0.5)
#ax.legend()
#ax.set_xlabel("Age")
#ax.set_ylabel("DeNovo Mutations")
#plt.show()
#fig.savefig( "ex2_c" )
#plt.close(fig)

#2.6
#Must be paried because each proband has multiple dnms and need to take that into account
#first test if data is parametric:

#checking for gaussian distribution 
#first visually:
"""
fig, ax = plt.subplots()
ax.hist(df3["maternal_dnm"])
ax.set_title("Maternal DNMs")
plt.show()
fig.savefig("ex2_a")
#right tail on hist

fig, ax = plt.subplots()
ax.hist(df3["paternal_dnm"])
ax.set_title("Paternal DNMs")
plt.show()
fig.savefig("ex2_b")
#also slight right tail, but more gaussian in distribution
"""
m_dnm = df3["maternal_dnm"]
p_dnm = df3["paternal_dnm"]

from scipy import stats
from scipy.stats import shapiro
import scipy.stats as stats

stat, p = shapiro(m_dnm)
#print(stat, p)
# p = 2.34 * 10^-10

statp, p_p = shapiro(p_dnm)
#print(statp, p_p)
# p = 1.24*10^-6

#Since the p value is so low, we reject the null hypothesis which was that the data was normally distributed
#Have to use Wilcoxon signed rank test

print(stats.wilcoxon(m_dnm, p_dnm))

#for the null hypothesis, evenly distributed around zero
# p = 1.20 * 10^-66
#reject that null that the two distributions are the same
#there is a singificant difference between maternally inherited dnms and paternal

print(stats.wilcoxon(m_dnm, p_dnm, alternative = 'less'))
# p = 5.98 * 10^-67
# specifically testing here that 
#the distribution underlying the difference between medians
#is stochastically less than a distribution symmetric about zero.
#in other words that the number of paternal dnms is significantly more than maternal for a given proband



