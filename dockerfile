FROM python:3.10.11
 
# Set the working directory to /usr/src/app.
WORKDIR /usr/src/app
 
# Copy the file from the local host to the filesystem of the container at the working directory.
COPY requirements.txt ./
 
# Install Scrapy specified in requirements.txt.
RUN pip3 install --no-cache-dir -r requirements.txt
 
# Copy the project source code from the local host to the filesystem of the container at the working directory.
COPY . .

# Expose the port your app will run on
EXPOSE 8000

# Run tests using pytest
RUN pytest cards_deck/tests

# Run the crawler when the container launches.
CMD ["uvicorn", "cards_deck.game.app:app","--reload","--host","0.0.0.0","--port","8000"]
