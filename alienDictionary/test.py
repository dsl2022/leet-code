from collections import defaultdict

adj_list = defaultdict(set)
adj_list['one'].add(1)
adj_list['one'].add(2)
print(adj_list)