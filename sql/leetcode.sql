

select p.sub_id post_id,count(distinct s.sub_id) number_of_comments from submissions p left join submissions s
on p.sub_id = s.parent_id
where p.parent_id is null
group by p.sub_id

-- Ads performance
https://leetcode.com/problems/ads-performance/
SELECT ad_id, 
IFNULL(ROUND((SUM(action = 'Clicked') /SUM(action != 'Ignored')*100),2),0.00) AS ctr 
FROM Ads 
GROUP BY ad_id 
ORDER BY ctr DESC,ad_id ASC
