# Example file showing a basic pygame "game loop"
import pygame

# pygame setups
pygame.init()

WINDOW_WIDTH = 800 
PIXEL_WIDTH = WINDOW_WIDTH // 3

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
clock = pygame.time.Clock()
running = True

board = [
    [None,None,None],
    [None,None,None],
    [None,None,None]
    ]    


font = pygame.font.Font('freesansbold.ttf', 32)
text=font.render("",True,"green")
textRect=text.get_rect()
textRect.center=(WINDOW_WIDTH // 2 - PIXEL_WIDTH // 2, WINDOW_WIDTH // 2)

player1 = 0
player2 = 1
player = player1

def load_icons(path,resolution):
    icon = pygame.image.load(path)
    return pygame.transform.scale(icon, resolution)

grid=load_icons('img/grid.png',[WINDOW_WIDTH,WINDOW_WIDTH])
iconX=load_icons('img/x-icon.png',[WINDOW_WIDTH//3,WINDOW_WIDTH//3])
iconO=load_icons('img/o-icon.png',[WINDOW_WIDTH//3,WINDOW_WIDTH//3])
 
def play_turn(current_player):
     current_coordinate = pygame.math.Vector2(pygame.mouse.get_pos())//PIXEL_WIDTH 
     if  pygame.mouse.get_pressed()[0]:
        col, row = map(int, current_coordinate)
        board[row][col] = current_player
        global player
        player = 1 - player
         
def draw_icons():
    for i,row in enumerate(board):
        for j,col in enumerate(board[i]):
            if board[i][j] == 0:
                screen.blit(iconX,(j*PIXEL_WIDTH,i*PIXEL_WIDTH))
            elif board[i][j] == 1:
                screen.blit(iconO,(j*PIXEL_WIDTH,i*PIXEL_WIDTH))

def has_equal_icons(elements, game_player):
    for element in elements:
        if element != game_player:
            return False
    return True
 
def is_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]): ##row
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]): ##col
            return True
    if all([board[i][i] == player for i in range(3)]): ##diagonal
        return True
    if all([board[i][2-i] == player for i in range(3)]): ##diagonal
        return True
    return False
                 
def check_victory():
    global text
    if is_winner(board, player1):
        text=font.render("Player 1 wins",True,"green")
        return True
    if is_winner(board, player2):
        text=font.render("Player 2 wins",True,"green")
        return True
    else :
        text=font.render("Draw",True,"Red")
        return False
 
def reset_game():
    global board, player
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
    player = player1

               
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    # RENDER YOUR GAME HERE
    # flip() the display to put your work on screen
    pygame.display.flip()
    screen.fill("white")
    
    screen.blit(grid,(0,0)) 
    pygame.event.wait()
    play_turn(player)
    draw_icons()
    clock.tick(60)  # limits FPS to 60
    if check_victory():
        screen.blit(text,textRect)
        pygame.time.wait(2000)  # Wait for 2 seconds
        reset_game()
    # screen.blit(iconX,(0,0))
    # screen.blit(iconO,(WINDOW_WIDTH//3,WINDOW_WIDTH//3))
    
pygame.quit()