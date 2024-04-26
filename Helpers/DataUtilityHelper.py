import itertools

import numpy as np
import pandas as pd

def distances_between_all_flies(fly_dict):
    """Calculate distances between all pairs of flies.

    Parameters:
    - fly_dict (dict): A dictionary where keys represent fly identifiers and values represent
      DataFrames containing coordinates of the flies.

    Returns:
    - df (pd.DataFrame): A DataFrame containing distances between all pairs of flies. The column
      names are formatted as "fly1_key fly2_key", and the values represent the distances between
      the corresponding flies.
    """

    df = pd.DataFrame()
    for fly1_key, fly2_key in list(itertools.combinations(fly_dict.keys(), 2)):
        df1 = fly_dict[fly1_key].copy(deep=True)
        df2 = fly_dict[fly2_key].copy(deep=True)

        df1_x = np.array(df1["pos x"].values)
        df1_y = np.array(df1["pos y"].values)

        df2_x = np.array(df2["pos x"].values)
        df2_y = np.array(df2["pos y"].values)

        name = f"{fly1_key} {fly2_key}"

        distance = np.sqrt((df1_x - df2_x) ** 2 + (df1_y - df2_y) ** 2)
        df[name] = np.round(distance, decimals=2)

    return df