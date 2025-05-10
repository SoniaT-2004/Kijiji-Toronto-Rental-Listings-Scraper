import pandas as pd
import re

df = pd.read_csv("kijiji.csv")

def extract_fsa(addr):
    match = re.search(r"[A-Z]\d[A-Z]", addr)
    return match.group(0) if match else "Unknown"

df["FSA"] = df["Address"].apply(extract_fsa)

df.to_csv("kijiji.csv", index=False)
