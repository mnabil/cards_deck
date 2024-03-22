# Deck of Cards Problem
## Info about service
An API which lets you deal cards from a deck , shuffle cards using FastAPI and Uvicorn in Python3

(Just a demonstration for making a big project from small problems such as the deck of cards problem)

## Local Run

```bash
pip install -r requirements.txt && uvicorn cards_deck.game.app:app --reload --host 0.0.0.0 --port 8000
```

## Docker Run
```bash
docker build -t pokerdeck .
```

```bash
# runs docker container with port forwarding
docker run -p 8000:8000 -d pokerdeck
```

## call API to get deck status

```bash
curl "http://localhost:8000/v1/deck_status/" -X GET # get deck status
curl "http://localhost:8000/v1/shuffle/" -X GET # shuffle deck
curl "http://localhost:8000/v1/deal/?ncards=4" -X GET # deal n cards
```

## Improvements
- Add functionality to reset deck
- Add better logging
- Add more test cases