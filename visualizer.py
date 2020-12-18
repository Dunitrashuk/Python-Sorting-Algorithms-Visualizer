import pygame
import random


ARRAY_SIZE = 79
STEP = 10
WHITE = (255, 255, 255)
PINK = (255, 105, 180)
PINK_2 = (219,112,147)
GREY = (211,211,211)
BLUE = (240,248,255)
DARK_GREY = (128,128,128)
BLACK = (0, 0, 0)
inf = 0
sup = 78


def fill_array(maximum):  
    global array
    array = []
    for i in range(ARRAY_SIZE):
        array.append(random.randint(0, maximum))

def draw_array(tick_time = 0):
    global array
    pygame.draw.rect(screen, WHITE, (0, 0, 800, 540))
    STEP = 10
    for i in array:
        pygame.draw.line(screen, PINK_2, (STEP,530-i), (STEP,530), 3)
        STEP += 10
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if tick_time:
        clock.tick(tick_time)

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac):
    mouse = pygame.mouse.get_pos()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y and pygame.mouse.get_pressed()[0]:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if msg == "Generate":
            fill_array(500)
            draw_array()
        if msg == "Bubble":
            bubbleSort() 
        if msg == "Selection":
            selectionSort()
        if msg == "Insertion":
            insertionSort()
        if msg == "QuickSort":
            quickSort(inf, sup)

    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",18)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def partition(low, high): 
    i = ( low-1 )          
    pivot = array[high]      
  
    for j in range(low , high):  
        if array[j] <= pivot: 
            i = i+1 
            array[i],array[j] = array[j],array[i] 
            draw_array(80)
  
    array[i+1],array[high] = array[high],array[i+1] 
    return ( i+1 ) 
   
def quickSort(low, high): 
    
    if low < high: 
  
        pi = partition(low,high) 
        draw_array(80)
        quickSort(low, pi-1)
        draw_array(80) 
        quickSort(pi+1, high)
        draw_array(80) 

def bubbleSort():
    global array
    n = len(array)

    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
            draw_array()
            button("Bubble", 680, 540, 100, 50, GREY, DARK_GREY)
           
def selectionSort():
    global array
    for i in range(len(array)): 
        min_idx = i 
        for j in range(i+1, len(array)): 
            if array[min_idx] > array[j]: 
                min_idx = j 
            draw_array()
                
        array[i], array[min_idx] = array[min_idx], array[i]
    draw_array(100)
    button("Selection", 540, 540, 100, 50, GREY, DARK_GREY)
        
def insertionSort(): 
    global array

    for i in range(1, len(array)): 
        key = array[i] 
        j = i - 1
        while j >= 0 and key < array[j] : 
                array[j+1] = array[j] 
                j -= 1
                draw_array(550)
        array[j + 1] = key 
        


pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

done = False
clock = pygame.time.Clock()
screen.fill(WHITE)

array = []
fill_array(500)


while not done:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fill_array(500)
                draw_array()
            if event.key == pygame.K_b:
                bubbleSort()
            if event.key == pygame.K_i:
                insertionSort()
            if event.key == pygame.K_s:
                selectionSort()
            if event.key == pygame.K_q:
                quickSort(inf, sup)
                
    
    mouse = pygame.mouse.get_pos()
    #print(mouse) 

    button("Generate", 25, 540, 100 , 50, GREY, DARK_GREY)
    button("QuickSort", 260, 540, 100 , 50, GREY, DARK_GREY)
    button("Insertion", 400, 540, 100, 50, GREY, DARK_GREY) 
    button("Selection", 540, 540, 100, 50, GREY, DARK_GREY) 
    button("Bubble", 680, 540, 100, 50, GREY, DARK_GREY) 

    pygame.display.flip()
    clock.tick(60)    

pygame.quit() 


