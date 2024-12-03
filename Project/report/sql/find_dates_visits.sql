select count(*)
from shedule
where year(rec_date) = "$yyear"
and month(rec_date) = "$mmonth"