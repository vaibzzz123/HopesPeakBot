class Character:
    def __init__(self, name, status, character_type):
        self.name = name
        self.status = status
        self.character_type = character_type

    def get_first_name(self):
        first_name = self.name.split()[0]
        return first_name.lower()

    def get_status(self):
        return self.status
    
    def get_character_type(self):
        return self.character_type
