# Head-to-Head Records Matrix Generator

A Python solution that generates a matrix table displaying head-to-head win-loss records between teams from JSON data.

## Problem

Given a JSON file containing each team's win-loss records versus opponents, build a table displaying a matrix of head-to-head records.

## Solution Overview

### Approach

The solution uses a straightforward approach:

1. **Load Data**: Read the JSON file containing team records
2. **Extract Teams**: Get a sorted list of all team names from both outer and inner dictionary keys
3. **Build Matrix**: Iterate through each team pair (row × column) to construct the table
4. **Format Output**: Display W-L records for each matchup, with "--" for self-matchups
5. **Handle Missing Data**: If a matchup is missing or lacks W/L values, display "NA"

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
            matchup = data.get(row_team, {}).get(col_team, {})
            W = matchup.get('W')
            L = matchup.get('L')
            if W is None or L is None:
                display "NA"
            else:
                display "W-L"
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
-------------------------------------------------------------------------
Tm          BRO     BSN     CHC     CIN     NYG     PHI     PIT     STL
-------------------------------------------------------------------------
BRO          --   10-12    15-7    15-7    14-8    14-8    15-7   11-11
BSN       12-10      --    13-9    13-9    13-9    14-8   12-10    9-13
CHC        7-15    9-13      --   12-10    7-15    16-6    8-14   10-12
CIN        7-15    9-13   10-12      --    13-9    13-9    13-9    8-14
NYG        8-14    9-13    15-7    9-13      --   12-10    15-7    13-9
PHI        8-14    8-14    6-16    9-13   10-12      --    13-9    8-14
PIT        7-15   10-12    14-8    9-13    7-15    9-13      --    6-16
STL       11-11    13-9   12-10    14-8    9-13    14-8    16-6      --
-------------------------------------------------------------------------
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
