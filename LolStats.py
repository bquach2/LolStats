from riotwatcher import LolWatcher, ApiError

lol_watcher = LolWatcher('RGAPI-9fe74b90-c36e-45d0-98c8-96513b02d593')

my_region = 'NA1'
user = input("Enter UserName")
me = lol_watcher.summoner.by_name(my_region, user)

my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
my_id = me['accountId']
# print(my_ranked_stats)
myMatches = lol_watcher.match.matchlist_by_account(my_region, my_id)
wr = my_ranked_stats[0]['wins']
# print(wr)

my_matches = lol_watcher.match.matchlist_by_account(my_region, me['accountId'])

# fetch last match detail
last_match = my_matches['matches'][0]
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
# print(allSummoners)
myIndex = allSummoners['skadongle']
# print(myIndex)
# print(match_detail['participants'][myIndex]) HAS ALL INFO INCLUDING CSDIFF. CREEPSPERMINDELTAS

name = match_detail['participants'][myIndex]['stats']
myKills = match_detail['participants'][myIndex]['stats']['kills']
cs = match_detail['participants'][myIndex]['stats']['totalMinionsKilled']
csDiff = match_detail['participants'][myIndex]['timeline']['creepsPerMinDeltas']['0-10']
myAssists = match_detail['participants'][myIndex]['stats']['assists']
thisDamage = match_detail['participants'][myIndex]['stats']['totalDamageDealtToChampions']
# print(name)
# print(myKills)
# print(myAssists)
# print(csDiff)
print(thisDamage)

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

thisTeamDamage = thisDamage1 + thisDamage2 + \
    thisDamage3 + thisDamage4 + thisDamage5
thisDamageRatio = round((float(thisDamage) / float(thisTeamDamage)) * 100, 2)

print(thisDamageRatio)

csd = 10


def csPerMinLast20(numGames):
    totalCs = 0
    for x in range(numGames):
        last_match = my_matches['matches'][x]
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
        myIndex = allSummoners['skadongle']
        temp = match_detail['participants'][myIndex]['stats']['totalMinionsKilled']
        totalCs += temp
    return totalCs / numGames


cs20 = csPerMinLast20(1)
print(cs20)
