CREATE OR REPLACE FUNCTION film_select() RETURNS VOID as $$

    UPDATE film_series
    SET
    rating = (
        SELECT CAST((SUM(rate)+ 0.0)/COUNT(rate) AS numeric(3,1))
        FROM review
        WHERE film_id = film_series.id
        GROUP BY film_id
    )
$$ LANGUAGE SQL;


