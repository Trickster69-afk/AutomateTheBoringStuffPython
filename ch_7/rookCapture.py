def main():
    board = {} #chessboard dict - manually enter
    rook = input("Enter rook's position: ").strip().lower() #square on which white rook is located

    print(white_rook_can_capture(rook, board)) #returns a list of all squares with black pieces that the rook can capture

def white_rook_can_capture(rook, board):
    capture_list = []
    for square in board:
        if (square[0] == rook[0] or square[1] == rook[1]) and board[square][0] == "b": #(same file OR same rank) AND black
            capture_list.append(square)  
    
    return capture_list

if __name__ == "__main__":
    main()