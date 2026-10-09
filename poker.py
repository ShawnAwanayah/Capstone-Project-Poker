import random
card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
card_suits = ["Diamonds", "Hearts", "Spades", "Clubs"]
pos_actions = ["raise", "call"]
folded_players = []
wins = 0
total_games = 0


def straight(diff_hands, card_mag_val):
    cons_count = 1
    max_cons_count = 1
    for l in range(len(diff_hands)-1):
        m = l + 1
        if card_mag_val[diff_hands[l][1]] == card_mag_val[diff_hands[m][1]] - 1:
            cons_count += 1
            max_cons_count = max(max_cons_count, cons_count)
        elif card_mag_val[diff_hands[l][1]] == card_mag_val[diff_hands[m][1]]:
            continue
        else:
            cons_count = 1

        if max_cons_count >= 5:
            return True
    return False


while True:
    game = input("Do you want to play(yes/no)? ")
    if game.strip().lower() == "no":
        if total_games == 0:
            print("No games have been played")
        else:
            print(f"Total number of wins: {wins}")
            print(f"Total games played: {total_games}")
            print(f"Win percentage: {round(100 * wins/total_games, 2)}%")
        break
    elif game.strip().lower() == "yes":
        total_games += 1
        card_deck = set()
        for suit in card_suits:
            for value in card_values:
                card_deck.add((suit, value))
        card_deck = list(card_deck)
        players = [{"player1": {"money": 100, "cards": []}}, {"player2": {"money": 100, "cards": []}}, {"player3": {"money": 100, "cards": []}},
                   {"user": {"money": 100, "cards": []}}]
        random.shuffle(players)
        pot = 0
        deck = []
        while len(deck) < 2:
            card = random.choice(card_deck)
            deck.append(card)
            card_deck.remove(card)
        print("deck:", deck)

        for person in players:
            for name, player in person.items():
                player_card1 = random.choice(card_deck)
                player["cards"].append(player_card1)
                card_deck.remove(player_card1)
                player_card2 = random.choice(card_deck)
                player["cards"].append(player_card2)
                card_deck.remove(player_card2)

        last_bet = 0
        while len(deck) < 5:
            for person in players:
                if person in folded_players:
                    continue
                print(f"last bet: {last_bet}")
                for name, player in person.items():
                    if player["money"] <= 0:
                        continue
                    print("Pot:", pot)
                    if pot == 0:
                        player["money"] -= 5
                        pot += 5
                        last_bet = 5
                        continue
                    elif name != "user":
                        action = random.choice(pos_actions)
                        if action == "raise":
                            if (10 + last_bet) > player["money"]:
                                player["money"] -= player["money"]
                                last_bet += player["money"]
                            else:
                                last_bet += 10
                                player["money"] -= last_bet
                            pot += last_bet
                        elif action == "call":
                            if last_bet >= player["money"]:
                                player["money"] -= player["money"]
                                last_bet = player["money"]
                            else:
                                player["money"] -= last_bet
                            pot += last_bet

                    elif name == "user":
                        print("Pot:", pot)
                        print(f"User's Money: {player["money"]}")
                        user_action = input(
                            "Do you want to (see cards),(raise), (call) or (fold)? ")
                        while user_action == "see cards":
                            print("My cards", player["cards"])
                            user_action = input(
                                "Do you want to (see cards),(raise), (call) or (fold)? ")
                        if user_action == "raise":
                            raise_bet = float(
                                input("How much do you want to raise by? "))
                            if (last_bet + raise_bet) > player["money"]:
                                player["money"] -= player["money"]
                                last_bet += player["money"]
                            else:
                                last_bet += raise_bet
                                player["money"] -= last_bet
                            pot += last_bet
                        elif user_action == "call":
                            if last_bet > player["money"]:
                                last_bet = player["money"]
                                player["money"] -= last_bet
                            else:
                                player["money"] -= (last_bet)
                            pot += last_bet
                        elif user_action == "fold":
                            folded_players.append(person)
                            players.remove(person)
                            print(f"{name} folded")

            new_card = random.choice(card_deck)
            deck.append(new_card)
            card_deck.remove(new_card)
            print("Deck:", deck)

        card_mag_val = {}
        for num, magnitude in enumerate(card_values, 2):
            card_mag_val[magnitude] = num

        winners = {}
        highest_card = 0
        high_card_people = {}
        for people in players:
            for person, player in people.items():
                player["cards"] += deck
                player["cards"].sort(key=lambda card: card_mag_val[card[1]])
                diff_hands = player["cards"]
                print(f"{person}: {diff_hands}")

                flush = []
                for i in range(len(card_suits)):
                    count = 0
                    max_count = 0
                    for j in range(len(diff_hands)):
                        if diff_hands[j][0] == card_suits[i]:
                            count += 1
                        max_count = max(max_count, count)
                        if max_count >= 5:
                            for suit, playing_card in diff_hands:
                                if suit == card_suits[i]:
                                    flush.append((suit, playing_card))

                                if straight(flush, card_mag_val):
                                    winners[person] = 1
                                elif winners.get(person) == None or winners[person] > 4:
                                    winners[person] = 4

                suits, playing_cards = zip(*diff_hands)
                playing_cards = list(playing_cards)
                for playing_card in playing_cards:
                    if playing_cards.count(playing_card) == 4:
                        winners[person] = 2

                full_house = [playing_cards.count(
                    i) > 1 for i in playing_cards]
                if sum(full_house) >= 5:
                    if winners.get(person) == None or winners[person] > 3:
                        winners[person] = 3

                if straight(diff_hands, card_mag_val):
                    if winners.get(person) == None or winners[person] > 5:
                        winners[person] = 5

                for playing_card in playing_cards:
                    if playing_cards.count(playing_card) >= 3:
                        if winners.get(person) == None or winners.get(person) > 6:
                            winners[person] = 6

                two_pair = [playing_cards.count(i) > 1 for i in playing_cards]
                if sum(two_pair) == 4:
                    if winners.get(person) == None or winners[person] > 7:
                        winners[person] = 7

                for playing_card in playing_cards:
                    if playing_cards.count(playing_card) >= 2:
                        if winners.get(person) == None or winners.get(person) > 8:
                            winners[person] = 8

                high_card = playing_cards[-1]
                if card_mag_val[high_card] >= highest_card:
                    highest_card = card_mag_val[high_card]
                    high_card_people[person] = highest_card

        high_cards = sorted(high_card_people.values())
        for name in high_card_people:
            if high_card_people[name] == high_cards[0]:
                if winners.get(name) == None:
                    winners[name] = 9

        results = sorted(winners.values())
        true_winners = []
        for person in winners:
            if winners[person] == results[0]:
                true_winners.append(person)
        if "user" in true_winners:
            wins += 1

        hands = {1: "straight flush",  2: "four of a kind",
                 3: "full house", 4: "flush",
                 5: "straight", 6: "three of a kind",
                 7: "two pair", 8: "one pair", 9: "high card"}
        print(f"Pot: {pot}")
        for names in true_winners:
            print(
                f"Congratulations {names}, you won with a {hands[winners[names]]}!! Your prize is £{round(pot / len(true_winners), 2)}")
