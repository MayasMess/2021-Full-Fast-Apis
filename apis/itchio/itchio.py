import requests
from bs4 import BeautifulSoup


class Itchio:
    def __init__(self):
        self.base_url = 'https://itch.io'

    @staticmethod
    def find_obj_or_none(obj):
        try:
            return obj.getText()
        except Exception:
            return None

    def retrieve_new_game_uploads(self, page_num: int) -> list:
        results = []
        response = requests.get(f"{self.base_url}/games/newest?page={page_num}&format=json").json()
        soup = BeautifulSoup(response['content'], features="html.parser")
        for game in soup.contents:
            game_id = game.get('data-game_id')
            game_link = game.find('a').get('href')
            game_title = self.find_obj_or_none(game.find("div", {"class": "game_title"}))
            game_text = self.find_obj_or_none(game.find("div", {"class": "game_text"}))
            game_author = self.find_obj_or_none(game.find("div", {"class": "game_author"}))
            game_genre = self.find_obj_or_none(game.find("div", {"class": "game_genre"}))

            results.append(
                {
                    'game_id':       game_id,
                    'game_link':     game_link,
                    'game_title':    game_title,
                    'game_text':     game_text,
                    'game_author':   game_author,
                    'game_genre':    game_genre,
                }
            )
        return results
