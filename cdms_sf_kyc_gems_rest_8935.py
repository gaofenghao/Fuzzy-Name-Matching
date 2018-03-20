# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 09:58:52 2017

@author: e610086
"""

import string
import numpy as np
import pandas as pd
import difflib
from functools import partial
from fuzzywuzzy import process
import re

from math import*
from decimal import Decimal


class Similarity():
        """ Five similarity measures function """
        def euclidean_distance(self,x,y):
            """ return euclidean distance between two lists """
            return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))
        def manhattan_distance(self,x,y):
            """ return manhattan distance between two lists """
            return sum(abs(a-b) for a,b in zip(x,y))
    
        def minkowski_distance(self,x,y,p_value):
            """ return minkowski distance between two lists """
            return self.nth_root(sum(pow(abs(a-b),p_value) for a,b in zip(x, y)),p_value)
        
        def nth_root(self,value, n_root):
            """ returns the n_root of an value """
            root_value = 1/float(n_root)
            return round (Decimal(value) ** Decimal(root_value),3)

        def cosine_similarity(self,x,y):
            """ return cosine similarity between two lists """
            numerator = sum(a*b for a,b in zip(x,y))
            denominator = self.square_rooted(x)*self.square_rooted(y)
            return round(numerator/float(denominator),3)
    
        def square_rooted(self,x):
            """ return 3 rounded square rooted value """
            return round(sqrt(sum([a*a for a in x])),3)
    
        def jaccard_similarity(self,x,y):
            """ returns the jaccard similarity between two lists """
            intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
            union_cardinality = len(set.union(*[set(x), set(y)]))
            return intersection_cardinality/float(union_cardinality)
        
        def jaccard_similarity1(self,x,y):
            """ returns the jaccard similarity between two lists """
            x = re.split('/|,| ',x)
            y = re.split('/|,| ',y)
            intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
            union_cardinality = len(set.union(*[set(x), set(y)]))
            return intersection_cardinality/float(union_cardinality)
measure = Similarity()


def stringmatcher(x1, x2):
    s =difflib.SequenceMatcher(isjunk=None,a=x1,b=x2)
    return s.ratio()

def stringmatcher1(x1, x2):
    x1 = x1.lower()
    x2 = x2.lower()
    s =difflib.SequenceMatcher(isjunk=None,a=x1.split(' '),b=x2.split(' '))
    return s.ratio()
    

full_universe = pd.read_excel('H:/Client Name Truth/Data/Copy of FULL_UNIVERSE 6-19-17_clean_name.xlsx')

#cdms_unmatched = pd.read_excel('H:/Client Name Truth/Data/CDMS_TO_GEMS_MASTER_06_30_2017.xlsx', sheetname = 'UNMATCHEDTOCHECK')
cdms_unmatched = pd.read_excel('H:/Client Name Truth/Data/Rest_8935_add_SF_clean_name.xlsx')

'''
#remove the former name"
cdms_unmatched['CDMS NAME'] = cdms_unmatched['CDMS NAME'].map(lambda x: str(x)[x.find('/')+1:])
#remove 'CLOSED'
cdms_unmatched['CDMS NAME'] = cdms_unmatched['CDMS NAME'].str.replace('CLOSED','')
#Change FDTN
cdms_unmatched['CDMS NAME'] = cdms_unmatched['CDMS NAME'].str.replace(' FDTN',' Foundation')
#
cdms_unmatched['CDMS NAME'] = cdms_unmatched['CDMS NAME'].str.replace('UNVI ',' University ')
#
cdms_unmatched['CDMS NAME'] = cdms_unmatched['CDMS NAME'].str.replace('UNVI. ','University ')
#
cdms_unmatched['CDMS NAME'] = cdms_unmatched['CDMS NAME'].str.replace(' MGMT',' Management ')

#
#lower case
cdms_unmatched['CDMS NAME'] = cdms_unmatched['CDMS NAME'].str.lower()
#
cdms_unmatched['CDMS NAME'] = cdms_unmatched['CDMS NAME'].str.replace(' corporation',' corp')
cdms_unmatched['CDMS NAME'] = cdms_unmatched['CDMS NAME'].str.replace(' corp',' corporation')
cdms_unmatched['CDMS NAME'] = cdms_unmatched['CDMS NAME'].str.replace(' corp.',' corporation')
#remove white spaces
cdms_unmatched['CDMS NAME'] = cdms_unmatched['CDMS NAME'].str.lstrip().str.rstrip()


full_universe['LEGAL_NAME'] = full_universe['LEGAL_NAME'].str.lower()
full_universe['LEGAL_NAME'] = full_universe['LEGAL_NAME'].str.replace(' corporation',' corp')
full_universe['LEGAL_NAME'] = full_universe['LEGAL_NAME'].str.replace(' corp',' corporation')
full_universe['LEGAL_NAME'] = full_universe['LEGAL_NAME'].str.replace(' corp.',' corporation')
full_universe['LEGAL_NAME'] = full_universe['LEGAL_NAME'].str.strip()

full_universe['PREVIOUS_NAMES'] = full_universe['PREVIOUS_NAMES'].str.lower()
full_universe['PREVIOUS_NAMES'] = full_universe['PREVIOUS_NAMES'].str.replace(' corporation',' corp')
full_universe['PREVIOUS_NAMES'] = full_universe['PREVIOUS_NAMES'].str.replace(' corp',' corporation')
full_universe['PREVIOUS_NAMES'] = full_universe['PREVIOUS_NAMES'].str.replace(' corp.',' corporation')

full_universe['TRADES_AS_NAMES'] = full_universe['TRADES_AS_NAMES'].str.lower()
full_universe['TRADES_AS_NAMES'] = full_universe['TRADES_AS_NAMES'].str.replace(' corporation',' corp')
full_universe['TRADES_AS_NAMES'] = full_universe['TRADES_AS_NAMES'].str.replace(' corp',' corporation')
full_universe['TRADES_AS_NAMES'] = full_universe['TRADES_AS_NAMES'].str.replace(' corp.',' corporation')
full_universe['TRADES_AS_NAMES'] = full_universe['TRADES_AS_NAMES'].str.strip()

cdms_unmatched = cdms_unmatched.fillna(' ')
cdms_unmatched['SF360 ACCOUNT ID'] = ''
cdms_unmatched['SF360 ACCOUNT NAME'] = ''

sf360 = pd.read_excel('H:/Client Name Truth/Data/cdms_to_SF360_Mapping (as of 6-2).xlsx')
kycall = pd.read_excel('H:/Client Name Truth/Data/KYC Legal_Entity_Details 6-9-17.xlsx')
'''
'''
for i in range(1000):
    tmp = sf360[sf360['UP'] == cdms_unmatched['CDMS CODE'].values[i]]
    if len(tmp) == 1:
        cdms_unmatched['SF360 ACCOUNT ID'].values[i] = tmp['Account__c'].values[0]
        cdms_unmatched['SF360 ACCOUNT NAME'].values[i] = tmp['SF360 Account Name'].values[0]
    if len(tmp) > 1:
        cdms_unmatched['SF360 ACCOUNT NAME'].values[i] = 'TO BE DETERMINED'
'''
cdms_unmatched = cdms_unmatched.fillna(' ')
full_universe = full_universe.fillna(' ')
cdms_unmatched['COMMENTS'] = ' '
cdms_unmatched['GEM ID (MANUAL)'] = ' '
cdms_unmatched['GEM LEGAL_NAME (MANUAL)'] = ' '

kycall = pd.read_excel('H:/Client Name Truth/Data/KYC Legal_Entity_Details 6-9-17.xlsx')

for j in range(len(cdms_unmatched)):
    cdmsnm = cdms_unmatched['CDMS NAME'].values[j].strip()
    sfnm = cdms_unmatched['SF360 ACCOUNT NAME'].values[j].strip()
    if stringmatcher1(cdmsnm, sfnm) <0.99:
        cdms_unmatched['COMMENTS'].values[j] = 'SF-CDMS Mismatch'
        
    if cdms_unmatched['DECISION'].values[j].strip() == 'MATCH':
        print(j)
        if stringmatcher1(cdmsnm,sfnm) >=0.99:
            cdms_unmatched['DECISION'].values[j] = 'MATCH SF & CDMS'
        else:
            cdms_unmatched['DECISION'].values[j] = 'MATCH CDMS'        
    elif cdms_unmatched['DECISION'].values[j].strip() == 'NO MATCH':
        print(j)
        gemsid = ''
        gemsnm = ''
        matchq = ''
        score1 = 0.0
        score2 = 0.0
        score3 = 0.0
        tmp =full_universe['LEGAL_NAME'].apply(partial(stringmatcher1,cdmsnm))
        score1 = max(tmp)
        ind1 = np.argmax(tmp)
        tmp = full_universe['PREVIOUS_NAMES'].apply(partial(stringmatcher1,cdmsnm))
        score2 = max(tmp)
        ind2 = np.argmax(tmp)
        score3 =0.0
        tmp = full_universe['TRADES_AS_NAMES'].apply(partial(stringmatcher1,cdmsnm))
        score3 = max(tmp)
        ind3 = np.argmax(tmp)
        score =[score1,score2,score3]
        ind = [ind1,ind2,ind3]
        finalscore = max(score)
        finalind=ind[np.argmax(score)]
        
        if finalscore >=0.95:
            gemsid = full_universe['GEM_ID'].values[finalind]
            gemsnm = full_universe['LEGAL_NAME'].values[finalind]
            if finalind == ind2:
                matchq = 'PARTIAL (PREVIOUS_NAMES) - ' + str(int(finalscore*100)) +'%'
            elif finalind == ind3:
                 matchq = 'PARTIAL (TRADES_AS_NAMES) - ' + str(int(finalscore*100)) +'%'
            else:
                 matchq = 'PARTIAL- ' + str(int(finalscore*100)) +'%'
            if stringmatcher1(cdmsnm,sfnm) >=0.99:
                 cdms_unmatched['DECISION'].values[j] = 'MATCH SF & CDMS'
            else:
                 cdms_unmatched['DECISION'].values[j] = 'MATCH CDMS'
        else:
             tmp3 = kycall['Legal Entity Name'].apply(partial(stringmatcher,cdmsnm))
             kscore = max(tmp3)
             if kscore >=0.95:
                 kind = np.argmax(tmp3)
                 gemsid = kycall['GEMS ID'].values[kind]
                 gemsnm = kycall['Legal Entity Name'].values[kind]
                 matchq = 'PARTIAL(KYC) ' + str(int(kscore*100)) +'%'
                 if stringmatcher1(cdmsnm, sfnm) >=0.99:
                     cdms_unmatched['DECISION'].values[j] = 'MATCH SF & CDMS'
                 else:
                     cdms_unmatched['DECISION'].values[j] = 'MATCH CDMS'
                 
        if gemsid == '' and stringmatcher1(cdmsnm, sfnm) <0.99: 
            if len(sfnm) != 0:
                cdmsnmsf = sfnm
                score1 = 0.0
                score2 =0.0
                score3 =0.0
                tmp =full_universe['LEGAL_NAME'].apply(partial(stringmatcher1,cdmsnmsf))
                score1 = max(tmp)
                ind1 = np.argmax(tmp)
                tmp = full_universe['PREVIOUS_NAMES'].apply(partial(stringmatcher1,cdmsnmsf))
                score2 = max(tmp)
                ind2 = np.argmax(tmp)
                score3 =0.0
                tmp = full_universe['TRADES_AS_NAMES'].apply(partial(stringmatcher1,cdmsnmsf))
                score3 = max(tmp)
                ind3 = np.argmax(tmp)
                score =[score1,score2,score3]
                ind = [ind1,ind2,ind3]
                finalscore = max(score)
                finalind=ind[np.argmax(score)]
                if finalscore >=0.95:
                    gemsid = full_universe['GEM_ID'].values[finalind]
                    gemsnm = full_universe['LEGAL_NAME'].values[finalind]
                    if finalind == ind2:
                        matchq = 'PARTIAL-SF (PREVIOUS_NAMES) - ' + str(int(finalscore*100)) +'%'
                    elif finalind == ind3:
                        matchq = 'PARTIAL-SF (TRADES_AS_NAMES) - ' + str(int(finalscore*100)) +'%'
                    else:
                        matchq = 'PARTIAL-SF ' + str(int(finalscore*100)) +'%'
                         
                    cdms_unmatched['DECISION'].values[j] = 'MATCH SF'
                else:
                    tmp3 = kycall['Legal Entity Name'].apply(partial(stringmatcher,sfnm))
                    kscore = max(tmp3)
                    if kscore >=0.95:
                        kind = np.argmax(tmp3)
                        gemsid = kycall['GEMS ID'].values[kind]
                        gemsnm = kycall['Legal Entity Name'].values[kind]
                        matchq = 'PARTIAL(KYC) ' + str(int(kscore*100)) +'%'
                        cdms_unmatched['DECISION'].values[j] = 'MATCH SF'       
        if gemsid == '':  
            tmp4 = full_universe[full_universe['LEGAL_NAME'].str.find(cdmsnm) != -1]
            if len(tmp4) == 1:
                gemsid = tmp4['GEM_ID'].values[0]
                gemsnm = tmp4['LEGAL_NAME'].values[0]
                cdms_unmatched['DECISION'].values[j]  = 'TO CHECK'
        if gemsid != '':
            cdms_unmatched['GEM ID'].values[j] = str(gemsid)
            cdms_unmatched['GEM LEGAL_NAME'].values[j] = gemsnm.upper()
            cdms_unmatched['MATCH QUALITY'].values[j] = matchq
    else:
        print(j)
        

    


#cdms_save = pd.read_excel('H:/Client Name Truth/Data/CDMS_TO_GEMS_MASTER_06_26_2017.xlsx', sheetname = 'UNMATCHEDTOCHECK')
#cdms_unmatched['CDMS NAME'] = cdms_save['CDMS NAME']
#rearrange columns
#cdms_to_gems = cdms_to_gems[['CDMS CODE','CDMS NAME','GEM ID','GEM LEGAL_NAME','MATCH QUALITY']]