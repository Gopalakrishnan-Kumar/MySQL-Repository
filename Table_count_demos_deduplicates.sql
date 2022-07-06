DROP TABLE IF EXISTS count_demos;
CREATE TABLE count_demos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    val INT
    );

INSERT INTO count_demos(val) 
VALUES (-1),(1),(1),(3),(NULL),(3),(4),(6),(NULL),(8),(9),(10);

SELECT val FROM count_demos;

SELECT DISTINCT val FROM count_demos;

SELECT val FROM count_demos
WHERE sqrt(val) > 2;

