SELECT
    rec_time
FROM
    shedule
WHERE
    id_doctor = '$id_doctor'
        AND rec_date = '$rec_date'
        AND id_visit_card IS NULL
        AND TIMESTAMP(rec_date, TIME(rec_time)) > NOW()