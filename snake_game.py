import random
import os
import time

# Define the game board dimensions
ROWS, COLS = 10, 10

# Snake directions
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

# Snake symbols
EMPTY = ' '
SNAKE_HEAD = 'O'
SNAKE_BODY = 'o'
FOOD = '*'

# Levels of difficulty
DIFFICULTY_LEVELS = {
    'easy': 0.2,
    'medium': 0.15,
    'hard': 0.1,
    'expert': 0.05,
    'insane': 0.02
}

# Function to initialize the game board
def initialize_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

# Function to display the game board
def display_board(board):
    for row in board:
        print(' '.join(row))
    print()

# Function to place the snake on the board
def place_snake(board, snake):
    head_row, head_col = snake[0]
    board[head_row][head_col] = SNAKE_HEAD
    for body_row, body_col in snake[1:]:
        board[body_row][body_col] = SNAKE_BODY

# Function to place the food on the board
def place_food(board, food):
    food_row, food_col = food
    board[food_row][food_col] = FOOD

# Function to move the snake
def move_snake(snake, direction):
    head_row, head_col = snake[0]
    dr, dc = direction
    new_head = (head_row + dr, head_col + dc)
    return [new_head] + snake[:-1]

# Function to generate new food
def generate_food(snake):
    while True:
        food_row = random.randint(0, ROWS - 1)
        food_col = random.randint(0, COLS - 1)
        if (food_row, food_col) not in snake:
            return food_row, food_col

# Function to check if the snake has collided with itself
def is_collision(snake):
    head = snake[0]
    return head in snake[1:]

# Function to get the user's move input
def get_move():
    while True:
        move = input("Enter your move (w/a/s/d): ").lower()
        if move in ['w', 'a', 's', 'd']:
            return move

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main game function
def play_game(difficulty):
    board = initialize_board()
    snake = [(ROWS//2, COLS//2)]
    direction = RIGHT
    food = generate_food(snake)
    place_food(board, food)
    place_snake(board, snake)

    while True:
        clear_screen()
        display_board(board)

        move = get_move()
        if move == 'w':
            direction = UP
        elif move == 'a':
            direction = LEFT
        elif move == 's':
            direction = DOWN
        elif move == 'd':
            direction = RIGHT

        new_snake = move_snake(snake, direction)

        if is_collision(new_snake):
            print("Game Over! You collided with yourself.")
            break

        head_row, head_col = new_snake[0]

        if head_row < 0 or head_row >= ROWS or head_col < 0 or head_col >= COLS:
            print("Game Over! You hit the wall.")
            break

        if (head_row, head_col) == food:
            food = generate_food(new_snake)
            place_food(board, food)
            snake = new_snake
        else:
            snake = new_snake

        time.sleep(difficulty)

if __name__ == "__main__":
    print("Welcome to Snake Game!")
    print("Choose your level of difficulty:")
    for i, level in enumerate(DIFFICULTY_LEVELS, 1):
        print(f"{i}. {level.capitalize()}")

    while True:
        choice = input("Enter the number of the level (1-5): ")
        try:
            choice = int(choice)
            if 1 <= choice <= 5:
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    difficulty_level = list(DIFFICULTY_LEVELS.values())[choice - 1]

    print(f"Starting Snake Game at {list(DIFFICULTY_LEVELS.keys())[choice - 1]} level...")
    time.sleep(2)
    play_game(difficulty_level)
