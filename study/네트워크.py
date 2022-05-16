# def solution(n, computers):
#     temp =[]
#     for i in range(n):
#         network = [i]
#         for j in range(n):
#             if computers[i][j] == 1:
#                 network.append(j)
        
#         if len(temp) != 0:
#             if list(temp[-1]) in network:    
#                 temp.pop()
#                 temp.append(tuple(set(network)))

#             elif network in list(temp[-1]):
#                 network = []

#             else:
#                 temp.append(tuple(set(network)))
#         else:
#             continue
    
#     print(temp)
#     return len(temp)

def solution(n, computers):
    temp =[]
    for i in range(n):
        network = [i]
        for j in range(n):
            if computers[i][j] == 1:
                network.append(j)
        temp.append((set(network)))
    
    # print(temp)
    queue = [temp[0]]
    for i in range(1,len(temp)):
        
        if queue[-1] | temp[i] == temp[i]:
            queue.pop()
            queue.append(temp[i])
        elif temp[i] | queue[-1] == queue[-1]:
            continue
        else:
            queue.append(temp[i])

    # print(queue)
    return len(queue)

print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))