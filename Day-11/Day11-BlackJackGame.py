from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
COMPUTER_MIN_SCORE = 17

def show_final_score(player, computer):
    print(f"Your final hand: {player['cards']}, final score: {player['score']}")
    print(f"Computer's hand: {computer['cards']}, final score: {computer['score']}")

def deal_card(user):
    """"# DEAL CARD AND ADD MARKS"""
    card = random.choice(cards)
    user["cards"].append(card)
    user["score"] += card

def change_ace(user):
    """"CHECK IF GOT ACE IN USER WHEN MARK OVER 21, IF YES, ACE COUNTED AS 1"""
    while user["score"] > 21 and 11 in user["cards"]:
        ace_index = user["cards"].index(11)
        user["score"] -= 10
        user["cards"][ace_index] = 1

def blackjack_game():
    while True:
        player = {
            "cards": [],
            "score": 0,
        }
        computer = {
            "cards": [],
            "score": 0,
        }
        # START
        choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if choice == "n":
            return
        print(logo)

        # DEAL 2 CARD FOR USER AND COMPUTER
        for _ in range(2):
            deal_card(player)
            deal_card(computer)

        while True:
            change_ace(player)
            print(f"Your cards: {player['cards']}, current score: {player['score']}")
            print(f"Computer's first card: {computer['cards'][0]}")
            # CHECK BLACKJACK CONDITION, IF EXIST, ANNOUNCE WINNER AND END GAME
            if player["score"] == 21 and len(player["cards"]) == 2:
                show_final_score(player, computer)
                print("Win with a Blackjack 😄")
                break
            if computer["score"] == 21 and len(computer["cards"]) == 2:
                show_final_score(player, computer)
                print("Computer wins with a blackjack")
                break

             # IF PLAYER MARK IS STILL > 21 AFTER CHANGE ACE TO 1, PLAYER LOSE
            if player["score"] > 21:
                show_final_score(player, computer)
                print("You lose ;-;")
                break

            choice2 = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            while choice2 not in ['y', 'n']:
                choice2 = input("Invalid input. Please type 'y' or 'n': ").lower()

            if choice2 == 'y':
                deal_card(player)

            elif choice2 == 'n':
                while computer["score"] < COMPUTER_MIN_SCORE:
                    deal_card(computer)
                    change_ace(computer)

                change_ace(computer)
                show_final_score(player, computer)
                if computer["score"]  > 21:
                    print("You win!")
                elif player["score"] > computer["score"]:
                    print("You win!")
                elif player["score"] < computer["score"]:
                    print("You lose ;-;")
                else:
                    print("Draw!")

                break
blackjack_game()