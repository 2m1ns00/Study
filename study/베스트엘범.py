def solution(genre, plays):
    answer = []
    hash = {}
    temp = []
    tot = zip(list(range(len(genre))),genre,plays)

    for i, n, m in tot:
        if n in hash.keys():
            hash[n] += m   
        else:
            hash[n] = m
        temp.append((i, n, m))
        
    sort_hash = sorted(hash.items(), key = lambda x : x[1] ,reverse = True)

    for k, _ in sort_hash:
        temp_temp = []
        temp_temp = [(j,m) for j, n, m in temp if n==k]
        st = sorted(temp_temp, key = lambda x : x[1], reverse = True)   
        if len(st) >= 3:
            st = st[:2]
            
        for i in range(len(st)):
            answer.append(st[i][0])

    return print(answer)

genre = ["classic", "pop", "classic", "pop", "classic", "classic"]
play =  [1950, 600, 500, 2500, 500, 150]
solution(genre,play)