import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # self.pack()
        
        self.info = {}

        self.create_labels()
        self.create_widgets()

    def create_labels(self):
        tk.Label(self.master, text="Character Name:").grid(row=0)
        tk.Label(self.master, text="Player Name:").grid(row=1)
        tk.Label(self.master, text="Class:").grid(row=2)
        tk.Label(self.master, text="Race:").grid(row=3)
        tk.Label(self.master, text="Starting Level:").grid(row=4)
        tk.Label(self.master, text="Character Alignment:").grid(row=5)
        tk.Label(self.master, text="Strength:").grid(row=6)
        

    def create_widgets(self):
        # InputValidation Command

        # valid percent substitutions (from the Tk entry man page)
        # note: you only have to register the ones you need; this
        # example registers them all for illustrative purposes
        #
        # %d = Type of action (1=insert, 0=delete, -1 for others)
        # %i = index of char string to be inserted/deleted, or -1
        # %P = value of the entry if the edit is allowed
        # %s = value of entry prior to editing
        # %S = the text string being inserted or deleted, if any
        # %v = the type of validation that is currently set
        # %V = the type of validation that triggered the callback
        #      (key, focusin, focusout, forced)
        # %W = the tk name of the widget
        vcmd = (self.register(self.check_stat),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

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

        self.strength_entry = tk.Entry(self.master, validate="focusout", validatecommand=vcmd)


        submit_button = tk.Button(self.master, text="Submit", command=self.submit_info)
        quit_button = tk.Button(self.master, text="Quit", command=self.master.destroy)

        # Places the widgets
        self.character_name_entry.grid(row=0, column=1)
        self.player_name_entry.grid(row=1, column=1)
        class_drop_down.grid(row=2, column=1)
        race_drop_down.grid(row=3, column=1)
        self.starting_level_entry.grid(row=4, column=1)
        alignment_drop_down.grid(row=5, column=1)
        self.strength_entry.grid(row=6, column=1)

        submit_button.grid(row=8, column=0)
        quit_button.grid(row=8, column=1)

      
                
        

    def submit_info(self):
        self.info['Character name'] = self.character_name_entry.get()
        self.info['Player name'] = self.player_name_entry.get()
        self.info['Class'] = self.class_display.get()
        self.info['Race'] = self.race_display.get()
        self.info['Character Level'] = self.starting_level_entry.get()
        self.info['Character Alignment'] = self.alignment_display.get()

        print(self.info)

    def check_stat(self, d, i, P, s, S, v, V, W):
        if int(s) >= 1 and int(s) <= 20:
            return True
        else:
            return False
        


