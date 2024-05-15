import pygame
import random
import math
import time
import os

# Defining colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Setting up display
WIDTH = 800
HEIGHT = 600
BAR_WIDTH = 4  # Bar width for spacing
GAP = 1  # Gap between bars

# Initializing pygame and mixer
pygame.init()
pygame.mixer.init()

def bubble_sort(arr, screen, clock, font):
    n = len(arr)
    comparisons = 0
    accesses = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            accesses += 2
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                accesses += 4
                update_screen(screen, arr, j, j + 1, comparisons, accesses, font)
                clock.tick(1200)  # The speed of the animation
        
        # Turning the last sorted element green, then back to white
        update_screen(screen, arr, -1, n - i - 1, comparisons, accesses, font, GREEN)
        pygame.time.wait(100)  # Waiting for a short time to show the green bar
        update_screen(screen, arr, -1, n - i - 1, comparisons, accesses, font, WHITE)

    # Final verification pass
    for i in range(n):
        update_screen(screen, arr, -1, i, comparisons, accesses, font, GREEN)
        pygame.time.wait(5)  # Smooth movement of the green bar
        update_screen(screen, arr, -1, i, comparisons, accesses, font, WHITE)

    pygame.quit()
    exit()

def update_screen(screen, arr, idx1, idx2, comparisons, accesses, font, color_override=None):
    screen.fill(BLACK)
    for i in range(len(arr)):
        if color_override is not None and i == idx2:
            color = color_override
        else:
            color = RED if i == idx1 else WHITE
        pygame.draw.rect(screen, color, (i * (BAR_WIDTH + GAP), HEIGHT - arr[i], BAR_WIDTH, arr[i]))

    # Rendering statistics text
    comparisons_text = font.render(f"Comparisons: {comparisons}", True, WHITE)
    accesses_text = font.render(f"Array Accesses: {accesses}", True, WHITE)

    # Drawing statistics text
    screen.blit(comparisons_text, (10, 10))
    screen.blit(accesses_text, (10, 30))

    pygame.display.flip()

def create_geometric_array(n, min_height, max_height):
    ratio = (min_height / max_height) ** (1 / (n - 1))
    arr = [int(max_height * (ratio ** i)) for i in range(n)]
    return arr

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("BUBBLE SORT - SOHEIL")
    clock = pygame.time.Clock()

    n = WIDTH // (BAR_WIDTH + GAP)  # Adjust number of bars to account for gap
    max_height = HEIGHT
    min_height = max_height * 0.01  # The smallest bar is 1% the height of the tallest bar

    arr = create_geometric_array(n, min_height, max_height)
    random.shuffle(arr)  # Shuffling the array to create an unsorted state

    # Setting up font for displaying statistics
    font = pygame.font.SysFont('Arial', 18)

    running = True
    sorting = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not sorting:
            sorting = True
            bubble_sort(arr, screen, clock, font)
            sorting = False

        update_screen(screen, arr, -1, -1, 0, 0, font)

    pygame.quit()

if __name__ == "__main__":
    main()