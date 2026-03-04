-- 코드를 작성해주세요
select count(f.id) as fish_count, n.fish_name
from fish_info f, fish_name_info n
where f.fish_type = n.fish_type
group by n.fish_name
order by fish_count desc;
