class RandomizedSet { // 95, 98
    Map<Integer, Integer> map; // val -> index@list O(1)
    List<Integer> list; // val (index -> val O(1))
    Random random;

    /** Initialize your data structure here. */
    public RandomizedSet() {
        this.map = new HashMap<Integer, Integer>();
        this.list = new ArrayList<Integer>();
        this.random = new Random();
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public boolean insert(int val) {
        if (map.containsKey(val))
            return false;
        this.map.put(val, this.list.size());
        this.list.add(val);
        return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public boolean remove(int val) {
        if (!map.containsKey(val))
            return false;
        // Swap val to the tail of list and delete
        int index = this.map.get(val);
        int lastVal = this.list.get(this.list.size() - 1);
        this.list.set(index, lastVal);
        this.map.put(lastVal, index);
        
        this.list.remove(this.list.size() - 1);
        this.map.remove(val);
        return true;
    }
    
    /** Get a random element from the set. */
    public int getRandom() {
        return this.list.get(this.random.nextInt(this.list.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */