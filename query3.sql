Select count(*) from
    (Select count(ic.item_ID) Categories
    From ItemCategory ic
    Group by  ic.item_id
    ) NumCategories
Where NumCategories.Categories = 4;