import random


class Deck:
    def __init__(self, hand: list, deck_id: int):
        self.winners = []
        self.active_cards = list(hand)
        self.deck_id = deck_id
        self.shuffle_count = 0
        self.shuffle_time = 0

    def __repr__(self):
        return f'Deck {self.deck_id}'

    @property
    def total_card_count(self):
        return len(self.winners) + len(self.active_cards)

    def shuffle_depleted_hand(self):
        random.shuffle(self.winners)

        self.active_cards = list(self.winners)  # Set active cards to the shuffled winners
        self.winners = []  # Reset winners
        print(f'After shuffling, deck {self.deck_id} now has {len(self.active_cards)} cards in hand.\n')
        self.shuffle_count += 1
        self.shuffle_time += 10

    def check_if_shuffle_needed(self):
        if not self.can_shuffle:
            raise Exception('Cannot shuffle, GG.')
        if len(self.active_cards) == 0:
            self.shuffle_depleted_hand()
        pass

    def draw_card(self) -> tuple:
        if not self.can_continue:
            raise Exception('Cannot draw.')
        self.shuffle_if_needed()
        return self.active_cards.pop(0)
        # returns the popped tuple for playing the game

    @property
    def can_shuffle(self):
        if len(self.winners) > 0 and len(self.active_cards) == 0:
            return True
        else:
            return False

    def shuffle_if_needed(self):
        if self.can_shuffle:
            self.shuffle_depleted_hand()

    @property
    def can_continue(self):
        if len(self.active_cards) > 0 or self.can_shuffle:
            return True
        else:
            return False

    def draw_four_if_possible(self) -> list:
        if self.can_draw_four:
            next_four = [self.draw_card() for _ in range(4)]
            return next_four


    @property
    def can_draw_four(self):
        if len(self.winners) + len(self.active_cards) >= 4:
            return True
        else:
            return False



