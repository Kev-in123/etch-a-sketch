
import pygame

def main():
    pygame.init()
    win = pygame.display.set_mode((1500,750))
    white = (255, 255, 255)
    win.fill(white)
    x, y, vel = 750, 375, 1

    while True:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:    
              return

        keys = pygame.key.get_pressed()
       
        if keys[pygame.K_LEFT] and x > 0:
          x -= vel
      
        if keys[pygame.K_RIGHT] and x < 1500-1:
          x += vel
        
        if keys[pygame.K_UP] and y > 0:
          y -= vel
                
        if keys[pygame.K_DOWN] and y < 750-1:
          y += vel
                    
        pygame.draw.rect(win, (0, 0, 0), (x, y, 1, 1))
            
        pygame.display.update() 
    
    pygame.quit()


if __name__ =='__main__':
    main()
