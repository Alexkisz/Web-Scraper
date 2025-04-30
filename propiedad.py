from filtros import Filtros

class Propiedad(Filtros):
    def __init__(self):
        super().__init__()

    def get_value(self, key):
      
        if self.subsection is not None:
            return self.subsection.get(key)
        else:
            print("Error: No hay subsección cargada.")
            return None

    def get_amenities(self):

        if self.subsection is not None:
            return list(self.subsection.keys())
        else:
            print("Error: No hay subsección cargada.")
            return []