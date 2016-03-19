__author__ = 'Triet'

import Vector

"""
    Block: A dictionary with:
        - Mandatory part (must have when input the blocks):
            + "start": vector() - Coordinates of the begin of the block.
            + "end": vector() - Coordinates of the end of the block.
            + "main": bool x - If the block is the main block.
        - Calculated part (will be calculated by Game class after inserted.
            + "vector": vector() - The vector of the block, [x,0] means horizontal and [0,y] mean vertical axis.
            + "range": [int x,...] - List of possible offsets of the block.

"""


class State:
    previous_state = None
    game = None
    blocks_offsets = []
    blocks_valid_offsets = []

    def calculate_board_map(self):
        map = [[0 for i in range(self.game.board_length)] for j in range(self.game.board_length)]
        for index, block in enumerate(self.game.blocks):
            length = block["vector"].norm()
            unit_vector = block["vector"]/length
            start_point = block["start"] + self.blocks_offsets[index]*unit_vector
            for i in range(length):
                pos = start_point

    def calculate_valid_offsets(self):




        return self.blocks_offsets


class Game:
    board_length = 6
    board_gate_y = 3
    blocks = []
    begin_state = None

    # @staticmethod
    def calculate_block_optional_values(self, block):
        if block["end"][0] < block["start"][0] or block["end"][1] < block["start"][1]:
                temp_end = block["end"]
                block["end"] = block["start"]
                block["start"] = temp_end

        block["vector"] = block["end"] - block["start"]
        main_axis = 0 if block["vector"][1] == 0 else 1

        min_offset = - block["start"][main_axis]
        max_offset = self.board_length - block["end"][main_axis]
        block["range"] = list(range(min_offset,max_offset))
        return block

    def calculate_valid_offsets(self, block_number):
        block = self.blocks[block_number]
        valid_offsets = []










