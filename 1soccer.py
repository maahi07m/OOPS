Q1 = "select avg(age) from player;"

Q2 = "select match_no , play_date from match where audience > 50000;"

Q3 = """ select team_id,count(win_lose) as num_of_wons from            
    	MatchTeamDetails where win_lose = 'W' 
    	group by team_id order by num_of_wons desc,team_id asc;"""

Q4 = """ select m.match_no,m.play_date
		 from match m where m.stop1_sec>(select avg(ma.stop1_sec) from match ma)	
		 order by m.match_no desc,m.play_date desc;"""

Q5 = """select match_no,team.name,player.name from matchcaptain 
	inner join team on MatchCaptain.team_id = team.team_id 
	inner join player on captain = player_id
	order by match_no,team.name; """

Q6 = """ select match_no,name,jersey_no 
	from match 
	inner join player on player_of_match = player_id 
	order by match_no;"""

Q7 = """ select team.name,avg(player.age) as average_age 
		from player inner join team on player.team_id = team.team_id	
		group by team.name having avg(player.age)>26 order by team.name;"""

Q8 = """ select p.name,p.jersey_no,p.age,mtd.goal_score from goaldetails gd inner join match m on m.match_no = gd.match_no inner join player p on p.player_id = gd.player_id inner join matchteamdetails mtd on mtd.match_no = m.match_no inner join team t on t.team_id = gd.team_id group by p.name having p.age<=27 and mtd.goal_score!=0  order by p.name ,mtd.goal_score desc;"""

Q10 = "select avg(mtd.goal_score) as total_number_of_goals_scored from goaldetails gd inner join match m on m.match_no = gd.match_no inner join player p on p.player_id = gd.player_id inner join matchteamdetails mtd on mtd.match_no = m.match_no inner join team t on t.team_id = gd.team_id group by t.team_id;"
