function solution(s){
    var answer = true;
    
    
    const stack = [];
    
    for (const currentValue of s) {
        // 열린 괄호일 때, stack에 추가
        if (currentValue === '(') {
            stack.push(currentValue);
            continue;
        }
        
        // 닫힌 괄호일 때, stack에 짝이 지어지는 지 확인 후, 짝이 지어진다면 stack pop
        if (currentValue === ')' && stack[stack.length - 1] === '(') {
            stack.pop();
        } 
        
        // 나머지 닫힌 괄호인데 짝이 지어지지 않는다면, 즉시 false
        else {
            return false;
        }
    }
    
    // 괄호가 다 짝지어지지 않았다면, false
    if (stack.length !== 0) {
        return false;
    }

    return answer;
}