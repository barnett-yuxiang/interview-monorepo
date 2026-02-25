设计一个缓存机制, LRUCache

let cache = LRUCache(capacity: 2)

cache.put(1, 1) // key=1, value=1
cache.put(2, 2) //

print(cache.get(1)) // value = 1

cache.put(1, 3)
print(cache.get(1)) // value = 3

cache.put(3, 4) // 容量已满，需淘汰最久未使用的 key=2 → 缓存: {1: [3 -> 1], 3: [4]}
print(cache.get(2)) // nil
