from Moves import Moves

class Cube:
    def __init__(self, turns=None):
        self.moves = Moves()
        self.cube = [[" " for _ in range(9)] for _ in range(12)]
        self.turns = turns
        self.cycles = 0
        for x in range(len(self.cube)):
            for y in range(len(self.cube[x])):
                if x <= 2 and y in range(3, 6):
                    self.cube[x][y] = "W"
                elif x in range(3, 6) and y <= 2:
                    self.cube[x][y] = "R"
                elif x in range(3, 6) and y in range(2, 6):
                    self.cube[x][y] = "B"
                elif x in range(3, 6) and y >= 6:
                    self.cube[x][y] = "O"
                elif x in range(6, 9) and y in range(3, 6):
                    self.cube[x][y] = "Y"
                elif x in range(9, 13) and y in range(3, 6):
                    self.cube[x][y] = "G"
        self.solved = self.cube

    def __str__(self):
        return '\n'.join([' '.join(str(y) for y in row) for row in self.cube]) + "\n"

    def move(self):

        self.turn()
        self.cycles += 1
        while self.cube != Cube.solved():
            print("Cycle: ", self.cycles)
            self.turn()
            self.cycles += 1
            if self.cycles == 6:
                print(self.__str__())
                break

    @staticmethod
    def solved():
        solved_cube = [[" " for _ in range(9)] for _ in range(12)]
        for x in range(len(solved_cube)):
            for y in range(len(solved_cube[x])):
                if x <= 2 and y in range(3, 6):
                    solved_cube[x][y] = "W"
                elif x in range(3, 6) and y <= 2:
                    solved_cube[x][y] = "R"
                elif x in range(3, 6) and y in range(2, 6):
                    solved_cube[x][y] = "B"
                elif x in range(3, 6) and y >= 6:
                    solved_cube[x][y] = "O"
                elif x in range(6, 9) and y in range(3, 6):
                    solved_cube[x][y] = "Y"
                elif x in range(9, 13) and y in range(3, 6):
                    solved_cube[x][y] = "G"

        return solved_cube

    def turn(self):
        top = ["U", "u", "White", "white", "Top", "top", "T", "t"]
        left = ["L", "l", "Left", "left"]
        right = ["R", "r", "Right", "right"]
        front = ["F", "f", "Front", "front"]
        back = ["B", "b", "Back", "back"]
        down = ["D", "d", "Down", "down"]
        for turn in self.turns:
            # top turns
            if turn in top:
                self.top()
            elif turn in [move + "\'" for move in top]:
                self.top(ccw=True)
            elif turn in [move + "2" for move in top]:
                self.top()
                self.top()

            # left turns
            elif turn in left:
                self.left()
            elif turn in [move + "\'" for move in left]:
                self.left(ccw=True)
            elif turn in [move + "2" for move in left]:
                self.left()
                self.left()

            # right turns
            elif turn in right:
                self.right()
            elif turn in [move + "\'" for move in right]:
                self.right(ccw=True)
            elif turn in [move + "2" for move in right]:
                self.right()
                self.right()

            # front turns
            elif turn in front:
                self.front()
            elif turn in [move + "\'" for move in front]:
                self.front(ccw=True)
            elif turn in [move + "2" for move in front]:
                self.front()
                self.front()

            # back turns
            elif turn in back:
                self.back()
            elif turn in [move + "\'" for move in back]:
                self.back(ccw=True)
            elif turn in [move + "2" for move in back]:
                self.back()
                self.back()

            # back turns
            elif turn in down:
                self.down()
            elif turn in [move + "\'" for move in down]:
                self.back(ccw=True)
            elif turn in [move + "2" for move in down]:
                self.down()
                self.down()

    def top(self, ccw=False):
        self.cube = self.moves.top(self.cube, ccw)

    def left(self, ccw=False):
        self.cube = self.moves.left(self.cube, ccw)

    def right(self, ccw=False):
        self.cube = self.moves.right(self.cube, ccw)

    def front(self, ccw=False):
        pass

    def back(self, ccw=False):
        pass

    def down(self, ccw=False):
        pass


cube = Cube(['t','l','t\'','l\''])
#print(cube)
cube.move()
print(cube.cycles)
