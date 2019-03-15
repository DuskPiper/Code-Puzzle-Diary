class Solution {
    public int coinChange(int[] coins, int amount) { // 20, 67
        // DP
        List<Integer> validCoins = new LinkedList<Integer>();
        int[] minStepAtI = new int[amount + 1];  
        for (int c : coins) // find valid coins
            if (c <= amount)
                validCoins.add(c);
        Arrays.fill(minStepAtI, Integer.MAX_VALUE); // set default values to MAXINT (meaning no path, should return -1)
        minStepAtI[0] = 0;
        
        for (int i = 0; i < amount; i++) {
            if (minStepAtI[i] != Integer.MAX_VALUE) { // if cur step is formerly accessible
                for (int coin : validCoins) { // go forward for all possible steps
                    int nextStep = i + coin; // cur next step
                    if (nextStep <= amount) { // make sure not overflow the array
                        minStepAtI[nextStep] = Math.min(minStepAtI[nextStep], minStepAtI[i] + 1); // renew value if shorter access to next step
                    }
                }
            }
        }
        return minStepAtI[amount] == Integer.MAX_VALUE ? -1 : minStepAtI[amount];
    }
}