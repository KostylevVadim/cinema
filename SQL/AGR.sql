/*Максимальная оценка по фильму*/

SELECT film_series.id,MAX(review.rate)
FROM film_series
JOIN review ON film_series.id = review.film_id
WHERE film_series.filorser = 'True'
GROUP BY film_series.id
ORDER BY film_series.id;

/*Количество профессий у каждой персоны*/

SELECT person.id, person.per_name, COUNT(profession.film_id)
FROM person
JOIN profession ON person.id = profession.per_id
GROUP BY person.id
ORDER BY person.id;

/*Средняя стоимость фильма*/

SELECT film_name, AVG(cost)
FROM film_series
WHERE filorser='True'
GROUP BY film_name;

/*Максимальный и минимальный возраст для просмотра фильмов по жанрам*/

SELECT MAX(film_series.age),MIN(film_series.age), genre.ganre
FROM film_series
JOIN filmganre ON film_series.id = filmganre.film_id
JOIN genre ON filmganre.ganre_id = genre.id
WHERE film_series.filorser = 'True' 
GROUP BY genre.ganre, genre.id
ORDER BY genre.id;

/*Подсчет количества фильмов и серий сериалов в компиляциях проверенных пользователей*/

SELECT users.username, comp.spec, COUNT(comp.film_id)
FROM users
JOIN comp ON users.id = comp.usr_id
WHERE users.verified = 'True'
GROUP BY users.id, comp.spec
ORDER BY users.id, comp.spec;

/*средняя оценка рецензий проверенного пользователя*/

SELECT users.username, AVG(review.review_rate)
FROM users
JOIN review ON review.usr_id = users.id
WHERE users.verified = 'True'
GROUP BY users.username;

