-- 방법 1
SELECT *
from car_rental_company_car
where options like '%네비게이션%'
order by car_id desc;

-- 방법 2
SELECT *
from car_rental_company_car
where instr(options, '네비게이션') >0
order by car_id desc;