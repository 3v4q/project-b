import numpy as np
import pandas as pd
import sys


# Grab CSV filename from arg list
# TODO: validate argv length
csv_filename = sys.argv[1]

# Load CSV into a dataframe
df = pd.read_csv(csv_filename)

# For now, just print the column names to see if we loaded the CSV properly
print(df.columns)