select year, month, count, doctor_name, specialization
from report_ended_visits
where year = "$year"
and month = "$month"