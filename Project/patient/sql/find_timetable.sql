SELECT
    rec_date, rec_time, id_shedule
FROM
    shedule
WHERE
    id_visit_card IS NULL AND id_doctor = "$id"
        AND ADDDATE(rec_date, TIME(rec_time)) >= NOW()