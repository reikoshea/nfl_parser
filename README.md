# Parse RDS files from Guga31bb

Random little tool I made to fiddle with the NFL analytics data

## Installation

Requires R to be installed.

```bash
pip install -r requirements.txt
```
## Usage

Download the RDS files from guga31bb
https://raw.githubusercontent.com/guga31bb/nflfastR-data/master/data/play_by_play_2019.rds

```bash
./convert_rds_to_csv.py [INFILE.rds] [OUTFILE.csv]

./parse_nfl.py [INFILE.csv]
```
