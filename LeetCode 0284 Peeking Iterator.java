// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html
class PeekingIterator implements Iterator<Integer> { // 94, 27
    private Iterator iter; // 在用户以为的位置的下一位
    private Integer next = null;

	public PeekingIterator(Iterator<Integer> iterator) {
	    // initialize any member here.
	    iter = iterator;
        if (iter.hasNext())
            next = (Integer)iter.next(); // collection[1]，此时iter已经移到下一位([1]的位置)，但用户会以为还在[0]
	}

    // Returns the next element in the iteration without advancing the iterator.
	public Integer peek() {
        return next;
	}

	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	@Override
	public Integer next() {
	    Integer ans = next;
        if (iter.hasNext())
            next = (Integer)iter.next();
        else
            next = null;
        return ans;
	}

	@Override
	public boolean hasNext() {
	    return next != null;
	}
}