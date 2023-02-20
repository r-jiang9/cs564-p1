SELECT Item_ID
FROM Item
WHERE Currently = 
(SELECT MAX(Currently)
FROM Item);
