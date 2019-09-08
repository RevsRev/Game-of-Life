import numpy as np
import copy
import matplotlib.pyplot as plt
from matplotlib import colors
import math

global click_coordinates, click_state
    
class things_i_found:
    """Things I found, but not necessarily discovered."""
    blinker_maker = np.array([[0,0,1], [1,0,1], [0,0,1]])

class methuselah:
    """A pattern that takes a large number of generalisations in order to
    stabalise and becomes much larger than its original confiuration at some
    point during its evolution."""
    acorn = np.array([[0,1,0,0,0,0,0], [0,0,0,1,0,0,0], [1,1,0,0,1,1,1]])
    b_heptomino = np.array([[1,0,1,1],[1,1,1,0],[0,1,0,0]])
    pi_heptomino = np.array([[1,1,1],[1,0,1],[1,0,1]])

class still_life:
    """A still life is an oscillator with period 1."""
    block = np.array([[1,1],[1,1]])
    bee_hive = np.array([[0,1,1,0],[1,0,0,1],[0,1,1,0]])
    table_on_table = np.array([[1,1,0,1,1], [0,1,0,1,0], [0,1,0,1,0],
                               [1,1,0,1,1]])

class oscillator:
    """Oscillator's are stationary self-contained configurations of a life board that exhibit
    periodic behaviour."""
    blinker = np.array([[1],[1],[1]])
    ocatgon_2 = np.array([[0,0,0,1,1,0,0,0], [0,0,1,0,0,1,0,0], [0,1,0,0,0,0,1,0],
                          [1,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,1], [0,1,0,0,0,0,1,0],
                          [0,0,1,0,0,1,0,0], [0,0,0,1,1,0,0,0]])
    pulsar = np.array([[0,0,1,1,1,0,0,0,1,1,1,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [1,0,0,0,0,1,0,1,0,0,0,0,1],
                       [1,0,0,0,0,1,0,1,0,0,0,0,1],
                       [1,0,0,0,0,1,0,1,0,0,0,0,1],
                       [0,0,1,1,1,0,0,0,1,1,1,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,1,1,1,0,0,0,1,1,1,0,0],
                       [1,0,0,0,0,1,0,1,0,0,0,0,1],
                       [1,0,0,0,0,1,0,1,0,0,0,0,1],
                       [1,0,0,0,0,1,0,1,0,0,0,0,1],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,1,1,1,0,0,0,1,1,1,0,0]])
    
class spaceship:
    """A spaceship is a pattern that repeats itself but translates some non-zero 
    distance every period."""
    glider = np.array([[0,0,1], [1,0,1], [0,1,1]])
    lightweight = np.array([[0,1,0,0,1], [1,0,0,0,0], [1,0,0,0,1], [1,1,1,1,0]])
   
class puffer:
    """A puffer is an object like a spaceship except it leaves debris behind."""
    blinker_puffer1 = np.array([[0,0,0,1,0,0,0,0,0],
                                [0,1,0,0,0,1,0,0,0],
                                [1,0,0,0,0,0,0,0,0],
                                [1,0,0,0,0,1,0,0,0],
                                [1,1,1,1,1,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,1,1,0,0,0,0,0,0],
                                [1,1,0,1,1,1,0,0,0],
                                [0,1,1,1,1,0,0,0,0],
                                [0,0,1,1,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,1,1,0,0],
                                [0,0,0,1,0,0,0,0,1],
                                [0,0,1,0,0,0,0,0,0],
                                [0,0,1,0,0,0,0,0,1],
                                [0,0,1,1,1,1,1,1,0]])
    
class gun:
    """A gun is a stationary (repeating) pattern that repeatedly emits spaceships."""
    gospel_glider_gun = np.array([[0,0,0,1,1,0,0,0,0],
                                  [0,0,0,1,1,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,1,1,1,0,0,0,0],
                                  [0,1,0,0,0,1,0,0,0],
                                  [1,0,0,0,0,0,1,0,0],
                                  [1,0,0,0,0,0,1,0,0],
                                  [0,0,0,1,0,0,0,0,0],
                                  [0,1,0,0,0,1,0,0,0],
                                  [0,0,1,1,1,0,0,0,0],
                                  [0,0,0,1,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,1,1,1,0,0],
                                  [0,0,0,0,1,1,1,0,0],
                                  [0,0,0,1,0,0,0,1,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,1,1,0,0,0,1,1],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,1,1,0,0],
                                  [0,0,0,0,0,1,1,0,0]])

class configuration:
    #Configurations to add to the board. Could be a beehive, spaceship, etc.
    #Array contains zeros and ones (dead/alive cells) and the location is the
    #top left corner of the location the array is to be placed on the board grid.
    
    def __init__(self, array, location):
        self.grid = array
        self.location = location  
        
    def rotate(self):
        #Rotates the array by 90 degrees clockwise (about the
        #centre of the array.)
        _ = np.zeros((self.grid.shape[1], self.grid.shape[0]))
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                _[j,self.grid.shape[0]-i-1] = self.grid[i,j]
        self.grid = _

class board:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((height,width))
        self.important_cells = []
        
    def add_config_to_board(self,config):
        #Add an array containing zeros and ones to the board. 
        for i in range(config.grid.shape[0]):
            for j in range(config.grid.shape[1]):
                try:
                    self.grid[config.location[0]+i][config.location[1]+j] = config.grid[i][j]
                except IndexError:
                    pass
    
    def find_important_cells(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == 1:
                    for m in range(-1,2):
                        for n in range(-1,2):
                            if [i+m,j+n] not in self.important_cells \
                            and 0<=i+m<=self.height-1 and 0<=j+n <= self.width-1:
                                self.important_cells.append([i+m,j+n])
                            
    def update(self):
        old_grid = copy.deepcopy(self.grid)
        for cells in self.important_cells:
            neighbours = 0
            for m in range(-1,2):
                for n in range(-1,2):
                    try:
                        if old_grid[cells[0]+m][cells[1]+n]==1:
                            neighbours = neighbours + 1
                    except IndexError:
                        pass
            if old_grid[cells[0]][cells[1]] == 1:
                neighbours = neighbours - 1
                if 2<= neighbours <= 3:
                    self.grid[cells[0]][cells[1]] = 1
                else:
                    self.grid[cells[0]][cells[1]] =0
            else:
                if neighbours == 3:
                    self.grid[cells[0]][cells[1]] =1
                    
def data_to_configuration(string, loc, rotations):
    M = {'acorn': configuration(methuselah.acorn, loc), 'b_heptomino': configuration(methuselah.b_heptomino, loc), 
         'pi_heptomino': configuration(methuselah.pi_heptomino, loc)}
    SL = {'block': configuration(still_life.block, loc) , 'bee_hive': configuration(still_life.bee_hive, loc),
          'table_on_table': configuration(still_life.table_on_table, loc)}
    O = {'blinker': configuration(oscillator.blinker, loc), 'octagon_2': configuration(oscillator.ocatgon_2, loc),
         'pulsar': configuration(oscillator.pulsar, loc)}
    SS = {'glider': configuration(spaceship.glider, loc), 'lightweight': configuration(spaceship.lightweight, loc)}
    P = {'blinker_puffer1': configuration(puffer.blinker_puffer1, loc)}
    G = {'gospel_glider_gun': configuration(gun.gospel_glider_gun, loc)}
    types = {'methuselah' : M, 'still_life': SL, 'oscillator': O, 'spaceship': SS, 'puffer': P, 'gun': G }
    
    i = 0
    while string[i] != '.' and i < len(string):
        i= i+1
    if i == len(string):
        return 1
    config_type = string[0:i]
    sub_type = string[i+1: len(string)]
    
    try: 
        config = types[config_type][sub_type]
        if rotations == 1:
            config.rotate()
        elif rotations == 2:
            config.rotate()
            config.rotate()
        elif rotations == 3:
            config.rotate()
            config.rotate()
            config.rotate()
        return config
    except KeyError:
        return 1

def onclick(event):
    global click_coordinates, click_state
    click_coordinates =  [math.floor(event.ydata+0.5), math.floor(event.xdata+0.5)]
        
def releaseclick(event):
    global click_coordinates, click_state
    click_coordinates = []

def onpress(event):
    global click_state
    if event.key == "escape":
        click_state =1
                    
def play():
    global click_coordinates, click_state
    print("Welcome to Conway's Game of Life! This game has a small but \n\
interesting library of configurations built in, as well as the \n\
ability to manually enter new configurations or just 'click' them \n\
in by using the 'click configuration' settings.")
    print("How large would you like your game to be? Ensure that entries are \n\
natural numbers:")
    
    while True:
        height = input("Board height: ")
        width = input("Board width: ")
        try:
            h1 = int(height)
            h2 = int(width)
            if h1<=0 or h2<=0:
                print("Sorry, those are not valid dimensions. Make sure both \n\
height and width are positive integers.")
                continue
            height, width = h1, h2
            del h1, h2
            break
        except ValueError:
            print("Sorry, at least one of height, width that you entered was not \n\
an integer. Please try again.")
    brd = board(height, width)
    fig , ax = plt.subplots()
    plot(brd, fig, ax)
    cmap = colors.ListedColormap(['white', 'black'])
    bounds = [-0.5, 0.5, 1.5]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    ax.grid(which = 'major', axis = 'both', linestyle = '-', color = 'k', linewidth = 0.5)
    ax.set_xlim(-0.5,brd.width - 0.5)
    ax.set_ylim(-0.5, brd.height - 0.5)
    ax.set_xticks(np.arange(-.5, brd.width, 1));
    ax.set_yticks(np.arange(-.5, brd.height, 1));
    
    frame = plt.gca()
    frame.axes.xaxis.set_ticklabels([])
    frame.axes.yaxis.set_ticklabels([])
    del frame
    
    while True:
        print("\nOptions: \n\n \
    [1] Add configuration to board from library. \n \
    [2] Add configuration to board by clicking squares. \n \
    [3] View library. \n \
    [4] Begin Life.")
        choice = input("Your choice (1,2,3 or 4): ")
        if choice == '1':
            print("\nPick a cofiguration to add to the board, its location, and #rotations.\n\
(#Rotations must be an integer, 0,1,2 or 3. other integer inputs will be mapped to these (mod4)) \n\
Ensure that configuration is referenced correctly using standard python\n\
notation used in the code for this module. For instance, reference the gospel\n\
glider gun as gun.gospel_glider_gun.\n")
            config = input("Your chosen configuration: ")
            while True:
                locheight = input("Height (y coordinate) of configuration: ")
                locwidth = input("Width (x coordinate) of configuration: ")
                try:
                    h1 = int(locheight)
                    h2 = int(locwidth)
                    if h1<=0 or h2<=0:
                        print("Sorry these are not valid coordinates. Make sure both\n\
height and width are positive integers.")
                        continue
                    locheight, locwidth = h1,h2
                    del h1, h2
                    break
                except ValueError:
                    print("Sorry, at least one of height, width that you entered was not\n\
an integer. Please try again.")
            while True:
                rotations = input("Rotations: ")
                try:
                    rot = int(rotations)%4
                    rotations = rot
                    del rot
                    break
                except ValueError:
                    print("Sorry, that was an invalid number of ratoations. Try again.")
            config = data_to_configuration(config, [locheight, locwidth], rotations)
            if config == 1:
                print("Invalid configuration entered. Returning to options menu.\n")
            else:
                brd.add_config_to_board(config)
                plot(brd, fig, ax)
                print("Configuration successfully added to board!")
            continue
        if choice == '2':
            print("Press escape key to stop drawing")
            cidpress = fig.canvas.mpl_connect('button_press_event', onclick)
            cidrelease = fig.canvas.mpl_connect('button_release_event', releaseclick)
            cidbutton = fig.canvas.mpl_connect('key_press_event', onpress)
            click_state = 0
            click_coordinates = []
            while click_state == 0:
                if click_coordinates != []:
                    if brd.grid[click_coordinates[0]][click_coordinates[1]] == 0:
                        brd.grid[click_coordinates[0]][click_coordinates[1]] =1
                    else:
                        brd.grid[click_coordinates[0]][click_coordinates[1]] = 0
                    plot(brd,fig,ax)
                plt.pause(0.05)
            fig.canvas.mpl_disconnect(cidpress)
            fig.canvas.mpl_disconnect(cidrelease)
            fig.canvas.mpl_disconnect(cidbutton)
            continue
        if choice == '3':
            print("\nLibarary of configurations:\n\n \
    Still Lifes: \n \
        block: A 2x2 square. \n \
        beehive: A still life that looks like a beehive. \n \
        table on table: A still life that looks like two tables. \n \
    Oscillators: \n \
        blinker: A 3x1 rod that oscillates between itself and a 1x3 rod.\n \
        octagon2: An octagon shaped oscillator. \n \
        pulsar: A more complex oscillator. \n \
    Spaceships: \n \
        glider: The smallest spaceship. It travels diagonally. \n \
        lightweight: The second smallest spaceship. It travels orthogonally. \n \
    Guns: \n \
        gospel_glider_gun: Fires gliders!\n \
    Puffers: \n \
        blinker_puffer1: Like a spaceship, but leaves debris behind. \n \
    Methuselahs: \n \
        acorn \n \
        b_heptomino \n \
        pi_heptomino\n")
            continue
        if choice == '4':
            del choice
            break
        else:
            print("Not a valid choice. Try again.")
            continue
    
    print("How many generations would you like to run Life for?")
    
    while True:
        generations = input("Generations = ")
        try:
            gen = int(generations)
            if gen<=0:
                print("Please ensure that #generations is a natural number.")
                continue
            generations = gen
            del gen
            break
        except ValueError:
            print("Sorry, that was not an integer. Please try again.")
            
    while True:
        frame_rate = input("Frame rate = ")
        try:
            fr = float(frame_rate)
            if fr <=0:
                print("Please ensure Frame rate is a positive real number.")
                continue
            frame_rate = fr
            del fr
            break
        except ValueError:
            print("Sorry, that was not a real number. Please try again.")
            
    brd.find_important_cells() 
    for i in range(generations):
        brd.update()
        brd.find_important_cells()
        plt.cla()
        ax.set_ylim(-0.5, brd.height - 0.5)
        ax.imshow(brd.grid, cmap = cmap, norm = norm)
        plt.pause(1/frame_rate)
    
def plot(board, fig, ax):
    plt.cla()
    cmap = colors.ListedColormap(['white', 'black'])
    bounds = [-0.5, 0.5, 1.5]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    
    ax.imshow(board.grid, cmap = cmap, norm = norm)
    
    ax.grid(which = 'major', axis = 'both', linestyle = '-', color = 'k', linewidth = 0.5)
    ax.set_xlim(-0.5,board.width - 0.5)
    ax.set_ylim(-0.5, board.height - 0.5)
    ax.set_xticks(np.arange(-.5, board.width, 1));
    ax.set_yticks(np.arange(-.5, board.height, 1));
    
    frame = plt.gca()
    frame.axes.xaxis.set_ticklabels([])
    frame.axes.yaxis.set_ticklabels([])    