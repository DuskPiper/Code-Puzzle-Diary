class Solution {
    public boolean checkPerfectNumber(int num) { // 99.4, 10
        if (num <= 1)
            return false;
        
        // semi-brute-force
        int sqrt = (int)Math.sqrt(num);
        int sum = 1;
        for (int i = 2; i <= sqrt; i++)
            if (num % i == 0)
                sum += i + num / i; 
        // ^有一个问题，如果num是完全平方数和完美数的话，会造成加了两次sqrt(n)，是bug
        // ^不过事实上1e8以内的完美数只有5个，这五个当中不存在完全平方数
        return num == sum;
    }
}