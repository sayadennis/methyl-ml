import numpy as np
import pandas as pd
import sklearn

# Load data
dn = "/projects/p30791/methylation"
betas = pd.read_csv(f"{dn}/sesame_data/betas_processed.csv", index_col=0, nrows=2000)
meta = pd.read_csv(f"{dn}/raw_data/meta.csv")

# Select only CUB/HDB
meta = meta.iloc[[x in ["CUB", "HDB"] for x in  meta["Sample Region"].values],:]
betas = betas.iloc[:,[x in meta.IDAT.values for x in betas.columns]]

# Only use probes without missing values
betas = betas.dropna(axis=0)

# Define functions

# Train & evaluate ML


