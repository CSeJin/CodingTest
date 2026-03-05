-- 코드를 작성해주세요
select sum(g.score) as score,
    e.emp_no,
    e.emp_name,
    e.position,
    e.email
from hr_employees e, hr_grade g
where e.emp_no = g.emp_no
group by g.emp_no
order by score desc
limit 1;