function solution(s) {
    var answer = '';
    
    let numList = s.split(' ').map(Number);
    
    let minValue = Math.min(...numList);
    let maxValue = Math.max(...numList);
    
    answer = minValue.toString() + ' ' + maxValue.toString();
    
    return answer;
}