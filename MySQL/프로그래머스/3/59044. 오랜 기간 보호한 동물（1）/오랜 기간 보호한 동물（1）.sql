-- 코드를 입력하세요
# SELECT distinct i.name, i.datetime
# from animal_ins i
# join animal_outs o on i.animal_id not in (o.animal_id)
# order by i.datetime
# limit 3;

select name, datetime
from animal_ins
where animal_id not in (select animal_id
                       from animal_outs)
order by datetime
limit 3;
