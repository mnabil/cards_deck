# FastAPI
from fastapi import FastAPI
import uvicorn
import os

from cards_deck.game.log_conf import Logger
from cards_deck.game.deck import Deck

# Create a FastAPI app
app = FastAPI()

deck = Deck()  # Create a deck of cards
Logger.debug("Deck created: %s" % deck)


@app.get("/v1/deck_status/", tags=["Deck"])
async def deck_status():
    """gets the deck status, gives length of deck so far"""
    return {"message": "Length of the deck: %s" % len(deck), "deck": str(deck)}


@app.get("/v1/shuffle/", tags=["Shuffle"])
async def shuffle_deck():
    """Shuffle the deck of cards"""
    deck.shuffle()
    Logger.debug("Deck shuffles , Deck: %s" % deck)
    return {"message": "Shuffling the deck of cards, Done!"}


@app.get("/v1/deal/", tags=["Deal"])
async def deal_card(ncards: int = 1):
    """Deal n cards from the deck"""
    dealt_cards = []
    # in case my query is bigger than my remaining cards, deal the whole deck
    if ncards > len(deck):
        ncards = len(deck)
    try:
        for i in range(ncards):
            dealt_card = deck.deal_one_card()
            dealt_cards.append(str(dealt_card))
            Logger.debug(
                "Dealing %s card[s], << %s >> \n Remaining cards: %s" %
                (ncards, dealt_cards, len(deck)))
        return {
            "message": f"Dealing {ncards} card[s]: {', '.join(dealt_cards)}, Number of Remaining cards: {len(deck)}"}
    except ValueError as e:  # exception handeling
        return {"message": str(e)}


def main(reload: bool = False) -> None:
    """Run the FastAPI server."""
    uvicorn.run(
        app,  # need string to be able to use reload
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", "8000")),
        reload=reload,
    )
