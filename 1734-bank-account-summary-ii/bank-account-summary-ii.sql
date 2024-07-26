# Write your MySQL query statement below
-- select name, balance
-- from 
--     (select t.account, u.name, sum(t.amount) as balance
--     from users u join transactions t on u.account = t.account
--     group by t.account, u.name) a
-- where balance > 10000;



select  u.name,sum(t.amount) as balance
from transactions t
join users u on t.account = u.account 
group by u.name
having balance>10000