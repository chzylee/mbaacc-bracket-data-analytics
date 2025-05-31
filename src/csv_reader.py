import csv
from src.models.player_result import PlayerResult
from src.models.bracket import Bracket

def load_brackets_from_csv(csv_path):
    brackets = []
    print(f"Loading brackets from {csv_path}...")
    if not csv_path.endswith('.csv'):
        raise ValueError("The provided file is not a CSV file.")
    try:
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                bracket = Bracket(
                    name=row['Bracket Name'],
                    date=row['Date'],
                    total_entrants=int(row['Total Entrants'])
                )
                bracket.top_8_results = [
                    PlayerResult(tag=row['1st Tag'], moon=row['1st Moon'], character=row['1st Char'], placement=1),
                    PlayerResult(tag=row['2nd Tag'], moon=row['2nd Moon'], character=row['2nd Char'], placement=2),
                    PlayerResult(tag=row['3rd Tag'], moon=row['3rd Moon'], character=row['3rd Char'], placement=3),
                    PlayerResult(tag=row['4th Tag'], moon=row['4th Moon'], character=row['4th Char'], placement=4),
                    PlayerResult(tag=row['5th Tag 1'], moon=row['5th Moon 1'], character=row['5th Char 1'], placement=5),
                    PlayerResult(tag=row['5th Tag 2'], moon=row['5th Moon 2'], character=row['5th Char 2'], placement=5),
                    PlayerResult(tag=row['7th Tag 1'], moon=row['7th Moon 1'], character=row['7th Char 1'], placement=7),
                    PlayerResult(tag=row['7th Tag 2'], moon=row['7th Moon 2'], character=row['7th Char 2'], placement=7),
                ]
                brackets.append(bracket)
    except FileNotFoundError:
        print(f"Error: The file {csv_path} was not found.")
        return []
    except KeyError as e:  # Handle missing columns
        print(f"Error: Missing column in CSV file - {e}")
        return []
    except ValueError as e:  # Handle conversion errors
        print(f"Error: Invalid data in CSV file - {e}")
        return []
    except Exception as e:  # Catch-all for any other exceptions
        print(f"An unexpected error occurred: {e}")
        return []

    return brackets
