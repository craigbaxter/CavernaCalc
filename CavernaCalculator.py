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
    Complete scoring input
    Expanded parlor/storage/chamber tile scoring (select which ones purchased & score added)
    Save/Load from file
    Better looking UI
"""

import tkinter as tk  # Python GUI


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

        # Create the UI
        self.grid()
        self.resizable(False, False)  # Prevent user from resizing the window

        self.rowcount = 0
        self.colcount = 0
        self.maxcols = 6
        input_width = 5  # Width of number input fields

        # Player board section
        heading_player = tk.Label(self, text="PLAYER BOARD", fg="white", bg="grey")
        heading_player.grid(column=0, row=self.rowcount, columnspan=self.maxcols, sticky='EW')
        self.newRow()
        
        label_dwarf = tk.Label(self, text="Dwarfs:", anchor="w")
        label_dwarf.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_dwarf = tk.Entry(self, textvariable=self.count_dwarfs, width=input_width, validate='key', validatecommand=vcmd)
        input_dwarf.grid(column=self.colcount, row=self.rowcount)
        self.count_dwarfs.set(u"2")
        self.newColumn()

        label_weapons = tk.Label(self, text=" with weapons:", anchor="w")
        label_weapons.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_weapons = tk.Entry(self, textvariable=self.count_weapons, width=input_width, validate='key', validatecommand=vcmd)
        input_weapons.grid(column=self.colcount, row=self.rowcount)
        self.count_weapons.set(u"0")
        self.newColumn()

        label_gold = tk.Label(self, text="Gold:", anchor="w")
        label_gold.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_gold = tk.Entry(self, textvariable=self.count_gold, width=input_width, validate='key', validatecommand=vcmd)
        input_gold.grid(column=self.colcount, row=self.rowcount)
        self.count_gold.set(u"0")
        self.newColumn()

        label_beg = tk.Label(self, text="Begging:", anchor="w")
        label_beg.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_beg = tk.Entry(self, textvariable=self.count_begging, width=input_width, validate='key', validatecommand=vcmd)
        input_beg.grid(column=self.colcount, row=self.rowcount)
        self.count_begging.set(u"0")
        self.newColumn()

        label_unused = tk.Label(self, text="Unused Spaces:", anchor="w")
        label_unused.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_unused = tk.Entry(self, textvariable=self.count_unused, width=input_width, validate='key', validatecommand=vcmd)
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
        input_dogs = tk.Entry(self, textvariable=self.count_dogs, width=input_width, validate='key', validatecommand=vcmd)
        input_dogs.grid(column=self.colcount, row=self.rowcount)
        self.count_dogs.set(u"0")
        self.newColumn()

        label_sheep = tk.Label(self, text="Sheep:", anchor="w")
        label_sheep.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_sheep = tk.Entry(self, textvariable=self.count_sheep, width=input_width, validate='key', validatecommand=vcmd)
        input_sheep.grid(column=self.colcount, row=self.rowcount)
        self.count_sheep.set(u"0")
        self.newColumn()

        label_donkey = tk.Label(self, text="Donkeys:", anchor="w")
        label_donkey.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_donkeys = tk.Entry(self, textvariable=self.count_donkeys, width=input_width, validate='key', validatecommand=vcmd)
        input_donkeys.grid(column=self.colcount, row=self.rowcount)
        self.count_donkeys.set(u"0")
        self.newColumn()

        label_boars = tk.Label(self, text="Wild Boars:", anchor="w")
        label_boars.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_boars = tk.Entry(self, textvariable=self.count_boars, width=input_width, validate='key', validatecommand=vcmd)
        input_boars.grid(column=self.colcount, row=self.rowcount)
        self.count_boars.set(u"0")
        self.newColumn()

        label_cows = tk.Label(self, text="Cattle:", anchor="w")
        label_cows.grid(column=self.colcount, row=self.rowcount, sticky='W')
        self.newColumn()
        input_cows = tk.Entry(self, textvariable=self.count_cows, width=input_width, validate='key', validatecommand=vcmd)
        input_cows.grid(column=self.colcount, row=self.rowcount)
        self.count_cows.set(u"0")
        self.newColumn()

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
        # 1 point per dwarf and dog
        score_dwarfs = int(self.count_dwarfs.get() or 0)
        score_dogs = int(self.count_dogs.get() or 0)

        score = score_dwarfs + score_dogs

        # 1 point per farm animal (-3 if you don't have any)
        score_sheep = int(self.count_sheep.get() or 0)
        score_donkeys = int(self.count_donkeys.get() or 0)
        score_cows = int(self.count_cows.get() or 0)
        score_boars = int(self.count_boars.get() or 0)

        if score_sheep == 0:
            score -= 3
        else:
            score += score_sheep
        if score_donkeys == 0:
            score -= 3
        else:
            score += score_donkeys
        if score_cows == 0:
            score -= 3
        else:
            score += score_cows
        if score_boars == 0:
            score -= 3
        else:
            score += score_boars

        # -1 per unused space
        score -= int(self.count_unused.get() or 0)

        # Update the display
        self.scorevalue.set(score)

# Create the app when run
if __name__ == "__main__":
    app = CavernaCalc(None)
    app.title("Caverna Calculator")
    app.mainloop()