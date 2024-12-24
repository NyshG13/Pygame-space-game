import pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Test")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((100, 100, 55))  # Fill the screen with Red, Green, Blue tuple 
    pygame.display.flip()    # Update the display

pygame.quit()

import pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drawing Shapes")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw shapes
    pygame.draw.rect(screen, RED, (50, 50, 200, 100))  # Red rectangle
    pygame.draw.circle(screen, GREEN, (400, 300), 50)  # Green circle
    pygame.draw.line(screen, BLUE, (0, 0), (800, 600), 5)  # Blue line

    pygame.display.flip()  # Update the screen

pygame.quit()


import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Drawing with Turtle")

# Create a turtle object
pen = turtle.Turtle()
pen.color("blue")
pen.pensize(3)

# Draw a square
for _ in range(4):
    pen.forward(100)
    pen.left(90)

# Keep the window open until clicked
screen.mainloop()
