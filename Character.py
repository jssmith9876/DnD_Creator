class Character:
    def __init__(self, info):
        self.info = info
        self.character_name = info['Character name']
        self.player_name = info['Player name']
        self.character_level = info['Character level']
        self.class_ = info['Class']
        self.race_ = info['Race']
        self.character_alignment = info['Character Alignment']
        self.background = info['Background']

        self.stats = {}
        for key in info['Stats']:
            self.stats[key] = int(info['Stats'][key])

        
        self.alter_stats()

        


    def show(self):
        for key in self.info:
            if key != 'Stats':
                print(key, end=": ")
                print(self.info[key])
            else:
                print('Stats: ', end="")
                print(self.stats)
    
    def alter_stats(self):
        # Check races
        if self.race_ == 'Dragonborn':
            self.stats['Strength'] += 2
            self.stats['Charisma'] += 1
        elif self.race_ == 'Dwarf':
            self.stats['Constitution'] += 2

        # Check Backgrounds
        
        