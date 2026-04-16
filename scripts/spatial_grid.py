from scripts import world_parameters

class SpatialGrid():
    def __init__(self):
        self.square_case_to_fishes = {}
        self.size_of_column, self.size_of_row = 0, 0
        self.number_of_column, self.number_of_row = 0, 0
        self.calculate_size_of_case()

    def calculate_size_of_case(self):
        minimum_size = world_parameters.FISH_FIELD_OF_VIEW
        self.number_of_column = world_parameters.SCREEN_WIDTH // minimum_size
        self.number_of_row = world_parameters.SCREEN_HEIGHT // minimum_size

        self.size_of_column = world_parameters.SCREEN_WIDTH / self.number_of_column
        self.size_of_row = world_parameters.SCREEN_HEIGHT / self.number_of_row

    def update_grid(self, fishes, food):
        pass

    def find_fish_neighbors(self, fish, fishes):
        fish.neighbors = []
        for other in fishes:
            if fish.distance_to(other.position_x, other.position_y) < fish.field_of_view:
                fish.neighbors.append(other)

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



