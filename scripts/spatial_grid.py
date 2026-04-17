from scripts import world_parameters

class SpatialGrid():
    def __init__(self):
        self.square_case_to_fishes = {}
        self.size_of_column, self.size_of_row = 0, 0
        self.number_of_column, self.number_of_row = 0, 0
        self.calculate_size_of_case()

        self.map_of_adjacent_cases = {}
        self.create_map_of_adjacent_cases()

    def calculate_size_of_case(self):
        minimum_size = world_parameters.FISH_FIELD_OF_VIEW
        self.number_of_column = world_parameters.SCREEN_WIDTH // minimum_size
        self.number_of_row = world_parameters.SCREEN_HEIGHT // minimum_size

        self.size_of_column = world_parameters.SCREEN_WIDTH / self.number_of_column
        self.size_of_row = world_parameters.SCREEN_HEIGHT / self.number_of_row
        self.create_empty_dicts()

    def create_empty_dicts(self):
        for column in range(self.number_of_column):
            for row in range(self.number_of_row):
                self.square_case_to_fishes[(column, row)] = []


    def find_adjacent_cases(self, column, row):
        self.map_of_adjacent_cases[(column, row)] = []
        for column_index in range((column - 1), (column + 2)):
            for row_index in range(row - 1, row + 2):
                if (column_index) in range(self.number_of_column) and row_index in range(self.number_of_row):
                    self.map_of_adjacent_cases[(column, row)].append((column_index, row_index))

    def create_map_of_adjacent_cases(self):
        for column in range(self.number_of_column):
            for row in range(self.number_of_row):
                self.find_adjacent_cases(column,row)


    def get_fish_square_case(self, fish):
        return (int(fish.position_x // self.size_of_column), int(fish.position_y // self.size_of_row))
        

    def update_grid(self, fishes, food):
        self.create_empty_dicts()
        for fish in fishes:
            self.square_case_to_fishes[self.get_fish_square_case(fish)].append(fish)
        

    def find_fish_neighbors(self, fish, fishes):
        fish.neighbors = []
        fishes_in_adjacent_cases = []
        column_of_fish, row_of_fish  = self.get_fish_square_case(fish)
        list_of_adjacent_cases = self.map_of_adjacent_cases[(column_of_fish, row_of_fish)]

        for case in list_of_adjacent_cases:
            fishes_in_adjacent_cases += self.square_case_to_fishes[case]

        # for other in fishes:
        #     if fish.distance_to(other.position_x, other.position_y) < fish.field_of_view:
        #         fish.neighbors.append(other)

        for other in fishes_in_adjacent_cases[0:20]:
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



