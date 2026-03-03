-- 코드를 입력하세요
SELECT i.INGREDIENT_TYPE, sum(f.total_order) as total_order
from icecream_info i, first_half f
where i.flavor = f.flavor
group by i.ingredient_type
order by total_order;