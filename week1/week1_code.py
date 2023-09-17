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
print(df3)

#This works! now its ID, F age, M age, Mdnm, Pdnm

