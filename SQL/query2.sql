select * from LogFinalData where BillingDate = '01/2010'

select * from NavData where FundNum = '1158' order by convert(int, substring(BillingDate,4,4)+substring(BillingDate,1,2))

select * from mHoldings where FUND = '1158' order by convert(int, substring(Hold_date,4,4)+substring(Hold_Date,1,2))

select distinct CrossProductID from CrossProducts

select * from Fund where FundNum = '2MN8'

select * from products where Producttype like '%custody%' or ProductKey1 like '%custody%' or ProductKey2 like '%custody%'

select HOLD_DATE, sum(MARKET_VALUE) from mholdings where FUND = '2M55' group by HOLD_DATE order by convert(int, substring(Hold_date,4,4)+substring(Hold_Date,1,2))

select distinct invest_type_CD from mTransactions

select * from mTransactions where FUND = '2MN1' order by TRADE_DATE

select * from mholdings where FUND = '2M44' order by convert(int, substring(Hold_date,4,4)+substring(Hold_Date,1,2))

select a0415.CUSIP, 