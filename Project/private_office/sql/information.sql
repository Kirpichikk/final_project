select
	doctor_name,
    specialization,
    name_department
from doctor
join department on doctor.id_department = department.id_department
where id_doctor = "$id_doctor"