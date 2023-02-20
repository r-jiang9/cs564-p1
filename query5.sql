SELECT COUNT(DISTINCT Seller_ID)
FROM Item i
INNER JOIN User u ON
i.Seller_ID = u.User_ID
WHERE u.Rating > 1000
