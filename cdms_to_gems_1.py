"""
Created on 01/26/2018 12:33 AM

@author: e612495
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
    s =difflib.SequenceMatcher(isjunk=None,a=x1.split(' '),b=x2.split(' '))
    return s.ratio()
    

full_universe = pd.read_excel('H:/Client Name Truth/Data/Copy of FULL_UNIVERSE.xlsx')

cdms_unmatched = pd.read_excel('H:/Client Name Truth/Data/CDMS_TO_GEMS_MASTER.xlsx', sheetname = 'UNMATCHED')

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
"""
for i in range(10):
    temp = process.extractOne(str(cdms_unmatched['CDMS NAME'].values[i]), full_universe['LEGAL_NAME'])
    print(full_universe['GEM_ID'].values[temp[2]], full_universe['LEGAL_NAME'].values[temp[2]], temp[1])
"""
"""
#remove substring of '(PARENT)'
cdms_curr_clean['CDMS UP Name'] = cdms_curr_clean['CDMS UP Name'].map(lambda x: x.replace('(PARENT)',''))
cdms_curr_clean['CDMS UP Name'] = cdms_curr_clean['CDMS UP Name'].map(lambda x: x.replace('(PARENTS)',''))
cdms_curr_clean['CDMS UP Name'] = cdms_curr_clean['CDMS UP Name'].map(lambda x: x.replace('(PARENT',''))
cdms_curr_clean['CDMS UP Name'] = cdms_curr_clean['CDMS UP Name'].map(lambda x: x.replace('(PARENTS',''))
cdms_curr_clean['CDMS UP Name'] = cdms_curr_clean['CDMS UP Name'].map(lambda x: x.replace('PARENT)',''))
cdms_curr_clean['CDMS UP Name'] = cdms_curr_clean['CDMS UP Name'].map(lambda x: x.replace('PARENTS)',''))
#remove trailing substring of 'CLSD'
for i in range(len(cdms_curr)):
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind('CLSD')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind(' - CLSD')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_cclean['CDMS UP Name'].values[i].rfind('- CLSD')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind('-CLSD')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind('CLOSED')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind(' - CLOSED')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind('- CLOSED')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind('-CLOSED')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos]
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind(' CLO ')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind(' - IFS')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind(' - SSKC')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind(' - GSAS')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos]
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind(' - WMS')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind(' - SSGM')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind(' - ST SSGM')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos] 
    pos = cdms_curr_clean['CDMS UP Name'].values[i].rfind(' - GX')
    if pos != -1:
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:pos]
    if cdms_curr_clean['CDMS UP Name'].values[i] == '-':
         cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:-1]
#strip heading and trailing spaces
    cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i].strip()
    if cdms_curr_clean['CDMS UP Name'].values[i] == '-':
        cdms_curr_clean['CDMS UP Name'].values[i] =  cdms_curr_clean['CDMS UP Name'].values[i][:-1]
#
#cdms_curr_clean['CDMS UP Name'] = cdms_curr_clean['CDMS UP Name'].map(lambda x: if x.rfind('CLSD') != -1: x[:x.rfind('CLSD')])
#cdms_curr_clean['CDMS UP Name'] = cdms_curr_clean['CDMS UP Name'].map(lambda x: x[:x.rfind('CLOSD')])
#cdms_curr_clean['CDMS UP Name'] = cdms_curr_clean['CDMS UP Name'].map(lambda x: x[:x.rfind(' - CLOSD')])
#cdms_curr_clean['CDMS UP Name'] = cdms_curr_clean['CDMS UP Name'].map(lambda x: x[:x.rfind('- CLOSD')])
#cdms_curr_clean['CDMS UP Name'] = cdms_curr_clean['CDMS UP Name'].map(lambda x: x[:x.rfind('-CLOSD')])
"""

#manual cleaned version of CDMS data
"""
cdms_curr_clean = pd.read_excel('H:/Client Name Truth/Data/CDMS hierarchy cleaned.xlsx')


#load GEMS
GEMS_UNIVERSE = pd.read_excel('H:/Client Name Truth/Data/Copy of FULL_UNIVERSE.xlsx')

cdms_to_gems = cdms_curr_clean
cdms_to_gems = cdms_to_gems.rename(columns = {'CDMS UP':'CDMS CODE','CDMS UP Name':'CDMS NAME'})
cdms_to_gems['GEM ID'] = ''
cdms_to_gems['GEM LEGAL_NAME'] = ''
cdms_to_gems['MATCH QUALITY'] = ''
"""

"""
for j in range(len(cdms_to_gems)):
    print(j)
    gemsid = ''
    gemsnm = ''
    matchq = ''
    cdmsnm =  cdms_curr_clean['CDMS UP Name'].values[j].lower()
    tmp = GEMS_UNIVERSE[GEMS_UNIVERSE['LEGAL_NAME'].str.lower().str.contains(cdmsnm) == True]
    if len(tmp) != 0:
        gemsid = tmp['GEM_ID'].values[0]
        gemsnm = tmp['LEGAL_NAME'].values[0]
        if gemsnm.lower() == cdmsnm.lower():
            matchq = 'EXACT'
        else:
            q =0.0
            qin = 0
            for k in range(len(tmp)):
                if stringmatcher(tmp['LEGAL_NAME'].values[k].lower(),cdmsnm) > q:
                    qin = k
                    q = stringmatcher(tmp['LEGAL_NAME'].values[k].lower(),cdmsnm)
            gemsid = tmp['GEM_ID'].values[qin]
            gemsnm = tmp['LEGAL_NAME'].values[qin]
            matchq = 'PARTIAL - ' + str(int(q*100))       
    else:
         tmp = GEMS_UNIVERSE[GEMS_UNIVERSE['PREVIOUS_NAMES'].str.lower().str.contains(cdmsnm) == True]
         if len(tmp) != 0:
              gemsid = tmp['GEM_ID'].values[0]
              gemsnm = tmp['PREVIOUS_NAMES'].values[0]
              if gemsnm.lower() == cdmsnm.lower():
                  matchq = 'EXACT (with PREVIOUS_NAMES)'
              else:
                  q =0.0
                  qin = 0
                  for k in range(len(tmp)):
                      if stringmatcher(tmp['PREVIOUS_NAMES'].values[k].lower(),cdmsnm) > q:
                          qin = k
                          q = stringmatcher(tmp['PREVIOUS_NAMES'].values[k].lower(),cdmsnm)
                  gemsid = tmp['GEM_ID'].values[qin]
                  gemsnm = tmp['PREVIOUS_NAMES'].values[qin]
                  matchq = 'PARTIAL (PREVIOUS_NAMES) - ' + str(int(q*100))  
         else:
              tmp = GEMS_UNIVERSE[GEMS_UNIVERSE['TRADES_AS_NAMES'].str.lower().str.contains(cdmsnm) == True]
              if len(tmp) != 0:
                  gemsid = tmp['GEM_ID'].values[0]
                  gemsnm = tmp['TRADES_AS_NAMES'].values[0]
                  if gemsnm.lower() == cdmsnm.lower():
                      matchq = 'EXACT (with TRADES_AS_NAMES)'
                  else:
                      q =0.0
                      qin = 0
                      for k in range(len(tmp)):
                          if stringmatcher(tmp['TRADES_AS_NAMES'].values[k].lower(),cdmsnm) > q:
                              qin = k
                              q = stringmatcher(tmp['TRADES_AS_NAMES'].values[k].lower(),cdmsnm)
                      gemsid = tmp['GEM_ID'].values[qin]
                      gemsnm = tmp['TRADES_AS_NAMES'].values[qin]
                      matchq = 'PARTIAL (TRADES_AS_NAMES) - ' + str(int(q*100))  
    cdms_to_gems['GEM ID'].values[j] = gemsid
    cdms_to_gems['GEM LEGAL_NAME'].values[j] = gemsnm
    cdms_to_gems['MATCH QUALITY'].values[j] = matchq
    del tmp
"""
cdms_unmatched = cdms_unmatched.fillna(' ')
full_universe = full_universe.fillna(' ')
for j in range(len(cdms_unmatched)):
    print(j)
    gemsid = ''
    gemsnm = ''
    matchq = ''
    cdmsnm =  cdms_unmatched['CDMS NAME'].values[j]
    score1 = 0.0
    score2 =0.0
    score3 =0.0
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
    
    gemsid = full_universe['GEM_ID'].values[finalind]
    gemsnm = full_universe['LEGAL_NAME'].values[finalind]
    matchq = 'PARTIAL - ' + str(int(finalscore*100)) +'%'
    cdms_unmatched['GEM ID'].values[j] = gemsid
    cdms_unmatched['GEM LEGAL_NAME'].values[j] = gemsnm.upper()
    cdms_unmatched['MATCH QUALITY'].values[j] = matchq
    
"""
    tmp = full_universe[full_universe['LEGAL_NAME'].apply(partial(stringmatcher1,cdmsnm)) >0.5]
    if len(tmp) != 0:
        q = 0
        totscore = 0.0
        for k in range(len(tmp)):
            #s1 = re.split('/|,| ',tmp['LEGAL_NAME'].values[k])
            #s2 = re.split('/|,| ',cdmsnm)
            s1 = tmp['LEGAL_NAME'].values[k]
            s2= cdmsnm
            totnew = 0.25*(stringmatcher(s1,s2) + measure.jaccard_similarity(s1,s2))
            totnew = totnew + 0.25*(stringmatcher(tmp['LEGAL_NAME'].values[k],cdmsnm) \
                                    + measure.jaccard_similarity(tmp['LEGAL_NAME'].values[k],cdmsnm))
            #totnew = stringmatcher(tmp['LEGAL_NAME'].values[k],cdmsnm)
            if totnew > totscore:
                totscore = totnew
                q = k
        gemsid = tmp['GEM_ID'].values[q]
        gemsnm = tmp['LEGAL_NAME'].values[q]
        matchq = 'PARTIAL - ' + str(int(totscore*100)) +'%'
        score = totscore
    del tmp
    tmp = full_universe[full_universe['PREVIOUS_NAMES'].apply(partial(stringmatcher1,cdmsnm)) >0.5]
    if len(tmp) != 0:
        q = 0
        totscore = 0.0
        for k in range(len(tmp)):
            #s1 = re.split('/|,| ',tmp['PREVIOUS_NAMES'].values[k])
            #s2 = re.split('/|,| ',cdmsnm)
            s1 = tmp['PREVIOUS_NAMES'].values[k]
            s2= cdmsnm
            totnew = 0.25*(stringmatcher(s1,s2) + measure.jaccard_similarity(s1,s2))
            totnew = totnew + 0.25*(stringmatcher(tmp['PREVIOUS_NAMES'].values[k],cdmsnm) \
                                    + measure.jaccard_similarity(tmp['PREVIOUS_NAMES'].values[k],cdmsnm))
            #totnew = stringmatcher(tmp['PREVIOUS_NAMES'].values[k],cdmsnm) 
            if totnew > totscore:
                totscore = totnew
                q = k
        if totscore > score:
            gemsid = tmp['GEM_ID'].values[q]
            gemsnm = tmp['LEGAL_NAME'].values[q]
            matchq = 'PARTIAL (PREVIOUS_NAMES) - ' + str(int(totscore*100)) +'%'
            score = totscore
    del tmp
    tmp = full_universe[full_universe['TRADES_AS_NAMES'].apply(partial(stringmatcher1,cdmsnm)) > 0.50]
    if len(tmp) != 0:
        q = 0
        totscore = 0.0
        for k in range(len(tmp)):
            #s1 = re.split('/|,| ',tmp['TRADES_AS_NAMES'].values[k])
            #s2 = re.split('/|,| ',cdmsnm)
            s1 = tmp['TRADES_AS_NAMES'].values[k]
            s2= cdmsnm
            totnew = 0.25*(stringmatcher(s1,s2) + measure.jaccard_similarity(s1,s2))
            totnew = totnew + 0.25*(stringmatcher(tmp['TRADES_AS_NAMES'].values[k],cdmsnm) \
                                    + measure.jaccard_similarity(tmp['TRADES_AS_NAMES'].values[k],cdmsnm))
            #totnew = stringmatcher(tmp['TRADES_AS_NAMES'].values[k],cdmsnm)
            if totnew > totscore:
                totscore = totnew
                q = k
        if totscore > score:
            gemsid = tmp['GEM_ID'].values[q]
            gemsnm = tmp['LEGAL_NAME'].values[q]
            matchq = 'PARTIAL (TRADES_AS_NAMES) - ' + str(int(totscore*100)) +'%'   
    del tmp
    cdms_unmatched['GEM ID'].values[j] = gemsid
    cdms_unmatched['GEM LEGAL_NAME'].values[j] = gemsnm.upper()
    cdms_unmatched['MATCH QUALITY'].values[j] = matchq
"""

cdms_save = pd.read_excel('H:/Client Name Truth/Data/CDMS_TO_GEMS_MASTER.xlsx', sheetname = 'UNMATCHED')
cdms_unmatched['CDMS NAME'] = cdms_save['CDMS NAME']
#rearrange columns
#cdms_to_gems = cdms_to_gems[['CDMS CODE','CDMS NAME','GEM ID','GEM LEGAL_NAME','MATCH QUALITY']]