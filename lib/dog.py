APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:
    def __init__(self, name='Fido', breed='Mastiff'):
        self.name = name
        self.breed = breed

    # def get_name(self):
    #     return self._name
    @property
    def name(self):
        """The name Property"""
        return self._name
    
    @name.setter
    def name(self,name):
        """Validation (type and length)"""
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            raise ValueError("Name must be string between 1 and 25 characters." )

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            raise ValueError("Breed must be in list of approved breeds.")

