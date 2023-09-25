/*Отзывы о фильмах, оценивших фильм более чем на 6 с текстом*/

SELECT film_series.id,review.rate,review.txt
FROM film_series
JOIN review ON film_series.id = review.film_id
WHERE review.rate>6
ORDER BY film_series.id;

/*Краткая биография живых персон с их профессиями в фильмах, в которых
Участвовали*/

SELECT person.per_name, 
       person.bio, count(DISTINCT(profession.prof)) as prof_count, count(DISTINCT(film_series.film_name)) as film_count
FROM person
JOIN profession ON person.id = profession.per_id
JOIN film_series ON profession.film_id = film_series.id
WHERE person.death_date IS NULL
GROUP BY person.per_name, person.bio
ORDER BY film_count DESC;


/*Названия фильмов, отсортированные по языкам, выпущенные после 1985-02-03*/

SELECT lang.langname, film_series.film_name
FROM film_series
JOIN film_lang ON film_series.id = film_lang.film_id
JOIN lang ON lang.id = film_lang.lang_id
WHERE film_series.date_real > '1985-02-03'
ORDER BY lang.langname;


/*Текст рецензии подтвержденных пользователей с названием фильма*/

SELECT film_series.film_name, review.txt
FROM film_series
JOIN review ON review.film_id = film_series.id
WHERE review.varified = 'True';

/*Польлзователь, фильм, рецензия фильма из просмотренных*/

SELECT users.username, film_series.film_name, review.txt
FROM users
JOIN comp ON users.id = comp.usr_id
JOIN film_series ON film_series.id = comp.film_id
JOIN review ON review.usr_id = users.id
WHERE review.film_id = film_series.id AND comp.spec = 1;
