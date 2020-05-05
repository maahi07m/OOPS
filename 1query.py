Q1 = "SELECT COUNT(*) FROM Movie WHERE year BETWEEN 1981 AND 1999;"

Q2 = "SELECT AVG(rank) FROM Movie WHERE year = 1991;"
	
Q3 = "SELECT MIN(rank) FROM Movie WHERE year = 1991;"

Q4 = "SELECT fname,lname FROM Cast inner join Actor on id=pid where mid=27;"

Q5 = "SELECT COUNT(*) FROM Cast inner join Actor on id=pid WHERE fname = 'Jon' and lname = 'Dough';"

Q6 = "SELECT name FROM Movie where (year between 2003 and 2006) and name like 'Young Latin Girls%';"

Q7 = "SELECT fname, lname FROM moviedirector inner join director on did = director.id inner join movie on movie.id = mid where name like 'Star Trek%'"

Q8 = "SELECT name from cast join actor on actor.id=pid join movie on movie.id = mid inner join director WHERE (actor.fname = 'Jackie (I)' and director.fname = 'Jackie (I)') and (actor.lname = 'Chan' and director.lname = 'Chan') order by name ASC;"

Q9 = "SELECT fname,lname FROM Director INNER JOIN MovieDIRECTOR ON `Director`.`id`=did INNER JOIN Movie ON `Movie`.`id`=mid WHERE year = 2001 GROUP BY did HAVING COUNT(mid)>=4 ORDER BY fname ASC,lname DESC;"

Q10 = "SELECT gender,COUNT(gender) FROM Actor where gender = 'F' UNION SELECT gender,COUNT(gender) FROM Actor where gender = 'M';"

Q11 = ""

Q12 = ""

Q13 = ""
