# This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

import importlib

def check_package(package_name):
    try:
        importlib.import_module(package_name)
        print(f"{package_name} is already installed.")
    except ImportError:
        print(f"{package_name} is not installed.")
        choice = input("Do you want to install it? (y/n): ")
        if choice.lower() == 'y':
            install_package(package_name)
        else:
            print("Package not installed.")

def install_package(package_name):
    try:
        import subprocess
        subprocess.check_call(['pip', 'install', package_name])
        print(f"{package_name} has been successfully installed.")
    except Exception as e:
        print(f"Failed to install {package_name}: {str(e)}")

# Check if packages are installed
packages = ['numpy', 'keyboard', 'os', 'time', 'traceback']

for package in packages:
    check_package(package)


import math
import numpy as np
import keyboard
import os
import time
import traceback
import random

time.sleep(1)

def main():
    # Define the labyrinths
    labyrinths = [
    [
        "#################",
        "#.............###",
        "#.#####.#####..#",
        "#.#...#........#",
        "#.#.###.######.#",
        "#.#............#",
        "#.############.#",
        "#..............#",
        "################"
    ],
    [
        "###################",
        "#...............##",
        "#.####...#########",
        "#.#.............##",
        "#.#..####...######",
        "#.#.............##",
        "#.#####.....######",
        "#...............##",
        "#################"
    ],
    [
        "##################",
        "#.............###",
        "#.#########.....#",
        "#.#.............#",
        "#.#.#############",
        "#.#.............#",
        "#.########..###.#",
        "#...............#",
        "#################"
    ],
    [
        "##################",
        "#.......#########",
        "#.#.#############",
        "#.#.............#",
        "#.#.#############",
        "#.#.............#",
        "#.###...#########",
        "#...............#",
        "#################"
    ],
    [
        "#################",
        "#...............#",
        "#.#########.....#",
        "#.#.............#",
        "#.#.###########.#",
        "#.#.............#",
        "#.#########.#####",
        "#...............#",
        "#################"
    ]
]
    
    # If you're reading this, you're a curious one. Keep exploring!
    print(" ")
    labyrinth = random.choice(labyrinths)
    print("Preloading map...")
    print(" ")
    for row in labyrinth:
        print(''.join(row))
    print(" ")
    print("Launching engine...")
    time.sleep(1)
    print("Ready")

    # Player position and direction
    player_x = 1.5
    player_y = 1.5
    player_dir = 0.0

    # Screen settings
    screen_width = 120
    screen_height = 28

    # Field of view (in radians)
    fov = math.pi / 3

    # Frustum culling parameters
    near_plane = 0.1
    far_plane = 10.0

    # Shading symbols for walls based on distance
    shading_symbols = ['█', '▓', '▒', '░']

    # Function to handle continuous movement
    def handle_movement():
        nonlocal player_x, player_y, player_dir
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

            # Calculate shading symbol based on distance
            symbol_index = min(int(distance_to_wall) // 2, len(shading_symbols) - 1)
            shading_symbol = shading_symbols[symbol_index]

            # Draw the wall segment
            for y in range(wall_top, wall_bottom + 1):
                screen[y, x] = shading_symbol

        # Build the complete frame as a string
        frame = '\n'.join([''.join(row) for row in screen])

        # Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')

        # Print the frame
        print(frame)
        print("FREE-MAZE DEMO GAMEPLAY - W, A, S, D to walk, Q to quit.")

        # Handle movement
        handle_movement()

        # Break the rendering loop if 'q' is pressed
        if keyboard.is_pressed('q'):
            break

        # Add a small delay to reduce screen tearing
        time.sleep(0.005)
    # Programmers never die; they just go offline.

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # Print the error traceback
        traceback.print_exc()

        # Prevent the program from immediately closing
        print(" ")
        print("An error occured.")
        print("Please create an issue on github for it to be fixed.")
        print(" ")
        time.sleep(2)
        if os.name == 'nt':
            os.system('pause')
        else:
            os.system('read -p "Press Enter to continue...')
