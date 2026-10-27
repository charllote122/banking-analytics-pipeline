-- Business Question: Who are our richest customers?
-- We need to JOIN the accounts table to the customers table.

SELECT 
    c.name,
    c.city,
    c.occupation,
    a.account_type,
    a.balance
FROM 
    accounts AS a
JOIN 
    customers AS c ON a.customer_id = c.customer_id
ORDER BY 
    a.balance DESC
LIMIT 10;