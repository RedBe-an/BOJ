from collections import defaultdict, deque


def bfs(start, graph, n):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    count = 0

    while queue:
        node = queue.popleft()
        count += 1

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return count - 1


def main():

    n, m = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[b].append(a)

    max_count = 0
    result = []

    for i in range(1, n + 1):
        count = bfs(i, graph, n)

        if count > max_count:
            max_count = count
            result = [i]
        elif count == max_count:
            result.append(i)

    print(" ".join(map(str, sorted(result))))


if __name__ == "__main__":
    main()
