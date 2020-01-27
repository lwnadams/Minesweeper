# GNU General Public License v3.0
# All code made in Python
# Programmed by Lawrence Adams
# Artwork and Images made by Martina Šmejkalová
# http://www.sireasgallery.com/"


import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import random


# Coding indroduction window
class intro:

    def __init__(self,window):
        # destroys any previous window used before opening window, such as pressing back button on game window
        window.destroy()
        window = tk.Toplevel(root)
        window.title("MINESWEEPER")
        window.geometry("800x800")
        window.resizable(FALSE,FALSE)
        window.configure(background='sky blue')
        window.iconbitmap('Images/Mine.ico')

        titleframe = Frame(window, padx=150, height=50, bg="sky blue", highlightcolor="green", highlightthickness=1)
        titleframe.grid(row=0, column=1,padx=20,pady=20)
        infoframe = Frame(window, padx=180, height=50, bg="sky blue", highlightcolor="green", highlightthickness=1)
        infoframe.grid(row=1, column=1,padx=20,pady=20)
        buttonframe = Frame(window, padx=180, height=50, bg="sky blue", highlightcolor="green", highlightthickness=1)
        buttonframe.grid(row=2, column=1,padx=20,pady=20)
        title = Label(titleframe, text="MINESWEEPER", font=("Helvetica", 40, 'bold'), fg="red", bg="sky blue", height=2)
        title.grid(column=1, row=1, pady=0)
        Label(infoframe, text="All code made in Python\nProgrammed by Lawrence Adams\n\nArtwork and Images made by Martina Šmejkalová\nhttp://www.sireasgallery.com/", font=("Helvetica", 10), fg="gray", bg="sky blue").pack()
        r = IntVar()
        r.set("10")
        Radiobutton(buttonframe, text="Easy", variable=r, value=10, bg="skyblue").grid(column=1, row=0, sticky=W)
        Radiobutton(buttonframe, text="Medium", variable=r, value=40, bg="skyblue").grid(column=1, row=1, sticky=W)
        Radiobutton(buttonframe, text="Hard", variable=r, value=80, bg="skyblue").grid(column=1, row=2, sticky=W)
        Radiobutton(buttonframe, text="Very Hard", variable=r, value=150, bg="skyblue").grid(column=1, row=3, sticky=W)
        Radiobutton(buttonframe, text="Basically Impossible", variable=r, value=479, bg="skyblue").grid(column=1, row=4, sticky=W)
        redmine = ImageTk.PhotoImage(Image.open("Images/mine.ico"))
        titleimage = Label(titleframe, image=redmine, bg="sky blue", height=300)
        titleimage.image = redmine
        titleimage.grid(column=1, row=2)
        playbutton = Button(buttonframe, text="PLAY", command=lambda: self.destroywindow(window, r.get()), padx=30, pady=20)
        playbutton.grid(row=2, column=2,padx=20, sticky=W, rowspan=3)
        exitbutton = Button(buttonframe, text="QUIT", command=window.quit, padx=30, pady=20)
        exitbutton.grid(row=2, column=0,padx=20, sticky=E, rowspan=3)

    # defines number of tiles in X and Y, grid size in pixels and number of total bombs, the latter changes depending on difficulty selected
    def destroywindow(self, window, numberofbombs):
        window.destroy()
        setup(32,15,"1480x810",numberofbombs)

# Setup main body of game
class setup:

    def __init__(self, x, y, gridsize, numberofbombs):
        self.x = x
        self.y = y
        self.gridsize = gridsize
        self.numberofbombs = numberofbombs
        self.window = tk.Toplevel(root)
        self.window.title("LETS PLAY!")
        self.window.iconbitmap('Images/Mine.ico')
        self.window.configure(background='sky blue')
        self.window.geometry(gridsize)
        self.window.resizable(FALSE, FALSE)
        self.buttonframe = Frame(self.window, padx=180, height=50, width=1460, bg="sky blue", highlightcolor="green", highlightthickness=1)
        self.buttonframe.grid(row=1, column=1, padx=20, pady=20)
        self.gameframe = Frame(self.window, padx=0, height=600, width=1460, highlightcolor="green", highlightthickness=1)
        self.gameframe.grid(row=0, column=1, padx=10, pady=20)
        self.backbutton = Button(self.buttonframe, text="BACK", command=lambda: intro(self.window), padx=30, pady=20)
        self.backbutton.grid(column=0,row=0,padx=20,pady=20, sticky=W)
        self.exitbutton = Button(self.buttonframe, text="QUIT", command=self.window.quit, padx=30, pady=20)
        self.exitbutton.grid(column=2,row=0,padx=20,pady=20, sticky=E)
        # Keeps columns and rows uniform to prevent resizing when tiles are pressed
        for i in range (0,x):
            self.gameframe.columnconfigure(i, weight=1, uniform=40)
        for i in range (0,y):
            self.gameframe.rowconfigure(i, weight=1,uniform=40)
        self.gameframe.grid_propagate(False)
        blanktile = Image.open("Images/Tile.ico").resize((40, 40), Image.ANTIALIAS)
        self.blanktile = ImageTk.PhotoImage(blanktile)
        self.Smiley1 = Image.open("Images/Smiley1.ico").resize((80, 80), Image.ANTIALIAS)
        self.Smiley1 = ImageTk.PhotoImage(self.Smiley1)
        self.Smiley2 = Image.open("Images/Smiley2.ico").resize((80, 80), Image.ANTIALIAS)
        self.Smiley2 = ImageTk.PhotoImage(self.Smiley2)
        self.Smiley3 = Image.open("Images/Smiley3.ico").resize((80, 80), Image.ANTIALIAS)
        self.Smiley3 = ImageTk.PhotoImage(self.Smiley3)
        self.Smiley = Image.open("Images/Smiley.ico").resize((80, 80), Image.ANTIALIAS)
        self.Smiley = ImageTk.PhotoImage(self.Smiley)
        self.happysmiley = Label(self.buttonframe, image=self.Smiley1, bg="skyblue")
        self.happysmiley.image = self.Smiley1
        self.happysmiley.grid(row=0, column=1)
        self.tilecoordinates = []
        self.bombcoordinates = []
        self.buttondic = {}

        i = 0
        # While loop used to randomly place bombs on range of (x,y) tile coordinates
        while i != numberofbombs:
            xchoice = random.randrange(0,x)
            ychoice = random.randrange(0,y)
            c = (xchoice,ychoice)
            if c not in self.bombcoordinates:
                self.bombcoordinates.append(c)
                i += 1

        # generates list of all tile coordinates
        for i in range(0, y):
            for r in range(0, x):
                self.tilecoordinates.append((r,i))

        # Places empty tile icons onto 480 tile coordinates in two embodied for loops
        for i in range(0, y):
            for r in range(0, x):
                clickcoordinates = [(r, i)]
                # function "checkfordata" uses bomb coordinates and tile coordinates to determine tile properties
                (hitmine, bombcount) = self.checkfordata(clickcoordinates[0])
                tile = self.drawtile(0, clickcoordinates)
                # Each tile is seperated as class object "classtile"
                classtile = tileID(hitmine, bombcount, tile)
                # Each tile object is added to dictionary "buttondic" so the instances of each one can be looked up using tile coordinates
                self.buttondic[clickcoordinates[0]] = classtile

    # at users repeated right clicking, functions called are drawflag > drawquestion > draw tile > drawflag > drawquestion > draw tile ect...
    def drawtile(self, event, click):
        coordinates = click[0]
        tile = Button(self.gameframe, image=self.blanktile, bg="sky blue", padx=0)
        if event != 0:
            self.buttondic.get(coordinates).button.destroy()
            self.buttondic[coordinates].button = tile
        # left button hold causes smiley to change from happy smiley to anxious smiley
        tile.bind('<ButtonPress-1>', lambda e, c=click: self.emoji(e))
        # left button release calls self.reveal function to execute
        tile.bind('<ButtonRelease-1>', lambda e, c=click: self.reveal(e, c))
        # right button press calls draw flag function to execute
        tile.bind('<Button-3>', lambda e, c=click: self.drawflag(e, c))
        tile.image = self.blanktile
        tile.grid(column=coordinates[0], row=coordinates[1], padx=0)
        return tile

    def drawflag(self, event, click):
        coordinates = click[0]
        self.buttondic.get(coordinates).button.destroy()
        redflag = Image.open("Images/Tile3.ico").resize((40, 40), Image.ANTIALIAS)
        redflag = ImageTk.PhotoImage(redflag)
        flagon = Button(self.gameframe, image=redflag, bg="sky blue", padx=0)
        self.buttondic[coordinates].button = flagon
        # left button hold causes smiley to change from happy smiley to anxious smiley
        flagon.bind('<ButtonPress-1>', lambda e, c=click: self.emoji(e))
        # left button release calls self.reveal function to execute
        flagon.bind('<ButtonRelease-1>', lambda e, c=click: self.reveal(e, c))
        # right button press calls question mark function to execute
        flagon.bind('<Button-3>', lambda e, c=click: self.drawquestion(e, c))
        flagon.image = redflag
        flagon.grid(column=coordinates[0], row=coordinates[1], padx=0)

    def drawquestion(self, event, click):
        coordinates = click[0]
        self.buttondic.get(coordinates).button.destroy()
        questionmark = Image.open("Images/Tile2.ico").resize((40, 40), Image.ANTIALIAS)
        questionmark = ImageTk.PhotoImage(questionmark)
        questionon = Button(self.gameframe, image=questionmark, bg="sky blue", padx=0)
        self.buttondic[coordinates].button = questionon
        questionon.image = questionmark
        # left button hold causes smiley to change from happy smiley to anxious smiley
        questionon.bind('<ButtonPress-1>', lambda e, c=click: self.emoji(e))
        # left button release calls self.reveal function to execute
        questionon.bind('<ButtonRelease-1>', lambda e, c=click: self.reveal(e, c))
        # right button press calls draw tile function to execute
        questionon.bind('<Button-3>', lambda e, c=click: self.drawtile(e, c))
        questionon.grid(column=coordinates[0], row=coordinates[1], padx=0)

    # Function that determines properties for each tile, hitmine being boolean term for if tile contains mine, and bombcount being how many bombs are in neighboring tiles
    def checkfordata(self, clickcoordinate):
        hitmine = FALSE
        check = self.tile_analysis(clickcoordinate)
        if clickcoordinate not in self.bombcoordinates:
            bombcount = 0
            for i in range(0, len(check)):
                if check[i] in self.tilecoordinates:
                    if check[i] in self.bombcoordinates:
                        bombcount += 1
        else:
            hitmine = TRUE
            bombcount = NONE

        return hitmine, bombcount


    # Function called on button release. Uses information stored in the tile dictionary "buttondic" to reveal its properties
    def reveal(self, event, clickcoordinates):
        self.buttondic.get(clickcoordinates[0]).button.destroy()
        # next few lines of code determine if there are any tiles left to press, sending to function "endgame" if all tiles have been pressed
        tilesleft=[]
        for i in range(0,len(self.tilecoordinates)):
            tilecoordinates = self.tilecoordinates[i]
            if self.buttondic.get(tilecoordinates).button.winfo_exists() == 1:
                tilesleft.append(tilecoordinates)
        if len(tilesleft) <= len(self.bombcoordinates):
            self.endgame(clickcoordinates, TRUE)
        emptybuttons = []
        for i in range(0,len(clickcoordinates)):
            clickcoordinate = clickcoordinates[i]
            if self.buttondic.get(clickcoordinate).numberofbombs != 0:
                self.drawimage(self.buttondic.get(clickcoordinate).hitmine, self.buttondic.get(clickcoordinate).numberofbombs, clickcoordinate)
            else:
                self.buttondic.get(clickcoordinate).button.destroy()
                # next two lines gather list of neighbor coordinates from tile_analysis into list "check"
                check=[]
                check = self.tile_analysis(clickcoordinate)
                for i in range(0,len(check)):
                    if check[i] in self.tilecoordinates:
                        if self.buttondic.get(check[i]).button.winfo_exists() == 1:
                            # if nearby bomb count is 0, list of neighbor zeros "Empty buttons is created, else function drawimage is called to create the physical image onto a clicked tile
                            if self.buttondic.get(check[i]).numberofbombs == 0:
                                if check[i] not in emptybuttons:
                                    emptybuttons.append(check[i])
                            else:
                                self.drawimage(self.buttondic.get(check[i]).hitmine, self.buttondic.get(check[i]).numberofbombs, check[i])
        if self.buttondic.get(clickcoordinates[0]).hitmine == FALSE:
            if len(tilesleft) > len(self.bombcoordinates):
                self.happysmiley = Label(self.buttonframe, image=self.Smiley1, bg="skyblue")
                self.happysmiley.image = self.Smiley1
                self.happysmiley.grid(row=0, column=1)

        # Recursion used expand grid. if the clicked tile was 0, def reveal is called again only with reveal instructions of all surrounding tiles.
        if 'emptybuttons' in locals():
            if len(emptybuttons) > 0:
                for i in range(0,len(emptybuttons)):
                    self.buttondic.get(emptybuttons[i]).button.destroy()
                self.reveal(0, emptybuttons)


    # Function used solely to draw a physical image onto a tile coordinate
    def drawimage(self, hitmine, bombcount,clickcoordinates):
        self.buttondic.get(clickcoordinates).button.destroy()
        if hitmine == TRUE:
            self.endgame(clickcoordinates, FALSE)
        elif bombcount > 0:
            if bombcount == 1:
                color = "blue"
            elif bombcount == 2:
                color = "green"
            elif bombcount == 3:
                color = "red"
            elif bombcount == 4:
                color = "Purple"
            elif bombcount == 5:
                color = "Maroon"
            elif bombcount == 6:
                color = "cyan"
            elif bombcount == 7:
                color = "black"
            elif bombcount == 8:
                color = "grey"
            text = Label(self.gameframe, text=str(bombcount), fg=color, font=("Helvetica", 25, 'bold'))
            text.grid(column=clickcoordinates[0], row=clickcoordinates[1])

    # Function used to draw anxious smiley whilst click button is held
    def emoji(self, event):
        self.anxioussmiley = Label(self.buttonframe, image=self.Smiley2, bg="skyblue")
        self.anxioussmiley.image = self.Smiley2
        self.anxioussmiley.grid(row=0, column=1)

    # When the input of this function being a single tile coordinate, the output will be a list of neighboring tile coordinates.
    def tile_analysis(self, clickcoordinates):
        check = []
        check.append((clickcoordinates[0]-1, clickcoordinates[1]-1))
        check.append((clickcoordinates[0]-1, clickcoordinates[1]  ))
        check.append((clickcoordinates[0]-1, clickcoordinates[1]+1))
        check.append((clickcoordinates[0]  , clickcoordinates[1]+1))
        check.append((clickcoordinates[0]+1, clickcoordinates[1]+1))
        check.append((clickcoordinates[0]+1, clickcoordinates[1]  ))
        check.append((clickcoordinates[0]+1, clickcoordinates[1]-1))
        check.append((clickcoordinates[0]  , clickcoordinates[1]-1))
        return check

    # Final function called when game is at an end, either by all tiles pressed (win = TRUE), or a bomb tile pressed (win = FALSE)
    def endgame(self,clickcoordinates, win):
        Mine2 = Image.open("Images/Mine2.ico").resize((40, 40), Image.ANTIALIAS)
        Mine2 = ImageTk.PhotoImage(Mine2)
        for i in range(0,len(self.bombcoordinates)):
            bombcoordinates = self.bombcoordinates[i]
            self.buttondic.get(bombcoordinates).button.destroy()
            blackmine = Label(self.gameframe, image=Mine2, text=clickcoordinates, padx=0)
            blackmine.image = Mine2
            blackmine.grid(column=bombcoordinates[0], row=bombcoordinates[1])
        if win == TRUE:
            smiley = self.Smiley
            color = "skyblue"
        else:
            color = "lightcoral"
            smiley = self.Smiley3
            Mine = Image.open("Images/Mine.ico").resize((40, 40), Image.ANTIALIAS)
            Mine = ImageTk.PhotoImage(Mine)
            redmine = Label(self.gameframe, image=Mine, text=clickcoordinates, padx=0)
            redmine.image = Mine
            redmine.grid(column=clickcoordinates[0], row=clickcoordinates[1])
            for i in range(0, len(self.tilecoordinates)):
                tilecoordinates = self.tilecoordinates[i]
                if self.buttondic.get(tilecoordinates).button.winfo_exists() == 1:
                    # Button control on the tiles need to be ceased so the user can't carry on clicking tiles after the game is lost
                    self.buttondic.get(tilecoordinates).button.unbind('<ButtonRelease-1>')
                    self.buttondic.get(tilecoordinates).button.unbind('<ButtonPress-1>')
                    self.buttondic.get(tilecoordinates).button.unbind('<ButtonPress-3>')
                    self.buttondic.get(tilecoordinates).button.config(state=DISABLED)


        finalsmiley = Label(self.buttonframe, image=smiley, bg=color)
        finalsmiley.image = smiley
        finalsmiley.grid(row=0, column=1)

        self.window.config(bg=color)
        self.buttonframe.config(bg=color)

# Class tileID whereby each instance is a property related to each tile object
class tileID:
    def __init__(self, hitmine, numberofbombs, button):
        self.hitmine = hitmine
        self.numberofbombs = numberofbombs
        self.button = button






















root = Tk()
root.withdraw()
window = tk.Toplevel(root)
intro(window)





root.mainloop()