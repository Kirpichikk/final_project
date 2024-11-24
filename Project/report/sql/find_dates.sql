select DISTINCT year(date_of_sale) as year, month(date_of_sale) as month
from sellproducts
order by month