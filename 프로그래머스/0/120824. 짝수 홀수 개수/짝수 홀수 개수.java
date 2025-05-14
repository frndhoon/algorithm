class Solution {
    public int[] solution(int[] num_list) {
        int n = num_list.length;
        int evenCnt = 0;
        int oddCnt = 0;
        
        for (int num : num_list) {
            if (num % 2 == 0) {
                evenCnt++;
            } else {
                oddCnt++;
            }
        }
        
        int[] result = new int[2];
        result[0] = evenCnt;
        result[1] = oddCnt;
        return result;
    }
}