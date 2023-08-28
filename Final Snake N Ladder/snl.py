from random import randint
import pygame
import time

clock=pygame.time.Clock() #create an object to help track time.
pygame.init() #Initialize
width=1364
height=765

GD=pygame.display.set_mode((width,height),pygame.FULLSCREEN) #Initialize a window or screen for the required display-Full screen.

black=(0,0,0) #Graphics, button colours.(rgb colors)
white=(250,250,250)
red=(200,0,0)
green=(0,200,0)
blue=(0,100,130)
yellow=(150,150,0)
purple=(60,0,190)

#load new image from a file.
introduction_background=pygame.image.load("introduction.png") #This image is the loading image of the game introduction.
menu_background=pygame.image.load("menu_background.jpg")
p=pygame.image.load("playing_background.jpg")
board=pygame.image.load("board.jpg") #Loading the board image.
d1=pygame.image.load("d1.jpg") #All the below statements are for the loading of the dice images.
d2=pygame.image.load("d2.jpg")
d3=pygame.image.load("d3.jpg")
d4=pygame.image.load("d4.jpg")
d5=pygame.image.load("d5.jpg")
d6=pygame.image.load("d6.jpg")
red_token=pygame.image.load("red_token.png") #Token images.
yellow_token=pygame.image.load("yellow_token.png")
green_token=pygame.image.load("green_token.png")
blue_token=pygame.image.load("blue_token.png")

mouse=pygame.mouse.get_pos() #function for getting the mouse cursor x, y coordinates.
click=pygame.mouse.get_pressed() #function for getting the state of the mouse buttons.
    
#Message displaying for buttons.
#So there's our message displaying function, 
#we define the large text, then we define the text and the rectangle that would encompass it. 
#We then center the text, using our width and height variables-x,y. 
#Then we blit this stuff to the surface, remembering this only draws it in the background, 
#and that we need to call "pygame.display.update()."
def message_display(text,x,y,fs): #function for Message displaying for field
  largeText=pygame.font.Font('freesansbold.ttf',fs) #create a new Font object from a file.
  TextSurf,TextRect=text_objects1(text,largeText,black)
  TextRect.center=(x,y)
  GD.blit(TextSurf,TextRect)
    
def text_objects1(text,font,colour): 
  textSurface=font.render(text,True,colour)
  return textSurface,textSurface.get_rect()

def button(text,xmouse,ymouse,x,y,width,height,i,fs,b): #Function for the making of PLAY, QUIT, MENU, BACK buttons.
  pygame.draw.rect(GD,i,[x,y,width,height]) #Drawing a rectangle on the screen of the desired colour.
  if x+width>xmouse>x and y+height>ymouse>y: #width and height are the length of and breadth of the rect from the left-top corner 
    #mouse.get_pressed returns a tupple of integer values. (1,0,0)
    if pygame.mouse.get_pressed()==(1,0,0):  #x,y signifies the top-left corner.
      if b==1: #for going from play game to the options menu.
        options()
      elif b==5: #for going from options menu to the PLAY,QUIT menu by pressing back.
        return 5
      elif b==0: #pressing the quit button and exiting the game.
        Quit()
      elif b=="s" or b==2 or b==3 or b==4:
        return b
      elif b==7: #for going from the running game to options menu by pressing back button.
        options()
      else: return True
  message_display(text,(x+width+x)/2,(y+height+y)/2,fs)    

def button1(text,xmouse,ymouse,x,y,width,height,i,fs): #Function for the making of buttons for PLAYER 1, 2, 3, 4 and COMPUTER during gameplay.
  mouse=pygame.mouse.get_pos() #function for getting the mouse cursor position.
  click=pygame.mouse.get_pressed() #function for getting the state of the mouse buttons.
  pygame.draw.rect(GD,i,[x,y,width,height])
  if x+width>xmouse>x and y+height>ymouse>y:
    if pygame.mouse.get_pressed()==(1,0,0):
      return True
  message_display(text,(x+width+x)/2,(y+height+y)/2,fs)

def snakes(x):  #Checking for a snake and returning appropriate position.
  if x==17: return 7
  elif x==54: return 34
  elif x==62: return 19
  elif x==64: return 60
  elif x==87: return 36
  elif x==93: return 73
  elif x==95: return 75
  elif x==98: return 79
  else: return x

def ladders(x): #Checking for a ladder and returning appropriate position.
  if x==1: return 38
  elif x==4: return 14
  elif x==9: return 31
  elif x==28: return 84
  elif x==21: return 42
  elif x==51: return 67
  elif x==80: return 99
  elif x==72: return 91
  else: return x

def dice(a): #Function that displays the appropriate dice image as per the number given by the function randint.
  if a==1:
    a=d1
  elif a==2:
    a=d2
  elif a==3:
    a=d3
  elif a==4:
    a=d4
  elif a==5:
    a=d5
  elif a==6:
    a=d6
  time=pygame.time.get_ticks() #get the time in milliseconds.
  while pygame.time.get_ticks()-time<1200: #displaying the dice for an interval of 1200 milli seconds at a particular co-ordiante.
    GD.blit(a,(140,500))
    pygame.display.update()

def token(a): #Token movement function. Accepts the square number as a parameter and returns its co-ordinates on the screen.
  l1=[[406,606],[456,606],[506,606],[556,606],[606,606],[656,606],[706,606],[756,606],[806,606],[856,606],[906,606],[906,560],[856,560],[806,560],[756,560],[706,560],[656,560],[606,560],[556,560],[506,560],[456,560],[456,506],[506,506],[556,506],[606,506],[656,506],[706,506],[756,506],[806,506],[856,506],[906,506],[906,460],[856,460],[806,460],[756,460],[706,460],[656,460],[606,460],[556,460],[506,460],[456,460],[456,406],[506,406],[556,406],[606,406],[656,406],[706,406],[756,406],[806,406],[856,406],[906,406],[906,360],[856,360],[806,360],[756,360],[706,360],[656,360],[606,360],[556,360],[506,360],[456,360],[456,306],[506,306],[556,306],[606,306],[656,306],[706,306],[756,306],[806,306],[856,306],[906,306],[906,260],[856,260],[806,260],[756,260],[706,260],[656,260],[606,260],[556,260],[506,260],[456,260],[456,206],[506,206],[556,206],[606,206],[656,206],[706,206],[756,206],[806,206],[856,206],[906,206],[906,160],[856,160],[806,160],[756,160],[706,160],[656,160],[606,160],[556,160],[506,160],[456,160]]
  l2=l1[a]
  return l2[0]-25,l2[1]-25 #Compensation of the size of the token.

def introduction():  #for displaying the intoduction image for a required time.
  time=pygame.time.get_ticks()
  while pygame.time.get_ticks()-time<2500:
    GD.blit(introduction_background,(0,0))
    pygame.display.update()

def Quit():     #This function is invoked when one wants to colse or quit the game.
  pygame.quit() #The pygame.quit() function is the opposite of pygame.init()function.It runs code that deactivates the Pygame library  
  quit()        #Its allows the user to exit the code.
  
def main(): #play and quit page (Main Menu)
  while True:
    for event in pygame.event.get():
      if event.type== pygame.KEYDOWN:
        if event.key== pygame.K_ESCAPE: #Escape key can be used to colse and quit the games.
          Quit()
    mouse=pygame.mouse.get_pos()  #mouse positions as per the buttons on screen and user requirements.
    click=pygame.mouse.get_pressed()
    GD.blit(menu_background,(0,0))
    button("PLAY GAME",mouse[0],mouse[1],(width/2-200),height/2-120,400,100,red,60,1)
    button("QUIT",mouse[0],mouse[1],(width/2-100),(height/2)+80,200,100,yellow,60,0)
    pygame.display.update()
        
def options(): #Options Menu.
  while True:
    for event in pygame.event.get():
      if event.type== pygame.KEYDOWN:
        if event.key== pygame.K_ESCAPE: 
          Quit()
    mouse=pygame.mouse.get_pos() #mouse position
    click=pygame.mouse.get_pressed()
    b1=b2=b3=b4=b5=-1
    GD.blit(menu_background,(0,0))
    b1=button("1 PLAYER",mouse[0],mouse[1],(width/2-136),250,272,50,red,30,"s") #Single player button
    b2=button("2 PLAYERS",mouse[0],mouse[1],(width/2)-150,350,300,50,yellow,30,2) #2 player button
    b3=button("3 PLAYERS",mouse[0],mouse[1],(width/2)-150,450,300,50,green,30,3) #3 player button
    b4=button("4 PLAYERS",mouse[0],mouse[1],(width/2)-150,550,300,50,blue,30,4) #4 player button
    b5=button("BACK",mouse[0],mouse[1],0,650,200,50,purple,30,5) #Back button
    if b5==5:
      main()
    if b1=="s":
      play(21)
    if b2==2:
      play(2)
    if b3==3:
      play(3)
    if b4==4:
      play(4)
    pygame.display.update()

def turn(score,l,s):
  a=randint(1,6) #player dice roll. random number generator.
  if a==6: #if the player gets 6 on dice roll then we need to give him another chance, thats why turn function returns six as well.
    six=True
  else:
    six=False
  p=dice(a) #an image
  score+=a
  if score<=100: #checking if the player is in the game or has won the game all-together.
    lad=ladders(score) #checking for ladders for player
    if lad!=score:
      l=True
      score=lad 
    snk=snakes(score)
    if snk!=score: #checking for snakes for player
      s=True
      score=snk      
  else: #checks if player score is not greator than 100
    score-=a
    time=pygame.time.get_ticks() #get the time in milliseconds
    while pygame.time.get_ticks()-time<1000: #Get the below message displayed for 1500 milli seconds.
      message_display("Can't move!",650,50,35) #If the player gets a score which takes him above 100 hewillnotbeabletomove.
      pygame.display.update()
  return score,l,s,six
 
def play(number_of_players): #Main game play function takes the number of players as a parameter.
  GD.blit(p,(0,0)) #displaying of the playing background image.
  GD.blit(board,(width/2-250,height/2-250)) #Displaying the game board.
  xcr=381
  xcy=381-25 # 50 is the diameter of the token.
  xcg=381-50
  xcb=381-75 #initial x co-ordinates of the tokens.
  ycr=ycy=ycg=ycb=581 #initial y co-ordiantes of the tokens.
  GD.blit(red_token,(xcy,ycy)) #Displaying the red token at the desired position on the screen.
  if 5>number_of_players>1 or number_of_players==21: #number of players is 2 ie. 2 real players or 1 player and 1 computer.
    GD.blit(yellow_token,(xcy,ycy)) #at least there is a need of 2 tokens in the game anyhow.   
  if 5>number_of_players>2: #3 real players
    GD.blit(green_token,(xcg,ycg)) #there is a need of 3rd token.
  if 5>number_of_players>3: #4 real player
    GD.blit(blue_token,(xcb,ycb)) #there is a need of 4th token.
  p1="PLAYER-1"
  p1score=0
  if number_of_players==21:
    p2="COMPUTER"
    p2score=0
  if 5>number_of_players>1:
    p2="PLAYER-2"
    p2score=0
  if 5>number_of_players>2:
    p3="PLAYER-3"
    p3score=0
  if 5>number_of_players>3:
    p4="PLAYER-4"
    p4score=0
  t=1
  while True:
    l=False
    s=False
    GD.blit(p,(0,0))
    GD.blit(board,(width/2-250,height/2-250))
    mouse=pygame.mouse.get_pos()
    for event in pygame.event.get(): 
      if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_ESCAPE:
          Quit()
    if number_of_players==21:
      if button1("PLAYER-1",mouse[0],mouse[1],100,700,200,50,red,30):
        if t==1:
          p1score,l,s,six=turn(p1score,l,s)
          if not six:
            t+=1
          xcr,ycr=token(p1score)
          if p1score==100:
            time=pygame.time.get_ticks()
            while pygame.time.get_ticks()-time<2000:
              message_display("PLAYER 1 WINS THE GAME",650,50,50)
              pygame.display.update()
            break
      button1("COMPUTER",mouse[0],mouse[1],400,700,200,50,yellow,30)
      if True:
        if t==2:
          p2score,l,s,six=turn(p2score,l,s)
          xcy,ycy=token(p2score)
          if not six:
            t+=1
            if number_of_players<3 or number_of_players==21:
              t=1
          if p2score==100:
            time=pygame.time.get_ticks()
            while pygame.time.get_ticks()-time<2000:
              message_display("Computer WINS",650,50,50)
              pygame.display.update()
            break
    if 5>number_of_players>1:
      if button1("PLAYER-1",mouse[0],mouse[1],100,700,200,50,red,30):
        if t==1:
          p1score,l,s,six=turn(p1score,l,s)
          xcr,ycr=token(p1score)
          if not six:
            t+=1
          if p1score==100:
            time=pygame.time.get_ticks()
            while pygame.time.get_ticks()-time<2000:
              message_display("Player 1 WINS",650,50,50)
              pygame.display.update()
            break 
      if button1("PLAYER-2",mouse[0],mouse[1],400,700,200,50,yellow,30):
        if t==2:
          p2score,l,s,six=turn(p2score,l,s)
          xcy,ycy=token(p2score)
          if not six:
            t+=1
            if number_of_players<3:
              t=1
          if p2score==100:
            time=pygame.time.get_ticks()
            while pygame.time.get_ticks()-time<2000:
              message_display("Player 2 WINS",650,50,50)
              pygame.display.update()
            break        
    if 5>number_of_players>2:
      if button1("PLAYER-3",mouse[0],mouse[1],700,700,200,50,green,30):
        if t==3:
          p3score,l,s,six=turn(p3score,l,s)
          xcg,ycg=token(p3score)
          if not six:
            t+=1
            if number_of_players<4:
              t=1
          if p3score==100:
            time=pygame.time.get_ticks()
            while pygame.time.get_ticks()-time<2000:
              message_display("Player 3 WINS",650,50,50)
              pygame.display.update()
            break            
    if 5>number_of_players>3:   
      if button1("PLAYER-4",mouse[0],mouse[1],1000,700,200,50,blue,30):
        if t==4:
          p4score,l,s,six=turn(p4score,l,s)
          xcb,ycb=token(p4score)
          if not six:
            t+=1
            if number_of_players<5:
              t=1
          if p4score==100:
            time=pygame.time.get_ticks()
            while pygame.time.get_ticks()-time<2000:
              message_display("Player 4 WINS",650,50,50)
              pygame.display.update()
            break
    b6=button("BACK",mouse[0],mouse[1],0,0,200,50,purple,30,7)
    GD.blit(red_token,(xcr,ycr))
    if 5>number_of_players>1 or number_of_players==21:
      GD.blit(yellow_token,(xcy+2,ycy))   
    if 5>number_of_players>2:
      GD.blit(green_token,(xcg+4,ycg)) 
    if 5>number_of_players>3:
      GD.blit(blue_token,(xcb+6,ycb))
    if l:
      time=pygame.time.get_ticks()
      while pygame.time.get_ticks()-time<1650:
        message_display("Oh YEAAAA!!! There is a LADDER",650,50,35)
        pygame.display.update()
    if s:
      time=pygame.time.get_ticks()
      while pygame.time.get_ticks()-time<1650:
        message_display("Oh NOOO!!! There is a SNAKE",650,50,35)
        pygame.display.update()
    pygame.display.update()
      
introduction()    
main()
