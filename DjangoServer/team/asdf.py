import pandas as pd
from riotwatcher import LolWatcher

class Name(object):
    def __init__(self):
        global api_key, watcher, my_region
        api_key = "RGAPI-32cda5e3-20d8-4836-a56c-02bbb0fc8f63"
        watcher = LolWatcher(api_key)
        my_region = "kr"

    def summoner(self, nickname):
        user = watcher.summoner.by_name(my_region, nickname)
        puuid = user['puuid']
        to_db = pd.DataFrame({
            'nickname': [nickname],
            'puuid' : [puuid]
        })

        json =to_db.to_json(orient = 'records', force_ascii=False)
        print(json)
        to_react ={
            'nickname': nickname,
            'puuid' : puuid
        }
        print(to_react)
        # print(to_react)

        return to_react

    def match_id(self, puuid):
        return watcher.match.matchlist_by_puuid(my_region, puuid, type='ranked')

    def play_list(self, matchid, puuid):
        matches = watcher.match.by_id(my_region, matchid)
        metadata = matches['metadata']['participants']
        user_num = [i for i in range(0,10)  if metadata[i] == puuid]

        user_info = matches['info']["participants"][user_num[0]]

        champion_name = user_info['championName']
        win = '승리' if str(user_info['win']) == 'True' else '패배'
        kills = user_info['kills']
        deaths = user_info['deaths']
        assists = user_info['assists']
        kda = 'perfect' if deaths == 0 else round((kills + assists) / deaths, 2)
        position = user_info['teamPosition']
        summoner_name = user_info['summonerName']


        print(f'챔피언 이름 :{champion_name} \n'
              f'승리 패배 : {win}\n'
              f'킬 : {kills}\n'
              f'데스 : {deaths}\n'
              f'어시스트 : {assists}\n'
              f'kda : {kda}\n'
              f'라인 : {position}\n'
              f'닉네임 : {summoner_name}\n')
        to_db = pd.DataFrame({'champion': champion_name, 'win': win, 'kills': kills,
          'deaths': deaths, 'assists': assists, 'kda' : kda, 'position':position, 'summoner_name': summoner_name},index = [0])
        print(to_db)
        json = to_db.to_json(orient='records', force_ascii=False)
        print(json)

        to_react = [{'champion': champion_name, 'win': win, 'kills': kills,
          'deaths': deaths, 'assists': assists, 'kda' : kda, 'position':position, 'summoner_name': summoner_name}]
        print(to_react)

        return to_react

    def all_death_time(self, matchid):
        time_line = watcher.match.timeline_by_match(my_region, matchid)
        death_list = list()
        for i in range(len(time_line['info']['frames'])):
            for j in range(len(time_line['info']['frames'][i]['events'])):
                if time_line['info']['frames'][i]['events'][j]['type']  == 'CHAMPION_KILL':
                   timestamp = time_line['info']['frames'][i]['events'][j]['timestamp']
                   death_list.append(timestamp)
        print(death_list)

    def user_death_time(self, matchid, puuid):
        time_line = watcher.match.timeline_by_match(my_region, matchid)
        death_list = list()
        puuid_list = time_line['metadata']['participants']
        in_game_id = [i for i in range(len(puuid_list)) if puuid_list[i] == puuid]

        for i in range(len(time_line['info']['frames'])):
            for j in range(len(time_line['info']['frames'][i]['events'])):
                if time_line['info']['frames'][i]['events'][j]['type']  == 'CHAMPION_KILL' \
                        and time_line['info']['frames'][i]['events'][j]['victimId'] == in_game_id[0]:
                       timestamp = time_line['info']['frames'][i]['events'][j]['timestamp']
                       death_list.append(timestamp)
        print(death_list)



if __name__ == '__main__':
    name = Name().summoner('hideonbush')
    puuid = name['puuid']
    match_id = Name().match_id(name['puuid'])
    Name().play_list(match_id[2], puuid)
    Name().all_death_time(match_id[0])
    Name().user_death_time(match_id[0], puuid)