SELECT
    rec_date, rec_time, id_shedule
FROM
    shedule
WHERE
    id_visit_card IS NULL AND id_doctor = "$id"
        AND TIMESTAMP(rec_date, TIME(rec_time)) >= NOW()
        AND TIMESTAMP(rec_date, TIME(rec_time)) <= DATE_ADD(NOW(), INTERVAL 1 MONTH)