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





