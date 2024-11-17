from collections import deque, defaultdict

def play_game(players, last_marble):
    scores = defaultdict(int)
    board = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            board.rotate(7)
            player = marble % players
            scores[player] += marble + board.pop()
            board.rotate(-1)
        else:
            board.rotate(-1)
            board.append(marble)
    
    return max(scores.values()) if scores else 0

print ('Part 1: {}'.format(play_game(455, 71223)))
print ('Part 2: {}'.format(play_game(455, 7122300)))