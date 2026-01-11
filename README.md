# Head-to-Head Records Matrix Generator

A Python solution that generates a matrix table displaying head-to-head win records between teams from JSON data.

## Problem

Given a JSON file containing each team's win-loss records versus opponents, build a table displaying a matrix of head-to-head records.

## Solution Overview

### Approach

The solution uses a straightforward approach:

1. **Load Data**: Read the JSON file containing team records
2. **Extract Teams**: Get a sorted list of all team names from the dictionary keys
3. **Build Matrix**: Iterate through each team pair (row × column) to construct the table
4. **Format Output**: Display wins for each matchup, with "--" for self-matchups

### Key Data Structures

- **Input**: Nested dictionary where:
  - Outer keys = team names
  - Inner keys = opponent names
  - Values = dictionaries with 'W' (wins) and 'L' (losses)

- **Output**: Formatted string table with teams on both axes

### Algorithm

```
for each row_team in teams:
    for each col_team in teams:
        if row_team == col_team:
            display "--"
        else:
            display data[row_team][col_team]['W']
```

Time Complexity: O(n²) where n = number of teams
Space Complexity: O(n²) for the output string

## Usage

```bash
# Run with default sample_data.json
python sol.py

# Run with custom JSON file
python sol.py your_data.json
```

## Example Output

```
---------------------------------
Tm   BRO BSN CHC CIN NYG PHI PIT STL
---------------------------------
BRO   --  10  15  15  14  14  15  11
BSN   12  --  13  13  13  14  12   9
CHC    7   9  --  12   7  16   8  10
CIN    7   9  10  --  13  13  13   8
NYG    8   9  15   9  --  12  15  13
PHI    8   8   6   9  10  --  13   8
PIT    7  10  14   9   7   9  --   6
STL   11  13  12  14   9  14  16  --
---------------------------------
Tm   BRO BSN CHC CIN NYG PHI PIT STL
---------------------------------
```

## JSON Data Format

```json
{
  "TEAM1": {
    "TEAM2": { "W": 10, "L": 12 },
    "TEAM3": { "W": 15, "L": 7 }
  },
  "TEAM2": {
    "TEAM1": { "W": 12, "L": 10 },
    "TEAM3": { "W": 8, "L": 14 }
  }
}
```
