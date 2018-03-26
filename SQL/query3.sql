select * from Products where ProductDescription like '%SUBCUSTdy%'

select * from LogCurrentData where ProductType like '%SAFEKEEPBP%'

select HOLD_DATE, sum(MARKET_VALUE) from mHoldings where FUND in (select FundNum as Fund from Fund where CBSCLient like 'AXAX') group by HOLD_DATE

select * from Fund where ClientID like '%AXA%'



select * from NavData where FundNum in (select FundNum from Fund where CBSCLient like 'AXAX')

select * from Fund where FundType <> 'A' order by FundType

select * from mTransactions where FUND = 'BGFX'
select * from LogCurrentData where FundNum = 'BGFX'

select * from Users where Role <> 'A' and Role <>'U' and Role <> 'P'
select distinct Status from Users
select * from Fund where FundType = 'A'
