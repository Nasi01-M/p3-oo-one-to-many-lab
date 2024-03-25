class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []

    def pets(self):
        """Returns a list of the owner's pets."""
        return self.pets_list

    def add_pet(self, pet):
        """Validates and adds a pet to the owner's list of pets."""
        if isinstance(pet, Pet):
            self.pets_list.append(pet)
            pet.owner = self
        else:
            raise Exception("Only instances of Pet class can be added as pets.")

    def get_sorted_pets(self):
        """Returns a sorted list of the owner's pets by their names."""
        return sorted(self.pets_list, key=lambda x: x.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.add_to_all()

    @classmethod
    def add_to_all(cls):
        """Stores all instances of Pet."""
        cls.all.append(cls)

