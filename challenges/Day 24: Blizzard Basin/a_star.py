from queue import PriorityQueue

def a_star(graph, initialNode, h):
  pqueue = PriorityQueue()
  _min = float('inf')
  visited = set()
  pqueue.put((h(initialNode), initialNode, 1)) # priority, pos, time
  while not pqueue.empty():
    priority, node, time = pqueue.get_nowait()
    if h(node) == 0:
      if (time < _min): print('min: ', time); _min = min(_min, time); continue
    for target_node in graph[(node, time)]:
      if (target_node, time) not in visited:
        visited.add((target_node, time))
        pqueue.put((
          priority + h(target_node),
          target_node,
          time + 1
        ))
  return _min