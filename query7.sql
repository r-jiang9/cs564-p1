select count(*) from (
select count (ItemCategory.category_ID)
from Bid, itemcategory
where bid.Item_ID = ItemCategory.Item_ID
and bid.Amount > 100
group by category_ID
)