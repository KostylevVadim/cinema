/*Рейтинг фильмов на основе рецензий всех пользователей
Разделение фильмов на хорошие, плохие и тд*/
WITH 
rating AS (
    SELECT film_series.id, AVG(review.rate) AS r
    FROM film_series
    jOIN review ON review.film_id = film_series.id
    GROUP BY film_series.id
    ORDER BY film_series.id
)

SELECT film_series.film_name,
CASE WHEN rating.r>8 THEN 'Brilliant'
     WHEN rating.r>6 AND rating.r<=8 THEN 'NICE'
     WHEN rating.r>4 and rating.r<=6 THEN 'NOT GOOD'
    ELSE 'BAD'
END
FROM film_series
JOIN rating ON rating.id = film_series.id;

/*
Рейтинг фильмов по жанрам
Разделение больше среднего и меньше среднего по жанру триллер
*/
WITH 
actions AS (
    SELECT film_series.id, AVG(review.rate) 
    FROM film_series
    JOIN review ON film_series.id = review.film_id
    JOIN filmganre ON filmganre.film_id = film_series.id
    JOIN genre ON genre.id = filmganre.ganre_id
    WHERE genre.ganre = 'action'
    GROUP BY film_series.id
    
),
adventures AS (
    SELECT film_series.id, AVG(review.rate) 
    FROM film_series
    JOIN review ON film_series.id = review.film_id
    JOIN filmganre ON filmganre.film_id = film_series.id
    JOIN genre ON genre.id = filmganre.ganre_id
    WHERE genre.ganre = 'adventure'
    GROUP BY film_series.id
    
),
animated AS (
    SELECT film_series.id, AVG(review.rate) 
    FROM film_series
    JOIN review ON film_series.id = review.film_id
    JOIN filmganre ON filmganre.film_id = film_series.id
    JOIN genre ON genre.id = filmganre.ganre_id
    WHERE genre.ganre = 'animated'
    GROUP BY film_series.id
    
),
comedy AS (
    SELECT film_series.id, AVG(review.rate) 
    FROM film_series
    JOIN review ON film_series.id = review.film_id
    JOIN filmganre ON filmganre.film_id = film_series.id
    JOIN genre ON genre.id = filmganre.ganre_id
    WHERE genre.ganre = 'comedy'
    GROUP BY film_series.id
    
),
drama AS (
    SELECT film_series.id, AVG(review.rate) 
    FROM film_series
    JOIN review ON film_series.id = review.film_id
    JOIN filmganre ON filmganre.film_id = film_series.id
    JOIN genre ON genre.id = filmganre.ganre_id
    WHERE genre.ganre = 'drama'
    GROUP BY film_series.id
    
),
fantasy AS (
    SELECT film_series.id, AVG(review.rate) 
    FROM film_series
    JOIN review ON film_series.id = review.film_id
    JOIN filmganre ON filmganre.film_id = film_series.id
    JOIN genre ON genre.id = filmganre.ganre_id
    WHERE genre.ganre = 'fantasy'
    GROUP BY film_series.id
    
),
historical AS (
    SELECT film_series.id, AVG(review.rate) 
    FROM film_series
    JOIN review ON film_series.id = review.film_id
    JOIN filmganre ON filmganre.film_id = film_series.id
    JOIN genre ON genre.id = filmganre.ganre_id
    WHERE genre.ganre = 'historical'
    GROUP BY film_series.id
    
),
horrors AS (
    SELECT film_series.id, AVG(review.rate) 
    FROM film_series
    JOIN review ON film_series.id = review.film_id
    JOIN filmganre ON filmganre.film_id = film_series.id
    JOIN genre ON genre.id = filmganre.ganre_id
    WHERE genre.ganre = 'horror'
    GROUP BY film_series.id
    
),
noir AS (
    SELECT film_series.id, AVG(review.rate) 
    FROM film_series
    JOIN review ON film_series.id = review.film_id
    JOIN filmganre ON filmganre.film_id = film_series.id
    JOIN genre ON genre.id = filmganre.ganre_id
    WHERE genre.ganre = 'noir'
    GROUP BY film_series.id
    
),
sci_fic AS (
    SELECT film_series.id, AVG(review.rate) 
    FROM film_series
    JOIN review ON film_series.id = review.film_id
    JOIN filmganre ON filmganre.film_id = film_series.id
    JOIN genre ON genre.id = filmganre.ganre_id
    WHERE genre.ganre = 'science fiction'
    GROUP BY film_series.id
    
),
thrill AS (
    SELECT film_series.id, AVG(review.rate) 
    FROM film_series
    JOIN review ON film_series.id = review.film_id
    JOIN filmganre ON filmganre.film_id = film_series.id
    JOIN genre ON genre.id = filmganre.ganre_id
    WHERE genre.ganre = 'Thriller'
    GROUP BY film_series.id
    
),
western AS (
    SELECT film_series.id, AVG(review.rate) 
    FROM film_series
    JOIN review ON film_series.id = review.film_id
    JOIN filmganre ON filmganre.film_id = film_series.id
    JOIN genre ON genre.id = filmganre.ganre_id
    WHERE genre.ganre = 'Western'
    GROUP BY film_series.id
    
),
trill_avg AS(
    SELECT  AVG(avg) AS AVG_FOREVER
    FROM thrill
)

SELECT thrill.id,
CASE 
    WHEN thrill.avg > trill_avg.AVG_FOREVER THEN 'ОК'
    WHEN thrill.avg < trill_avg.AVG_FOREVER THEN 'NOT OK'
END
FROM thrill, trill_avg;

/*Серии сериала, длина сериала основываясь на одной серии*/

WITH 
series AS (
    SELECT * 
    FROM film_series
    WHERE filorser = 'False' 
)

SELECT id, film_name,
CASE
    WHEN season < 50 THEN 'NOT LONG'
    WHEN season >= 50 AND season <=60 THEN 'LONG'
    WHEN season >= 61 AND season <=100 THEN 'VERY LONG'
    WHEN season >= 101 AND season <=200 THEN 'TOO LONG'
    WHEN season >= 201 THEN 'ONE OF THE LONGEST'
END
FROM series
ORDER BY series.season;

/*Ранжирование ревью проверенных пользователей по 
полезности относительно рейтинга*/

WITH 
review_rating AS (
    SELECT users.username AS username, 
        review.review_rate AS review_rate, 
        review.varified AS varified
    FROM users
    JOIN review ON users.id = review.usr_id

)
SELECT username,
CASE 
    WHEN review_rate >= 60 THEN 'VERY USEFULL'
    WHEN review_rate < 60 AND review_rate>=20 THEN 'USEFULL'
    WHEN review_rate < 20 AND review_rate>=0 THEN 'USEFULL ENOUGH'
    WHEN review_rate < 0 AND review_rate>=-20 THEN 'USELESS'
    WHEN review_rate < -20 THEN 'VERY USELESS'
END
FROM review_rating
WHERE varified = 'True'
ORDER BY review_rate DESC;

/*Вывод количества фильмов в подписке для обладателей подписки
и не в подписке - для не обладателей*/

WITH 
not_in_sub AS(
    SELECT id 
    FROM film_series fs
    WHERE NOT EXISTs (
        SELECT *
        FROM sub
        WHERE fs.id = film_id
    )
)


SELECT username,
CASE
    WHEN sub = 'True' THEN (SELECT COUNT(sub.film_id) FROM sub)
    WHEN sub = 'False' THEN 
    (SELECT  COUNT(not_in_sub.id) FROM not_in_sub)
END
FROM users;
