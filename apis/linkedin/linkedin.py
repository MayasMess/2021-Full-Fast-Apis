import requests


class Linkedin:
    def __init__(self):
        self.linkedin_url = 'https://www.linkedin.com/in'

    def retrieve_linkedin_user_info(self, slug: str) -> dict:
        response = requests.get(f"{self.linkedin_url}/{slug}")
        return {'url': self.linkedin_url}
