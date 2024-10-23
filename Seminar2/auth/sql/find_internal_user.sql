SELECT
    user_id,
    user_group
from users
where
    login = '$login'
    and password = '$password'