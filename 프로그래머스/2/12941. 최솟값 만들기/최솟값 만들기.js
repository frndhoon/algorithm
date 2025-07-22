function solution(A,B){
    
    // 저장할 최소값 (1000이하 자연수, 원소 크기 1000이하이므로 최대값 100억)
    let minValue = 100_000_0000;
    
    // 가장 작은 값은 가장 큰 값과, 두 번째 작은 값은 두 번째 큰 값과 곱하면 최소값
    A.sort((a, b) => a - b); // 오름차순
    B.sort((a, b) => b - a); // 내림차순
    
    minValue = A.reduce((acc, currentValue, idx) => {
        return acc + (currentValue * B[idx]);
    }, 0);
    
    
    // 배열 길이 : A, B 배열은 길이가 같음
    const arrayLength = A.length;
    
    // 해당 배열의 index를 사용했는지 여부 체크
    const aArrayIndexCheck = new Array(arrayLength).fill(false);
    const bArrayIndexCheck = new Array(arrayLength).fill(false);
    
    // 시간초과 (N이 1000, 1000으로 너무 큼 O(N!)에 가까움)
    // dfs(0, 0);
    
    // 완전탐색
    // turn : 현재 몇 번 숫자를 뽑았는지
    // value : 현재 더한 값이 얼마인지
    function dfs (turn, value) {
        // 가지치기 : 최소값보다 크면 탐색 X
        if (value >= minValue) {
            return;
        }
        
        if (turn === arrayLength) {
            minValue = value;
            return;
        }
        
        for (let i = 0; i < arrayLength; i++) {
            
            for (let j = 0; j < arrayLength; j++) {
                // 아직 해당 배열의 index를 사용하지 않았다면,
                // 해당 배열 index를 더하기
                if (!aArrayIndexCheck[i] && !bArrayIndexCheck[j]) {
                    
                    aArrayIndexCheck[i] = true;
                    bArrayIndexCheck[j] = true;
                    value += A[i] * B[j];
                    
                    dfs(turn + 1, value);
                    
                    value -= A[i] * B[j];
                    aArrayIndexCheck[i] = false;
                    bArrayIndexCheck[j] = false;
                    
                }
            }
        }
    }
    
    return minValue;
}