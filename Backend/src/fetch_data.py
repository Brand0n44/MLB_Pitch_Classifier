"""Downloads pitch data from Statcast and saves it as CSV files in backend/data/."""
from pybaseball import  playerid_lookup
from pybaseball import  statcast_pitcher

def Player_stats_to_CSV(first_name: str,last_name: str,start_date: str,end_date: str):
    player_id = playerid_lookup(last_name,first_name)["key_mlbam"].iloc[0]
    player_stats = statcast_pitcher(start_date,end_date, player_id)
    player_stats.to_csv(f"Backend/data/{last_name}.csv")

Player_stats_to_CSV("clayton","kershaw","2015-04-05","2015-11-01")
Player_stats_to_CSV("gerrit","cole","2015-04-05","2015-11-01")
Player_stats_to_CSV("max","scherzer","2015-04-05","2015-11-01")
Player_stats_to_CSV("zack","greinke","2015-04-05","2015-11-01")
Player_stats_to_CSV("madison","bumgarner","2015-04-05","2015-11-01")
Player_stats_to_CSV("chris","sale","2015-04-05","2015-11-01")
Player_stats_to_CSV("sonny","gray","2015-04-05","2015-11-01")
Player_stats_to_CSV("david","price","2015-04-05","2015-11-01")
Player_stats_to_CSV("corey","kluber","2015-04-05","2015-11-01")
Player_stats_to_CSV("jacob","degrom","2015-04-05","2015-11-01")
