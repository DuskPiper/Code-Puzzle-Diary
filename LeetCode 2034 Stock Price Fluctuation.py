from sortedcontainers import SortedDict

class StockPrice: # 45%, 12%

    def __init__(self):
        # 两个TreeMap
        self.timeToPrice = SortedDict() # 时间->价格，key已排序
        self.priceToTimes = SortedDict() # 价格->Set<该价格的时间>，key已排序
        

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.timeToPrice: # 时间已存在，是更新价格
            oldPrice = self.timeToPrice[timestamp]
            self.priceToTimes[oldPrice].remove(timestamp) # 去掉老的价格中的时间，因为已失效
            if not self.priceToTimes[oldPrice]: # 如果老价格不再对应任何时间，去除key
                self.priceToTimes.pop(oldPrice)
            
        self.timeToPrice[timestamp] = price # 更新/新建 时间->价格
        if not price in self.priceToTimes: # 更新/新建 价格->时间们
            self.priceToTimes[price] = set()
        self.priceToTimes[price].add(timestamp)
        
                
        

    def current(self) -> int:
        return self.timeToPrice.peekitem(-1)[1] # 找最大的时间key，得到其对应价格
        

    def maximum(self) -> int:
        return self.priceToTimes.peekitem(-1)[0] # 找最大的价格key，得到key
        

    def minimum(self) -> int:
        return self.priceToTimes.peekitem(0)[0] # 找最小的价格key，得到key
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
