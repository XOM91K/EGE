l = [d.strip().split('\t') for d in open('1.txt')]
sl = {}
for x in l:
    sl[int(x[0])] = [int(x[1]), [int(d) for d in x[2].split(';')], []]
print(sl)
for x in sl:
    if len(sl[x][1]) == 1 and sl[x][1][0] != 0:
        sl[sl[x][1][0]][-1].append(sl[x][0])
groups = []
for x in sl:
    if sl[x][1][0] == 0:
        groups.append([x])
    else:
        inds = []
        new_group = [x]
        for y in sl[x][1]:
            gg = sl[x][1]

            i = 0
            for z in range(len(groups)):
                if y in groups[z]:
                    inds.append(z)
                    new_group.append(y)
        groups.append(list(set(new_group)))

print(groups)




# for_sort = {}
# for x in sl:
#     for_sort[x] = [] if sl[x][1][0] == 0 else sl[x][1]








# def topological_sort(graph):
#     visited = set()
#     stack = []
#     def dfs(node):
#         visited.add(node)
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 dfs(neighbor)
#         stack.append(node)
#     for node in list(graph.keys()):  # Создаем копию ключей словаря
#         if node not in visited:
#             dfs(node)
#     return stack[::-1]
# sorted_processes = topological_sort(for_sort)
# print(sorted_processes)
# groups = []
# for x in sl:
#     if sl[x][1][0] == 0:
#         groups.append([])

#[10, 12, 9, 11, 2, 1, 3, 5, 6, 4, 7, 8]

# from collections import defaultdict
#
# def topological_sort(graph):
#     visited = set()
#     stack = []
#
#     def dfs(node):
#         visited.add(node)
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 dfs(neighbor)
#         stack.append(node)
#
#     for node in list(graph.keys()):  # Создаем копию ключей словаря
#         if node not in visited:
#             dfs(node)
#
#     return stack[::-1]
#
# def max_parallel_time(processes):
#     graph = defaultdict(list)
#     for process in processes:
#         for dependency in process[2]:
#             graph[dependency].append(process[0])
#
#     sorted_processes = topological_sort(graph)
#     end_times = {}
#     for process in sorted_processes:
#         dependencies_times = [end_times.get(dependency, 0) for dependency in processes[process-1][2]]
#         end_times[process] = processes[process-1][1] + max(dependencies_times) if dependencies_times else processes[process-1][1]
#
#     max_times = [0] * 5
#     for process in sorted_processes:
#         max_times[1] = max(max_times[1], processes[process-1][1])
#         for i in range(2, 5):
#             if not graph[process]:
#                 max_times[i] = max(max_times[i], processes[process-1][1] + max_times[i-1])
#
#     return max_times[4]
#
# processes = [
#     [1, 4, []],
#     [2, 3, []],
#     [3, 5, [1, 2]],
#     [4, 7, [3]],
#     [5, 6, [3]],
#     [6, 2, [5]],
#     [7, 5, [4, 6]],
#     [8, 2, [7]],
#     [9, 7, []],
#     [10, 8, []],
#     [11, 6, [9]],
#     [12, 6, [10]]
# ]
#
# result = max_parallel_time(processes)
# print("Максимальное время параллельного выполнения четырех процессов:", result, "секунд")
