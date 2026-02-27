-- 코드를 입력하세요
SELECT b.title,
        b.board_id,
        r.reply_id,
        r.writer_id,
        r.contents,
        date_format(r.created_date, '%Y-%m-%d')
from USED_GOODS_BOARD as b, USED_GOODS_REPLY as r
where b.board_id = r.board_id
and b.created_date like '2022-10%'
order by r.created_date asc, b.title asc;