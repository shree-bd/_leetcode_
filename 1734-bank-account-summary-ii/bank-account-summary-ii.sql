# Write your MySQL query statement below
select name, balance
from 
    (select t.account, u.name, sum(t.amount) as balance
    from users u join transactions t on u.account = t.account
    group by t.account, u.name) a
where balance > 10000;