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
# print(thisDamage)

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

# print(thisDamageRatio)

csd = 10


#cs20 = csPerMinLast10(1)
# print(cs20)
