SELECT
    role,
    id_inside
from users
where
    login = '$login'
    and password = '$password'