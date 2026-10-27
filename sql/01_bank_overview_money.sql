-- ==========================================
-- Project: Banking Analytics
-- File: 01_bank_overview_money.sql
-- Business Question: Where is the bank's money?
-- ==========================================

SELECT 
    account_type,
    COUNT(account_id) AS total_number_of_accounts,
    SUM(balance) AS total_money_in_bank,
    ROUND(AVG(balance), 2) AS average_balance_per_account
FROM 
    accounts
GROUP BY 
    account_type
ORDER BY 
    total_money_in_bank DESC;