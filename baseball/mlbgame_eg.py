#include "stdio.h"
from __future__ import print_function
import mlbgame

month = mlbgame.games(2020,10, home='Dodgers')
games = mlbgame.combine_games(month)
for game in games:
  print(game)
  
day = mlbgame.day(2015, 4, 12, home='Royals', away='Royals')
game = day[0]
output = 'Winning pitcher: %s (%s) - Losing Pitcher: %s (%s)'
print(output % (game.w_pitcher, game.w_team, game.l_pitcher, game.l_team))

game = mlbgame.day(2015, 11, 1, home='Mets')[0]
stats = mlbgame.player_stats(game.game_id)
for player in stats.home_batting:
    print(player)
