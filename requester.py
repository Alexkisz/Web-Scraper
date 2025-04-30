import requests

class Requester():
    def __init__(self):
        self.__requests_tries = 3
        self.timeout = 15
        self.__init_session()
        self.last_response = None

    def __init_session(self):

        self.session = requests.Session()

    def get_requests(self, url, headers, proxy=None):

        self.last_response == None

        for _ in range(self.__requests_tries):
            try:
                response = self.session.get(
                    url,
                    headers=headers,
                    proxies=proxy,
                    timeout=self.timeout
                )
                if response.status_code == 200: ## Tener en cuenta que no siempre puede ser 200 para futuros srappers
                    self.last_response = response  
            except requests.exceptions.RequestException as e:
                print(e)
            except requests.exceptions.Timeout as e:
                print(e)

        if self.last_response == None:
            print(f"No se obtuvo respuesta para: {url}")

       
