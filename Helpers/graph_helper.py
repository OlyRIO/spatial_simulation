import community as community_louvain
import networkx as nx
import numpy as np
import pandas as pd


def calculate_weighted_in_degree(g, weight_value):
    in_degrees = {}

    for node in g.nodes:
        in_degree = 0

        in_edges = g.in_edges(node, data=True)
        for edge in in_edges:
            _, _, data = edge
            in_degree += data.get(weight_value, 0)

        in_degrees[node] = in_degree

    return in_degrees


def calculate_weighted_out_degree(g, weight_value):
    out_degrees = {}

    for node in g.nodes:
        out_degree = 0

        out_edges = g.out_edges(node, data=True)
        for edge in out_edges:
            _, _, data = edge
            out_degree += data.get(weight_value, 0)

        out_degrees[node] = out_degree

    return out_degrees


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


def group_comm_stats(G, group_name, weight):
    """Graph partitions found using Louvian algorithm."""
    partition = community_louvain.best_partition(G, weight=weight)

    communities, count = [], 0.0
    for c in set(partition.values()):
        count += 1.0
        list_nodes = [n for n in partition.keys() if partition[n] == c]
        communities.append(list_nodes)

    communities.sort(key=len, reverse=True)

    single_element_comm = len([c for c in communities if len(c) == 1])
    all_comm_len_no_sing = [len(com) for com in communities if len(com) > 1]
    ave_comm_size_no_sing = sum(all_comm_len_no_sing) / len(all_comm_len_no_sing)

    if len(communities) > 1:
        second_biggest_community = len(communities[1])
    else:
        second_biggest_community = 0

    d = {
        "number of nodes: ": len(G.nodes()),
        "comm_size=1 (single nodes):": single_element_comm,
        "percentage of single nodes: ": float(single_element_comm / len(G.nodes())),
        "number of communities: ": len(communities),
        "comm_size>1": len(communities) - single_element_comm,
        "biggest_community_size:": len(communities[0]),
        "second_biggest_community:": second_biggest_community,
        "ave_comm_size_no_sing:": ave_comm_size_no_sing,
    }

    col_name = group_name.replace(".gml", "")
    df = pd.DataFrame(d, index=[f"{col_name} weight={weight}"])

    return df.T


def get_selectivity(g):
    # selectivity = strenth / degree
    pass


def get_interaction_duration(g):
    pass


def get_interaction_rate(g):
    pass
    # CONFIG_PATH = os.path.join(settings.CONFIG_DIR, "main.toml")
    # with open(CONFIG_PATH, "r") as file:
    #     config = toml.load(file)

    # edges_weights = nx.degree(g, weight="count")

    # return edges_weights


def local_measures_functions():
    """Return list of tuples. Each tuple consists of two values.
    First one is string name of the funciton and second is function.

    Returns:
        list: list of tuples
    """

    graph_functions = [
        ("Degree centrality", lambda g: nx.degree_centrality(g)),
        ("In-degree centrality", lambda g: nx.in_degree_centrality(g)),
        ("Out-degree centrality", lambda g: nx.out_degree_centrality(g)),
        ("Eigenvector centrality", lambda g: nx.eigenvector_centrality(g)),
        ("Closeness centrality", lambda g: nx.closeness_centrality(g)),
        ("In-Strength distribution, w=count", lambda g: calculate_weighted_in_degree(g, "count")),
        (
            "Out-Strength distribution, w=count",
            lambda g: calculate_weighted_out_degree(g, "count"),
        ),
        (
            "In-Strength distribution, w=duration",
            lambda g: calculate_weighted_in_degree(g, "total_interaction_times"),
        ),
        (
            "Out-Strength distribution, w=duration",
            lambda g: calculate_weighted_out_degree(g, "total_interaction_times"),
        ),
        ("Weighted Degree (count)", lambda g: dict(nx.degree(g, weight="count"))),
        (
            "Weighted Degree (duration(seconds))",
            lambda g: dict(nx.degree(g, weight="total_interaction_times")),
        ),
        ("In-degree", lambda g: dict(g.in_degree())),
        ("Out-degree", lambda g: dict(g.out_degree())),
        ("Selectivity", lambda g: get_selectivity(g)),
        ("Betweenness centrality w=None", lambda g: nx.betweenness_centrality(g, weight=None)),
        ("Betweenness centrality w=count", lambda g: nx.betweenness_centrality(g, weight="count")),
        (
            "Betweenness centrality w=duration(seconds)",
            lambda g: nx.betweenness_centrality(g, weight="total_interaction_times"),
        ),
        ("Clustering coefficient w=None", lambda g: nx.clustering(g, weight=None)),
        ("Clustering coefficient w=count", lambda g: nx.clustering(g, weight="count")),
        (
            "Clustering coefficient w=duration(seconds)",
            lambda g: nx.clustering(g, weight="total_interaction_times"),
        ),
        ("PageRank centrality", lambda g: nx.pagerank(g)),
    ]

    return graph_functions