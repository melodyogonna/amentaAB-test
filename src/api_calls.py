import requests
from decouple import config


api_url = 'https://api.fortnox.se/3/'

class FortNoxRequestHandler():
    """Handles requests and responses to FortNox API"""
    def __init__(self):
        self.headers = {
                'Access-Token': config("ACCESS_TOKEN"),
                'Client-Secret': config("FORTNOX_CLIENT_SECRET")
            }

    def get_all_articles(self):
        '''Return all articles'''
        r = requests.get(f'{api_url}articles', headers=self.headers)
        return r.json()

    def update_article(self, article):
        '''Update and article'''
        r = requests.put(f'{api_url}article/{article.ArticleNumber}',
                data={"Article":article}, headers=self.headers)
        return r.json()

    def create_article(self, article):
        '''Create a new article'''
        r = requests.post(f'{api_url}article/', data={"Article":article},
                headers=self.headers)
        return r.json()

    def get_customers(self, pages=None):
        '''Get a list of customers'''
        r = requests.get(f'{api_url}customers/', headers=self.headers)
        return r.json()

        
