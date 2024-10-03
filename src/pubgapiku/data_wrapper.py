"""Wrap response data into other data types which are easy to handle"""
import pandas as pd
from pubgapiku.api_connector import Connector

class DataWrapper():
    """Data wrapper class"""
    def __init__(self, api_key:str, timeout:int=1):
        self.conn = Connector(api_key, timeout)

    def get_sample_matches(self) -> list|None:
        """
        Get a list of random sample match

        [Return]
        list |-> Successfully extracted matchid list
        None |-> Fail signal
        """

        data:dict|None = self.conn.sample_matches()
        if isinstance(data, dict):
            match_list:list = [
                item['id'] for item in
                data['data']['relationships']['matches']['data']
            ]
            return match_list
        else:
            return None

    def get_players_in_match(self, match_id:str) -> pd.DataFrame|None:
        """
        Get a dataframe containing player names and account ids of a matchß

        [Return]
        pd.DataFrame |-> Successfully extracted player info
        None         |-> Fail signal
        """

        data:dict|None = self.conn.match(match_id)
        if isinstance(data, dict):
            player_list:list = [
                {'accountId': item['attributes']['stats']['playerId'],
                 'playerName': item['attributes']['stats']['name']}
                for item in data['included']
                if item['type'] == 'participant'
            ]
            return pd.DataFrame(player_list)
        else:
            return None

    def get_player_data(self, **kargs):
        """
        Get a dataframe containing matches and corresponding players to each match

        [Keyword arguments]
        ids:list[str]   |-> filters by player IDs
        names:list[str] |-> filters by player names

        [Return]
        pd.DataFrame |-> Successfully extracted player-match relations
        None         |-> Fail signal
        """

        data:dict|None = self.conn.players(**kargs)
        if isinstance(data, dict):
            player_datas = []
            for player in data['data']:
                player_id = player['id']
                player_name = player['attributes']['name']
                player_bantype = player['attributes']['banType']

                for match in player['relationships']['matches']['data']:
                    if match['type'] == 'match':
                        match_info = {
                            'accountId': player_id,
                            'playerName': player_name,
                            'banType': player_bantype,
                            'matchId': match['id']
                        }
                        player_datas.append(match_info)
            return pd.DataFrame(player_datas)
        else:
            return None
        
    def __parse_match(self, match_data:dict) -> tuple[dict, pd.DataFrame]:
        '''
        Parse a metadata and participants data from a match data

        [Arguments]
        match_data:dict |-> A match data in dictionary type

        [Return]
        tuple[dict, pd.DataFrame] |-> Extracted metadata in dictionary type, and a DataFrame of participants data
        '''
        meta_data = {
            'id': match_data['data']['id'],
            'created': match_data['data']['attributes']['createdAt'],
            'mode': match_data['data']['attributes']['gameMode'],
            'map': match_data['data']['attributes']['mapName'],
            'duration': match_data['data']['attributes']['duration']
        }
        participants = []
        rosters = {}
        for included in match_data['included']:
            if included['type'] == 'participant':
                stats = list(included['attributes']['stats'].keys())
                player_data = {
                    key: included['attributes']['stats'][key] for key in stats
                }
                player_data['id'] = included['id']
                player_data['teamId'] = ''
                player_data['teamRank'] = 0
                participants.append(player_data)
            elif included['type'] == 'roster':
                rosters[included['id']] = {
                    'rank': included['attributes']['stats']['rank'],
                    'participants': [
                        player['id'] for player
                        in included['relationships']['participants']['data']
                    ]
                }
        participants = pd.DataFrame(participants)
        for rid, rdata in rosters:
            pfilter = participants['id'].isin(rdata['participants'])
            participants.loc[pfilter, 'teamId'] = rid
            participants.loc[pfilter, 'teamRank'] = rdata['rank']
        return meta_data, participants

    def __parse_telemetry(self, telemetry_data:list) -> pd.DataFrame:
        

    def get_match_data(self, match_id:str) -> tuple[dict, dict]|None:
        """
        Get a tuple of dataframe containing a match's metadata and the address of telemetry file

        [Argument]
        match_id:str |-> target match's id

        [Return]
        tuple[dict, dict] |-> Successfully acquired match and telemetry data
        None              |-> Fail signal
        """

        match_data:dict|None = self.conn.match(match_id)
        if isinstance(match_data, dict):
            telemetry_addr:str|None = self.conn.telemetry_addr(match_data)
            if not isinstance(telemetry_addr, str):
                return None
            
            telemetry_data:dict|None = self.conn.get_telemetry(telemetry_addr)
            if not isinstance(telemetry_data, dict):
                return None
            
            meta_data, participants = self.__parse_match(match_data)
            return , telemetry_data
        else:
            return None
