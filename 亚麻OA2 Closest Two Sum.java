class Solution {
    public static int[] closestTwoSum(int[] numbers, int target) {
        Arrays.sort(numbers);
        int h = numbers.length - 1;
        int l = 0; // pointers low and high
        int closestDiff = Integer.MAX_VALUE;
        int[] ans = new int[2];
        while (l < h) {
            int curSum = numbers[h] + numbers[l];
            int curDiff = target - curSum;
            if (curDiff < closestDiff> && curDiff >= 0) { // found better
                ans[0] = numbers[l];
                ans[1] = numbers[h];
                closestDiff = curDiff;
            }

            if (curDiff < 0) h --;
            else l ++;
        }
        return ans;
    }
}