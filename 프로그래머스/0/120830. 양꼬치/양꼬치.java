class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        k -= n / 10;
        
        answer += n * 12000;
        answer += k * 2000;
        return answer;
    }
}