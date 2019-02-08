class Moves:

    @staticmethod
    def top(cube, ccw):
        temp = [[" " for _ in range(9)] for _ in range(12)]
        # These are all the moves when turning the top side. In the list, each index contains a list containing two
        # tuples. The first tuple is the starting coordinate for a piece of the cube, the next tuple is the finish
        # coordinate.
        top_moves = [[(0,3),(2,3)], [(3,0),(3,3)], [(11,3),(3,2)], [(0,4),(1,3)], [(11,4),(3,1)],
                     [(0,5),(0,3)], [(11,5),(3,0)], [(3,8),(11,3)], [(1,3),(2,4)], [(3,1),(3,4)],
                     [(1,5),(0,4)], [(3,7),(11,4)], [(2,3),(1,5)], [(3,2),(3,5)], [(3,3),(3,6)],
                     [(2,4),(1,5)], [(3,4),(3,7)], [(2,5),(0,5)], [(3,5),(3,8)], [(3,6),(11,5)]]

        # if counterclockwise, flip all the starting and finishing coordinates, effectively turning the side in the
        # other direction.
        if ccw:
            top_moves_r = top_moves
            for x in range(len(top_moves_r)):
                top_moves_r[x] = [top_moves_r[x][1], top_moves_r[x][0]]

            for move in top_moves_r:
                temp[move[0][0]][move[0][1]] = cube[move[1][0]][move[1][1]]
        else:
            for move in top_moves:
                temp[move[0][0]][move[0][1]] = cube[move[1][0]][move[1][1]]

        for x in range(12):
            for y in range(9):
                if temp[x][y] is not " ":
                    cube[x][y] = temp[x][y]

        return cube

    @staticmethod
    def left(cube, ccw):
        temp = [[" " for _ in range(9)] for _ in range(12)]
        # These are all the moves when turning the left side. In the list, each index contains a list containing two
        # tuples. The first tuple is the starting coordinate for a piece of the cube, the next tuple is the finish
        # coordinate.
        left_moves = [[(3,0),(5,0)], [(0,3),(9,3)], [(11,3),(8,3)], [(3,1),(4,0)], [(1,3),(10,3)], [(3,2),(3,0)],
                      [(2,3),(11,3)], [(3,3),(0,3)], [(4,0),(5,1)], [(10,3),(7,3)], [(4,2),(3,1)], [(4,3),(1,3)],
                      [(5,0),(5,2)], [(9,3),(6,3)], [(8,3),(5,3)], [(5,1),(4,2)], [(7,3),(4,3)], [(5,2),(3,2)],
                      [(5,3),(2,3)], [(6,3),(3,3)]]

        # if counterclockwise, flip all the starting and finishing coordinates, effectively turning the side in the
        # other direction.
        if ccw:
            left_moves_r = left_moves
            for x in range(len(left_moves_r)):
                left_moves_r[x] = [left_moves_r[x][1], left_moves_r[x][0]]

            for move in left_moves_r:
                temp[move[0][0]][move[0][1]] = cube[move[1][0]][move[1][1]]
        else:
            for move in left_moves:
                temp[move[0][0]][move[0][1]] = cube[move[1][0]][move[1][1]]

        for x in range(12):
            for y in range(9):
                if temp[x][y] is not " ":
                    cube[x][y] = temp[x][y]

        return cube

    @staticmethod
    def right(cube, ccw):
        temp = [[" " for _ in range(9)] for _ in range(12)]

        right_moves = [
                        # right top left
                        [(3,6),(5,6)],
                        [(2,5),(5,5)],
                        [(3,5),(6,5)],

                        # right top middle
                        [(3,7),(4,6)],
                        [(1,5),(4,5)],

                        # right top right
                        [(3,8),(3,6)],
                        [(0,5),(3,5)],
                        [(11,5),(0,5)],

                        # right middle left
                        [(4,6),(5,7)],
                        [(4,5),(7,5)],

                        # right middle right
                        [(4,8),(3,7)],
                        [(10,5),(1,5)],

                        # right bottom left
                        [(5,6),(5,8)],
                        [(5,5),(8,5)],
                        [(6,5),(9,5)],

                        # right bottom middle
                        [(5,7),(4,8)],
                        [(7,5),(10,5)],

                        # right bottom right
                        [(5,8),(3,8)],
                        [(8,5),(11,5)],
                        [(9,5),(0,5)]]

        if ccw:
            left_moves_r = right_moves
            for x in range(len(left_moves_r)):
                left_moves_r[x] = [left_moves_r[x][1], left_moves_r[x][0]]

            for move in left_moves_r:
                temp[move[0][0]][move[0][1]] = cube[move[1][0]][move[1][1]]
        else:
            for move in right_moves:
                temp[move[0][0]][move[0][1]] = cube[move[1][0]][move[1][1]]

        for x in range(12):
            for y in range(9):
                if temp[x][y] is not " ":
                    cube[x][y] = temp[x][y]

        return cube

