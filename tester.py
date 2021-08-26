from riotwatcher import LolWatcher, ApiError

lol_watcher = LolWatcher('RGAPI-aa6dd901-77cf-47b7-8d6e-2bab46744030')


def getSummoner():
    names = input("Enter Summoner Name: ")
    return names


def getRegion():
    region = input("Enter Region: ")
    return region


def getGameCount():
    getInput = input("How many games would you like to analyze? ")
    while(getInput.isdigit() == False):
        getInput = input("Please enter a positive number ")
    return getInput


def getIndex(my_region1, my_matches1, gameCount, userName):
    last_match = my_matches1['matches'][gameCount]
    match_detail = lol_watcher.match.by_id(my_region1, last_match['gameId'])
    allSummoners = {
        (match_detail['participantIdentities'][0]['player']['summonerName']).lower().replace(" ", ""): 0,
        (match_detail['participantIdentities'][1]['player']['summonerName']).lower().replace(" ", ""): 1,
        (match_detail['participantIdentities'][2]['player']['summonerName']).lower().replace(" ", ""): 2,
        (match_detail['participantIdentities'][3]['player']['summonerName']).lower().replace(" ", ""): 3,
        (match_detail['participantIdentities'][4]['player']['summonerName']).lower().replace(" ", ""): 4,
        (match_detail['participantIdentities'][5]['player']['summonerName']).lower().replace(" ", ""): 5,
        (match_detail['participantIdentities'][6]['player']['summonerName']).lower().replace(" ", ""): 6,
        (match_detail['participantIdentities'][7]['player']['summonerName']).lower().replace(" ", ""): 7,
        (match_detail['participantIdentities'][8]['player']['summonerName']).lower().replace(" ", ""): 8,
        (match_detail['participantIdentities'][9]['player']['summonerName']).lower().replace(" ", ""): 9,
    }
    myIndex = allSummoners[userName]
    print(myIndex)
    return myIndex


def csPerMinLast10(my_region1, my_matches1, gameCount, userName):
    totalCs = 0
    for x in range(gameCount):
        last_match = my_matches1['matches'][x]
        match_detail = lol_watcher.match.by_id(my_region, last_match['gameId'])
        allSummoners = {
            (match_detail['participantIdentities'][0]['player']['summonerName']).lower().replace(" ", ""): 0,
            (match_detail['participantIdentities'][1]['player']['summonerName']).lower().replace(" ", ""): 1,
            (match_detail['participantIdentities'][2]['player']['summonerName']).lower().replace(" ", ""): 2,
            (match_detail['participantIdentities'][3]['player']['summonerName']).lower().replace(" ", ""): 3,
            (match_detail['participantIdentities'][4]['player']['summonerName']).lower().replace(" ", ""): 4,
            (match_detail['participantIdentities'][5]['player']['summonerName']).lower().replace(" ", ""): 5,
            (match_detail['participantIdentities'][6]['player']['summonerName']).lower().replace(" ", ""): 6,
            (match_detail['participantIdentities'][7]['player']['summonerName']).lower().replace(" ", ""): 7,
            (match_detail['participantIdentities'][8]['player']['summonerName']).lower().replace(" ", ""): 8,
            (match_detail['participantIdentities'][9]['player']['summonerName']).lower().replace(" ", ""): 9,
        }
        myIndex = allSummoners[userName]
        temp = match_detail['participants'][myIndex]['stats']['totalMinionsKilled']
        print(match_detail['participants'][myIndex]['stats'])
        totalCs += temp
    return totalCs / gameCount


def damageRatio(myIndex, match_detail):
    thisDamage = match_detail['participants'][myIndex]['stats']['totalDamageDealtToChampions']
    if myIndex > 4:
        thisDamage1 = match_detail['participants'][5]['stats']['totalDamageDealtToChampions']
        thisDamage2 = match_detail['participants'][6]['stats']['totalDamageDealtToChampions']
        thisDamage3 = match_detail['participants'][7]['stats']['totalDamageDealtToChampions']
        thisDamage4 = match_detail['participants'][8]['stats']['totalDamageDealtToChampions']
        thisDamage5 = match_detail['participants'][9]['stats']['totalDamageDealtToChampions']
    else:
        thisDamage1 = match_detail['participants'][0]['stats']['totalDamageDealtToChampions']
        thisDamage2 = match_detail['participants'][1]['stats']['totalDamageDealtToChampions']
        thisDamage3 = match_detail['participants'][2]['stats']['totalDamageDealtToChampions']
        thisDamage4 = match_detail['participants'][3]['stats']['totalDamageDealtToChampions']
        thisDamage5 = match_detail['participants'][4]['stats']['totalDamageDealtToChampions']
        thisDamage = match_detail['participants'][myIndex]['stats']['totalDamageDealtToChampions']
    thisTeamDamage = thisDamage1 + thisDamage2 + \
        thisDamage3 + thisDamage4 + thisDamage5
    thisDamageRatio = round(
        (float(thisDamage) / float(thisTeamDamage)) * 100, 2)
    return thisDamageRatio


def statsLastX(my_region1, my_matches1, gameCount, userName):
    totalCs = 0
    kills = 0
    deaths = 0
    assists = 0
    wins = 0  # win
    losses = 0  # gameCount - wins
    damageRatioChamps = 0
    controlWards = 0  # visionWardsBoughtInGame
    visionScore = 0  # visionScore
    gameDuration = 0
    for x in range(gameCount):
        last_match = my_matches1['matches'][x]
        match_detail = lol_watcher.match.by_id(my_region, last_match['gameId'])
        allSummoners = {
            (match_detail['participantIdentities'][0]['player']['summonerName']).lower().replace(" ", ""): 0,
            (match_detail['participantIdentities'][1]['player']['summonerName']).lower().replace(" ", ""): 1,
            (match_detail['participantIdentities'][2]['player']['summonerName']).lower().replace(" ", ""): 2,
            (match_detail['participantIdentities'][3]['player']['summonerName']).lower().replace(" ", ""): 3,
            (match_detail['participantIdentities'][4]['player']['summonerName']).lower().replace(" ", ""): 4,
            (match_detail['participantIdentities'][5]['player']['summonerName']).lower().replace(" ", ""): 5,
            (match_detail['participantIdentities'][6]['player']['summonerName']).lower().replace(" ", ""): 6,
            (match_detail['participantIdentities'][7]['player']['summonerName']).lower().replace(" ", ""): 7,
            (match_detail['participantIdentities'][8]['player']['summonerName']).lower().replace(" ", ""): 8,
            (match_detail['participantIdentities'][9]['player']['summonerName']).lower().replace(" ", ""): 9,
        }
        myIndex = allSummoners[userName]

        temp = match_detail['participants'][myIndex]['stats']['neutralMinionsKilled']
        totalCs += temp
        totalCs += match_detail['participants'][myIndex]['stats']['totalMinionsKilled']
        kills += match_detail['participants'][myIndex]['stats']['kills']
        deaths += match_detail['participants'][myIndex]['stats']['deaths']
        assists += match_detail['participants'][myIndex]['stats']['assists']
        if match_detail['participants'][myIndex]['stats']['win']:
            wins += 1
        else:
            losses += 1
        controlWards += match_detail['participants'][myIndex]['stats']['visionWardsBoughtInGame']
        visionScore += match_detail['participants'][myIndex]['stats']['visionScore']
        damageRatioChamps += damageRatio(myIndex, match_detail)
        gameDuration += int(match_detail['gameDuration'])/60

    totalCs /= gameCount
    kills /= gameCount
    assists /= gameCount
    deaths /= gameCount
    wins /= gameCount
    losses /= gameCount
    damageRatioChamps /= gameCount
    controlWards /= gameCount
    visionScore /= gameCount
    gameDuration /= gameCount
    stats = {
        ('damageRatioChampsX'): round(damageRatioChamps, 3),
        ('totalCsX'): round(totalCs, 3),
        ('killsX'): round(kills, 3),
        ('assistsX'): round(assists, 3),
        ('deathsX'): round(deaths, 3),
        ('winsX'): round(wins, 3),
        ('lossesX'): round(losses, 3),
        ('controlWardsX'): round(controlWards, 3),
        ('visionScoreX'): round(visionScore, 3),
        ('gameDurationX'): round(gameDuration, 3)
    }
    return stats


def printInfo(stats):
    print("Average stats for", name, "per game for the last", getInput, "games:")
    print("damage ratio: ", round(stats['damageRatioChampsX'], 3), "%", sep="")
    print("Minions Killed:", stats['totalCsX'])
    print("Kills:", stats['killsX'])
    print("Deaths:", stats['deathsX'])
    print("Assists:", stats['assistsX'])
    print("Wins:", stats['winsX'])
    print("Losses:", stats['lossesX'])
    print("Control Wards bought:", stats['controlWardsX'])
    print("Vision Score:", stats['visionScoreX'])
    print("Game Duration:", stats['gameDurationX'])


name = getSummoner()
my_region = getRegion()

me = lol_watcher.summoner.by_name(my_region, name)
my_matches = lol_watcher.match.matchlist_by_account(my_region, me['accountId'])

getInput = getGameCount()
gameStats = statsLastX(my_region, my_matches, int(getInput), name)
printInfo(gameStats)
# while(getInput != "quit"):

newInput = input("What would you like to do next?\n 'Compare' to compare to another summoner,\n 'Stats' to view stats for a different number of games, \n 'Quit' to quit the program ")
while(newInput.lower() != "quit"):
    if newInput.lower() == "stats":
        gameCount = getGameCount()
        newStats = statsLastX(my_region, my_matches, int(gameCount), name)
        printInfo(newStats)
        newInput = input(
            "What would you like to do next?\n 'Compare' to compare to another summoner,\n 'Stats' to view stats for a different number of games, \n 'Quit' to quit the program ")
    elif newInput.lower() == "compare":
        gameCountComp = getGameCount()
        newName = getSummoner()
        region = getRegion()
        comp = lol_watcher.summoner.by_name(region, newName)
        comp_matches = lol_watcher.match.matchlist_by_account(
            region, comp['accountId'])
        compStats = statsLastX(region, comp_matches,
                               int(gameCountComp), newName)
        printInfo(compStats)
        newInput = input(
            "What would you like to do next?\n 'Compare' to compare to another summoner,\n 'Stats' to view stats for a different number of games, \n 'Quit' to quit the program ")
print("Thank you for using LoLStats. Hope you enjoyed your stay")
