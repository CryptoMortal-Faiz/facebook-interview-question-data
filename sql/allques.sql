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


