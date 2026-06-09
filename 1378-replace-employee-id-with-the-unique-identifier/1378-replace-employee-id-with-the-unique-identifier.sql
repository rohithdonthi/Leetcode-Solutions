# Write your MySQL query statement below
select e.unique_id, emp.name from employees emp
left join employeeUNI e on e.id = emp.id 
order by e.unique_id