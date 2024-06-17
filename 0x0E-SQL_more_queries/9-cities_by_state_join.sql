-- this will print all the cities in the databes hbtn_0d_usa.
SELECT cities.`id`, cities.`name`, states.`name`
  FROM `cities` AS c
       JOIN `states` AS s
       ON c.`state_id` = s.`id`
 ORDER BY c.`id`;
