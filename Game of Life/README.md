# Conway's Game of Life (In the Terminal)

This is a Python implementation of John Conway's Cellular Automata "game" the Game of Life. This game evolves based upon the initial starting conditions of the board and iteratively creates the next position on the board. The rules of the game are relatively simple, and can be found on the [Wikipedia Article](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) linked here. This implementation wraps around the edge, so the game is really played on a Torus, not an Disc topologically.

## Use
1. Ensure you have Python 3.x installed
2. Clone the repository and run:

```bash
python3 game_of_life.py
```

3. The script will prompt you for dimensions and delay of the grid, then it will print the board to terminal every delay ms until you Keyboard Interrupt with ctrl+C or cmd+C on Mac


## Features

- Grid-based simulation using a 2D list
- Simple visualization in the terminal
- Adjustable delay between generations
- Rule based evolution

## Future Improvements
- Allow custom game states to start with using an interactive GUI for now such edits must be made within the script

## Example of Running it


https://github.com/user-attachments/assets/c45bacb2-6460-4eea-94ea-8508ec8c659f

