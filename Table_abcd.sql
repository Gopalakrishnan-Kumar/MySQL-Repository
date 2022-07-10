SELECT * FROM test.abcd;
SELECT id,val FROM count_demos;

SELECT id,val FROM count_demos
WHERE sqrt(val) > 2;

SELECT id,val FROM count_demos
WHERE abs(val) < 2;


SELECT id,val FROM count_demos
WHERE abs(val) < 1;