
import collections
import heapq
def networkDelayTime( times, n, k):
    graph = collections.defaultdict(list)
   
    for u,v,w in times:
        if u == v: return -1
        graph[u].append((v,w))
    if k not in graph: return -1
    
    pq = [(0,k)]    
    dict ={}
    while pq:
        step, source = heapq.heappop(pq)
        print(step,source,'step and source')
        if source in dict: continue
        dict[source]=step
        print(step,source,pq,dict)
        print('graph[source]',graph[source])
        for target, distance in graph[source]:
            if target not in dict:
                heapq.heappush(pq, (step+distance, target))
    return max(dict.values()) if len(dict) == n else -1

times = [[2,1,1],[2,3,1],[3,4,1]]        
print(networkDelayTime(times,4,2))        