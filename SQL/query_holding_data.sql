select case a.FundNum when '71WR' then 1000 end assign_num, a.* from fund a where  a.FundNum in (select FundNum from FeeScheduleTbl)
select 'F'+ cast(Dense_rank() over(order by f.FundNum, f.FundName) as nvarchar(5)) as rank, f.* from Fund f
select * from Fund where ClientID like '%COHEN%'

select (case f.ClientID when 'Goldman' then 'Client1' when 'Cohen & Steers' then  'Client2' end) Client_Name,Dense_rank() over(order by f.FundNum) as Fund_ID, Dense_rank() over(order by f.FundCompositeName) as Composite_Name, f.FundType as Fund_Type, 
(case m.HOLD_DATE when '01/2016' then '200610' when '03/2016' then '200611' end) as Hold_Date, m.CUSIP, m.SHARES as Holding_shares, m.CURR_PRICE as Price, m.MARKET_VALUE as Market_Value, m.PRICE_CURR as Currency, m.TRADE_CTRY as Trade_Country, m.INVEST_TYPE as Invest_Type  from Fund f, mholdings m where  f.FundNum = m.FUND and (f.ClientID = 'Goldman' or f.ClientID = 'Cohen & Steers') and m.HOLD_DATE in ('01/2016','03/2016') order by f.ClienID,  f.FundCompositeName, f.FundNum, convert(int, substring(m.Hold_date,4,4)+substring(m.Hold_Date,1,2)),m. CUSIP 

select (case f.ClientID when 'Goldman' then 'Client1' when 'Cohen & Steers' then  'Client2' end) as Client_Name,f.FundNum as Fund_ID, f.FundCompositeName as Composite_Name, f.FundType as Fund_Type, 
(case m.HOLD_DATE when '01/2016' then '200610' when '03/2016' then '200611' end) as Hold_Date, m.CUSIP, m.SHARES as Holding_shares, m.CURR_PRICE as Price, m.MARKET_VALUE as Market_Value, m.PRICE_CURR as Currency, m.TRADE_CTRY as Trade_Country, m.INVEST_TYPE as Invest_Type  from Fund f inner join mholdings m on f.FundNum = m.FUND and (f.ClientID = 'Goldman' or f.ClientID = 'Cohen & Steers') and m.HOLD_DATE in ('01/2016','03/2016') group by f.ClientID,  f.FundNum, f.FundCompositeName, convert(int, substring(m.Hold_date,4,4)+substring(m.Hold_Date,1,2)),m.CUSIP, f.FundType 

select (case f.ClientID when 'Goldman' then 'Client1' when 'Cohen & Steers' then  'Client2' when 'Invesco' then 'Client3' when 'Brandeis University' then 'Client4'  when 'General Shale Products' then 'Client5' end) as Client_Name, 
'FeeSchedule' + cast(Dense_rank() over (order by f.FeeSchedule) as nvarchar(5)) as Fee_Schedule_ID, 'F' + cast(Dense_rank() over (order by f.FundNum) as nvarchar(5)) as Fund_ID, (case when f.FundCompositeName = f.FundNum then '' else 'COMP' + cast(Dense_rank() over (order by f.FundCompositeName) as nvarchar(5)) end) as Composite_Name, f.FundType as Fund_Type, 
convert(int, substring(m.Hold_date,4,4)+substring(m.Hold_Date,1,2)) as Hold_Date, m.CUSIP, m.SHARES as Holding_shares, m.CURR_PRICE as Price, m.MARKET_VALUE as Market_Value, m.PRICE_CURR as Currency, m.TRADE_CTRY as Trade_Country, 
m.INVEST_TYPE as Invest_Type from mholdings m, fund f where m.FUND = f.FundNum and f.ClientID in ('Goldman','Cohen & Steers','Inveco','Brandeis University','Gneral Shale Products')
order by Client_Name, Fee_Schedule_ID,  Fund_ID, Composite_Name, convert(int, substring(m.Hold_date,4,4)+substring(m.Hold_Date,1,2)),m.CUSIP, f.FundType 

select m.FUND, f.clientID, f.feeschedule, f.FundCompositeName, f.FundType, convert(int, substring(m.Hold_date,4,4)+substring(m.Hold_Date,1,2)) as Hold_Date, m.CUSIP, m.SHARES as Holding_shares, m.CURR_PRICE as Price, m.MARKET_VALUE as Market_Value, m.PRICE_CURR as Currency, m.TRADE_CTRY as Trade_Country
from mHoldings m, fund f where m.FUND = f.FundNum and f.FundName like '%etf%'
order by f.ClientID, m.FUND, Hold_Date

select distinct CUSIP, CURR_PRICE, convert(int, substring(Hold_date,4,4)+substring(Hold_Date,1,2)) as Hold_Date from mholdings order by CUSIP, Hold_date

select distinct CUSIP from mholdings

select * from mholdings where CUSIP = '58933YAS4' order by convert(int, substring(Hold_date,4,4)+substring(Hold_Date,1,2))

select 'Client_' + cast(Dense_rank() over (order by f.ClientID) as nvarchar(25)) as Client_Name, 'FS_' + cast(Dense_rank() over (order by f.FeeSchedule) as nvarchar(5)) as Fee_Schedule_ID, 'F' + cast(Dense_rank() over (order by f.FundNum) as nvarchar(5)) as Fund_ID,
(case when f.FundCompositeName = f.FundNum then 'N/A' else 'COMP' + cast(Dense_rank() over (order by f.FundCompositeName) as nvarchar(5)) end) as Composite_Name, f.FundType as Fund_Type, f.HoldType as Hold_Type, f.Division as Division from fund f

select 'Client_' + cast(Dense_rank() over (order by f.ClientID) as nvarchar(25)) as Client_Name, 'FS_' + cast(Dense_rank() over (order by f.FeeSchedule) as nvarchar(5)) as Fee_Schedule_ID, 'F' + cast(Dense_rank() over (order by f.FundNum) as nvarchar(5)) as Fund_ID,
(case when f.FundCompositeName = f.FundNum then 'N/A' else 'COMP' + cast(Dense_rank() over (order by f.FundCompositeName) as nvarchar(5)) end) as Composite_Name, f.FundType as Fund_Type, f.HoldType as Hold_Type,
convert(int, substring(m.Hold_date,4,4)+substring(m.Hold_Date,1,2)) as Hold_Date, m.CUSIP, m.SHARES as Holding_shares, m.CURR_PRICE as Price, m.MARKET_VALUE as Market_Value, m.PRICE_CURR as Currency, m.TRADE_CTRY as Trade_Country, 
m.INVEST_TYPE as Invest_Type from mholdings m, fund f where m.FUND = f.FundNum 

select distinct f.FundName as Fundtruth, 'Client_' + cast(Dense_rank() over (order by f.ClientID) as nvarchar(25)) as Client_Name, 'FS_' + cast(Dense_rank() over (order by f.FeeSchedule) as nvarchar(5)) as Fee_Schedule_ID, 'F' + cast(Dense_rank() over (order by f.FundNum) as nvarchar(5)) as Fund_ID,
(case when f.FundCompositeName = f.FundNum then 'N/A' else 'COMP' + cast(Dense_rank() over (order by f.FundCompositeName) as nvarchar(5)) end) as Composite_Name, f.FundType as Fund_Type, f.HoldType as Hold_Type,  m.CUSIP as CUSIP
from mholdings m, fund f where m.FUND = f.FundNum