function solution(s) {
    var answer = 0;
    const originalS = s.split('');
    
    for (let i = 0; i < s.length; i++) {
        
        // 왼쪽으로 한 칸 회전
        const firstChar = originalS.shift();
        originalS.push(firstChar);
        
        if (isValid(originalS)) {
            answer ++;
        }
    }
    
    function isValid(arr) {
        const stack = [];
        const GalhoMap = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        };
        
        for (const char of arr) {
            if (char === '(' || char === '{' || char === '[') {
                stack.push(char);
            }
            else {
                
                // 괄호 없거나 짝이 안 맞으면 false
                if (stack.length === 0 || stack[stack.length - 1] !== GalhoMap[char]) {
                    return false;
                }
                
                // 짝 맞으면 스택 제거
                stack.pop();
            }
        }
        return stack.length === 0;
        
    }
    return answer;
}