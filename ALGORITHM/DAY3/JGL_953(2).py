players = input().split()
fouls = {}

for player in players:
    if player in fouls:
        fouls[player] += 1
    else:
        fouls[player] = 1
    
min_foul = min(fouls.values())

for player, foul in fouls.items():
    if foul == min_foul:
        print(player)

print(min_foul)