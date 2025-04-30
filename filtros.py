import json
from requester import Requester

class Filtros(Requester):
    def __init__(self):
        super().__init__()
        self._json = None
        self.subsection = None

    def get_json(self):
        self._json = None
        if self.last_response:
            try:
                self._json = self.last_response.json()
            except json.JSONDecodeError:
                print("Error: La respuesta no es un JSON válido.")
        else:
            print("Error: response es None")

    def get_subsection(self, keyWord, bracket):
        self.subsection = None
        if self._json is not None:
            # Si bracket no se especifica, asumimos un solo nivel de acceso
                self.subsection = self._json.get(keyWord, bracket)

        else:
            print("Error: No se ha cargado el JSON aún.")
