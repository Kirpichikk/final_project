SELECT
    id_shedule,
    rec_date,
    rec_time,
    doctor_name,
    specialization,
    number AS office
FROM
    shedule
        JOIN
    doctor ON shedule.id_doctor = doctor.id_doctor
        JOIN
    office ON shedule.id_office = office.id_office
WHERE
    id_shedule = "$id"