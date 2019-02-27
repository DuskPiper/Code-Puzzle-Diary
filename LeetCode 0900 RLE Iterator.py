class RLEIterator: #13%
    iter = -1
    a = []
    length = 0

    def __init__(self, A):
        """
        :type A: List[int]
        """
        #for i in range(0, len(A), 2):
        #    self.a += [A[i+1]]*A[i]
        self.a = A
        for i in range(0, len(A), 2):
            self.length += A[i]
        

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.iter += n
        if self.iter >= self.length: return -1
        else: #这是效率低下的原因，每次都要从头查值。更好的解决方法是保存一个现在的state，避免每次从头
            counter = self.iter
            a = list(self.a)
            for i in range(0, len(a), 2):
                counter -= a[i]
                if counter < 0: return a[i+1]
            return a[-1]
        
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)