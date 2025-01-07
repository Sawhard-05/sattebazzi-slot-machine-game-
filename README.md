# Sattebazzi (Slot Machine Game)

## Introduction
Sattebazzi is a text-based slot machine game written in Python. It's an exciting gambling simulation where you can deposit money, place bets on different lines, and spin to test your luck. With a mix of symbols like `$`, `♥`, `♧`, and `♢`, the game offers a simple yet engaging slot machine experience.

---

## Features
- Bet on 1 to 3 lines per spin.
- Symbols have varying probabilities and payouts.
- Keeps track of total money won, lost, and number of spins played.
- Hinglish (Hindi-English) dialogue style for a fun and entertaining user experience.

---

## Gameplay
### Symbols and Their Values:
| Symbol | Frequency in Reels | Payout Multiplier |
|--------|---------------------|-------------------|
| `$`    | 2                   | 5                 |
| `♥`    | 4                   | 4                 |
| `♧`    | 6                   | 3                 |
| `♢`    | 8                   | 2                 |

### Steps to Play:
1. **Deposit Money**:
   - The game starts by asking how much money you want to deposit.
2. **Choose Lines**:
   - You can choose between 1 to 3 lines to bet on.
3. **Place Bet**:
   - Decide how much money to bet per line (minimum ₹1, maximum ₹100).
   - The total bet is calculated as `bet × number of lines`.
4. **Spin**:
   - The slot machine will randomly generate symbols on a 3x3 grid.
   - If all symbols on a line match, you win!
5. **Repeat or Exit**:
   - Continue playing until you run out of money or decide to quit.

---

## Code Overview
### Key Functions:
- **`deposit()`**:
  Prompts the user to deposit money and validates the input.
- **`get_number_of_lines()`**:
  Asks the user how many lines to bet on (1 to 3).
- **`get_bet()`**:
  Takes the bet amount per line and validates it.
- **`get_slot_machine_spin(rows, cols, symbols)`**:
  Generates a random 3x3 grid of slot machine symbols based on their frequency.
- **`check_winnings(columns, lines, bet, values)`**:
  Checks for winning lines and calculates the total winnings.
- **`print_slot_machine(columns)`**:
  Prints the 3x3 slot machine grid in a readable format.
- **`spin(balance)`**:
  Handles a single round of betting, spinning, and updating the balance.
- **`main()`**:
  The main game loop that manages deposits, spins, and the end of the game.

---

## Example Gameplay:
### Sample Input/Output:
```
Kitna paisa daalna hai bhai? ₹100
Kitne lines pe  khelna hai (1-3)? 2
Har line pe kitna lagana hai bhai? ₹10
Tune ₹10 ka bet lagaya hai 2 lines pe. Total bet ban rha hai : ₹20
♢|♥|♧
♧|♧|♢
♧|♧|♢
Bhai, tune jeeta ₹60!
Jeeta lines pe: 1 2
Tera current balance hai ₹140
Khelne ka hai? Enter daba, warna q daba ke nikal le.
```

---

## Requirements
- Python 3.6 or higher.

---

## How to Run
1. Copy the code into a Python file, e.g., `sattebazzi.py`.
2. Run the file using the command:
   ```bash
   python sattebazzi.py
   ```
3. Follow the on-screen instructions to play the game.

---

## Future Enhancements
- Add a graphical user interface (GUI) for a more immersive experience.
- Introduce bonus rounds and jackpots.
- Add a leaderboard to track high scores.

---

Enjoy playing Sattebazzi and may the odds be ever in your favor!
