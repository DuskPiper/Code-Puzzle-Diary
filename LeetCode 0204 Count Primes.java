public class Solution {
    public int countPrimes(int n) { // 78, 75
        boolean[] notPrime = new boolean[n]; // initialized as true
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (notPrime[i] == false) { // prime num encountered
                count++;
                for (int j = 2; i * j < n; j++)
                    notPrime[i * j] = true; // calculate future non-primes based on current factor
            }
        }
        return count;
    }
}