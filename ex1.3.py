def func(n, cache={0:0, 1:1}):
    if n not in cache:
        cache[n] = func(n-1, cache) + func(n-2, cache)
    return cache[n]
