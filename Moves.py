class Moves:

    @staticmethod
    def top(first, second, ccw):
        # These are all the moves when turning the top side. In the list, each index contains a list containing two
        # tuples. The first tuple is the starting coordinate for a piece of the cube, the next tuple is the finish
        # coordinate.
        top_moves = [[(0,3),(2,3)], [(3,0),(3,3)], [(11,3),(3,2)], [(0,4),(1,3)], [(11,4),(3,1)],
                     [(0,5),(0,3)], [(11,5),(3,0)], [(3,8),(11,3)], [(1,3),(2,4)], [(3,1),(3,4)],
                     [(1,5),(0,4)], [(3,7),(11,4)], [(2,3),(2,5)], [(3,2),(3,5)], [(3,3),(3,6)],
                     [(2,4),(1,5)], [(3,4),(3,7)], [(2,5),(0,3)], [(3,5),(3,8)], [(3,6),(11,5)]]

        # if counterclockwise, flip all the starting and finishing coordinates, effectively turning the side in the
        # other direction.
        if ccw:
            top_moves_r = top_moves
            for x in range(len(top_moves_r)):
                top_moves_r[x] = [top_moves_r[x][1], top_moves_r[x][0]]

            for move in top_moves_r:
                first[move[0][0]][move[0][1]] = second[move[1][0]][move[1][1]]
        else:
            for move in top_moves:
                first[move[0][0]][move[0][1]] = second[move[1][0]][move[1][1]]

        for x in range(12):
            for y in range(9):
                if first[x][y] is not " ":
                    second[x][y] = first[x][y]

        return second

