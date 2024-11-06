SELECT
    rec_time, name_patient, id_shedule, shedule.id_visit_card as id_patient
FROM
    shedule
        JOIN
    visit_card ON shedule.id_visit_card = visit_card.id_visit_card
WHERE
    rec_date = date("$date") AND id_doctor = "$id_doctor" and app_mark = 0