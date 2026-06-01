import shelve
import random
def main():
    win = tie = loss = 0

    print(get_score(win, tie, loss))
   
def get_score(win, tie, loss):
    values = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    } #win values
    key_values = list(values.keys())

    print("Type q to quit")
    while True:
        turn = input("Rock, Paper or Scissors: ").lower().strip()
        if turn.lower() == "q":
            break
        choice = random.choice(key_values)

        if turn == choice:
            tie += 1
            print("It's a Tie")

        elif values[turn] == choice:
            win += 1
            print(f"You win! {turn} beats {choice}")

        else:
            loss += 1
            print(f"You lose! {choice} beats {turn}")

    with shelve.open("scoreDB", writeback=True) as db:
        db["wins"] = db.get("wins", 0) + win
        db["ties"] = db.get("ties", 0) + tie
        db["losses"] = db.get("losses", 0) + loss

    return win, tie, loss

if __name__ == "__main__":
    main()    