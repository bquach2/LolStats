msg = "hello world"
print(msg)

me = watcher.summoner.by_name(str(riotApiRegion), summonerName)
my_matches = watcher.match.matchlist_by_account(
    str(riotApiRegion), me['accountId'])
last_match = my_matches['matches'][0]
match_detail = watcher.match.by_id(
    str(riotApiRegion), last_match['gameId'])
latest = watcher.data_dragon.versions_for_region(str(riotApiRegion))[
                                                 'n']['champion']
static_champ_list = watcher.data_dragon.champions(latest, False, 'de_DE')

  # champion id to champion name translation
  champ_dict = {}
for key in static_champ_list['data']:
        row = static_champ_list['data'][key]
        champ_dict[row['key']] = row['id']

    # finding out the id of the wanted summoner
    dic = {
        (match_detail['participantIdentities'][0]['player']['summonerName']).lower().replace(" ", ""): 0,
        (match_detail['participantIdentities'][1]['player']['summonerName']).lower().replace(" ", ""): 1,
        (match_detail['participantIdentities'][2]['player']['summonerName']).lower().replace(" ", ""): 2,
        (match_detail['participantIdentities'][3]['player']['summonerName']).lower().replace(" ", ""): 3,
        (match_detail['participantIdentities'][4]['player']['summonerName']).lower().replace(" ", ""): 4,
        (match_detail['participantIdentities'][5]['player']['summonerName']).lower().replace(" ", ""): 5,
        (match_detail['participantIdentities'][6]['player']['summonerName']).lower().replace(" ", ""): 6,
        (match_detail['participantIdentities'][7]['player']['summonerName']).lower().replace(" ", ""): 7,
        (match_detail['participantIdentities'][8]['player']['summonerName']).lower().replace(" ", ""): 8,
        (match_detail['participantIdentities'][9]['player']['summonerName']).lower().replace(" ", ""): 9
    }

    # stats
    thisId = dic[summonerName.lower().replace(" ", "")]
    thisQId = match_detail['queueId']
    thisQ = ' '
    thisChamp = match_detail['participants'][thisId]['championId']
    thisChampName = champ_dict[str(thisChamp)]
    thisKills = match_detail['participants'][thisId]['stats']['kills']
    print(thisKills)
    thisDeaths = match_detail['participants'][thisId]['stats']['deaths']
    thisAssists = match_detail['participants'][thisId]['stats']['assists']
    thisWinId = match_detail['participants'][thisId]['stats']['win']
    thisWin = ' '
    thisTime = round((int(match_detail['gameDuration']) / 60), 2)
    thisMultiKill = match_detail['participants'][thisId]['stats']['largestMultiKill']
    thisDamage = match_detail['participants'][thisId]['stats']['totalDamageDealtToChampions']
    thisVision = match_detail['participants'][thisId]['stats']['visionScore']
    thisMinion = match_detail['participants'][thisId]['stats']['totalMinionsKilled']
    thisPink = match_detail['participants'][thisId]['stats']['visionWardsBoughtInGame']
    thisGold = int(match_detail['participants'][thisId]['stats']['goldEarned'])
    thisMinionPerMin = round((thisMinion / thisTime), 2)
    thisVisionPerMin = round((thisVision / thisTime), 2)
    thisGoldPerMinute = round((thisGold / thisTime), 2)
    thisStats = watcher.league.by_summoner(str(riotApiRegion), me['id'])
    thisWinrateStat = ' '
    thisWinrate = ' '
    thisRank = ' '
    thisLP = ' '

    if thisQId == 420:
        thisQ = "RANKED"
    elif thisQId == 400:
        thisQ = "NORMAL"
    else:
        thisQ = "OTHER"

    if str(thisWinId) == 'True':
        thisWin = "won"
    else:
        thisWin = "lost"

    if thisId > 4:
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
    thisDamageRatio = round(
        (float(thisDamage) / float(thisTeamDamage)) * 100, 2)

    try:
        thisWinrate = int(
            thisStats[0]['wins']) / (int(thisStats[0]['wins']) + int(thisStats[0]['losses']))
        thisWinrateStat = str(int(thisWinrate * 100))
        thisRank = str(thisStats[0]['rank'])
        thisTier = str(thisStats[0]['tier'])
        thisLP = str(thisStats[0]['leaguePoints'])
    except IndexError:
        print("no ranked stats available for " + str(summonerName))
