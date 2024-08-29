from itertools import permutations

NUM_PLAYERS = 9
FAVORITE_PLAYER_INDEX = 3
NUM_BASES = 3


def play_baseball_game(batting_order, game):
    point = 0
    number = 0

    for inning in game:
        out = 0
        p1 = p2 = p3 = 0

        while out < 3:
            current_batter = batting_order[number]
            batting_result = inning[current_batter]

            if batting_result == 0:
                out += 1
            elif batting_result == 1:
                point += p3
                p1, p2, p3 = 1, p1, p2
            elif batting_result == 2:
                point += p2 + p3
                p1, p2, p3 = 0, 1, p1
            elif batting_result == 3:
                point += p1 + p2 + p3
                p1, p2, p3 = 0, 0, 1
            elif batting_result == 4:
                point += p1 + p2 + p3 + 1
                p1 = p2 = p3 = 0

            number = (number + 1) % NUM_PLAYERS

    return point


def generate_permutations(game):
    result = 0
    order = list(range(1, NUM_PLAYERS))

    for perm in permutations(order, NUM_PLAYERS - 1):
        batter = list(perm[:FAVORITE_PLAYER_INDEX]) + [0] + list(perm[FAVORITE_PLAYER_INDEX:])
        point = play_baseball_game(batter, game)
        result = max(result, point)

    return result


N = int(input())
game = [list(map(int, input().split())) for _ in range(N)]

result = generate_permutations(game)
print(result)