# Movie Recommendation System

A modern, robust movie recommendation web application built with Flask and Scikit-learn.

## Features
- **Smart Recommendations**: Uses Cosine Similarity to find movies with similar themes, actors, and directors.
- **Premium UI**: Modern dark-themed design with glassmorphism and smooth interactions.
- **Robust Integration**: Ready for TMDB/OMDB API integration for real-time movie data.
- **Sentiment Analysis**: Analyzes IMDB user reviews to provide a "Good" or "Bad" sentiment rating.

## Setup

1. **Clone the Repo** (if you haven't already).
2. **Setup environment**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure API Keys** (Optional but recommended):
   - Copy `.env.example` to `.env`.
   - Add your TMDB API key to `.env`.
4. **Run the App**:
   ```bash
   python main.py
   ```
   The app will start at `http://127.0.0.1:5000`.

## Directory Structure
- `main.py`: The heart of the application.
- `templates/`: HTML templates for the frontend.
- `static/`: CSS and JS files for styling and interactivity.
- `main_data.csv`: Sample dataset for the recommendation engine.
- `.env`: Configuration for API keys.

## Improvements Made
- **Refactored Code**: Improved error handling and modularity.
- **Modernized UI**: Transitioned from a basic design to a premium, responsive interface.
- **Robust Data Handling**: Replaced fragile string parsing with standard JSON handling.
- **Directory Cleanup**: Renamed directory and removed redundant duplicate files.