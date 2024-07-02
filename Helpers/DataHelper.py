import itertools
import numpy as np
import pandas as pd
from Helpers.ConstantHelper import *
from Helpers.UtilityHelper import *

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

def getInteractionsFromColumn(col, threshold):
   columnIndices = []

   for i, num in enumerate(col, start=0):
      if num <= threshold:
         columnIndices.append(i)

   return columnIndices

def getFlyInteractions(df, distanceThreshold):

        edgelist = pd.DataFrame(
        columns=[
            "node_1",
            "node_2",
            "start_of_interaction",
            "end_of_interaction",
            "duration",
            ]
        )
        
        specific_array = df.values
        
        for column_index in range(specific_array.shape[1]):
            node_1, node_2 = df.columns[column_index].split()
            interactionMoments = getInteractionsFromColumn(specific_array[:, column_index], distanceThreshold)
            subarray = []
            result = []

            for num in interactionMoments:
                if len(subarray) == 0 or num == subarray[-1] + 1:
                    subarray.append(num)
                else:
                    if len(subarray) > 1:
                        result.append(subarray)
                    subarray = [num]

            for row in result:
                start_of_interaction = row[0]
                end_of_interaction = row[-1]
                duration = end_of_interaction - start_of_interaction
                data = {
                    "node_1": node_1,
                    "node_2": node_2,
                    "start_of_interaction": int(start_of_interaction),
                    "end_of_interaction": int(end_of_interaction),
                    "duration": int(duration),
                }

                row = pd.DataFrame.from_dict(data, orient="index").T
                edgelist = pd.concat([edgelist, row], ignore_index=True)
        
        return edgelist


def getDistancesData():
    """ Gets the real-life distances (expressed in millimeters) between the flies used to simulate data and normalizes them to
    the [0, 1] interval
    
    Returns:
    - distances (numpy.array): A numpy array containing real-life distances between flies. See the documentation for more information on 
    input data formatting.
    """

    distances = np.load(getInputDirectory() + "/distances.npy")
    normalized_distances = normalizeDistancesData(distances)

    return normalized_distances

def normalizeDistancesData(distances):
    """ Normalizes the real-life fly distances to a [0, 1] interval
    
    Returns:
    - distances_normalized  (numpy.array): A numpy array containing normalized distances between flies.
    """

    distances_normalized = distances
    f = lambda x: x * SCALING_RATIO
    distances_normalized = f(distances)

    return distances_normalized
