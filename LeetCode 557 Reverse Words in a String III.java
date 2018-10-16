//8ms,83%
class Solution {
    public String reverseWords(String s) {
        String[] st=s.split(" ");
        StringBuffer sb = new StringBuffer();
        for(String st_:st){
        StringBuffer word = new StringBuffer(st_);
            sb.append(word.reverse());
            sb.append(" ");
        }
        return sb.deleteCharAt(sb.length()-1).toString();
    }
}