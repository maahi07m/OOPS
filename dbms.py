Q1 = """
	SELECT COUNT(*) FROM Movie 
	WHERE year BETWEEN 1981 AND 1999;
	"""
Q2 = """
	SELECT AVG(rank) FROM Movie
	WHERE year = 1991;
	"""
Q3 = """
	SELECT MIN(rank) FROM Movie
	WHERE year = 1991;
	"""
Q4 = "SELECT fname,lname FROM Cast inner join Actor on id=pid where mid=27;"

Q5 = "SELECT COUNT(*) FROM Cast inner join Actor on id=pid WHERE fname = 'Jon' and lname = 'Dough';"

Q6 = "SELECT name FROM Movie where (year between 2003 and 2006) and name like 'Young Latin Girls%';"

Q7 = "SELECT fname, lname FROM moviedirector inner join director on did = director.id inner join movie on movie.id = mid where name like 'Star Trek%'"
