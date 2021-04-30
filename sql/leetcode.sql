
select p.sub_id post_id,count(distinct s.sub_id) number_of_comments from submissions p left join submissions s
on p.sub_id = s.parent_id
where p.parent_id is null
group by p.sub_id
---------------------------------------------------------------------------------------------------

-- Ads performance
https://leetcode.com/problems/ads-performance/
SELECT ad_id, 
IFNULL(ROUND((SUM(action = 'Clicked') /SUM(action != 'Ignored')*100),2),0.00) AS ctr 
FROM Ads 
GROUP BY ad_id 
ORDER BY ctr DESC,ad_id ASC
---------------------------------------------------------------------------------------------------

-- Customer who bought A,B but not C
select  C.customer_id, C.customer_name
from Orders O
join Customers C on O.customer_id = C.customer_id
group by C.customer_id, C.customer_name
having 
sum(case when product_name='A' then 1 else 0 end) > 0 and 
sum(case when product_name='B' then 1 else 0 end) > 0 and
sum(case when product_name='C' then 1 else 0 end) = 0;

--Approach 2
with cte as
(
select
customer_id,
sum(case 
         when product_name = 'A' then 1
         when product_name = 'B' then 1
         when product_name = 'C' then 3
         else null end)   as score
from Orders
group by  customer_id
)
select
c.customer_id,
c.customer_name
from Customers c
left join cte on cte.customer_id = c.customer_id
where cte.score =  2

---------------------------------------------------------------------------------------------------

-- Emplloyees earning more tha thier managers
select e1.Name as Employee from Employee e1, Employee e2 where e2.Id = e1.ManagerID and e1.salary > e2.salary and e1.ManagerID is not null

---------------------------------------------------------------------------------------------------

-- n facebook, there is a follow table with two columns: followee, follower.Please write a sql query to get the amount of each follower’s follower if he/she has on
select f.followee as follower, count(distinct f.follower) as num
from follow f
join
(
    select distinct follower
    from follow
) g on f.followee = g.follower
group by 1
order by 1
---------------------------------------------------------------------------------------------------

-- Write an SQL query that reports all the projects that have the most employees
SELECT project_id
FROM
(SELECT project_id, RANK() OVER (ORDER BY COUNT(*) DESC) AS rk
FROM Project
GROUP BY project_id)a
WHERE rk = 1
-- #2
WITH t AS (
    SELECT project_id, COUNT(DISTINCT employee_id) N
FROM Project
GROUP BY project_id )
SELECT project_id
FROM t
WHERE N = (SELECT MAX(N) FROM t)

---------------------------------------------------------------------------------------------------
-- Avg experience years of employees of each project rounded to 2 digits
select project_id, round(avg(experience_years), 2) as average_years
from project p
join employee e on p.employee_id = e.employee_id
group by 1

---------------------------------------------------------------------------------------------------
-- Write an SQL query that reports the most experienced employees in each project. In case of a tie, report all employees with the maximum number of experience years.
with cte as (
SELECT a.project_id, a.employee_id,
RANK() OVER(partition by project_id order by experience_years DESC) as rnk
FROM Project a JOIN EMployee b ON a.employee_id = b.employee_id)
SELECT distinct a.project_id, a.employee_id
FROM cte JOIN Project a ON cte.employee_id = a.employee_id
and cte.project_id = a.project_id
where rnk = 1;

---------------------------------------------------------------------------------------------------
-- Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking.
-- Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.
select c.score, d.ran as 'Rank' from (
select a.score, ROW_NUMBER() OVER (ORDER BY a.score desc) AS ran from
(select distinct score from Scores) as a ) as d
inner join
Scores as c
on c.score = d.score
order by ran asc
