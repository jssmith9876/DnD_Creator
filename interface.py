import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # self.pack()
        
        self.info = {}
        self.stats = {}

        self.create_labels()
        self.create_widgets()

    def create_labels(self):
        tk.Label(self.master, text="Character Name:").grid(row=0)
        tk.Label(self.master, text="Player Name:").grid(row=1)
        tk.Label(self.master, text="Class:").grid(row=2)
        tk.Label(self.master, text="Race:").grid(row=3)
        tk.Label(self.master, text="Starting Level:").grid(row=4)
        tk.Label(self.master, text="Character Alignment:").grid(row=5)

        tk.Label(self.master, text="Strength:").grid(row=0, column=3)
        tk.Label(self.master, text="Dexterity:").grid(row=1, column=3)
        tk.Label(self.master, text="Constitution:").grid(row=2, column=3)
        tk.Label(self.master, text="Intelligence:").grid(row=3, column=3)
        tk.Label(self.master, text="Wisdom:").grid(row=4, column=3)
        tk.Label(self.master, text="Charisma:").grid(row=5, column=3)
        

    def create_widgets(self):
        # InputValidation Command

        validation = self.register(self.check_stat)

        # Creates the widgets
        self.character_name_entry = tk.Entry(self.master)
        self.player_name_entry = tk.Entry(self.master)

        class_choices = ['Baribarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 
                         'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
        self.class_display = tk.StringVar(self.master)
        self.class_display.set("Please Select")
        class_drop_down = tk.OptionMenu(self.master, self.class_display, *class_choices)

        race_choices = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Halfling',
                        'Half-Orc', 'Human', 'Tiefling']
        self.race_display = tk.StringVar(self.master)
        self.race_display.set("Please Select")
        race_drop_down = tk.OptionMenu(self.master, self.race_display, *race_choices)

        self.starting_level_entry = tk.Entry(self.master)
        
        alignment_choices = ['Lawful Evil', 'Lawful Neutral', 'Lawful Good',
                             'Neutral Evil', 'True Neutral', 'Neutral Good',
                             'Chaotic Evil', 'Chaotic Neutral', 'Chaotic Good']
        self.alignment_display = tk.StringVar(self.master)
        self.alignment_display.set("Please Select")
        alignment_drop_down = tk.OptionMenu(self.master, self.alignment_display, *alignment_choices)

        self.strength_entry = tk.Entry(self.master, validate="key", validatecommand=(validation, '%S'), width=5)
        self.dexterity_entry = tk.Entry(self.master, validate="key", validatecommand=(validation, '%S'), width=5)
        self.constitution_entry = tk.Entry(self.master, validate="key", validatecommand=(validation, '%S'), width=5)
        self.intelligence_entry = tk.Entry(self.master, validate="key", validatecommand=(validation, '%S'), width=5)
        self.wisdom_entry = tk.Entry(self.master, validate="key", validatecommand=(validation, '%S'), width=5)
        self.charisma_entry = tk.Entry(self.master, validate="key", validatecommand=(validation, '%S'), width=5)


        submit_button = tk.Button(self.master, text="Submit", command=self.submit_info)
        quit_button = tk.Button(self.master, text="Quit", command=self.master.destroy)

        # Places the widgets
        self.character_name_entry.grid(row=0, column=1)
        self.player_name_entry.grid(row=1, column=1)
        class_drop_down.grid(row=2, column=1)
        race_drop_down.grid(row=3, column=1)
        self.starting_level_entry.grid(row=4, column=1)
        alignment_drop_down.grid(row=5, column=1)

        self.strength_entry.grid(row=0, column=4)
        self.dexterity_entry.grid(row=1, column=4)
        self.constitution_entry.grid(row=2, column=4)
        self.intelligence_entry.grid(row=3, column=4)
        self.wisdom_entry.grid(row=4, column=4)
        self.charisma_entry.grid(row=5, column=4)

        submit_button.grid(row=8, column=0)
        quit_button.grid(row=8, column=1)

      
                
        

    def submit_info(self):
        self.info['Character name'] = self.character_name_entry.get()
        self.info['Player name'] = self.player_name_entry.get()
        self.info['Class'] = self.class_display.get()
        self.info['Race'] = self.race_display.get()
        self.info['Character Level'] = self.starting_level_entry.get()
        self.info['Character Alignment'] = self.alignment_display.get()

        self.stats['Strength'] = self.strength_entry.get()
        self.stats['Dexterity'] = self.dexterity_entry.get()
        self.stats['Consitution'] = self.constitution_entry.get()
        self.stats['Intelligence'] = self.intelligence_entry.get()
        self.stats['Wisdom'] = self.wisdom_entry.get()
        self.stats['Charisma'] = self.charisma_entry.get()

        self.info['Stats'] = self.stats

        print(self.info)

    def check_stat(self, num):
        return num.isdigit()
        


