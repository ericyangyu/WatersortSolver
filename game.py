import copy

EMPTY_CONSTANT = ''

COLOR_CONSTANTS = [
    'RED',
    'ORANGE',
    'YELLOW',
    'LIGHT_BLUE',
    'DARK_BLUE',
    'LIME_GREEN',
    'LIGHT_GREEN',
    'DARK GREEN',
    'PURPLE',
    'GRAY',
    'PINK',
    'BROWN'
]

class WaterSortGame:
    def __init__(self):
        self.state = None # Current state
        self.original_state = None # State first set

    def get_state(self):
        """
        Gets the current state.
        :return: list of list of colors
        """
        return self.state

    def set_state(self, state):
        """
        Sets the current state.
        :param state: the state in form [[color1, color2, ...], ...] where color1 is at the top of the vial
        :return:
        """
        self.state = copy.deepcopy(state)
        self.original_state = copy.deepcopy(state)

    def get_valid_actions(self):
        """
        Gets valid actions to take at the current state
        :return: [[src vial index, dest vial index], ...]
        """
        valid_actions = []

        for i, vial in enumerate(self.state):
            # Get top color information
            num_empty, top_color, top_color_len = self.get_vial_info(vial)

            # Skip vial if empty
            if num_empty == len(vial):
                continue

            # Check for valid moves for current color
            for j, other_vial in enumerate(self.state):
                # Skip the same vial
                if i == j:
                    continue

                # Get other top color information
                other_num_empty, other_top_color, _ = self.get_vial_info(other_vial)

                # Skip if there's not enough empty space or other vial color is not the same
                if top_color_len > other_num_empty or \
                top_color != other_top_color and other_top_color != EMPTY_CONSTANT:
                    continue

                # Add new valid action
                valid_actions.append([i, j])

        return valid_actions

    def reset(self):
        """
        Resets the state to the original state set by user.
        :return:
        """
        self.state = copy.deepcopy(self.original_state)

    def step(self, action):
        """
        Takes a step in the game given an action.
        :param action: a single tuple as (src index, dest index)
        :return:
        """
        # Check if the action is valid
        valid_actions = self.get_valid_actions()
        if action not in valid_actions:
            raise Exception(f'Invalid action: {action}')

        src_i, dst_i = action
        num_empty, top_color, num_top_color = self.get_vial_info(self.state[src_i])
        other_num_empty, other_top_color, other_num_top_color = self.get_vial_info(self.state[dst_i])

        # First, pour out the top color from src vial
        for i in range(num_empty, num_empty + num_top_color):
            self.state[src_i][i] = ''

        # Second, pour in the src top colors to dst vial
        for i in range(other_num_empty - 1, other_num_empty - 1 - num_top_color, -1):
            self.state[dst_i][i] = top_color


    def get_done(self):
        """
        Checks if game is done.
        :return: 0 if not done, 1 if win, 2 if loss
        """
        # First, check if all vials are done
        for i, vial in enumerate(self.state):
            _, _, color_len = self.get_vial_info(vial)

            # Not done, but need to check if not done or loss
            if color_len != 4:
                break

            # win
            if i == len(self.state) - 1:
                return 1

        # Check if loss
        valid_actions = self.get_valid_actions()
        if len(valid_actions) == 0:
            return 2

        # Return not done
        return 0

    def get_vial_info(self, vial):
        """
        :param vial: a list of colors
        :return: A tuple (number of empty slots at the top, the top color (empty constant if none), top color len (4 if empty))
        """
        # first, count empty slots at the top
        num_empty = self.__get_number_of_color_at_top(EMPTY_CONSTANT, vial)

        # second, find top color and number of it
        top_color, num_top_color = self.__get_top_color_info(vial)

        return num_empty, top_color, num_top_color

    def __get_top_color_info(self, vial):
        """
        Gets the first top color and number of them

        :param vial: list of colors
        :return: a tuple (top color, num of top color)
        """
        top_color = EMPTY_CONSTANT
        num_top_color = None
        for i in range(len(vial)):
            # skip empty slots
            if vial[i] == EMPTY_CONSTANT:
                continue

            if top_color == EMPTY_CONSTANT:
                # initilize top color
                top_color = vial[i]
                num_top_color = 1
            else:
                # early terminate if nonmatching color found
                if top_color != vial[i]:
                    return top_color, num_top_color

                # increment the number of top color found
                num_top_color += 1

        return top_color, 4 if not num_top_color else num_top_color

    def __get_number_of_color_at_top(self, color, vial):
        """
        :param color: a color constant
        :param vial: a list of colors
        :return: the number of blocks of the same color at the top of a vial
        """
        for i in range(len(vial)):
            if vial[i] != color:
                return i

        return len(vial)
