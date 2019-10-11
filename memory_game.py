import random ,pygame , sys ,time
from pygame.locals import *

FPS=60
WIDTH=640
HEIGHT=480
BOX=60
GAP=20
REVEALS=4
BWIDTH=4
BHEIGHT=3
XMARGIN = int((WIDTH - (BWIDTH * (BOX + GAP))) / 2)
YMARGIN = int((HEIGHT - (BHEIGHT * (BOX + GAP))) / 2)

assert (BWIDTH*BHEIGHT)%2==0,'BOARD IS DISMISSED'

GRAY  = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE = (255, 255, 255)
RED  = (255,  0,  0)
GREEN  = (  0, 255,  0)
BLUE  = (  0,  0, 255)
YELLOW  = (255, 255,  0)
ORANGE  =(255, 128,  0)
PURPLE  = (255,  0, 255)
CYAN  = (  0, 255,255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE 
HIGHLIGHTCOLOR = BLUE

DONUT='donut'
SQUARE='square'
LINES='lines'
DIAMOND='diamond'
OVAL='oval'

ALLCOLORS=(RED,GREEN,BLUE,YELLOW,ORANGE,PURPLE,CYAN)
ALLSHAPES=(DONUT,SQUARE,LINES,DIAMOND,OVAL)
 
assert len(ALLCOLORS)*len(ALLSHAPES)*2 >= BWIDTH*BHEIGHT ,"BOARD IS TOO BIG"

class button():
    def __init__(self,color,x,y,width,height,text=''):
        self.x=x
        self.y=y
        self.color=color
        self.width=width
        self.height=height
        self.text=text

    def draw(self,DISPLAYSURF,outline=None):
        if outline:
            pygame.draw.rect(DISPLAYSURF,outline,(self.x -2 , self.y-2 , self.width+4 , self.height+4),0)
        pygame.draw.rect(DISPLAYSURF,self.color,(self.x -2 , self.y-2 , self.width+4 , self.height+4),0)
        if self.text != '':
            font = pygame.font.SysFont('comicsans',60)
            text = font.render(self.text, 1, (0,0,0))
            DISPLAYSURF.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

welcome=button(RED,130,30,350,60,'MEMORY GAME')
ashish=button(RED,150,400,490,60,'-By Ashish Maheshwari')

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    
    pygame.mixer.music.load('You Belong with me.mp3')
    pygame.mixer.music.play(-1,30.0)

    DISPLAYSURF=pygame.display.set_mode((WIDTH,HEIGHT),FULLSCREEN)

    mousex=0
    mousey=0

    pygame.display.set_caption('Memory Game')

    mainBoard= getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)

    firstSelection = None

    DISPLAYSURF.fill(BGCOLOR)
    welcome.draw(DISPLAYSURF,WHITE)
    ashish.draw(DISPLAYSURF,WHITE)
    startGameAnimation(mainBoard)

    while True:
        mouseClicked = False

        DISPLAYSURF.fill(BGCOLOR)
        welcome.draw(DISPLAYSURF,WHITE)
        ashish.draw(DISPLAYSURF,WHITE)
        drawBoard(mainBoard, revealedBoxes)

        for event in pygame.event.get():
            if (event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE) :
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEMOTION :
                mousex,mousey = event.pos

            elif event.type == MOUSEBUTTONUP:
                mousex,mousey = event.pos
                mouseClicked = True

        boxx,boxy=getBoxAtPixel(mousex,mousey)

        if boxx != None and boxy != None :

            if not revealedBoxes[boxx][boxy]:
                drawHighlightBox(boxx,boxy)
            if not revealedBoxes[boxx][boxy] and mouseClicked :
                drawHighlightBox(boxx,boxy)
                revealBoxesAnimation(mainBoard ,[(boxx,boxy)])
                revealedBoxes[boxx][boxy]=True

                if firstSelection == None :
                    firstSelection=(boxx,boxy)
                else:
                    icon1shape,icon1color = getShapeAndColor(mainBoard,firstSelection[0],firstSelection[1])
                    icon2shape,icon2color = getShapeAndColor(mainBoard,boxx,boxy)

                    if icon1shape != icon2shape or icon1color != icon2color :
                        pygame.time.wait(1000)
                        coverBoxesAnimation(mainBoard , [(firstSelection[0],firstSelection[1]),(boxx,boxy)])
                        revealedBoxes[firstSelection[0]][firstSelection[1]]=False
                        revealedBoxes[boxx][boxy] = False

                    elif hasWon(revealedBoxes):
                        gameWonAnimation(mainBoard)
                        pygame.time.wait(2000)

                        mainBoard=getRandomizedBoard()
                        revealedBoxes= generateRevealedBoxesData(False)

                        drawBoard(mainBoard, revealedBoxes)
                        pygame.display.update()
                        pygame.time.wait(1000)

                        startGameAnimation(mainBoard)

                    firstSelection=None
    
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    pygame.mixer.music.stop()
        
def generateRevealedBoxesData(val):
    revealedBoxes=[]
    for i in range(BWIDTH):
        revealedBoxes.append([val]*BHEIGHT)
    return revealedBoxes

def getRandomizedBoard():
    icons=[]
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append((shape,color))

    random.shuffle(icons)
    numIconsUsed = int(BWIDTH*BHEIGHT /2)
    icons=icons[:numIconsUsed]*2
    random.shuffle(icons)

    board=[]
    for x in range(BWIDTH):
        column=[]
        for y in range(BHEIGHT):
            column.append(icons[0])
            del icons[0]
        board.append(column)
    return board

def splitIntoGroupsOf(groupSize,theList):
    result=[]
    for i in range(0,len(theList),groupSize):
        result.append(theList[i:i + groupSize])
    return result

def leftTopCoordsOfBox(boxx,boxy):
    left=boxx * (BOX + GAP) + XMARGIN
    top=boxy * (BOX + GAP) + YMARGIN
    return (left,top)

def getBoxAtPixel(x,y):
    for boxx in range(BWIDTH):
        for boxy in range(BHEIGHT):
            left,top=leftTopCoordsOfBox(boxx,boxy)
            boxRect = pygame.Rect(left, top, BOX, BOX)
            if boxRect.collidepoint(x,y):
                return (boxx,boxy)
    return (None,None)

def drawIcon(shape,color,boxx,boxy):
    quarter = int(BOX*0.25)
    half = int(BOX*0.50)
    left, top = leftTopCoordsOfBox(boxx,boxy)
    if shape==DONUT:
        pygame.draw.circle(DISPLAYSURF, color , (left+half , top+half),half-5)
        #pygame.draw.circle(DISPLAYSURF, BGCOLOR,(left+half , top+half),quarter-5)

    elif shape == SQUARE:
        pygame.draw.rect(DISPLAYSURF,color,(left+1 , top+1 , BOX-1 , BOX-1))

    elif shape == DIAMOND:
        pygame.draw.polygon(DISPLAYSURF, color ,((left+half,top),(left,top+quarter),(left+half-1,top+BOX-1),(left+BOX-1,top+quarter-1)))
    
    elif shape == LINES:
        for i in range(0,BOX,4):
            pygame.draw.line(DISPLAYSURF,color,(left,top+i),(left+i,top))
            pygame.draw.line(DISPLAYSURF, color , (left+i,top+BOX-1) , (left+BOX-1,top+i))
            
    elif shape == OVAL:
        pygame.draw.ellipse(DISPLAYSURF,color,(left,top+quarter,BOX,half))

def getShapeAndColor(board,boxx,boxy):
    return board[boxx][boxy][0],board[boxx][boxy][1]

def drawBoxCovers(board,boxes,coverage):
    for box in boxes:
        left,top = leftTopCoordsOfBox(box[0],box[1])
        pygame.draw.rect(DISPLAYSURF,BGCOLOR,(left,top,BOX,BOX))
        shape, color = getShapeAndColor(board,box[0],box[1])
        drawIcon(shape,color,box[0],box[1])
        if coverage>0:
            pygame.draw.rect(DISPLAYSURF,BGCOLOR,(left,top,coverage,BOX))
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def revealBoxesAnimation(board, boxesToReveal):
    for coverage in range(BOX,(-REVEALS)-1,-REVEALS):
        drawBoxCovers(board,boxesToReveal,coverage)

def coverBoxesAnimation(board, boxesToCover):
    for coverage in range(0, BOX+REVEALS ,REVEALS):
        drawBoxCovers(board,boxesToCover,coverage)

def drawBoard(board,revealed):
    for boxx in range(BWIDTH):
        for boxy in range(BHEIGHT):
            left,top = leftTopCoordsOfBox(boxx,boxy)
            if not revealed[boxx][boxy]:
                pygame.draw.rect(DISPLAYSURF, BOXCOLOR , (left,top,BOX,BOX))
            else:
                shape,color = getShapeAndColor(board,boxx,boxy)
                drawIcon(shape,color,boxx,boxy)

def drawHighlightBox(boxx, boxy):
    left, top = leftTopCoordsOfBox(boxx, boxy)
    pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left - 5, top - 5, BOX + 10, BOX + 10), 4)

def startGameAnimation(board):
    coveredBoxes = generateRevealedBoxesData(False)
    boxes = []
    for x in range(BWIDTH):
        for y in range(BHEIGHT):
            boxes.append( (x, y) )
    random.shuffle(boxes)
    boxGroups = splitIntoGroupsOf(BWIDTH*BHEIGHT, boxes)
    drawBoard(board, coveredBoxes)
    for boxGroup in boxGroups:
        revealBoxesAnimation(board, boxGroup)
        #time.sleep(5)
        coverBoxesAnimation(board, boxGroup)

def gameWonAnimation(board):
    coveredBoxes = generateRevealedBoxesData(True)
    color1 = LIGHTBGCOLOR
    color2 = BGCOLOR
    for i in range(20):
        color1, color2 = color2, color1
        DISPLAYSURF.fill(color1)
        welcome.draw(DISPLAYSURF,WHITE)
        drawBoard(board, coveredBoxes)
        pygame.display.update()
        pygame.time.wait(100)
        
    DISPLAYSURF.fill(RED)
    font=pygame.font.Font('freesansbold.ttf',80)
    text=font.render('YOU WON!!!',True,WHITE,RED)
    textRect=text.get_rect()
    textRect.center=(WIDTH//2,HEIGHT//2)
    DISPLAYSURF.blit(text,textRect)
    pygame.display.update()

    pygame.time.wait(5000)
    pygame.quit()
    sys.exit()

def hasWon(revealedBoxes):
    for i in revealedBoxes:
        if False in i:
            return False
    return True

main()
