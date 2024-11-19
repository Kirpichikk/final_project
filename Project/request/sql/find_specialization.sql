SELECT
    doctor_name
FROM
    doctor
WHERE
    specialization = '$specialization'
    and  date_layoff IS NULL