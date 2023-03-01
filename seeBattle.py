import random

class Ship:
    def __init__(self, points):
        self.points = set(points)

    def __contains__(self, point):
        return point in self.points

class Board:
    def __init__(self, ships):
        self.ships = ships
        self.grid = [[' ' for _ in range(6)] for _ in range(6)]

        for ship in self.ships:
            for point in ship.points:
                x, y = point
                self.grid[x][y] = 'X'

    def __str__(self):
        rows = ['   1 2 3 4 5 6',
                '  +-+-+-+-+-+-+']

        for i in range(6):
            row = [chr(ord('A') + i), '|']
            row.extend(self.grid[i])
            row.append('|')
            rows.append(' '.join(row))
            rows.append('  +-+-+-+-+-+-+')

        return '\n'.join(rows)

class Player:
    def __init__(self, board):
        self.board = board

    def take_turn(self):
        while True:
            try:
                x = input('Enter x coordinate (1-6): ')
                y = input('Enter y coordinate (A-F): ')
                x = int(x) - 1
                y = ord(y.upper()) - ord('A')
                if self.board.grid[x][y] == 'T' or self.board.grid[x][y] == 'X':
                    raise ValueError('You already shot there!')
                break
            except (ValueError, IndexError):
                print('Invalid input. Please try again.')

        if self.board.grid[x][y] == ' ':
            self.board.grid[x][y] = 'T'
            print('Miss!')
        else:
            self.board.grid[x][y] = 'X'
            print('Hit!')

class AIPlayer(Player):
    def take_turn(self):
        while True:
            x = random.randint(0, 5)
            y = random.randint(0, 5)
            if self.board.grid[x][y] != 'T' and self.board.grid[x][y] != 'X':
                break

        if self.board.grid[x][y] == ' ':
            self.board.grid[x][y] = 'T'
            print('AI Missed!')
        else:
            self.board.grid[x][y] = 'X'
            print('AI Hit!')

def generate_ships(num_ships_1, num_ships_2, num_ships_4):
    ships = []
    for num_ships, size in [(num_ships_1, 3), (num_ships_2, 2), (num_ships_4, 1)]:
        for _ in range(num_ships):
            while True:
                x = random.randint(0, 5)
                y = random.randint(0, 5)
                orientation = random.choice(['horizontal', 'vertical'])
                points = [(x, y)]
                if orientation == 'horizontal':
                    for i in range(1, size):
                        if x + i > 5 or (x+i, y) in points or (x+i-1, y) in [(a, b) for a in range(x-1, x+2) for b in range(y-1, y+2) if 0 <= a < 6 and 0 <= b < 6]:
                            break
                        points.append((x+i, y))
                    else:
                        ships.append(Ship(points))
                        break
               
