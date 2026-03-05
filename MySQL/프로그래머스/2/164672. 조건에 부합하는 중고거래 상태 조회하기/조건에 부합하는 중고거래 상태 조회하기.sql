-- 코드를 입력하세요
SELECT board_id, writer_id, title, price,
        case
            when u.status = 'SALE' then '판매중'
            when u.status = 'RESERVED'then '예약중'
            when u.status = 'DONE' then '거래완료'
        end as 'STATUS'
from used_goods_board u
where created_date = '2022-10-05'
order by board_id desc;
