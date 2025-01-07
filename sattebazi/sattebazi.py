import random

# Constants defining the slot machine's configuration
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3 # Number of rows in the slot machine
COLS = 3 # Number of columns in the slot machine

# Symbol configuration: number of symbols and their respective payout values

symbol_count = {
    "$" : 2,
    "♥" : 4,
    "♧" : 6,
    "♢" : 8
}

symbol_value = {
    "$" : 5,
    "♥" : 4,
    "♧" : 3,
    "♢" : 2
}

# Function to check winnings based on the lines bet, the spin result, and bet amount

def check_winnings(columns,lines,bet,values):
    winnings=0
    winnings_lines = []
    for line in range(lines):  # Iterate through each line being bet on
        symbol = columns[0][line]   # Check the first symbol in the line
        for column in columns:  # Check if the same symbol appears in all columns for this line
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:  # If all symbols match, calculate winnings and store the winning line
           winnings += values[symbol] * bet
           winnings_lines.append(lines + 1)
    return winnings, winnings_lines

# Function to generate a random spin for the slot machine
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):  # Add each symbol to a pool based on its count
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):   # Generate each column of the slot machine
        column = []
        current_symbols = all_symbols[:]  # Copy the pool of symbols to select from
        for _ in range(rows):  # Pick random symbols for each row in the column
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns

# Function to print the slot machine's current state
def print_slot_machine(columns):
    for row in range(len(columns[0])):  # Iterate through rows
        for i, column in enumerate(columns): # Iterate through columns
            if i != len(columns) -1 :
                print(column[row], end="|")   # Print symbol with a separator
            else:
                print(column[row], end="")  # Print the last symbol in the row without a separator
        
        print()

# Function to get the user's deposit amount
def deposit():
    while True:
        amount = input("Kitna paisa daalna hai bhai? ₹") # Ask user for deposit amount
        if amount.isdigit():  # Check if the input is a number
            amount = int(amount)
            if amount > 0:
                break  # Accept if greater than 0
            else:
                print("Arre bhai, kuch toh daal, 0 se zyada hona chahiye. ")
        else:
            print("Abe number daal, yeh kya mazaak hai!")
    return amount

# Function to get the number of lines the user wants to bet on
def get_number_of_lines():
    while True:
        lines = input("Kitne lines pe  khelna hai (1-"+ str(MAX_LINES)+")?")
        if lines.isdigit(): # Check if input is a number
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:   # Ensure the number of lines is within the allowed range
                break
            else:
                print("Arre sahi number daal bhai. ")
        else:
            print("Number daal bhai, joke mat maar")
    return lines

# Function to get the amount the user wants to bet per line
def get_bet():
    while True:
        amount = input("Har line pe kitna lagana hai bhai? ₹") # Ask for bet amount
        if amount.isdigit(): # Check if input is a number
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET: # Ensure bet is within the allowed range
                break
            else:
                print(f"Abe bhai, paisa ₹{MIN_BET} aur ₹{MAX_BET}ke beech mein daal. ")
        else:
            print("Number daal bhai, nautanki mat kar.")
    return amount

# Function to handle a single spin of the slot machine
def spin(balance):
    lines = get_number_of_lines()  # Get number of lines to bet on
    while True:
        bet = get_bet() # Get bet amount per line
        total_bet = bet * lines # Calculate total bet
        if total_bet > balance: # Check if user has enough balance
            print(f"Abe bhai, itna paisa nahi hai tere paas. Balance hai ₹{balance}")
        else:
            break
    print(f"Tune ₹{bet} ka bet lagaya hai {lines} lines pe. Total bet ban rha hai : ₹{total_bet} ")
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count) # Generate a spin result
    print_slot_machine(slots) # Display the slot machine
    winnings, winnings_lines = check_winnings(slots,lines,bet,symbol_value) # Check for winnings
    print(f"Bhai, tune jeeta ₹{winnings}!")
    print(f"Jeeta lines pe:", *winnings_lines)
    balance += winnings - total_bet # Update the balance
    return balance

# Main function to run the game  
def main():
    balance = deposit() # Get the initial deposit amount
    total_money_won = 0 # Track total money won
    total_money_lost = 0 # Track total money lost
    spins_played = 0  # Track number of spins played
    while True:
        print(f"Tera current balance hai ₹{balance}")
        if balance == 0: # If balance is 0, ask user to deposit more money
            print("Bhai, paisa khatam ho gaya!")
            answer = input("Aur paisa daalega kya khelne ke liye? (y/n):")
            if answer.lower() =='y':
                balance = deposit()

            else: 
                break
        else:
            answer = input("Khelne ka hai? Enter daba, warna q daba ke nikal le.")
            if answer == "q": # Quit if user enters 'q'
                break
            initial_balance = balance 
            balance = spin(balance) # Play a spin
            spins_played += 1 # Increment spin count
            if balance > initial_balance: # Update money won/lost
                total_money_won += balance - initial_balance
            else:
                total_money_lost += initial_balance - balance

    # Print game summary
    print(f"\nGame khatam!")
    print(f"Total spins kiye: {spins_played}")
    print(f"Total money jeeta: ₹{total_money_won}")
    print(f"Total money haara: ₹{total_money_lost}")
    print(f"Bhai, ab tere  paas bacha hai ₹{balance}")
    
main()