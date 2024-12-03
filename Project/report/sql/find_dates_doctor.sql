select count(*)
from doctor
where year(date_layoff) = "$yyear"
and month(date_layoff) = "$mmonth"