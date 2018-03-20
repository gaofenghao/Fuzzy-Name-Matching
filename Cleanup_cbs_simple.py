# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 13:49:14 2017

@author: e610086
"""

import string
import numpy as np
import pandas as pd

simple_clients = pd.read_excel('H:/Client Name Truth/CBS_Simple_Clients.xlsx')

#lower case
#simple_clients = simple_clients.Client_Name.str.lower()

#create a holder 
#example_cbs_simple_client = simple_clients['Client_Name']


#loading CBS address data
cbs_address = pd.read_excel('H:/Client Name Truth/Data/Cleint_address_from_CBS_Mark.xlsx')
#loading full universe data
#full_universe = pd.read.csv('H:/Client Name Truth/Data/FULL_UNIVERSE.csv')
#loading MCH
#full_MCH = pd.read_excel('H:/Client Name Truth/Data/Recon_by_client_id_0516.xlsx')
#loading CDMS customer hier
#CDMS_hier = pd.read_excel('H:/Client Name Truth/Data/CDMS_customer_hier.xlsx')
#MCH to CDMS
MCH_to_CDMS = pd.read_excel('H:/Client Name Truth/Data/MCH to CDMS Mappings.xlsx')
#FAR to CDMS
FAR_to_CDMS = pd.read_excel('H:/Client Name Truth/Data/FAR to CDMS Mappings.xlsx')
#MCH to GEMS
MCH_TO_GEMS = pd.read_excel('H:/Client Name Truth/Data/MCH_to_GEMS.xlsx')
#KYC Customer
KYC_LEGAL = pd.read_excel('H:/Client Name Truth/Data/KYC Legal_Entity_Details 6-9-17.xlsx')
#FTDR
FTDR_Fund_Client_Customer = pd.read_excel('H:/Client Name Truth/Data/FTDR_Fund_Client_Customer.xlsx')

result = pd.DataFrame(columns=('FUND_NO','FUND_NAME','MATCH_FUND_','GEMS_ID','CUSTOMER_NAME','PARENT_CUSTOMER','MATCH_CUSTOMER','CLIENT_NAME','PARENT_CLIENT','MATCH_CLIENT'))

for i in range(len(simple_clients)):
    tmp_funds = FTDR_Fund_Client_Customer[FTDR_Fund_Client_Customer['CUSTOMER_NAME'] == simple_clients['CUSTOMER_NAME'].values[i]]
    tmp_funds = tmp_funds[tmp_funds['BUSINESS_LINE'] != 'AIS']
    i = 0
    if len(tmp_funds) != 0:
        for j in range(len(tmp_funds)):
            fundnm = tmp_funds['FUND_NO'].values[j]
            fundname = tmp_funds['FUND_NAME'].values[j]
            MCH_set = MCH_TO_GEMS[MCH_TO_GEMS['ACCNT_ID'] == fundnm]
            gemsid = -1
            customernm = 'Not Found'         
            match_fund = 0.0
            match_client = 0.0
            match_customer = 0.0
            clientnm = 'Not Found'
            tmp_cbs = cbs_address[cbs_address['Fact ID'] == fundnm]
            if len(MCH_set) !=0:
                gemsid = MCH_set['GEMS_ID'].values[0]
                customernm = MCH_set['LGL_ENTITY_NM'].values[0]
                result.loc[i] = [fundnm,fundname,match_fund,gemsid,customernm,'tbd',match_customer,clientnm, 'tbd',match_client]
                i = i+1
                