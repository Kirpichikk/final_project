select year, month, count_doctors, department
from report_layoff_doctor
where year = "$year"
and month = "$month"