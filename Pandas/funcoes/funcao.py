import pandas as pd 
import os 
from pathlib import Path

def importbase(nome = 'houses_to_rent.csv' ):
    p = Path(os.getcwd())
    base = str(p.parent) + f"\\data\\{nome}"
    return pd.read_csv(base)

importbase('houses_to_rent.csv').head()