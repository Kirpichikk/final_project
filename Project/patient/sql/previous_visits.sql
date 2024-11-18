SELECT
    appoint_date,
    complains,
    doctor_name,
    specialization,
    diagnosis,
    appointments
FROM
    visit
        JOIN
    doctor ON doctor.id_doctor = visit.id_doctor
WHERE
    id_visit_card = '$id'
ORDER BY appoint_date DESC
LIMIT 2