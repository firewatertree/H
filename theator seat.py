def create_theater(rows, cols):
    return [['A' for _ in range(cols)] for _ in range(rows)]

def display_seating_arrangement(theater):
    for row in theater:
        print(' '.join(row))

def validate_seat(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols

def mark_reserved_seats(theater, reserved_seats):
    for seat in reserved_seats:
        row, col = map(int, seat.split(','))
        if validate_seat(row, col, len(theater), len(theater[0])):
            theater[row][col] = 'R'
        else:
            print(f"Ignoring reserved seat {seat} as it is outside the theater's dimensions.")

def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    theater = create_theater(rows, cols)
    reserved_seats_input = input("Enter the reserved seats (format: 'row,col|row,col|...'): ")
    reserved_seats = reserved_seats_input.split('|')
    mark_reserved_seats(theater, reserved_seats)
    display_seating_arrangement(theater)

if __name__ == "__main__":
    main()