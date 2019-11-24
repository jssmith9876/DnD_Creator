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

        self.prof_bonus = 2
        self.set_prof_bonus()

        self.stat_mods = {}
        self.set_stat_mods()

        self.prof_save_throws = {}
        self.set_save_throw_prof()

        self.saving_throws = self.stat_mods.copy()
        self.set_save_throws()

        

        


    def show(self):
        #print the stuff gathered from the info
        for key in self.info:
            if key != 'Stats':
                print(key, end=": ")
                print(self.info[key])
            else:
                # Print the stats and modifiers
                print('\nStats/Modifiers: ')
                for s in self.stats:
                    print(s, end=": ")
                    print(self.stats[s], end="  ")
                    print(self.stat_mods[s])


        #print the proficiency bonus
        print("\nProficiency Bonus: " + str(self.prof_bonus))

        #print the saving throws their prof with
        print("\nSaving Throws:")
        for save_throw in self.saving_throws:
            print(str(save_throw), end=": ")
            print(self.saving_throws[save_throw])


    
    def alter_stats(self):
        # Check races
        if self.race_ == 'Dragonborn':
            self.stats['Strength'] += 2
            self.stats['Charisma'] += 1
        elif self.race_ == 'Dwarf':
            self.stats['Constitution'] += 2
        elif self.race_ == 'Elf':
            self.stats['Dexterity'] += 2
        elif self.race_ == 'Gnome':
            self.stats['Intelligence'] += 2
        elif self.race_ == 'Half-Elf':
            self.stats['Charisma'] += 2
            # +1 to two other ability scores
        elif self.race_ == 'Halfling':
            self.stats['Dexterity'] += 2
        elif self.race_ == 'Half-Orc':
            self.stats['Strength'] += 2
            self.stats['Constitution'] += 1
        elif self.race_ == 'Human':
            for stat in self.stats:
                self.stats[stat] += 1
        elif self.race_ == 'Tiefling':
            self.stats['Charisma'] += 2
            self.stats['Intelligence'] += 1

    def set_prof_bonus(self):
        self.prof_bonus = ((int(self.character_level) - 1) // 4) + 2

    def set_stat_mods(self):
        for stat in self.stats:
            if self.stats[stat] == 1:
                self.stat_mods[stat] = -5
            elif self.stats[stat] == 2 or self.stats[stat] == 3:
                self.stat_mods[stat] = -4
            elif self.stats[stat] == 4 or self.stats[stat] == 5:
                self.stat_mods[stat] = -3
            elif self.stats[stat] == 6 or self.stats[stat] == 7:
                self.stat_mods[stat] = -2
            elif self.stats[stat] == 8 or self.stats[stat] == 9:
                self.stat_mods[stat] = -1
            elif self.stats[stat] == 10 or self.stats[stat] == 11:
                self.stat_mods[stat] = 0
            elif self.stats[stat] == 12 or self.stats[stat] == 13:
                self.stat_mods[stat] = 1
            elif self.stats[stat] == 14 or self.stats[stat] == 15:
                self.stat_mods[stat] = 2
            elif self.stats[stat] == 16 or self.stats[stat] == 17:
                self.stat_mods[stat] = 3
            elif self.stats[stat] == 18 or self.stats[stat] == 19:
                self.stat_mods[stat] = 4
            elif self.stats[stat] >= 20:
                self.stat_mods[stat] = 5
            
    def set_save_throw_prof(self):
        for stat in self.stats:
            self.prof_save_throws[stat] = False
        

        # Check classes
        if self.class_ == 'Barbarian' or self.class_ == 'Fighter':
            self.prof_save_throws['Strength'] = True
            self.prof_save_throws['Constitution'] = True
        elif self.class_ == 'Bard':
            self.prof_save_throws['Dexterity'] = True
            self.prof_save_throws['Charisma'] = True
        elif self.class_ == 'Cleric' or self.class_ == 'Paladin' or self.class_ == 'Warlock':
            self.prof_save_throws['Wisdom'] = True
            self.prof_save_throws['Charisma'] = True
        elif self.class_ == 'Druid' or self.class_ == 'Wizard':
            self.prof_save_throws['Intelligence'] = True
            self.prof_save_throws['Wisdom'] = True
        elif self.class_ == 'Monk' or self.class_ == 'Ranger':
            self.prof_save_throws['Stength'] = True
            self.prof_save_throws['Dexterity'] = True
        elif self.class_ == 'Rogue':
            self.prof_save_throws['Dexterity'] = True
            self.prof_save_throws['Intelligence'] = True
        elif self.class_ == 'Sorcerer':
            self.prof_save_throws['Constitution'] = True
            self.prof_save_throws['Charisma'] = True

    def set_save_throws(self):
        for stat in self.saving_throws:
            if self.prof_save_throws[stat]:
                self.saving_throws[stat] += self.prof_bonus
        



        
        