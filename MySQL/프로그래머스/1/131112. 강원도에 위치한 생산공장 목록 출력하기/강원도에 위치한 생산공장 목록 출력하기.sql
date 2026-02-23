-- 코드를 입력하세요
SELECT factory_id, factory_name, address
from food_factory
where address like "강원도%" ;

-- like 와일드 카드를 사용한다.

-- %: 0개 이상의 문자(null은 제외)

-- _: 한 개의 문자

-- []: 대괄호 내 문자 중 하나 이상 존재하는 컬럼 반환

-- [^ ]: 대괄호 내 문자가 없는 컬럼 반환
