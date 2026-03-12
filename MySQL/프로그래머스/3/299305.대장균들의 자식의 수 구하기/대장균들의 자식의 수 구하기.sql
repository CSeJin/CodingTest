select e1.id,
    ifnull(e2.child_count, 0) as child_count
from ecoli_data e1
left join (select parent_id, count(parent_id) as child_count
    from ecoli_data
    group by parent_id) e2
on e1.id = e2.parent_id
order by e1.id;

