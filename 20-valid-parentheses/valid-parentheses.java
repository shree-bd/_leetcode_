// Timecomplexity : O[s] | Space complexity: O[s]  where s is length of stack
class Solution {
    public boolean isValid(String s) {
        if(s==null || s.length() == 0){
            return true;
        }

        // //declare and initialize the character array
        // char[] charArray = { '(',')','{','}','[',']' };

        Stack<Character> stck = new Stack<>();
        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);
            if(c=='(')
                stck.push(')');

            else if(c=='{')
                stck.push('}');

            else if(c=='[')
                stck.push(']');

            else if (stck.isEmpty() || stck.pop() !=c)
                return false;
        }

        return stck.isEmpty();

        

    }


}
