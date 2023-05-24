import math
import numpy as np
import keyboard
import os
import time
import random

# Predefined mazes
predefined_mazes = [
    [
        ['█', '█', '█', '█', '█', '█', '█'],
        ['█', ' ', ' ', ' ', ' ', ' ', '█'],
        ['█', ' ', '█', ' ', '█', ' ', '█'],
        ['█', ' ', '█', ' ', '█', ' ', '█'],
        ['█', ' ', ' ', ' ', ' ', ' ', '█'],
        ['█', ' ', '█', '█', '█', ' ', '█'],
        ['█', ' ', ' ', ' ', ' ', ' ', '█'],
        ['█', '█', '█', '█', '█', '█', '█'],
    ],
    [
        ['█', '█', '█', '█', '█', '█', '█'],
        ['█', ' ', ' ', ' ', ' ', ' ', '█'],
        ['█', '█', ' ', '█', '█', ' ', '█'],
        ['█', ' ', ' ', ' ', '█', ' ', '█'],
        ['█', ' ', '█', ' ', ' ', ' ', '█'],
        ['█', ' ', ' ', ' ', '█', ' ', '█'],
        ['█', ' ', '█', ' ', ' ', ' ', '█'],
        ['█', '█', '█', '█', '█', '█', '█'],
    ],
    [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '█', ' ', '█', ' ', ' '],
        [' ', ' ', '█', ' ', '█', ' ', ' '],
        [' ', ' ', '█', ' ', '█', ' ', ' '],
        [' ', ' ', '█', ' ', '█', ' ', ' '],
        [' ', ' ', '█', ' ', '█', ' ', ' '],
        [' ', ' ', '█', ' ', '█', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]
    # Add more predefined mazes here...
]


# Function to choose a random maze
def choose_random_maze():
    return random.choice(predefined_mazes)

# Define the labyrinth size
labyrinth_width = 7
labyrinth_height = 8

# Generate the random labyrinth
labyrinth = choose_random_maze()

# Player position and direction
player_x = 1.5
player_y = 1.5
player_dir = 0.0

# Screen settings
screen_width = 70
screen_height = 30

# Field of view (in radians)
fov = math.pi / 3

# Shading symbols for walls based on distance
shading_symbols = ['█', '▓', '▒', '░']

# Function to handle continuous movement
def handle_movement():
    global player_x, player_y, player_dir
    if keyboard.is_pressed('w'):
        new_x = player_x + math.cos(player_dir) * 0.1
        new_y = player_y + math.sin(player_dir) * 0.1
        if labyrinth[int(new_y)][int(new_x)] == ' ':
            player_x = new_x
            player_y = new_y
    if keyboard.is_pressed('a'):
        player_dir -= 0.1
    if keyboard.is_pressed('s'):
        new_x = player_x - math.cos(player_dir) * 0.1
        new_y = player_y - math.sin(player_dir) * 0.1
        if labyrinth[int(new_y)][int(new_x)] == ' ':
            player_x = new_x
            player_y = new_y
    if keyboard.is_pressed('d'):
        player_dir += 0.1

# Rendering loop
while True:
    # Create a blank screen
    screen = np.full((screen_height, screen_width), ' ')

    for x in range(screen_width):
        ray_angle = (player_dir - (fov / 2)) + (x / screen_width) * fov

        # Raycast
        ray_x = player_x
        ray_y = player_y
        ray_dir_x = math.cos(ray_angle)
        ray_dir_y = math.sin(ray_angle)

        distance_to_wall = 0
        hit_wall = False

        while not hit_wall and distance_to_wall < 10:
            distance_to_wall += 0.1
            test_x = int(ray_x + ray_dir_x * distance_to_wall)
            test_y = int(ray_y + ray_dir_y * distance_to_wall)

            if test_x < 0 or test_x >= len(labyrinth[0]) or test_y < 0 or test_y >= len(labyrinth):
                hit_wall = True
                distance_to_wall = 10  # Max rendering distance
            elif labyrinth[test_y][test_x] == '█':
                hit_wall = True

        # Calculate wall height
        wall_height = int(screen_height / distance_to_wall)

        # Draw the wall segment
        ceiling = int(screen_height / 2) - int(wall_height / 2)
        floor = screen_height - ceiling
        for y in range(screen_height):
            if y <= ceiling:
                screen[y, x] = ' '
            elif y > ceiling and y <= floor:
                # Apply shading based on distance
                shading_index = min(int(distance_to_wall) - 1, len(shading_symbols) - 1)
                screen[y, x] = shading_symbols[shading_index]
            else:
                screen[y, x] = ' '



    # Print the frame
    print("FREE-MAZE GAMEPLAY BETA")
    for row in screen:
        print(''.join(row))


    # Handle movement
    handle_movement()


    # Break the rendering loop if 'q' is pressed
    if keyboard.is_pressed('q'):
        break

    # Add a small delay to reduce screen tearing
    time.sleep(0.032)
