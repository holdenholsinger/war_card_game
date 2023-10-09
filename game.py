from all_cards import Cards
from decks import Deck


class Game:

    def __init__(self):
        dealt_hand = Cards.deal_cards()
        self.my_deck1 = Deck(dealt_hand[0], 1)
        self.my_deck2 = Deck(dealt_hand[1], 2)
        # We assume it takes 10 seconds to shuffle a deck below
        self.game_time = 0
        self.total_battles = 0

    @property
    def total_cards_between_decks(self):
        return self.my_deck1.total_card_count + self.my_deck2.total_card_count

    @property
    def converted_game_time(self):
        seconds = self.my_deck1.shuffle_time + self.my_deck2.shuffle_time + self.game_time
        minutes = seconds / 60
        minutes_rounded = round(minutes, 2)
        return minutes_rounded


    @property
    def total_card_count_comparison(self):
        return f'Deck 1: {self.my_deck1.total_card_count} Deck2: {self.my_deck2.total_card_count}'

    @property
    def total_shuffle_count(self):
        return self.my_deck1.shuffle_count + self.my_deck2.shuffle_count

    def find_shorter_deck(self):
        return min(len(self.my_deck1.active_cards), len(self.my_deck2.active_cards))

    def active_cards_fight(self):
        while self.my_deck1.can_continue and self.my_deck2.can_continue:
            if self.my_deck1.can_shuffle and self.my_deck2.can_shuffle:
                # To ensure we don't add twenty seconds to the game time if both decks need to shuffle at the same time
                self.game_time -= 10

            self.total_battles += 1
            self.game_time += 1

            card1, card2 = self.my_deck1.draw_card(), self.my_deck2.draw_card()

            if card1[1] > card2[1]:
                self.my_deck1.winners += [card1, card2]

            elif card1[1] < card2[1]:
                self.my_deck2.winners += [card1, card2]

            else:
                self.war(war_pot=[card1, card2])

        return [self.total_battles, self.total_shuffle_count, f'{self.converted_game_time} minutes']

    def war(self, war_pot):
        if self.my_deck1.can_draw_four and self.my_deck2.can_draw_four:
            war_hand1, war_hand2 = self.my_deck1.draw_four_if_possible(), self.my_deck2.draw_four_if_possible()
            self.game_time += 4
            war_pot.extend(war_hand1 + war_hand2)
            final_card1, final_card2 = war_hand1[-1][1], war_hand2[-1][1]
            winning_deck = self.my_deck1 if final_card1 > final_card2 else (self.my_deck2 if final_card2 > final_card1 else None)
            if winning_deck:
                winning_deck.winners.extend(war_pot)
            else:
                self.war(war_pot)

        else:
            shorter_deck = self.my_deck1 if not self.my_deck1.can_draw_four else self.my_deck2
            longer_deck = self.my_deck2 if shorter_deck == self.my_deck1 else self.my_deck1

            shorter_deck_remaining_cards = [shorter_deck.draw_card() for card in range(shorter_deck.total_card_count)] if shorter_deck.total_card_count else None
            if shorter_deck_remaining_cards:
                longer_deck.winners.extend(shorter_deck_remaining_cards)
            longer_deck.winners.extend(war_pot)



