select DISTINCT year(date_layoff) as year, month(date_layoff) as month
from doctor
where date_layoff is not null
order by month