SELECT COUNT(*) FROM (
SELECT COUNT(ItemCategory.category_ID)
FROM Bid, itemcategory
WHERE  bid.Item_ID = ItemCategory.Item_ID
    AND bid.Amount > 100
GROUP BY category_ID
);