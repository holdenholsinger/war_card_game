import random
import typing
from typing import Tuple, Dict, Any, List


class Cards:
    all_cards = [
        ('2 of Hearts', 2),
        ('3 of Hearts', 3),
        ('4 of Hearts', 4),
        ('5 of Hearts', 5),
        ('6 of Hearts', 6),
        ('7 of Hearts', 7),
        ('8 of Hearts', 8),
        ('9 of Hearts', 9),
        ('10 of Hearts', 10),
        ('J of Hearts', 11),
        ('Q of Hearts', 12),
        ('K of Hearts', 13),
        ('A of Hearts', 14),
        ('2 of Diamonds', 2),
        ('3 of Diamonds', 3),
        ('4 of Diamonds', 4),
        ('5 of Diamonds', 5),
        ('6 of Diamonds', 6),
        ('7 of Diamonds', 7),
        ('8 of Diamonds', 8),
        ('9 of Diamonds', 9),
        ('10 of Diamonds', 10),
        ('J of Diamonds', 11),
        ('Q of Diamonds', 12),
        ('K of Diamonds', 13),
        ('A of Diamonds', 14),
        ('2 of Clubs', 2),
        ('3 of Clubs', 3),
        ('4 of Clubs', 4),
        ('5 of Clubs', 5),
        ('6 of Clubs', 6),
        ('7 of Clubs', 7),
        ('8 of Clubs', 8),
        ('9 of Clubs', 9),
        ('10 of Clubs', 10),
        ('J of Clubs', 11),
        ('Q of Clubs', 12),
        ('K of Clubs', 13),
        ('A of Clubs', 14),
        ('2 of Spades', 2),
        ('3 of Spades', 3),
        ('4 of Spades', 4),
        ('5 of Spades', 5),
        ('6 of Spades', 6),
        ('7 of Spades', 7),
        ('8 of Spades', 8),
        ('9 of Spades', 9),
        ('10 of Spades', 10),
        ('J of Spades', 11),
        ('Q of Spades', 12),
        ('K of Spades', 13),
        ('A of Spades', 14)
    ]

    @classmethod
    def shuffle_cards(cls) -> list:
        random.shuffle(Cards.all_cards)
        return Cards.all_cards

    @classmethod
    def deal_cards(cls) -> tuple[list[all_cards], list[all_cards]]:
        shuffled_cards = Cards.shuffle_cards()
        total_cards = len(shuffled_cards)
        split_index = total_cards // 2  # Split the cards into two equal parts

        hand1 = list(shuffled_cards[:split_index])
        hand2 = list(shuffled_cards[split_index:])

        return hand1, hand2









