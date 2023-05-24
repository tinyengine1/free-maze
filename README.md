# 3D ASCII Raycaster Engine "free-maze"

A basic 3D ASCII Raycaster engine made in Python.

The 3D ASCII Raycaster Engine is a Python-based rendering engine that creates a pseudo-3D effect using ASCII art. This engine allows you to navigate through a predefined maze using the WASD keys, providing a nostalgic and immersive experience reminiscent of early computer games.

#### Watch the [official demo gameplay video](https://www.youtube.com/watch?v=gOGdCZ24sSE).

## Features

- Simple and intuitive navigation through the maze using the WASD keys.
- Pseudo-3D rendering using ASCII characters, creating a retro visual style.
- Basic collision detection to prevent movement through walls.
- Raycasting technique to calculate the distance to walls and determine their height on the screen.
- Real-time rendering with adjustable field of view for a customizable viewing experience.
- Basic frustum culling to optimize rendering by only displaying visible walls.
- Compatibility with various operating systems, including Windows, macOS, and Linux.

## Getting Started

Prerequisites
The 3D ASCII Raycaster Engine is a self-contained program that automatically handles its library dependencies. You do not need to install any additional libraries manually. However, please ensure you have Python 3.x with PATH installed on your system.

This means that when you run the program for the first time, it will automatically check for the required libraries and install them if they are not already present on your system. This ensures a seamless setup process and eliminates the need for manual library installation.

Please note that an active internet connection is required during the initial setup to download and install any necessary libraries.

Once again, you can simply run the program without worrying about installing any additional libraries manually.

The program uses the following libraries:

- importlib
- math
- numpy
- keyboard
- os
- time
- traceback
- random

To install the required libraries manually, run `pip install numpy keyboard` in your terminal, the others are built-in Python.

## License

The 3D ASCII Raycaster Engine is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

This means you are free to:

- Share: Copy and redistribute the program in any medium or format.
- Adapt: Remix, transform, and build upon the program for any purpose.

Under the following conditions:

- Attribution: You must give appropriate credit, provide a link to the license, and indicate if changes were made.
- ShareAlike: If you remix, transform, or build upon the program, you must distribute your contributions under the same license as the original.

For more details about the license, please refer to the [license](LICENSE.md) file.


# Latest update
### Version 1.1
- Improved maps.
- Hopefully fixed an error where the game would crash when a player walked through a corner.
