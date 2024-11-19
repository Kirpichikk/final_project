SELECT
    id_inside,
    NULL AS user_group,
    db_config
FROM external_users
WHERE 1=1
    AND login ='$login'
    AND password = '$password'
