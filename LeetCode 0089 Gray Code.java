class Solution { 
    public List<Integer> grayCode(int n) { // 100, 100
        List<Integer> result = new ArrayList<>(1 << n);
        for (int i = 0; i < 1 << n; i ++) 
            result.add(i ^ i >> 1); //  G(i) = i^ (i/2) 算是个公式
        return result;
    }
}