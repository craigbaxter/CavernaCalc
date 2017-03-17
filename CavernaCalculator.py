""""
A small app for easily calculating your score at the end of playing the tabletop board game "Caverna".
Written by Craig Baxter, 2017

RULES FOR SCORING
    1pt per dwarf
    1pt per farm animal and dog
    -2pt per missing type of farm animal
    1/2pt per grain (rounded up)
    1pt per vegetable
    1pt per ruby
    -1pt per unused space
    + points from purchased furnishing tiles, pastures & mines
    + points from parlors, storage and chamber tiles
    1 per gold
    -3 per begging marker

TO DO/POSSIBLE FUTURE ADDITIONS
    Save/Load from file
    Better looking UI
"""

import tkinter as tk  # Python GUI
import math


class CavernaCalc(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent

        # Call validate function on key press event in input fields
        vcmd = (self.register(self.validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        # Variables for each of the input values
        self.count_dwarfs = tk.StringVar()
        self.count_weapons = tk.StringVar()
        self.count_gold = tk.StringVar()
        self.count_begging = tk.StringVar()
        self.count_unused = tk.StringVar()
        self.count_dogs = tk.StringVar()
        self.count_sheep = tk.StringVar()
        self.count_donkeys = tk.StringVar()
        self.count_cows = tk.StringVar()
        self.count_boars = tk.StringVar()
        self.count_grain = tk.StringVar()
        self.count_veg = tk.StringVar()
        self.count_wood = tk.StringVar()
        self.count_stone = tk.StringVar()
        self.count_ore = tk.StringVar()
        self.count_ruby = tk.StringVar()
        self.count_rooms = tk.StringVar()
        self.count_fields = tk.StringVar()
        self.count_mines = tk.StringVar()
        self.count_yellow = tk.StringVar()
        self.store_main = tk.IntVar()
        self.store_weapon = tk.IntVar()
        self.store_supplies = tk.IntVar()
        self.store_ore = tk.IntVar()
        self.store_stone = tk.IntVar()
        self.chamber_food = tk.IntVar()
        self.chamber_broom = tk.IntVar()
        self.chamber_writing = tk.IntVar()
        self.chamber_treasure = tk.IntVar()
        self.chamber_prayer = tk.IntVar()
        self.chamber_fodder = tk.IntVar()
        self.parlor_weaving = tk.IntVar()
        self.parlor_milking = tk.IntVar()
        self.parlor_state = tk.IntVar()
        self.count_state = tk.StringVar()

        # Create the UI
        self.grid()
        self.resizable(False, False)  # Prevent user from resizing the window

        self.rowcount = 0
        self.colcount = 0
        self.maxcols = 6  # How many columns per row (should be even and >= 6)
        input_width = 5  # Width of number input fields

        # Player board section
        heading_player = tk.Label(self, text="PLAYER BOARD", fg="white", bg="grey")
        heading_player.grid(column=0, row=self.rowcount, columnspan=self.maxcols, sticky='EW')
        self.newRow()
        
        label_dwarf = tk.Label(self, text="Dwarfs:", anchor="w")
        label_dwarf.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_dwarf = tk.Entry(self, textvariable=self.count_dwarfs, width=input_width,
                               validate='key', validatecommand=vcmd)
        input_dwarf.grid(column=self.colcount, row=self.rowcount)
        self.count_dwarfs.set(u"2")
        self.newColumn()

        label_weapons = tk.Label(self, text=" with weapons:", anchor="w")
        label_weapons.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_weapons = tk.Entry(self, textvariable=self.count_weapons, width=input_width,
                                 validate='key', validatecommand=vcmd)
        input_weapons.grid(column=self.colcount, row=self.rowcount)
        self.count_weapons.set(u"0")
        self.newColumn()

        label_gold = tk.Label(self, text="Gold:", anchor="w")
        label_gold.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_gold = tk.Entry(self, textvariable=self.count_gold, width=input_width,
                              validate='key', validatecommand=vcmd)
        input_gold.grid(column=self.colcount, row=self.rowcount)
        self.count_gold.set(u"0")
        self.newColumn()

        label_beg = tk.Label(self, text="Begging:", anchor="w")
        label_beg.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_beg = tk.Entry(self, textvariable=self.count_begging, width=input_width,
                             validate='key', validatecommand=vcmd)
        input_beg.grid(column=self.colcount, row=self.rowcount)
        self.count_begging.set(u"0")
        self.newColumn()

        label_unused = tk.Label(self, text="Unused Spaces:", anchor="w")
        label_unused.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_unused = tk.Entry(self, textvariable=self.count_unused, width=input_width,
                                validate='key', validatecommand=vcmd)
        input_unused.grid(column=self.colcount, row=self.rowcount)
        self.count_unused.set(u"0")
        self.newColumn()

        # Dogs and Farm Animals section
        if self.colcount > 0:
            self.newRow()
        heading_animals = tk.Label(self, text="ANIMALS", fg="white",bg="grey")
        heading_animals.grid(column=self.colcount, row=self.rowcount, columnspan=self.maxcols, sticky='EW')
        self.newRow()

        label_dog = tk.Label(self, text="Dogs:", anchor="w")
        label_dog.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_dogs = tk.Entry(self, textvariable=self.count_dogs, width=input_width,
                              validate='key', validatecommand=vcmd)
        input_dogs.grid(column=self.colcount, row=self.rowcount)
        self.count_dogs.set(u"0")
        self.newColumn()

        label_sheep = tk.Label(self, text="Sheep:", anchor="w")
        label_sheep.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_sheep = tk.Entry(self, textvariable=self.count_sheep, width=input_width,
                               validate='key', validatecommand=vcmd)
        input_sheep.grid(column=self.colcount, row=self.rowcount)
        self.count_sheep.set(u"0")
        self.newColumn()

        label_donkey = tk.Label(self, text="Donkeys:", anchor="w")
        label_donkey.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_donkeys = tk.Entry(self, textvariable=self.count_donkeys, width=input_width,
                                 validate='key', validatecommand=vcmd)
        input_donkeys.grid(column=self.colcount, row=self.rowcount)
        self.count_donkeys.set(u"0")
        self.newColumn()

        label_boars = tk.Label(self, text="Wild Boars:", anchor="w")
        label_boars.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_boars = tk.Entry(self, textvariable=self.count_boars, width=input_width,
                               validate='key', validatecommand=vcmd)
        input_boars.grid(column=self.colcount, row=self.rowcount)
        self.count_boars.set(u"0")
        self.newColumn()

        label_cows = tk.Label(self, text="Cattle:", anchor="w")
        label_cows.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_cows = tk.Entry(self, textvariable=self.count_cows, width=input_width,
                              validate='key', validatecommand=vcmd)
        input_cows.grid(column=self.colcount, row=self.rowcount)
        self.count_cows.set(u"0")
        self.newColumn()

        # Resources section
        if self.colcount > 0:
            self.newRow()
        heading_resources = tk.Label(self, text="RESOURCES", fg="white", bg="grey")
        heading_resources.grid(column=self.colcount, row=self.rowcount, columnspan=self.maxcols, sticky='EW')
        self.newRow()

        label_grain = tk.Label(self, text="Grain:", anchor="w")
        label_grain.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_grain = tk.Entry(self, textvariable=self.count_grain, width=input_width,
                               validate='key', validatecommand=vcmd)
        input_grain.grid(column=self.colcount, row=self.rowcount)
        self.count_grain.set(u"0")
        self.newColumn()

        label_veg = tk.Label(self, text="Vegetables:", anchor="w")
        label_veg.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_veg = tk.Entry(self, textvariable=self.count_veg, width=input_width,
                               validate='key', validatecommand=vcmd)
        input_veg.grid(column=self.colcount, row=self.rowcount)
        self.count_veg.set(u"0")
        self.newColumn()

        label_wood = tk.Label(self, text="Wood:", anchor="w")
        label_wood.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_wood = tk.Entry(self, textvariable=self.count_wood, width=input_width,
                               validate='key', validatecommand=vcmd)
        input_wood.grid(column=self.colcount, row=self.rowcount)
        self.count_wood.set(u"0")
        self.newColumn()

        label_stone = tk.Label(self, text="Stone:", anchor="w")
        label_stone.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_stone = tk.Entry(self, textvariable=self.count_stone, width=input_width,
                             validate='key', validatecommand=vcmd)
        input_stone.grid(column=self.colcount, row=self.rowcount)
        self.count_stone.set(u"0")
        self.newColumn()

        label_ore = tk.Label(self, text="Ore:", anchor="w")
        label_ore.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_ore = tk.Entry(self, textvariable=self.count_ore, width=input_width,
                             validate='key', validatecommand=vcmd)
        input_ore.grid(column=self.colcount, row=self.rowcount)
        self.count_ore.set(u"0")
        self.newColumn()

        label_ruby = tk.Label(self, text="Rubies:", anchor="w")
        label_ruby.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_ruby = tk.Entry(self, textvariable=self.count_ruby, width=input_width,
                             validate='key', validatecommand=vcmd)
        input_ruby.grid(column=self.colcount, row=self.rowcount)
        self.count_ruby.set(u"0")
        self.newColumn()

        # Constructed tiles section
        if self.colcount > 0:
            self.newRow()
        heading_tiles = tk.Label(self, text="CONSTRUCTED TILES", fg="white", bg="grey")
        heading_tiles.grid(column=self.colcount, row=self.rowcount, columnspan=self.maxcols, sticky='EW')
        self.newRow()

        subhead_tiles = tk.Label(self, text="Enter total points earned from each:", anchor="w")
        subhead_tiles.grid(column=self.colcount, row=self.rowcount, columnspan=(self.maxcols - 1), sticky='EW')
        self.newRow()

        label_rooms = tk.Label(self, text="Furnishing tiles:", anchor="w")
        label_rooms.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_rooms = tk.Entry(self, textvariable=self.count_rooms, width=input_width,
                              validate='key', validatecommand=vcmd)
        input_rooms.grid(column=self.colcount, row=self.rowcount)
        self.count_rooms.set(u"0")
        self.newColumn()

        label_fields = tk.Label(self, text="Pastures:", anchor="w")
        label_fields.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_fields = tk.Entry(self, textvariable=self.count_fields, width=input_width,
                               validate='key', validatecommand=vcmd)
        input_fields.grid(column=self.colcount, row=self.rowcount)
        self.count_fields.set(u"0")
        self.newColumn()

        label_mines = tk.Label(self, text="Mines:", anchor="w")
        label_mines.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_mines = tk.Entry(self, textvariable=self.count_mines, width=input_width,
                               validate='key', validatecommand=vcmd)
        input_mines.grid(column=self.colcount, row=self.rowcount)
        self.count_mines.set(u"0")
        self.newRow()

        # Storage
        input_mainstore = tk.Checkbutton(self, text="Main Storage", variable=self.store_main)
        input_mainstore.grid(column=self.colcount, row=self.rowcount, columnspan=2, sticky="W")
        self.newColumn()
        self.newColumn()

        input_weaponstore = tk.Checkbutton(self, text="Weapon Storage", variable=self.store_weapon)
        input_weaponstore.grid(column=self.colcount, row=self.rowcount, columnspan=2, sticky="W")
        self.newColumn()
        self.newColumn()

        input_suppliesstore = tk.Checkbutton(self, text="Supplies Storage", variable=self.store_supplies)
        input_suppliesstore.grid(column=self.colcount, row=self.rowcount, columnspan=2, sticky="W")
        self.newColumn()
        self.newColumn()

        input_orestore = tk.Checkbutton(self, text="Ore Storage", variable=self.store_ore)
        input_orestore.grid(column=self.colcount, row=self.rowcount, columnspan=2, sticky="W")
        self.newColumn()
        self.newColumn()

        input_stonestore = tk.Checkbutton(self, text="Stone Storage", variable=self.store_stone)
        input_stonestore.grid(column=self.colcount, row=self.rowcount, columnspan=2, sticky="W")
        self.newRow()

        input_foodchamber = tk.Checkbutton(self, text="Food Chamber", variable=self.chamber_food)
        input_foodchamber.grid(column=self.colcount, row=self.rowcount, columnspan=2, sticky="W")
        self.newColumn()
        self.newColumn()

        input_broomchamber = tk.Checkbutton(self, text="Broom Chamber", variable=self.chamber_broom)
        input_broomchamber.grid(column=self.colcount, row=self.rowcount, columnspan=2, sticky="W")
        self.newColumn()
        self.newColumn()

        input_writingchamber = tk.Checkbutton(self, text="Writing Chamber", variable=self.chamber_writing)
        input_writingchamber.grid(column=self.colcount, row=self.rowcount, columnspan=2, sticky="W")
        self.newColumn()
        self.newColumn()

        input_treasurechamber = tk.Checkbutton(self, text="Treasure Chamber", variable=self.chamber_treasure)
        input_treasurechamber.grid(column=self.colcount, row=self.rowcount, columnspan=2, sticky="W")
        self.newColumn()
        self.newColumn()

        input_prayerchamber = tk.Checkbutton(self, text="Prayer Chamber", variable=self.chamber_prayer)
        input_prayerchamber.grid(column=self.colcount, row=self.rowcount, columnspan=2, sticky="W")
        self.newColumn()
        self.newColumn()

        input_fodderchamber = tk.Checkbutton(self, text="Fodder Chamber", variable=self.chamber_fodder)
        input_fodderchamber.grid(column=self.colcount, row=self.rowcount, columnspan=2, sticky="W")
        self.newRow()

        input_weavingparlor = tk.Checkbutton(self, text="Weaving Parlor", variable=self.parlor_weaving)
        input_weavingparlor.grid(column=self.colcount, row=self.rowcount, columnspan=2, sticky="W")
        self.newColumn()
        self.newColumn()

        input_milkingparlor = tk.Checkbutton(self, text="Milking Parlor", variable=self.parlor_milking)
        input_milkingparlor.grid(column=self.colcount, row=self.rowcount, columnspan=2, sticky="W")
        self.newRow()

        input_stateparlor = tk.Checkbutton(self, text="State Parlor", variable=self.parlor_state)
        input_stateparlor.grid(column=self.colcount, row=self.rowcount, columnspan=2, sticky="W")
        self.newColumn()
        self.newColumn()
        label_state = tk.Label(self, text="Dwellings adjacent to State Parlor:", anchor="w")
        label_state.grid(column=self.colcount, row=self.rowcount, columnspan=2, sticky='W')
        self.newColumn()
        self.newColumn()
        input_state = tk.Entry(self, textvariable=self.count_state, width=input_width,
                               validate='key', validatecommand=vcmd)
        input_state.grid(column=self.colcount, row=self.rowcount)
        self.count_state.set(u"0")
        self.newRow()

        # Score display section
        if self.colcount > 0:
            self.newRow()
        heading_score = tk.Label(self, text="SCORE", fg="white", bg="grey")
        heading_score.grid(column=self.colcount, row=self.rowcount, columnspan=self.maxcols, sticky='EW')
        self.newRow()

        self.scorevalue = tk.StringVar()
        scorelabel = tk.Label(self, text="Score: ", anchor="w")
        scorelabel.grid(column=0, row=self.rowcount, sticky='EW')
        score = tk.Label(self, textvariable=self.scorevalue, anchor="w")
        if input_width < 10:
            span = self.maxcols - 3
        else:
            span = self.maxcols - 2
        score.grid(column=1, row=self.rowcount, sticky='EW', columnspan=span)

        # Update button
        if input_width < 10:
            span = 2
            col = self.maxcols - 2
        else:
            span = 1
            col = self.maxcols - 1
        button = tk.Button(self, text=u"Update", command=self.CalcScore, width=10)
        button.grid(column=col, row=self.rowcount, sticky='E', columnspan=span)

    # Validation for input fields to only allow numbers
    def validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        # action 1 = user is inserting a character
        if (action == '1'):
            if text in '0123456789':
                try:
                    float(value_if_allowed)
                    return True
                except ValueError:
                    return False
            else:
                return False
        else:
            return True

    # Dynamic positioning
    def newColumn(self):
        self.colcount += 1
        if self.colcount >= self.maxcols:
            self.newRow()
            
    def newRow(self):
        self.rowcount += 1
        self.colcount = 0

    # Calculate the score (update button clicked)
    def CalcScore(self):
        negative_points = 0

        # 1 pt per dwarf and dog
        dwarfs = int(self.count_dwarfs.get() or 0)
        score = dwarfs + int(self.count_dogs.get() or 0)

        # 1 pt per gold, -3 per begging marker
        score += int(self.count_gold.get() or 0)
        beg = int(self.count_begging.get() or 0) * 3
        score -= beg

        # 1 pt per farm animal (-2 if you don't have any)
        score_sheep = int(self.count_sheep.get() or 0)
        score_donkeys = int(self.count_donkeys.get() or 0)
        score_cows = int(self.count_cows.get() or 0)
        score_boars = int(self.count_boars.get() or 0)

        if score_sheep == 0:
            negative_points += 2
        else:
            score += score_sheep
        if score_donkeys == 0:
            negative_points += 2
        else:
            score += score_donkeys
        if score_cows == 0:
            negative_points += 2
        else:
            score += score_cows
        if score_boars == 0:
            negative_points += 2
        else:
            score += score_boars

        # -1 pt per unused space
        negative_points += int(self.count_unused.get() or 0)

        # 1/2 pt per grain (rounded up), 1 pt per veg, 1 pt per ruby
        grain = int(self.count_grain.get() or 0)
        score_grain = math.ceil(grain / 2)

        score += score_grain + int(self.count_veg.get() or 0) + int(self.count_ruby.get() or 0)

        # Add points from rooms, pastures and mines built
        score += int(self.count_rooms.get() or 0) + int(self.count_fields.get() or 0) + int(self.count_mines.get() or 0)

        # Add bonus points from yellow tiles (parlors, chambers and storage rooms)
        yellows = 0
        if self.chamber_food.get() == 1:
            yellows += 1
            # 2 pts per grain & veg pairing
            veg = int(self.count_veg.get() or 0)
            if grain > veg:
                score += (veg * 2)
            else:
                score += (grain * 2)
        if self.chamber_broom.get() == 1:
            yellows += 1
            # 5 pts for 5 dwarfs, 10 pts if 6 (max)
            if dwarfs == 6:
                score += 10
            elif dwarfs == 5:
                score += 5
        if self.chamber_writing.get() == 1:
            yellows += 1
            # Ignore up to 7 negative points
            negative_points -= 7
            if negative_points < 0:
                negative_points = 0
        if self.chamber_treasure.get() == 1:
            yellows += 1
            score += int(self.count_ruby.get() or 0)  # 1 pt per Ruby
        if self.chamber_prayer.get() == 1:
            yellows += 1
            if int(self.count_weapons.get() or 0) == 0:
                score += 8  # 8 pts if no dwarfs have weapons
        if self.chamber_fodder.get() == 1:
            yellows += 1
            # 1 pt for each 3 farm animals
            animals = score_donkeys + score_sheep + score_boars + score_cows
            score += math.floor(animals / 3)

        if self.parlor_weaving.get() == 1:
            yellows += 1
            # 1 pt for each 2 sheep
            score += math.floor(score_sheep / 2)
        if self.parlor_milking.get() == 1:
            yellows += 1
            # 1 pt per cattle
            score += score_cows
        if self.parlor_state.get() == 1:
            yellows += 1
            # 4 pts per dwelling adjacent to state parlor
            score += (int(self.count_state.get() or 0) * 4)

        if self.store_weapon.get() == 1:
            yellows += 1
            score += (int(self.count_weapons.get() or 0) * 3)  # 3 pts per weapon
        if self.store_supplies.get() == 1:
            yellows += 1
            if int(self.count_dwarfs.get() or 0) == int(self.count_weapons.get() or 0):
                score += 8  # 8 pts if every dwarf has a weapon
        if self.store_ore.get() == 1:
            yellows += 1
            score += math.floor(int(self.count_ore.get() or 0) / 2)  # 1 pt for every 2 ore
        if self.store_stone.get() == 1:
            yellows += 1
            score += int(self.count_stone.get() or 0)   # 1 pt for every stone
        if self.store_main.get() == 1:
            yellows += 1
            score += (yellows * 2)  # 2 pts per yellow tile built

        # Subtract any remaining negative points
        score -= negative_points

        # Update the display
        self.scorevalue.set(score)

# Create the app when run
if __name__ == "__main__":
    app = CavernaCalc(None)
    app.title("Caverna Calculator")
    app.mainloop()