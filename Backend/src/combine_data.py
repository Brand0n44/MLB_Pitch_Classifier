"""Combines the per-pitcher CSVs in Backend/data/ into one file."""
from pathlib import Path
import pandas as pd

folder_path = Path("Backend") / ("data")
all_files = []
for file in folder_path.glob("*.csv"):
    all_files.append(pd.read_csv(file))

combined_data_frame = pd.concat(all_files, ignore_index=True)
combined_data_frame.to_csv(Path("Backend")/("data")/("Processed_data")/'combined_pitcher_stats.csv', index=False)
