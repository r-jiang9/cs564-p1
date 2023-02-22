SELECT Count(*) FROM
    (SELECT Count(ic.item_ID) Categories
    FROM ItemCategory ic
    GROUP BY ic.item_id) NumCategories
WHERE NumCategories.Categories = 4;