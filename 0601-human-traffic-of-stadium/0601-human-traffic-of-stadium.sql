# Write your MySQL query statement below
with cte as (
    select
        id,
        visit_date,
        people,
        id - ROW_NUMBER() over (order by id) as grp
    from Stadium
    where people >= 100
)
select
    id,
    visit_date,
    people
from cte
where grp in (
    select grp
    from cte
    group by grp
    having count(*) >= 3
)
order by visit_date