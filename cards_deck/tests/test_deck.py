import pytest
from cards_deck.game.deck import Deck, Card


@pytest.fixture
def deck():
    return Deck()


def test_deck_initialization(deck):
    assert len(deck) == 52


def test_deck_shuffle(deck):
    initial_order = str(deck)
    deck.shuffle()
    shuffled_order = str(deck)
    assert initial_order != shuffled_order


def test_deck_deal_one_card(deck):
    initial_len = len(deck)
    card = deck.deal_one_card()
    assert isinstance(card, Card)
    assert len(deck) == initial_len - 1


def test_deck_deal_all_cards(deck):
    while len(deck) > 0:
        deck.deal_one_card()
    with pytest.raises(ValueError):
        deck.deal_one_card()


def test_card_str_representation():
    card = Card(10, 'Hearts')
    assert str(card) == '10-Hearts'
