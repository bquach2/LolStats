from riotwatcher import LolWatcher, ApiError

lol_watcher = LolWatcher('RGAPI-9fe74b90-c36e-45d0-98c8-96513b02d593')


def getSummoner():
    names = input("Enter Summoner Name: ")
    return names


def getRegion():
    region = input("Enter Region: ")
    return region


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
        totalCs += temp
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

    totalCs /= gameCount
    kills /= gameCount
    assists /= gameCount
    deaths /= gameCount
    wins /= gameCount
    losses /= gameCount
    damageRatioChamps /= gameCount
    controlWards /= gameCount
    visionScore /= gameCount
    stats = {
        ('damageRatioChampsX'): damageRatioChamps,
        ('totalCsX'): totalCs,
        ('killsX'): kills,
        ('assistsX'): assists,
        ('deathsX'): deaths,
        ('winsX'): wins,
        ('lossesX'): losses,
        ('controlWardsX'): controlWards,
        ('visionScoreX'): visionScore
    }
    return stats


name = getSummoner()
my_region = getRegion()

me = lol_watcher.summoner.by_name(my_region, name)

my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
my_id = me['accountId']
my_matches = lol_watcher.match.matchlist_by_account(my_region, me['accountId'])


#csd20 = csPerMinLast10(my_region, my_matches, 1, name)
getInput = input("How many games would you like to analyze?")
while(getInput.isdigit() == False):
    getInput = input("Please enter a number")
csd20 = statsLastX(my_region, my_matches, int(getInput), name)
# while(getInput != "quit"):
print("Average stats per game for the last", getInput, "games:")
print("damage ratio:", round(csd20['damageRatioChampsX'], 3), "%")
print("Minions Killed:", csd20['totalCsX'])
print("Kills:", csd20['killsX'])
print("Deaths:", csd20['deathsX'])
print("Assists:", csd20['assistsX'])
print("Wins:", csd20['winsX'])
print("Losses:", csd20['lossesX'])
print("Control Wards bought:", csd20['controlWardsX'])
print("Vision Score:", csd20['visionScoreX'])
