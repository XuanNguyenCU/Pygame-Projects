import sys
import pygame


def main():
    img = pygame.image.load(sys.argv[1])
    img_rect = img.get_rect()
    imgLength = img.get_width()
    imgHeight = img.get_height()

    surface = pygame.display.set_mode((imgLength, imgHeight))
    surface.blit(img, img_rect)

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False


            if event.type == pygame.MOUSEBUTTONDOWN:
                x = tuple(pygame.mouse.get_pos())


            if event.type == pygame.MOUSEBUTTONUP:
                y = tuple(pygame.mouse.get_pos())
                xPos = abs(x[0]-y[0])
                yPos = abs(x[1]-y[1])

                difference = y[0] - x [0]

                if(difference < 0):
                    tmp = y
                    y = x
                    x = tmp

                for i in range(xPos):
                    for j in range(yPos):
                        color = tuple(surface.get_at((x[0] + i, x[1] + j)))
                        newColor = (255-color[0], 255-color[1], 255-color[2])
                        pygame.draw.rect(surface, newColor, pygame.Rect(x[0]+i, x[1]+j, 1, 1))   
                        
        pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


if __name__ == "__main__":
    main()