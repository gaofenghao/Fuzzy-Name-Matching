"""
Created on 11/30/2017 10:31 AM

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
    

rest_name = pd.read_excel('H:/Client Name Truth/Data/Rest_8935_add_SF.xlsx')

#clening 
rest_name['CDMS NAME'] = rest_name['CDMS NAME'].str.lower()
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace('\n',' \n')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace('.',' ')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace(',',' ')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace('\'','')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace(' & ',' and ')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace(' &',' and ')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace('& ',' and ')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace('&',' and ')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace(' l p ',' lp ')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace('l l p ','llp ')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace('l l c ','llc ')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace(' ltd ',' limited ')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace(' p l c ',' plc')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace(' co ltd ',' company limited ')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace(' co ',' company ')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace(' corp ',' corporation ')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace(' univ ',' university ')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace(' fdtn ',' foundation ')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace(' inc ',' incorporated ')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace(' assoc ',' association ')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace(' mgmt ',' management ')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace(' svsc ',' services ')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace(' ag ',' aktiengesellschaft ')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace(' govt ',' goverment ')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace(' svgs ',' savings ')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace(' intl ',' international ')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace('intl ','international ')
rest_name['CDMS NAME'] =rest_name['CDMS NAME'].str.replace(' investmentco lt ',' investment company limited ')
rest_name['CDMS NAME'] = rest_name['CDMS NAME'].str.replace('the ','')
rest_name['CDMS NAME'] = rest_name['CDMS NAME'].str.replace(' the ','')
rest_name['CDMS NAME'] = rest_name['CDMS NAME'].str.strip()

rest_name['SF360 ACCOUNT NAME'] = rest_name['SF360 ACCOUNT NAME'].str.lower()
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace('\n','  \n')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace('.',' ')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace(',',' ')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace('\'','')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace(' & ',' and ')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace(' &',' and ')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace('& ',' and ')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace('&',' and ')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace(' l p',' lp ')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace('l l p','llp ')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace('l l c','llc ')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace(' ltd',' limited ')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace(' p l c',' plc')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace(' co ltd',' company limited ')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace(' co',' company ')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace(' corp',' corporation ')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace(' univ',' university ')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace(' fdtn',' foundation ')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace(' inc',' incorporated ')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace(' assoc',' association ')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace(' mgmt',' management ')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace(' svsc',' services ')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace(' ag',' aktiengesellschaft ')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace(' govt',' goverment ')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace(' svgs',' savings ')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace(' intl',' international ')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace('intl ','international ')
rest_name['SF360 ACCOUNT NAME'] =rest_name['SF360 ACCOUNT NAME'].str.replace(' investmentco lt',' investment company limited ')
rest_name['SF360 ACCOUNT NAME'] = rest_name['SF360 ACCOUNT NAME'].str.replace('the ','')
rest_name['SF360 ACCOUNT NAME'] = rest_name['SF360 ACCOUNT NAME'].str.replace(' the ','')
rest_name['SF360 ACCOUNT NAME'] = rest_name['SF360 ACCOUNT NAME'].str.strip()

rest_name.to_excel('H:/Client Name Truth/Data/Rest_8935_add_SF_clean_name.xlsx',index=False)

del rest_name
rest_name = pd.read_excel('H:/Client Name Truth/Data/Copy of FULL_UNIVERSE 6-19-17.xlsx')
rest_name['LEGAL_NAME'] = rest_name['LEGAL_NAME'].str.lower()
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace('\n',' \n')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace('.',' ')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace(',',' ')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace('\'','')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace(' & ',' and ')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace(' &',' and ')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace('& ',' and ')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace('&',' and ')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace(' l p ',' lp ')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace('l l p ','llp ')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace('l l c ','llc ')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace(' ltd ',' limited ')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace(' p l c ',' plc')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace(' co ltd ',' company limited ')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace(' co ',' company ')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace(' corp ',' corporation ')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace(' univ ',' university ')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace(' fdtn ',' foundation ')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace(' inc ',' incorporated ')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace(' assoc ',' association ')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace(' mgmt ',' management ')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace(' svsc ',' services ')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace(' ag ',' aktiengesellschaft ')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace(' govt ',' goverment ')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace(' svgs ',' savings ')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace(' intl ',' international ')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace('intl ','international ')
rest_name['LEGAL_NAME'] =rest_name['LEGAL_NAME'].str.replace(' investmentco lt ',' investment company limited ')
rest_name['LEGAL_NAME'] = rest_name['LEGAL_NAME'].str.replace('the ','')
rest_name['LEGAL_NAME'] = rest_name['LEGAL_NAME'].str.replace(' the ','')
rest_name['LEGAL_NAME'] = rest_name['LEGAL_NAME'].str.strip()

rest_name['PREVIOUS_NAMES'] = rest_name['PREVIOUS_NAMES'].str.lower()
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace('\n',' \n')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace('.',' ')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace(',',' ')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace('\'','')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace(' & ',' and ')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace(' &',' and ')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace('& ',' and ')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace('&',' and ')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace(' l p ',' lp ')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace('l l p ','llp ')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace('l l c ','llc ')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace(' ltd ',' limited ')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace(' p l c ',' plc')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace(' co ltd ',' company limited ')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace(' co ',' company ')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace(' corp ',' corporation ')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace(' univ ',' university ')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace(' fdtn ',' foundation ')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace(' inc ',' incorporated ')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace(' assoc ',' association ')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace(' mgmt ',' management ')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace(' svsc ',' services ')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace(' ag ',' aktiengesellschaft ')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace(' govt ',' goverment ')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace(' svgs ',' savings ')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace(' intl ',' international ')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace('intl ','international ')
rest_name['PREVIOUS_NAMES'] =rest_name['PREVIOUS_NAMES'].str.replace(' investmentco lt ',' investment company limited ')
rest_name['PREVIOUS_NAMES'] = rest_name['PREVIOUS_NAMES'].str.replace('the ','')
rest_name['PREVIOUS_NAMES'] = rest_name['PREVIOUS_NAMES'].str.replace(' the ','')
rest_name['PREVIOUS_NAMES'] = rest_name['PREVIOUS_NAMES'].str.strip()

rest_name['TRADES_AS_NAMES'] = rest_name['TRADES_AS_NAMES'].str.lower()
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace('\n',' \n')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace('.',' ')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace(',',' ')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace('\'','')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace(' & ',' and ')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace(' &',' and ')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace('& ',' and ')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace('&',' and ')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace(' l p ',' lp ')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace('l l p ','llp ')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace('l l c ','llc ')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace(' ltd ',' limited ')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace(' p l c ',' plc')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace(' co ltd ',' company limited ')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace(' co ',' company ')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace(' corp ',' corporation ')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace(' univ ',' university ')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace(' fdtn ',' foundation ')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace(' inc ',' incorporated ')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace(' assoc ',' association ')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace(' mgmt ',' management ')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace(' svsc ',' services ')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace(' ag ',' aktiengesellschaft ')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace(' govt ',' goverment ')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace(' svgs ',' savings ')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace(' intl ',' international ')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace('intl ','international ')
rest_name['TRADES_AS_NAMES'] =rest_name['TRADES_AS_NAMES'].str.replace(' investmentco lt ',' investment company limited ')
rest_name['TRADES_AS_NAMES'] = rest_name['TRADES_AS_NAMES'].str.replace('the ','')
rest_name['TRADES_AS_NAMES'] = rest_name['TRADES_AS_NAMES'].str.replace(' the ','')
rest_name['TRADES_AS_NAMES'] = rest_name['TRADES_AS_NAMES'].str.strip()

rest_name.to_excel('H:/Client Name Truth/Data/Copy of FULL_UNIVERSE_clean_name.xlsx',index=False)