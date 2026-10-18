"""Downloads pitch data from Statcast and saves it as CSV files in backend/data/."""
from pybaseball import  playerid_lookup
from pybaseball import  statcast_pitcher

def Player_stats_to_CSV(first_name: str,last_name: str,start_date: str,end_date: str):
    player_id = playerid_lookup(last_name,first_name)["key_mlbam"].iloc[0]
    player_stats = statcast_pitcher(start_date,end_date, player_id)
    player_stats.to_csv(f"Backend/data/{first_name+'_'+last_name}.csv")

Player_stats_to_CSV("jacob","degrom","2018-03-29","2018-11-28") #righty starter
Player_stats_to_CSV("corey","kluber","2018-03-29","2018-11-28")#righty starter 
Player_stats_to_CSV("justin","verlander","2018-03-29","2018-11-28")#righty starter 
Player_stats_to_CSV("gerrit","cole","2018-03-29","2018-11-28")#righty starter 
Player_stats_to_CSV("aaron","nola","2018-03-29","2018-11-28") #righty starter
Player_stats_to_CSV("trevor","bauer","2018-03-29","2018-11-28") # righty starter
Player_stats_to_CSV("blake","snell","2018-03-29","2018-11-28") #lefty starter 
Player_stats_to_CSV("kyle","freeland","2018-03-29","2018-11-28") #lefty starter 
Player_stats_to_CSV("patrick","corbin","2018-03-29","2018-11-28")#lefty starter
Player_stats_to_CSV("josh","hader","2018-03-29","2018-11-28") #lefty closer

