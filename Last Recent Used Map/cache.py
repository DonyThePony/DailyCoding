import time

class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = {}
        self.recently_dict = {}
        self.frequently_dict = {}

    def __update_stats(self, key):
        self.frequently_dict[key] += 1
        self.recently_dict[key] = time.time_ns()

    def __set(self, key, value):
        self.dict[key] = value
        self.frequently_dict[key] = 0
        self.recently_dict[key] = time.time_ns()

    def __get_least_recently_used_key(self):
        return min(self.recently_dict, key=self.recently_dict.get)

    def __get_least_frequently_used_key(self):
        least_frequent_use = min(self.frequently_dict)
        frequent_use_amount = sum(int(i) == least_frequent_use for i in self.frequently_dict.values())
        if frequent_use_amount != 1:
            return -1
        else:
            return min(self.frequently_dict, key=self.frequently_dict.get)

    def __get_unused_key(self):
        least_frequent_used_key = self.__get_least_frequently_used_key()
        if least_frequent_used_key != -1:
            return least_frequent_used_key
        else:
            return self.__get_least_recently_used_key()

    def put(self, key, value):
        if key in self.dict.keys():
            self.__set(key, value)
        else:
            if len(self.dict) >= self.capacity:
                unused_key = self.__get_unused_key()
                self.dict.pop(unused_key)
                self.frequently_dict.pop(unused_key)
                self.recently_dict.pop(unused_key)
            self.__set(key, value)

    def get(self, key):
        if key in self.dict.keys():
            self.__update_stats(key)
            return self.dict[key]
        else:
            return -1


