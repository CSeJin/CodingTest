-- 방법 1
select *
from food_product
where price = (select max(price) from food_product);

-- 방법 2
select *
from food_product
order by price desc
limit 1;