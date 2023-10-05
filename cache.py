import json

class Cache():
    def __init__(self, data: list, limit :int):
        x = {data[i]:data.count(data[i]) for i in range(len(data))}
        self.__cache = x
        self.__limit = limit
        
        self.__cache = dict(sorted(x.items(), key=lambda item: item[1])[::-1][:min(self.__limit, len(data))])
    
    def __str__(self):
        s = 'Cache can store '+str(self.__limit)+' elements\nNow stored: '+str(len(self.__cache))+'\nData:'
        for key, value in self.__cache.items():
            s+='\nData '+ str(key)+ ' requested '+ str(value)+ ' times'
        return s
    
    def get_data(self):
        return self.__cache.keys()
    
    def add(self, data):
        if data in self.__cache.keys():
             self.__cache[data]+=1
        else:
            if len(self.__cache) < self.__limit:
                self.__cache[data] = 1
            else:
                self.__cache.popitem()
                self.__cache[data] = 1
        x = self.__cache
        self.__cache = dict(sorted(x.items(), key=lambda item: item[1])[::-1])

    def get_most_requested(self):
        x = max(self.__cache.values())
        for key, value in self.__cache.items():
            if value == x:
                return key
    
    def get_least_requested(self):
        x = min(self.__cache.values())
        for key, value in self.__cache.items():
            if value == x:
                return key
            
    def dump_cache_to_json(self):
        string = self.__cache
        
        with open("data.json", "w") as json_file:
            json.dump(string, json_file)

    def load_from_json(self):
        self.__cache = {}

        with open("data.json", "r") as json_file:
            data = json.load(json_file)
            for key, value in data.items():
                if len(self.__cache) < self.__limit:
                    self.__cache[int(key)] = value

    

        





    
    
        
