select year, month, pname, name, price_of_kg, sum_price, value_in_kg
from reports
join categories on id_categories = category
where year = "$year"
and month = "$month"