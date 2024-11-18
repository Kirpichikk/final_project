SELECT
    rec_date, rec_time, id_shedule
FROM
    shedule
WHERE
    id_visit_card IS NULL AND id_doctor = "$id"
        AND rec_date >= NOW()
        AND rec_time >= NOW()