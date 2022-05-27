def solution(cacheSize, cities):
    answer = 0
    hitCnt = dict()
    cache = set()
    l = len(cities)
    if not cacheSize:
        return 5 * l
    idx = 0
    while len(cache) != cacheSize:
        city = cities[idx].lower()
        hitCnt[city] = idx
        if city in cache:
            answer += 1
        else:
            cache.add(city)
            answer += 5
        idx += 1
        if idx == l:
            break

    while idx < l:
        city = cities[idx].lower()
        hitCnt[city] = idx
        if city in cache:
            answer += 1
        else:
            if len(cache) < cacheSize:
                cache.add(city)
            else:
                min_city = ""
                cur = l
                for c in cache:
                    if hitCnt[c] < cur:
                        cur = hitCnt[c]
                        min_city = c
                cache.discard(min_city)
                cache.add(city)
            answer += 5
        idx += 1

    return answer