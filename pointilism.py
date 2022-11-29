import pygame
import sys
import random


def main():

    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)

    # importing the image
    image_name = sys.argv[1]
    src_image = pygame.image.load(image_name)


    (w,h) = src_image.get_size()
    surface = pygame.display.set_mode((w,h))


    for y in range(h):
        for x in range(w):

            # Iterate through each pixel to get the color (rgb) value 
            (r, g, b, _) = src_image.get_at((x,y))

            num_red, num_green, num_blue = r // 50, g // 50, b // 50
            
            # Initialize the color values as lists
            # Sstore the RGB value relating to number of cicles for each corresponding color
            red_color,green_color, blue_color = [],[],[]
            for r in range(num_red): 
                red_color += [RED]
        
            for g in range(num_green): 
                green_color += [GREEN]

            for b in range(num_blue): 
                blue_color += [BLUE]

            # Divides each color evenly, doesn't create any overlap of one color
            colors = red_color + green_color + blue_color 
            random.shuffle(colors)

            for c in colors: 
                pygame.draw.circle(surface,c,(random.randint((x)-6,(x)), random.randint((y)-6, (y))), 1)


    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()	

                

if __name__ == "__main__":
    main()