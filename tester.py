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
        totalCs += temp
    return totalCs / gameCount


my_region = getRegion()
name = getSummoner()
me = lol_watcher.summoner.by_name(my_region, name)

my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
my_id = me['accountId']
my_matches = lol_watcher.match.matchlist_by_account(my_region, me['accountId'])


csd20 = csPerMinLast10(my_region, my_matches, 20, name)
#csd20 = csPerMinLast20(1)
print(csd20)
