from fastapi.testclient import TestClient

from cards_deck.game.app import app

client = TestClient(app)


def test_shuffle_deck():
    """
    Test Shuffle deck endpoint
    """
    response = client.get("/v1/shuffle/")
    assert response.status_code == 200
    assert response.json() == {"message": "Shuffling the deck of cards, Done!"}
