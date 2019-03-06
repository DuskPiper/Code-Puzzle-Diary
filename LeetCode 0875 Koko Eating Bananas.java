class Solution {
    public int minEatingSpeed(int[] piles, int H) { // 14, 92
        if (piles == null || piles.length == 0) 
            return 0;
        // Binary search
        int lo = 1;
        int hi = Arrays.stream(piles).max().getAsInt();
        int mid = 1;
        while (lo < hi) {
            mid = (lo + hi) / 2;
            // Now calculate time eat at speed "mid"
            int hr = eatTime(piles, mid);
            // Now binary search
            if (hr > H) lo = mid + 1; // eat too slow, +1 to prevent infinity loop
            else hi = mid; // eat too fast || eat right at H but need to try if lower speed also does
        }
            
        return lo;
    }
    
    public int eatTime(int[] piles, int speed) {
        int time = 0;
        for (int pile : piles) {
            time += pile / speed;
            if (pile % speed > 0)
                time ++;
        }
        return time;
    }
}