from __future__ import absolute_import, division, print_function
from math import sqrt, log, inf
from game import WaterSortGame
import copy
import time
import random

EMPTY_CONSTANT = ''

class AI:
    def __init__(self, state, max_depth=30, print_interval=1e3):
        self.simulator = WaterSortGame()
        self.simulator.set_state(state)
        self.max_depth = max_depth

        self.visited = {}  # {state: true}

        self.num_moves = 0
        self.print_interval = print_interval

    def solve(self, previous_actions):
        self.num_moves += 1
        if self.num_moves % self.print_interval == 0:
            print(f'Simulated {self.num_moves} moves so far...')
            print('Just for fun, current moveset so far is: ', previous_actions)

        curr_state = copy.deepcopy(self.simulator.get_state())
        visited_state = copy.deepcopy(curr_state)
        visited_state = tuple(e for vial in visited_state for e in vial)

        # Do not explore current state if we've already seen it before
        if self.visited.get(visited_state) is not None:
            return False, previous_actions
        else:
            self.visited[visited_state] = True

        done = self.simulator.get_done()
        # win
        if done == 1:
            return True, previous_actions
        # loss
        if done == 2:
            return False, previous_actions

        valid_actions = self.simulator.get_valid_actions()

        # Edge case: if depth is too large, probably wrong path
        if len(previous_actions) > self.max_depth:
            return False, previous_actions

        # Optimization, remove valid actions that move homogeneous vials into empty vials
        i = 0
        while i < len(valid_actions):
            src, dest = valid_actions[i]
            empty_len, color, color_len = self.simulator.get_vial_info(curr_state[src])
            dest_empty_len, dest_color, dest_color_len = self.simulator.get_vial_info(curr_state[dest])
            if empty_len + color_len == 4 and color != EMPTY_CONSTANT and dest_empty_len == 4:
                # Don't move homogeneous semi-done vials into empty vials (there's no point!!)
                valid_actions.remove(valid_actions[i])
            else: 
                i += 1

        for action in valid_actions:
            self.simulator.set_state(curr_state)
            self.simulator.step(action)

            win, moves = self.solve(previous_actions + [action])

            if win:
                return True, moves

        return False, None
