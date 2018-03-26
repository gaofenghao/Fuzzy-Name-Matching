select p.*, t.* from products p, translation t where p.Productdescription like '%DTC%' and p.ProductType like 'trades' and p.ProductID = t.ProductID
select * from FundSpecificCode where FundNum is not null

select * from NavExclusionData where BillingDate = '09/2016'

select * from fund where FundNum like '%#%'

select distinct fs.feeschedule, fs.productID, p.productdescription, f.CBSID, f.ClientID from FeeScheduleTbl as fs, Fund as f, products as p
where fs.feeschedule in (select distinct feeschedule from Fund) and fs.FeeSchedule = f.FeeSchedule and fs.ProductID = p.ProductID    order by fs.FeeSchedule, fs.ProductID
select * from Products where ProductID like 'trades%'
select f.* from fund as f inner join FeeScheduleTbl as fs on f.FeeSchedule = fs.FeeSchedule inner join Products as p on fs.ProductID = p.ProductID where p.ProductType like 'trades%'

select distinct fs.feeschedule, f.CBSID from FeeScheduleTbl as fs, fund as f where fs.FeeSchedule = f.FeeSchedule