SELECT
    id_shedule, rec_date, rec_time, doctor_name
FROM
    shedule
        JOIN
    doctor ON doctor.id_doctor = shedule.id_doctor
WHERE
    TIMESTAMP(rec_date, TIME(rec_time)) > NOW()  -- Записи в будущем
    AND TIMESTAMP(rec_date, TIME(rec_time)) <= DATE_ADD(NOW(), INTERVAL 1 MONTH)  -- Записи не позже чем через месяц
    AND id_visit_card IS NULL