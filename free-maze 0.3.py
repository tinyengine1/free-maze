import math
import numpy as np
import keyboard
import os
import time

# Define the labyrinth
labyrinth = [
    "#########",
    "#.......#",
    "#.###...#",
    "#...#...#",
    "#.....###",
    "#.......#",
    "#########"
]

# Player position and direction
player_x = 1.5
player_y = 1.5
player_dir = 0.0

# Screen settings
screen_width = 80
screen_height = 40

# Field of view (in radians)
fov = math.pi / 3

# Frustum culling parameters
near_plane = 0.1
far_plane = 10.0

# Function to handle continuous movement
def handle_movement():
    global player_x, player_y, player_dir
    if keyboard.is_pressed('w'):
        new_x = player_x + math.cos(player_dir) * 0.1
        new_y = player_y + math.sin(player_dir) * 0.1
        if labyrinth[int(new_y)][int(new_x)] == '.':
            player_x = new_x
            player_y = new_y
    if keyboard.is_pressed('a'):
        player_dir -= 0.1
    if keyboard.is_pressed('s'):
        new_x = player_x - math.cos(player_dir) * 0.1
        new_y = player_y - math.sin(player_dir) * 0.1
        if labyrinth[int(new_y)][int(new_x)] == '.':
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

        while not hit_wall and distance_to_wall < far_plane:
            distance_to_wall += 0.1
            test_x = int(ray_x + ray_dir_x * distance_to_wall)
            test_y = int(ray_y + ray_dir_y * distance_to_wall)

            if test_x < 0 or test_x >= len(labyrinth[0]) or test_y < 0 or test_y >= len(labyrinth):
                hit_wall = True
                distance_to_wall = far_plane  # Max rendering distance
            elif labyrinth[test_y][test_x] == '#':
                hit_wall = True

        # Perform 2D AABB checking for visible surface determination
        wall_height = int(screen_height / distance_to_wall)
        wall_top = int(screen_height / 2 - wall_height / 2)
        wall_bottom = int(screen_height / 2 + wall_height / 2)

        # Frustum culling
        if wall_top < 0:
            wall_top = 0
        if wall_bottom >= screen_height:
            wall_bottom = screen_height - 1

        # Draw the wall segment
        for y in range(wall_top, wall_bottom + 1):
            screen[y, x] = '#'

    # Draw the player
    screen[int(player_y), int(player_x)] = 'P'

    # Build the complete frame as a string
    frame = '\n'.join([''.join(row) for row in screen])

    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Print the frame
    print(frame)

    # Handle movement
    handle_movement()

    # Break the rendering loop if 'q' is pressed
    if keyboard.is_pressed('q'):
        break

    # Add a small delay to reduce screen tearing
    time.sleep(0.03)
