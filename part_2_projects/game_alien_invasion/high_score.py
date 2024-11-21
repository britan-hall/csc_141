import pygame
import json


# Filepath for high scores
high_scores_file = 'high_scores.json'

title_image = pygame.image.load('images\cover.jpg')

# Function to load high scores from a JSON file
def load_high_scores():
    """Loads high scores from a file, returns an empty list if the file doesn't exist or is invalid."""
    try:
        with open(high_scores_file, 'r') as f:
            data = f.read().strip()  # Strip any leading/trailing spaces or newlines
            if not data:
                return []  # If file is empty, return an empty list
            return json.loads(data)  # Parse the JSON data
    except FileNotFoundError:
        return []  # If no file, return an empty list
    except json.JSONDecodeError:
        return []  # If file is invalid, return an empty list

# Function to save high scores to a JSON file
def save_high_scores(high_scores):
    """Saves high scores to a file."""
    with open(high_scores_file, 'w') as f:
        json.dump(high_scores, f, indent=4)

# Function to update the high scores if the current score qualifies
def update_high_scores(name, score):
    """Updates the high score list if the current score is in the top 3."""
    # Load existing high scores
    high_scores = load_high_scores()

    # Append new score
    high_scores.append({'name': name, 'score': score})

    # Sort scores in descending order by score
    high_scores = sorted(high_scores, key=lambda x: x['score'], reverse=True)

    # Keep only the top 5 scores, can be changed
    high_scores = high_scores[:5]

    # Save the updated high scores
    save_high_scores(high_scores)