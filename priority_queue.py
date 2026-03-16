class PriorityQueue:
    def __init__(s): s.heap = []; s.index_map = {}
    def push(s, item, priority):
        entry = [priority, item]; s.heap.append(entry)
        idx = len(s.heap) - 1; s.index_map[item] = idx; s._sift_up(idx)
    def pop(s):
        if not s.heap: raise IndexError("empty")
        s._swap(0, len(s.heap) - 1)
        priority, item = s.heap.pop(); del s.index_map[item]
        if s.heap: s._sift_down(0)
        return item, priority
    def peek(s): return s.heap[0][1], s.heap[0][0] if s.heap else (None, None)
    def decrease_key(s, item, new_priority):
        idx = s.index_map[item]; s.heap[idx][0] = new_priority; s._sift_up(idx)
    def _swap(s, i, j):
        s.heap[i], s.heap[j] = s.heap[j], s.heap[i]
        s.index_map[s.heap[i][1]] = i; s.index_map[s.heap[j][1]] = j
    def _sift_up(s, i):
        while i > 0:
            parent = (i - 1) // 2
            if s.heap[i][0] < s.heap[parent][0]: s._swap(i, parent); i = parent
            else: break
    def _sift_down(s, i):
        n = len(s.heap)
        while True:
            smallest = i; l = 2*i+1; r = 2*i+2
            if l < n and s.heap[l][0] < s.heap[smallest][0]: smallest = l
            if r < n and s.heap[r][0] < s.heap[smallest][0]: smallest = r
            if smallest != i: s._swap(i, smallest); i = smallest
            else: break
    def __len__(s): return len(s.heap)
    def __bool__(s): return bool(s.heap)
def demo():
    pq = PriorityQueue()
    for item, pri in [("task_c", 3), ("task_a", 1), ("task_e", 5), ("task_b", 2), ("task_d", 4)]:
        pq.push(item, pri)
    print(f"Peek: {pq.peek()}")
    pq.decrease_key("task_e", 0)
    while pq:
        item, pri = pq.pop(); print(f"  {item} (priority={pri})")
if __name__ == "__main__": demo()
