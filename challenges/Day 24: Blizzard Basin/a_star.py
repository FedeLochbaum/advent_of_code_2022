from queue import PriorityQueue

def a_star(graph, initialNode, h):
  pqueue = PriorityQueue()
  _min = float('inf')
  visited = set()
  pqueue.put((h(initialNode), initialNode, 0)) # priority, pos, steps
  while not pqueue.empty():
    priority, node, deep = pqueue.get_nowait()
    if h(node) == 0:
      _min = min(_min, deep); print('min: ', _min); continue
    for edge_label, target_node in graph[node].items():
      if str(target_node) not in visited:
        visited.add(str(target_node))
        pqueue.put((
          priority + h(target_node),
          target_node,
          path + [edge_label]
        ))
  return _min