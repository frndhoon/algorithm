class Solution {
    public int solution(int n) {
        int min_num = 0;
        for (int i=2; i <= n; i++) {
            if (n % i == 1) {
                min_num = i;
                break;
            }
        }
        
        return min_num;
    }
}