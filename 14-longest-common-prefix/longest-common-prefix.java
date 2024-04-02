class Solution {
    public String longestCommonPrefix(String[] strs) {

        StringBuilder longPrefix = new StringBuilder();

        //sort the arrays
        Arrays.sort(strs);

        //get the first and last strings
        char[] first = strs[0].toCharArray();
        char[] last = strs[strs.length-1].toCharArray();

        //start comparing the first and last word characters

        for(int i=0;i<first.length;i++){
            if(first[i]!=last[i])
            break;

            longPrefix.append(first[i]);
        }

        return longPrefix.toString();
        
    }
}