import pandas as pd
df = pd.read_csv('10yearAUSOpenMatches.csv')
from collections import defaultdict

year = [i for i in range(2004, 2015)]
rounds = [i for i in df["round"].unique()]

## all players
players = set()
for player in df['player1'].unique():
    players.add(player)
for player in df['player2'].unique():
    players.add(player)

## generate data by year
data = defaultdict(list)
for i in year:
    test_df = df[df["year"] == i]
    if len(test_df.index) > 0:
        for player in players:
            player_df =  test_df[(test_df['player1'] == player) | (test_df['player2'] == player)]
            if len(player_df.index) > 0:
                for r in rounds:
                    round_df = player_df[player_df['round'] == r]
                    if len(round_df.index) > 0:
                        ## check win and create object
                        win_df = round_df[round_df['winner'] == player]
                        if len(win_df.index) > 0:
                            win_obj = {}
                            win_obj["year"] = i
                            win_obj["player"] = player
                            win_obj["round"] = r
                            win_obj["result"] = "win"
                            win_obj["interactions"] = len(win_df.index)
                            win_obj["key"] = player
                            win_obj["ace"] = win_df["ace1"].mean()
                            win_obj["double"] = win_df["double1"].mean()
                            win_obj["fastServe"] = win_df["fastServe1"].mean()
                            win_obj["avgFirstServe"] = win_df["avgFirstServe1"].mean()
                            win_obj["avgSecServe"] = win_df["double1"].mean()
                            win_obj["error"] = win_df["error1"].mean()
                            win_obj["positiveInteractions"] = len(win_df.index)
                            data["year"].append(win_obj)
                        ## check lose and create object
                        lose_df = round_df[round_df['winner'] != player]
                        if len(lose_df.index) > 0:
                            lose_obj = {}
                            lose_obj["year"] = i
                            lose_obj["player"] = player
                            lose_obj["round"] = r
                            lose_obj["result"] = "lose"
                            lose_obj["interactions"] = -len(lose_df.index)
                            lose_obj["key"] = player
                            lose_obj["ace"] = lose_df["ace2"].mean()
                            lose_obj["double"] = lose_df["double2"].mean()
                            lose_obj["fastServe"] = lose_df["fastServe2"].mean()
                            lose_obj["avgFirstServe"] = lose_df["avgFirstServe2"].mean()
                            lose_obj["avgSecServe"] = lose_df["double2"].mean()
                            lose_obj["error"] = lose_df["error2"].mean()
                            lose_obj["positiveInteractions"] = len(lose_df.index)
                            data["year"].append(lose_obj)

import json
with open('new_data.txt', 'w') as file:
     file.write(json.dumps(data))
