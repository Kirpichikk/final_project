SELECT
    id_doctor, doctor_name
FROM
    doctor
WHERE
    specialization = "$specialization"
        AND date_layoff IS NULL