# Write your MySQL query statement below
select name, ifnull(sum(distance),0) as travelled_distance 
from Users u left join Rides r on u.id=r.user_id
group by name, u.id
order by travelled_distance desc, name