from collections import defaultdict, Counter, deque

def alienOrder( words):
    
    # Step 0: create data structures + the in_degree of each unique letter to 0.
    adj_list = defaultdict(set)
    print("adj_list",adj_list)
    in_degree = Counter({c : 0 for word in words for c in word})
    print("in_degree",in_degree)
    # Step 1: We need to populate adj_list and in_degree.
    # For each pair of adjacent words...
    print("zip 13",words, words[1:])
    for first_word, second_word in zip(words, words[1:]):
        print("first_word",first_word)
        print("second_word",second_word)
        for c, d in zip(first_word, second_word):
            
            print("c",c)
            print("d",d)
            if c != d:
                if d not in adj_list[c]:
                    adj_list[c].add(d)
                    in_degree[d] += 1
                break
        else: # Check that second word isn't a prefix of first word.
            if len(second_word) < len(first_word): return ""
    print(adj_list,'adj_list')
    # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
    output = []
    print("indgree",in_degree)
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    
    print("queue",queue)
    while queue:
        c = queue.popleft()
        output.append(c)
        for d in adj_list[c]:
            in_degree[d] -= 1
            if in_degree[d] == 0:
                queue.append(d)
                
    # If not all letters are in output, that means there was a cycle and so
    # no valid ordering. Return "" as per the problem description.
    if len(output) < len(in_degree):
        return ""
    # Otherwise, convert the ordering we found into a string and return it.
    return "".join(output)
print(alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))