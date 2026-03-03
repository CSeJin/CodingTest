-- 숫자로 변환 정렬
SELECT date_format(datetime, '%k') as HOUR,
        count(animal_id) as 'COUNT'
from animal_outs
where date_format(datetime, '%k') between 09 and 19
group by hour
order by hour + 0; 