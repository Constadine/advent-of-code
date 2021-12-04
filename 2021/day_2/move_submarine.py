import json

with open('input_move.txt', 'r') as f:
    lines = json.load(f)


    movements = []
    for movement in lines:
        movements.append(movement.split())

if __name__ == "__main__":
    hor_position = 0
    depth = 0
    for move in movements:
        command = move[0]
        if command == 'forward':
            hor_position += int(move[1])
        elif command == 'down':
            depth += int(move[1])
        elif command == 'up':
            depth -= int(move[1])
    print(hor_position*depth)
