SELECT 
    floor
FROM
    department
        JOIN
    office ON department.id_department = office.id_department
WHERE
    number = '$number'