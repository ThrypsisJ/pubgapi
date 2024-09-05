"""KRAFTON API Wrapper"""
import time
import requests
import json

class Connector:
    """API Wrapper class"""
    def __init__(self):
        self.api_base = "https://api.pubg.com/shards/steam/"

        with open('./apikey', 'r', encoding='utf-8') as f:
            api_key = f.readline()
            self.header = {
                'Authorization': f'Bearer {api_key}',
                'Accept': 'application/vnd.api+json'
            }

    def sample_matches(self) -> dict:
        """Get sample match list"""
        api = self.api_base + '/samples'
        response:dict = requests.get(api, headers=self.header, timeout=5).json()
        return response
