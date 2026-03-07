-- 코드를 작성해주세요
select i.item_id, i.item_name, i.rarity
from item_info i
join item_tree t on i.item_id = t.item_id
join item_info i2 on i2.item_id = t.parent_item_id
where i2.rarity = 'RARE'
order by i.item_id desc;