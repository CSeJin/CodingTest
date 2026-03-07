-- 코드를 작성해주세요
select concat(quarter(differentiation_date), 'Q') as quarter,
        count(id) as ecoli_count
from ecoli_data
group by quarter
order by quarter;






# select extract(quarter from differentiation_date) as quarter, count(*) as ecoli_count
# from ecoli_data
# group by extract(quarter from differentiation_date) as 
# order by quarter;