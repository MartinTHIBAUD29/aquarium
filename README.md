# Aquarium Simulation

A real-time aquarium simulation built with Python and pygame, featuring emergent flocking behaviour based on the classic **Boids algorithm**.

## Features

- **Fish flocking** — Fish exhibit collective movement through three Boids rules: cohesion, separation, and alignment.
- **Sharks** — Sharks chase the nearest fish; fish detect sharks and flee at increased speed.
- **Food** — Drop food into the tank; nearby fish abandon flocking to chase it.
- **Spatial grid** — Neighbor lookups use a spatial grid partition to reduce per-frame computation.
- **Interactive controls** — Spawn new entities at runtime without pausing the simulation.

## Project Structure

```
aquarium/
+-- main.py                  # Entry point — initialises pygame and runs the main loop
+-- requirements.txt
+-- scripts/
    +-- aquarium.py          # Aquarium container: manages fish, food, and simulation steps
    +-- boid_system.py       # Cohesion, separation, and alignment rule calculations
    +-- creature.py          # Base class for all entities (position, speed, wall avoidance)
    +-- fish.py              # Fish behaviour: flocking, fear, food-seeking
    +-- food.py              # Food entity
    +-- parent_system.py     # Shared helpers for BoidSystem and SharkSystem
    +-- sharks.py            # Shark behaviour: chasing fish
    +-- sharks_system.py     # Shark-specific calculations (chase, eating)
    +-- spatial_grid.py      # Grid-based spatial partitioning for efficient neighbor detection
    +-- ui.py                # Rendering and input handling (pygame)
    +-- world_parameters.py  # All tunable simulation constants
```

## Requirements

- Python 3.x
- [pygame](https://www.pygame.org/)
- [numpy](https://numpy.org/)

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Simulation

```bash
python main.py
```

## Controls

| Input | Action |
|---|---|
| `Space` | Spawn a shark at a random position |
| Left click | Drop food at the cursor position |
| Close window | Quit the simulation |

## Configuration

All simulation parameters are centralised in `scripts/world_parameters.py`:

| Parameter | Description |
|---|---|
| `INITIAL_NUMBER_OF_FISH` | Number of fish at startup |
| `TARGET_FPS` | Frame rate cap |
| `FISH_FIELD_OF_VIEW` | Neighbor detection radius (px) |
| `FISH_MAX_SPEED` / `FISH_MAX_SPEED_IN_CHASE` | Normal and fear speed |
| `SHARK_MAX_SPEED` / `SHARK_MAX_SPEED_IN_CHASE` | Normal and chase speed |
| `COHESION_RATIO`, `SEPARATION_RATIO`, `ALIGNMENT_RATIO` | Boids rule weights |
| `SEPARATION_RANGE` | Distance below which fish repel each other |
| `FOOD_RANGE_OF_DETECTION` | Radius within which fish detect food |
