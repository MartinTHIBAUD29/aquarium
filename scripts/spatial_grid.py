from scripts import world_parameters, sharks, boids

# Divides the screen into a uniform grid of cells to optimise neighbor searches
# Instead of checking every fish pair, only fish in adjacent cells are compared
class SpatialGrid():
    def __init__(self):
        self.square_case_to_fishes = {} #Dict mapping (column, row) -> list of fish in that cell
        self.size_of_column, self.size_of_row = 0, 0
        self.number_of_column, self.number_of_row = 0, 0
        self.calculate_size_of_case()

        self.map_of_adjacent_cases = {} #Dict mapping (column, row) -> list of its neighbouring cells
        self.create_map_of_adjacent_cases()

    # Compute cell dimensions so that each cell is at least FISH_FIELD_OF_VIEW wide/tall
    # This guarantees that all potential neighbors lie in at most the 3x3 surrounding cells
    def calculate_size_of_case(self):
        minimum_size = world_parameters.FISH_FIELD_OF_VIEW
        self.number_of_column = world_parameters.SCREEN_WIDTH // minimum_size
        self.number_of_row = world_parameters.SCREEN_HEIGHT // minimum_size

        self.size_of_column = world_parameters.SCREEN_WIDTH / self.number_of_column
        self.size_of_row = world_parameters.SCREEN_HEIGHT / self.number_of_row
        self.create_empty_dicts()

    # Reset all cell lists to empty so the grid can be repopulated each step
    def create_empty_dicts(self):
        for column in range(self.number_of_column):
            for row in range(self.number_of_row):
                self.square_case_to_fishes[(column, row)] = []

    # Build the list of valid neighbours (including itself) for a single cell
    # Boundary cells only get neighbours that exist within the grid
    def find_adjacent_cases(self, column, row):
        self.map_of_adjacent_cases[(column, row)] = []
        for column_index in range((column - 1), (column + 2)):
            for row_index in range(row - 1, row + 2):
                if (column_index) in range(self.number_of_column) and row_index in range(self.number_of_row):
                    self.map_of_adjacent_cases[(column, row)].append((column_index, row_index))

    # Pre-compute adjacent cell lists for every cell in the grid (done once at init)
    def create_map_of_adjacent_cases(self):
        for column in range(self.number_of_column):
            for row in range(self.number_of_row):
                self.find_adjacent_cases(column, row)

    # Return the (column, row) cell index for a fish based on its current position
    # Clamps to grid bounds to handle fish exactly on the screen edge
    def get_fish_square_case(self, fish):
        column = max(0, min(int(fish.position_x // self.size_of_column), self.number_of_column - 1))
        row = max(0, min(int(fish.position_y // self.size_of_row), self.number_of_row - 1))
        return (column, row)

    # Clear the grid and re-insert every fish into its current cell
    # Called at the start of each simulation step before neighbor searches
    def update_grid(self, fishes, food):
        self.create_empty_dicts()
        for fish in fishes:
            self.square_case_to_fishes[self.get_fish_square_case(fish)].append(fish)

    # Populate fish.neighbors with all fish within field_of_view distance
    # Only fish in the 3x3 block of cells around the current fish are checked,
    # reducing the search from O(n^2) to O(k) where k << n
    def find_fish_neighbors(self, fish, fishes):
        fish.neighbors = []
        fish.sharks_in_sight = []
        fishes_in_adjacent_cases = []
        column_of_fish, row_of_fish = self.get_fish_square_case(fish)
        list_of_adjacent_cases = self.map_of_adjacent_cases[(column_of_fish, row_of_fish)]

        for case in list_of_adjacent_cases:
            fishes_in_adjacent_cases += self.square_case_to_fishes[case]

        for other in fishes_in_adjacent_cases:
            if fish.distance_to(other.position_x, other.position_y) < fish.field_of_view:
                if isinstance(other, boids.Boid):
                    fish.neighbors.append(other)
                elif isinstance(other, sharks.Shark):
                    fish.sharks_in_sight.append(other)

    # Populate fish.food_in_sight with food objects within detection range
    # Food within FOOD_SIZE (eating range) is consumed and added to the removal list
    # Returns the list of food objects to remove from the aquarium this step
    def find_food_in_sight(self, fish, foods):
        fish.food_in_sight = {}
        food_to_remove = []
        for food in foods:
            distance_to_food = fish.distance_to(food.position_x, food.position_y)
            if distance_to_food < world_parameters.FOOD_SIZE:
                food_to_remove.append(food)
            elif distance_to_food < food.range_of_detection:
                fish.food_in_sight[food] = distance_to_food
        return food_to_remove
