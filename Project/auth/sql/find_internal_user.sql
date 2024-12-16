SELECT
    role,
    id_inside,
    doctor_name,
    specialization,
    name_department,
    db_config
FROM
    users
        JOIN
    doctor ON id_inside = id_doctor
        JOIN
    department ON doctor.id_department = department.id_department
WHERE
    login = '$login'
        AND password = '$password'