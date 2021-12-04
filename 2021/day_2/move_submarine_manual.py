from move_submarine import movements

"""
down X increases your aim by X units.
up X decreases your aim by X units.
forward X does two things:
    It increases your horizontal position by X units.
    It increases your depth by your aim multiplied by X.
"""

if __name__ == "__main__":
    aim = 0
    hor_position = 0 
    depth = 0

    for move in movements:
        command = move[0]
        offset = int(move[1])
        if command == "up":
            aim -= offset
            print(f"Turned up by {offset}. Current aim: {aim}") # Well, aim should cap at 90/-90, thus travelling vertically, but k.
        elif command == "down":
            aim += offset
            print(f"Turned down by {offset}. Current aim: {aim}") # or go crazy and do full circles.
        elif command == "forward": 
            hor_position += offset
            vertical_move = aim * offset
            depth += vertical_move
            
            print(f"Moved horizontally by {offset} and vertically by {vertical_move}. Current depth: {depth}m")

    print(aim, hor_position, depth)
    print(f"Answer: {hor_position*depth}")