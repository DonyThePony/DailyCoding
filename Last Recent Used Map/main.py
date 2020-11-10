import cache

if __name__ == '__main__':
    cache_ = cache.Cache(2)
    print("None")
    print(cache_.put(2, 1))
    print(cache_.put(1, 1))
    print(cache_.put(2, 3))
    print(cache_.put(4, 1))
    print(cache_.get(1))
    print(cache_.get(2))
