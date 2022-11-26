# Water Sort Puzzle Solver

Been stuck on level 107 for a couple days, so the most intuitive next step is to make a script and ruin the game for myself. If you want to ruin the game for yourself too, help yourself. Here is the [water sort puzzle game](https://play.google.com/store/apps/details?id=com.gma.water.sort.puzzle&hl=en_US&gl=US).

## Usage:
1. Enter the game state into `main.py`.

2. 
```
python main.py
```

## How to interpret answer
The ai will return a list of moves to perform from your current state, where each tuple is (source vial index, destination vial index). This is normally not very user-friendly (neither is the game-state-entering part), but it's designed for the frustrated, and the frustrated can be quite persistent.
