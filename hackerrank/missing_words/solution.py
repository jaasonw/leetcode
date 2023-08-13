from collections import deque


def missingWords(s, t):
    s_queue = deque(s.split(" "))
    t_queue = deque(t.split(" "))

    result = []
    while s_queue and t_queue:
        if s_queue[0] == t_queue[0]:
            s_queue.popleft()
            t_queue.popleft()
        else:
            result.append(s_queue.popleft())

    result.extend(s_queue)
    print(result)
    return result
