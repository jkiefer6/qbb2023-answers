#!/usr/bin/env python
import pandas as pd 
dnm = pd.read_csv('aau1043_dnm.csv')
print(dnm)

#keys_ID = dnm.Proband_id.unique() #specifying only one indv per key

#look line by line and for indv count how many time you see father and mother
#when key occurs if not new append versus create new key
#Andrew showed us how to do this earlier in the week witha  codon dict

deNovoCount = {}

# if key in deNovoCount.keys():
#   deNovoCount[key].append(value)
# else:
#   results[key] = [value] # But here i need to change this from making list of values to returning a count
#also will need to specify via Phase_combined which is father and mother


#for individual in dnm:
    #for every unique Proband_ID count how many times father occurs in "Phase_combined"
    #repeat for mother




