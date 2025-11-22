# GENOCIDE FLOWEY — Undertale Fan Game

An experimental Undertale-inspired fan game built in Python with pygame.<br>
**You play through a dark AU, facing Lord Flowey.**

---

## Running

1. **Install requirements:**
    ```
    pip install pygame
    ```

2. **Download or clone the repo,** put your art/music in `assets/`, then run:
    ```
    python main.py
    ```

## How to Expand

- Replace the placeholder art in `main.py` with your own PNG sprites, e.g.:
  ```
  flowey_sprite = pygame.image.load("assets/flowey.png").convert_alpha()
  ```
- Expand each scene class for story details or dialogue.
- Build a battle system in `LordFloweyBattle`.
- Add title screen, save/load, etc!

## Credits

Inspired by Undertale by Toby Fox.
Fan project for learning, not for commercial use.

## Folders

- `assets/` — Place all art/music here!
