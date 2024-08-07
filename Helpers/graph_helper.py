import community as community_louvain
import networkx as nx
import numpy as np
import pandas as pd

def graph_global_measures(g, pop_name):
    """ """

    weighted_degree_count = nx.degree(g, weight="count")
    ave_weighted_degree_count = np.mean([k for k in dict(weighted_degree_count).values()])

    weighted_degree_time = nx.degree(g, weight="total_interaction_times")
    ave_weighted_degree_time = np.mean([k for k in dict(weighted_degree_time).values()])

    deg_list = [g.degree(node) for node in list(g.nodes)]
    average_degree = np.mean(deg_list)

    standard_deviation_degree = round(np.std(deg_list))

    clustering_coeff = nx.clustering(g)
    average_cl_coeff_unweighted = np.mean([k for k in clustering_coeff.values()])
    clustering_coeff_w_count = nx.clustering(g, weight="count")
    average_cl_coeff_w_count = np.mean([k for k in clustering_coeff_w_count.values()])
    clustering_coeff_w_duration = nx.clustering(g, weight="total_interaction_times")
    average_cl_coeff_w_duration = np.mean([k for k in clustering_coeff_w_duration.values()])

    betweenness_centrality = nx.betweenness_centrality(g)
    average_betw_cent_unweighted = np.mean([k for k in betweenness_centrality.values()])
    betweenness_c_w_count = nx.betweenness_centrality(g, weight="count")
    average_betw_c_w_count = np.mean([k for k in betweenness_c_w_count.values()])
    betweenness_c_w_duration = nx.betweenness_centrality(g, weight="total_interaction_times")
    average_betw_c_w_duration = np.mean([k for k in betweenness_c_w_duration.values()])

    closeness_centrality_unweighted = nx.closeness_centrality(g)
    ave_closeness_cent_unw = np.mean([k for k in closeness_centrality_unweighted.values()])
    closeness_c_w_count = nx.closeness_centrality(g, distance="count")
    ave_closeness_c_w_count = np.mean([k for k in closeness_c_w_count.values()])
    closeness_c_w_duration = nx.closeness_centrality(g, distance="total_interaction_times")
    ave_closeness_c_w_duration = np.mean([k for k in closeness_c_w_duration.values()])
    
    partition = community_louvain.best_partition(g.to_undirected())
    try:
        newman_modularity_unweighted = community_louvain.modularity(
            partition, g.to_undirected(), weight=None
        )
        newman_modularity_count = community_louvain.modularity(
            partition, g.to_undirected(), weight="count"
        )
        newman_modularity_duration = community_louvain.modularity(
            partition, g.to_undirected(), weight="total_interaction_times"
        )
        
    except BaseException:
        newman_modularity_unweighted, newman_modularity_count, newman_modularity_duration = 0, 0, 0

    d = {
        "Total edges": g.number_of_edges(),
        "Average degree weight=count": ave_weighted_degree_count,
        "Average degree weight=duration(seconds)": ave_weighted_degree_time,
        "Average clustering coefficient unweighted": average_cl_coeff_unweighted,
        "Average clustering coefficient weight=count": average_cl_coeff_w_count,
        "Average clustering coefficient weight=duration(seconds)": average_cl_coeff_w_duration,
        "Average betweenness centrality unweighted": average_betw_cent_unweighted,
        "Average betweenness centrality weight=count": average_betw_c_w_count,
        "Average betweenness centrality weight=duration(seconds)": average_betw_c_w_duration,
        "Average closseness centrality unweighted": ave_closeness_cent_unw,
        "Average closseness centrality weight=count": ave_closeness_c_w_count,
        "Average closseness centrality weight=duration(seconds)": ave_closeness_c_w_duration,
        "Newman modularity unweighted": newman_modularity_unweighted,
        "Newman_modularity weight=count": newman_modularity_count,
        "Newman_modularity weight=dration(seconds)": newman_modularity_duration,
    }

    df = pd.DataFrame(d, index=[pop_name.replace(".gml", "")])
    df = df.T

    return df