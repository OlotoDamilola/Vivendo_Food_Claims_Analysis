UPDATE food_claims
SET amount_paid = 'R$ 19286.44'
WHERE amount_paid = 'NA';

SELECT * FROM human.food_claims;
SELECT 
	  claim_id,
      time_to_close,
      claim_amount,
      CONCAT('R$', ' ', amount_paid) AS amount_paid,
      location,
      individuals_on_claim,
      linked_cases,
      cause
FROM 
	  food_claims;

SELECT 
	   DISTINCT(location), 
	   COUNT(individuals_on_claim) OVER(PARTITION BY location) AS number_of_claims
FROM 
	   food_claims;
     

 
SELECT COUNT(individuals_on_claim) AS total_claim
FROM food_claims;

SELECT time_to_close, COUNT(time_to_close) AS occurence 
FROM food_claims
GROUP BY time_to_close
ORDER BY occurence DESC;

SELECT time_to_close, COUNT(time_to_close) AS count, DENSE_RANK() OVER(ORDER BY COUNT(time_to_close) DESC) AS ranks
FROM food_claims
WHERE location = "RECIFE"
GROUP BY time_to_close;

SELECT AVG(1.0 * time_to_close) AS mean 
FROM food_claims;

SELECT location, MAX(time_to_close) AS max_days, MIN(time_to_close) AS min_days
FROM food_claims
GROUP BY location;

SELECT location, COUNT(time_to_close) AS count
FROM food_claims
WHERE time_to_close > 272
GROUP BY location
ORDER BY count DESC;