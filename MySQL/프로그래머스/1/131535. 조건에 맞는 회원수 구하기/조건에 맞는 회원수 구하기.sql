-- 코드를 입력하세요
SELECT count(*) as USERS
from user_info
where joined between '2021-01-01'
                and '2021-12-31'
and age >= 20 and age <=29;