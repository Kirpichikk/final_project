SELECT
    id_inside,
    NULL AS role,
    db_config
FROM external_users
WHERE 1=1
    AND login ='$login'
    AND password = '$password'
