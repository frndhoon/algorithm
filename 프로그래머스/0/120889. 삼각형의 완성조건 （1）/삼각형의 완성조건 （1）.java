class Solution {
    public int solution(int[] sides) {
        int answer = 0;
        int sum = 0;
        int big_side = 0;
        
        for (int s : sides) {
            sum += s;
            if (s > big_side) {
                big_side = s;
            }
        }
        
        if (sum - big_side <= big_side) {
            return 2;
        } else {
            return 1;
        }
        
    }
}