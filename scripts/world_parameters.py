# --- Screen ---
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

# --- Tank ---
TANK_MARGIN = 60       # Distance from the edge where wall-avoidance kicks in
WALL_PUSH_STRENGTH = 0.002  # Force applied per pixel inside the margin zone

# --- Simulation ---
INITIAL_NUMBER_OF_FISH = 25
TARGET_FPS = 120                # Maximum frames (cycles) per second

# --- Fish movement ---
MAX_TURN_DEG = 2                    # Maximum heading change per step in degrees
RANDON_MOVEMENT_PROBABILITY = 0.005  # Probability of random wandering each step
FISH_FIELD_OF_VIEW = 60             # Radius in pixels for neighbor detection
FISH_MAX_SPEED = 1.0                      # Maximum fish speed in pixels per step
FISH_MAX_SPEED_IN_CHASE = 2.0             # Maximum fish speed in pixels per step when shark in sight


# --- Sharks movement ---
SHARK_FIELD_OF_VIEW = 60  # Radius in pixels for neighbor detection
SHARK_MAX_SPEED = 1.5
SHARK_MAX_SPEED_IN_CHASE = 2.3
SHARK_EATING_RANGE = 5

# --- Boids rule weights ---
COHESION_RATIO = 0.02    # Weight applied to the cohesion rule contribution
SEPARATION_RATIO = 0.001 # Weight applied to the separation rule contribution
ALIGNMENT_RATIO = 0.150  # Weight applied to the alignment rule contribution
SEPARATION_RANGE = 12    # Distance below which two fish repel each other

# --- Food ---
FOOD_RANGE_OF_DETECTION = 100  # Radius in pixels within which fish detect food
FOOD_SIZE = 10                 # Side length of the food square; also eating range

# --- Rendering ---
FISH_SIZE = 5
FISH_COLOR = (255, 0, 0)
SHARK_COLOR = (255, 255, 0)
FOOD_COLOR = (0, 255, 0)
