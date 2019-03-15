class Trie { // 97, 96
    Node root;
    
    class Node {
        Node[] children;
        boolean isStr;
        
        public Node() {
            children = new Node[26];
            isStr = false;
        }
    }

    /** Initialize your data structure here. */
    public Trie() {
        this.root = new Node();
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        Node ptr = root;
        for (int i = 0; i < word.length(); i++) {
            int index = word.charAt(i) - 'a';
            if (ptr.children[index] == null)
                ptr.children[index] = new Node();
            ptr = ptr.children[index];
        }
        ptr.isStr = true;
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        Node ptr = root;
        for (int i = 0; i < word.length(); i++) {
            int index  = word.charAt(i) - 'a';
            if (ptr.children[index] == null || (i == word.length() - 1 && !ptr.children[index].isStr))
                return false;
            ptr = ptr.children[index];
        }
        return true;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        Node ptr = root;
        for (int i = 0; i < prefix.length(); i++) {
            int index = prefix.charAt(i) - 'a';
            if (ptr.children[index] == null)
                return false;
            ptr = ptr.children[index];
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */