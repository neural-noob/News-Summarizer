News Fetcher Python App
A lightweight Python application that fetches live news articles based on user-defined topics using the News API.

Features
Topic-Based Search: Search for news headlines globally on any specific topic.

Environment Security: Uses python-dotenv to keep sensitive API keys secure.

Direct API Integration: Connects directly with the OpenWeatherMap and News API infrastructure.

Prerequisites
Python 3.x

News API Key: Obtain a free key from NewsAPI.org.

Installation & Setup
Clone the Repository:

Bash
git clone https://github.com/yourusername/news-fetcher.git
cd news-fetcher
Install Dependencies:
You will need the requests and python-dotenv libraries.

Bash
pip install requests python-dotenv
Configure Environment Variables:

Create a file named .env in the root directory.

Add your API key to the file:

Plaintext
NEWS_API_KEY=your_actual_api_key_here
Usage
Run the script using the following command:

Bash
python news.py
When prompted, enter a topic (e.g., "technology", "Banaras", or "software development").

The script will display the top 5 articles related to that topic.

Type quit or exit to close the application.

Project Structure
news.py: The main Python script containing the fetch logic.

.env: (Private) Stores your API credentials.

.gitignore: Prevents the .env file from being uploaded to GitHub.

.env.example: A template for other users to set up their own environment.

About the Developer
Developed as part of a technical portfolio focusing on software development, Python automation, and technical documentation.
