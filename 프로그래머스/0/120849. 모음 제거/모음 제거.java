class Solution {
    public String solution(String my_string) {
        StringBuilder answer = new StringBuilder();
        char[] vowels = {'a', 'e', 'i', 'o', 'u'};
        
        for (int i = 0; i < my_string.length(); i++) {
            char ch = my_string.charAt(i);
            boolean isVowel = false;
            
            
            for (char v : vowels) {
                if (ch == v) {
                    isVowel = true;
                    break;
                }
            }
            
            if (!isVowel) {
                answer.append(ch);
            }
        }
        
        return answer.toString();
    }
}