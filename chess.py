import pygame

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)

# Load piece images
pieces = {
    "wp": pygame.transform.scale(pygame.image.load("white_pawn.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "wR": pygame.transform.scale(pygame.image.load("white_rook.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "wN": pygame.transform.scale(pygame.image.load("white_knight.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "wB": pygame.transform.scale(pygame.image.load("white_bishop.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "wQ": pygame.transform.scale(pygame.image.load("white_queen.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "wK": pygame.transform.scale(pygame.image.load("white_king.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "bp": pygame.transform.scale(pygame.image.load("black_pawn.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "bR": pygame.transform.scale(pygame.image.load("black_rook.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "bN": pygame.transform.scale(pygame.image.load("black_knight.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "bB": pygame.transform.scale(pygame.image.load("black_bishop.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "bQ": pygame.transform.scale(pygame.image.load("black_queen.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "bK": pygame.transform.scale(pygame.image.load("black_king.png"), (SQUARE_SIZE, SQUARE_SIZE)),
}

# Chessboard setup
board = [
    ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
    ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
    ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
]

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Function to draw the chessboard
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Function to draw the pieces
def draw_pieces():
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece:
                screen.blit(pieces[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))

# Function to get the row and column from mouse position
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# Main game loop
def main():
    running = True
    selected_piece = None
    selected_pos = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)

                if selected_piece is None:
                    # Select a piece
                    if board[row][col] != "":
                        selected_piece = board[row][col]
                        selected_pos = (row, col)
                else:
                    # Move the selected piece
                    board[selected_pos[0]][selected_pos[1]] = ""
                    board[row][col] = selected_piece
                    selected_piece = None
                    selected_pos = None

        # Draw the board and pieces
        draw_board()
        draw_pieces()
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()