/*Все фильмы начинающиеся на Lord*/
SELECT * 
FROM film_series
WHERE film_name LIKE 'Lord%';

/*Все пользователи с началом юзернейма на а */

SELECT * 
FROM users
WHERE username LIKE 'a%';

/*Все пользователи, у которых привязанная почта - gmail*/

SELECT * 
FROM users
WHERE mail LIKE '%@gmail.com';

/*Все отзывы, которые имеют в своем тексте слово Bad, 
пользователь,
фильм к которому рецензия*/

SELECT review.rate, review.txt, users.username, film_series.film_name
FROM review
JOIN users ON users.id = review.usr_id
JOIN film_series ON film_series.id = review.film_id
WHERE txt LIKE '%bad%' OR txt LIKE '%Bad%'
ORDER BY review.rate DESC;


/*имена персон - не профессионалов*/

SELECT per_name
FROM person
WHERE bio LIKE '%not proffesional%';

/*Имя персон в имени есть а, название фильма в название b
*/

SELECT person.per_name, film_series.film_name
FROM person
JOIN profession ON profession.per_id = person.id
JOIN film_series ON film_series.id = profession.film_id
WHERE (person.per_name LIKE 'A%' OR person.per_name LIKE '%a%') 
AND (film_series.film_name LIKE '%b%');


/*Экстремальные оценки отзывов проверенных пользователей*/

WITH 
review_rating AS (
    SELECT users.username AS username, 
    review.review_rate AS review_rate, review.varified AS varified
    FROM users
    JOIN review ON users.id = review.usr_id

),
review_ranking AS (
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
    ORDER BY review_rate DESC
)

SELECT * FROM review_ranking WHERE review_ranking.case LIKE 'VERY%';


