select DISTINCT year(rec_date) as year, month(rec_date) as month
from shedule
order by month