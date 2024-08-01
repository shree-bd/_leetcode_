# Write your MySQL query statement below
select name as Customers 
from customers c left join orders o on c.id=o.customerId 
group by c.id, c.name
having count(o.id) = 0