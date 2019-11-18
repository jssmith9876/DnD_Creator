class Character:
    def __init__(self, character_name, player_name, level 
                character_alignment, character_race):
        self.character_name = character_name
        self.player_name = player_name
        self.character_alignment = character_alignment
        self.level = level
    

        # self.character_class = character_class
        # self.character_race = character_race

    def show(self):
        print("Character: " + str(self.character_name))
        print("Class: ")
        print("Level: " + str(self.level))
        print("Playe: " + str(self.player_name))
        print("Race: ")
        print("Alignment: " + str(self.character_alignment))