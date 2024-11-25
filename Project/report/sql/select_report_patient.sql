select year, month, count_patient
from report_count_new_patient
where year = "$year"