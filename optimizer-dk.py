from pydfs_lineup_optimizer import get_optimizer, Site, Sport

optimizer = get_optimizer(Site.DRAFTKINGS, Sport.BASKETBALL)
optimizer.load_players_from_csv("projections.csv")
optimizer.settings.max_from_one_team = 3
pool = optimizer.player_pool
lineups = optimizer.optimize(n=1, max_exposure=0.99)
for lineup in lineups:
    print(lineup)