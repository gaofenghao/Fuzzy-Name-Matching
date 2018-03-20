# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:23:08 2017

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

#cdms_code = 'WELL000'
#client_gemid = '196016807'

#cdms_code = 'QSUP000'
#client_gemid = '215912645'

cdms_code = 'GOLD000'
client_gemid = '218112600'

mch_cdms = pd.read_excel('H:/Client Name Truth/Data/MCH to CDMS Mappings.xlsx')
mch_gems = pd.read_excel('H:/Client Name Truth/Data/MCH_to_GEMS.xlsx') 
kycall = pd.read_excel('H:/Client Name Truth/Data/KYC Legal_Entity_Details 6-9-17.xlsx') 

mch_fund = mch_cdms[mch_cdms['CDMS Ulitmate Parent Code'] == cdms_code]
cust_gems = mch_gems[mch_gems['ACCNT_ID'].isin(mch_fund['MCH Fund ID'])]

cust_gems = cust_gems.drop_duplicates(['GEMS_ID'],keep ='first')

client_request = pd.DataFrame(index = range(5000))
client_request['Client GEM ID'] = '' 
client_request['Client Name'] = ''
client_request['Customer GEM ID'] = ''
client_request['Customer Name'] = ''
client_request['Product Division'] = ''
client_request['Product BU'] = ''
client_request['Product BU Location'] = ''
client_request['Product Family'] = ''
client_request['Product Tier'] = ''
client_request['Contracting Entity'] = ''
 
ind = 0              
for i in range(len(cust_gems)):
    gemid = cust_gems['GEMS_ID'].values[i]
    tmp = kycall[kycall['GEMS ID'] == str(gemid)]
    if len(tmp) > 0:
        for j in range(len(tmp)):
            client_request['Client GEM ID'][ind] = client_gemid
            #client_request['Client Name'][ind] = 'Wellington Management Company LLP'
            #client_request['Client Name'][ind] = 'QSuper Limited'
            client_request['Client Name'][ind] = 'The Goldman Sachs Group, Inc.'
            client_request['Customer GEM ID'][ind] = gemid
            client_request['Customer Name'][ind] = tmp['Legal Entity Name'].values[j]
            client_request['Product Division'][ind] = tmp['Product Division'].values[j]
            client_request['Product BU'][ind] = tmp['PRODUCT BU'].values[j]
            client_request['Product BU Location'][ind] = tmp['PRODUCT BU LOCATION'].values[j]
            client_request['Product Family'][ind] = tmp['Product Family'].values[j]
            client_request['Product Tier'][ind] = tmp['Product Tier'].values[j]
            client_request['Contracting Entity'][ind] = tmp['Contracting Entity'].values[j]
            ind = ind + 1
        del tmp
    else:
        client_request['Client GEM ID'][ind] = client_gemid
        #client_request['Client Name'][ind] = 'Wellington Management Company LLP'
        #client_request['Client Name'][ind] = 'QSuper Limited'
        client_request['Client Name'][ind] = 'The Goldman Sachs Group, Inc.'
        client_request['Customer GEM ID'][ind] = gemid
        client_request['Customer Name'][ind] = cust_gems['LGL_ENTITY_NM'].values[i]
        client_request['Product Division'][ind] = 'N/A'
        client_request['Product BU'][ind] = 'N/A'
        client_request['Product BU Location'][ind] = 'N/A'
        client_request['Product Family'][ind] = 'N/A'
        client_request['Product Tier'][ind] = 'N/A'
        client_request['Contracting Entity'][ind] = 'N/A'
        ind = ind + 1


