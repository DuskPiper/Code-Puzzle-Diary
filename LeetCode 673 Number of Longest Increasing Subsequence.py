class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        本题的思路来自于LeetCode300的解答，本问题是该问题的延申，要读懂本题解题，需先读300的解题
        本质是在ll之外使用一个平行的lc，来记录该位置截止的最大子序列的数量，
            因此答案即是所有ll最大值对应的元素对应的lc之和
        lc和ll一样，是逐个生长出来的，每一项的值取决于前面所有项，生长过程是外循环，对强项的逐个考察是内循环：
            本项的最长长度当是max_so_far+1，故就是前面所有最长长度项为max_so_far的元素的lc之和
            如此递归，直到最长长度为1，便是lc值便是1
        """
        if not nums:return 0
        ll=[1]*len(nums)#ll[i]最终会是nums[i]的最长子序列长度
        lc=[0]*len(nums)#lc[i]最终会是nums[i]的最长子序列数量
        for i,n in enumerate(nums):#外循环，逐个考察，ll和lc从i=0开始生长
            max_so_far=0#循环内最大值寄存器，避免了每次去update ll[i]，这样就只需要在循环末update
            for j in range(i):#内循环，逐个扫描前序的元素
                if nums[j]<n:#前序元素<本元素，则本元素可以增补到前序元素结尾的子序列后面
                    if max_so_far<ll[j]:#考察是否是目前最长的子序列，如果不是就忽略
                        max_so_far=ll[j]#update最长值
            for j in range(i):#上面内循环得到了完整的ll[i]，现在以此计算lc[i]
                if nums[j]<n and ll[j]==max_so_far:#本质上是寻找前序列中最长的一个或几个，也就是本元素有效增补的对象
                    if max_so_far==1:lc[i]+=1#特殊情况，递归的底点，最长长度为1了，lc值便是1，因为没有超出1种可能的子序列了
                    else:lc[i]+=lc[j]#前序的一个或几个中，每一个的生成都有多种可能，生长过程中已经记录到lc[]中，查表即可
            ll[i]=max_so_far+1
        #print(ll,lc)
        m=max(ll)
        if m==1:return len(nums)
        return sum([lc[i] for i,n in enumerate(ll) if n==m])
            

        
            