products
+---------------------------+
| product_id | int |
| product_class_id | int |
| brand_name | varchar | |
| product_name | varchar |
| price | int | 
---------------------
sales
| product_id | int |
| store_id | int |
| customer_id | int |
| promotion_id | int |
| store_sales | decimal |
| store_cost | decimal |
| units_sold | decimal |
| transaction_date | date 
---------------------
stores
| store_id | int |
| type | varchar  | 
| name | varchar  | 
| state | varchar | 
| first_opened_date | datetime|
| last_remodel_date | datetime|
| area_sqft | int |
---------------------------------
customers
| customer_id | int |
| first_name | varchar |
| state | varchar |
| birthdate | date |
| gender | varchar |
| date_account_opened | date |


--  What brands have an average price above $3 and contain at least 2 different products?
select brand_name
from product
group by brand_name
having avg(price)>3 and count(distinct product_id) >= 2;

-- what percent of our sales transactions had a valid promotion applied?
select
round(sum(case
when promotion_id > 0 then 1
else 0
end)*100.0/count(*),2)
from sales;

-- what are the top 3 selling product classes by total sales?
select p.product_class_id
from
sales s
join product p
on s.product_id = p.product_id
group by p.product_class_id
order by sum(p.price*s.units_sold) desc limit 3;

-- We are considering running a promo across brands. We want to target customers who have bought products from two specific brands.
-- Can you find out which customers have bought products from both the “Fort West" and the "Golden" brands?
select customer_id, count(distinct brandname) from sales s inner join products p
on s.product_id = p.product_id
where p.brand_name in ("fort west", " Golden")
group by customer_id having count(distinct brandname ) = 2

-- given table products(product_id, brand_name,product_name, product_price), find brand_names with avg price > 3 and having more then 5 products
select distinct brand_names from sales s inner join products p
on s.product_id = p.product_id
group by brand_names having AVG(price) > 3 and count(distinct product_id) > 5

-- what %age of products have both low fat and recycable .
select
sum(case when is_low_fat = 1 and is_recyclable = 1 then 1 else 0 end) * 100.0 / count(*) as percentage
from product

select s.promotion_id,
 round((sum(case when s.transaction_date = (p.promo_start_date) 
            or s.transaction_date = (p.promo_end_date) then (store_cost * units_sold) else 0 end) * 100.0
 / sum((store_cost * units_sold))),2)
 from sales s inner join  promotion p on p.promotion_id = s.promotion_id
 group by s.promotion_id

-- find top 5 sales products having promotions

select product_id
from sales
where promotion_id is not null
group by product_id
order by sum(units_sold * store_cost) desc
limit 5

-- what %age of sales happened on first and last day of the promotion
-- Not sure if this asked for all promotions or % for each promotion. in case all -
SELECT Round(Sum(
CASE
WHEN Min(start_date) = transaction_date THEN 1
WHEN Max(end_date) = transaction_date THEN 1
ELSE 0
END) 100/ Count(), 2)
FROM sales s
JOIN promotions p s.promotion_id = p.promotion_id

-- What are the top five (ranked in decreasing order) single-channel media types that correspond to the most money the grocery chain had spent on its promotional campaigns?
select media_type
from promotions
order by cost desc
limit 5

-- the proportion of valid sales that occurred on certain dates.
select
sum(case when transaction_date = 'certain_date' then 1 end)/count(*)
from sales
where valid sales

-- Manager want to analyze the how the promotions on certain products are performing.find how the the percent of promoted sales?
count of promoted sales* 100 /total sale

-- Get the top3 product class_id by the total sales.
select product_class_id
from product join sales on product_id
order by sum(units * store_cost) desc
limit 3
