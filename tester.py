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
    assists = 0
    deaths = 0
    wins = 0
    losses = 0
    damageRatioChamps = 0
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
        damageRatioChamps += damageRatio(myIndex, match_detail)
        temp = match_detail['participants'][myIndex]['stats']['totalMinionsKilled']
        # print(match_detail['participants'][myIndex]['stats'])
        totalCs += temp
    damageRatioChamps /= gameCount
    print(damageRatioChamps)
    return totalCs / gameCount


my_region = getRegion()
name = getSummoner()
me = lol_watcher.summoner.by_name(my_region, name)

my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
my_id = me['accountId']
my_matches = lol_watcher.match.matchlist_by_account(my_region, me['accountId'])


#csd20 = csPerMinLast10(my_region, my_matches, 1, name)
csd20 = statsLastX(my_region, my_matches, 20, name)
print(csd20)
