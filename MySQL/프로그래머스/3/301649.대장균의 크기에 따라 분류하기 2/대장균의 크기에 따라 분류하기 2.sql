select id,
    case
        when pct <= 25 then 'CRITICAL'
        when pct <= 50 then 'HIGH'
        when pct <= 75 then 'MEDIUM'
        else 'LOW'
    end as colony_name
from (select id,
        percent_rank() over (order by size_of_colony desc) *100 as pct
     from ecoli_data) d
order by id asc;