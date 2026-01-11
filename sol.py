#!/usr/bin/env python3
import json
import sys


def load_data(filepath: str) -> dict:
    with open(filepath, 'r') as f:
        return json.load(f)


def build_matrix_table(data: dict) -> str:
    # Get sorted list of teams for consistent ordering
    teams = sorted(data.keys())

    # Calculate column width (max of team name length and W-L format like "100-62")
    col_width = max(len(team) for team in teams)
    col_width = max(col_width, 5)  # Minimum width of 5 for W-L format

    # Build the table
    lines = []
    separator = '-' * ((col_width + 1) * (len(teams) + 1) + 1)

    header = f"{'Tm':<{col_width}}"
    for team in teams:
        header += f" {team:>{col_width}}"
    lines.append(separator)
    lines.append(header)
    lines.append(separator)

    for row_team in teams:
        row = f"{row_team:<{col_width}}"
        for col_team in teams:
            if row_team == col_team:
                cell = "--"
            else:
                # Safe access with .get() to handle missing data
                matchup = data.get(row_team, {}).get(col_team, {})
                wins = matchup.get('W')
                losses = matchup.get('L')

                if wins is None or losses is None:
                    cell = "NA"
                else:
                    cell = f"{wins}-{losses}"
            row += f" {cell:>{col_width}}"
        lines.append(row)

    lines.append(separator)

    return '\n'.join(lines)


def main():
    filepath = sys.argv[1] if len(sys.argv) > 1 else 'sample_data.json'
    
    try:
        data = load_data(filepath)
        table = build_matrix_table(data)
        print(table)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in '{filepath}'.")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Missing expected data key: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()