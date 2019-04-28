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
    
    def get_character_path(self):
        return "./assets/characters/formatted sprites/" + self.get_first_name() + "/" + self.get_status() + ".png"

dr1_test = [
    (
        Character("Leon Kuwata", "dead", "killer"),
        Character("Sayaka Maizono", "dead", "victim"),
    ),
    (
        Character("Mukuro Ikusaba", "dead", "victim"),
    ),
    (
        Character("Mondo Oowada", "dead", "killer"),
        Character("Chihiro Fujisaki", "dead", "victim"),
    ),
    (
        Character("Celestia Ludenburg", "dead", "killer"),
        Character("Hifumi Yamada", "dead", "victim"),
        Character("Kiyotaka Ishimaru", "dead", "victim"),
    ),
    (
        Character("Sakura Oogami", "dead", "victim"),
    ),
    (
        Character("Junko Enoshima", "dead", "victim"),
    ),
    (
        Character("Makoto Naegi", "alive", "spotless"),
    ),
    (
        Character("Kyoko Kirigiri", "alive", "spotless"),
    ),
    (
        Character("Toko Fukawa", "alive", "spotless"),
    ),
    (
        Character("Byakuya Togami", "alive", "spotless"),
    ),
    (
        Character("Asahina Aoi", "alive", "spotless"),
    ),
    (
        Character("Yasuhiro Hagakure", "alive", "spotless"),
    )
]