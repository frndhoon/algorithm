/**
 * x를 n번 곱한 수를 반환함
 *
 * @param {number} n 사람 명 수
 * @param {string[]} words 단어들
 * return {number, number} 탈락되는 번호, 차례
 * 주어진 단어들로 탈락자가 생기지 않는다면, [0, 0]
 */
function solution(n, words) {

    const alreadyWords = [];
    
    let currentNumber = 1; // 현재 번호
    let currentSequence = 1; // 현재 차례
    
    var answer = [currentNumber, currentSequence];
    
    for (let i = 0; i < words.length; i++) {
        
        const currentWord = words[i];
        
        // 1. 이미 나왔는지
        if (alreadyWords.includes(currentWord)) {
            return [currentNumber, currentSequence];
        }
        
        
        // 2. 끝말잇기 규칙 위반 확인
        if (i > 0 && words[i - 1].slice(-1) !== currentWord[0]) {
            return [currentNumber, currentSequence];
        }
            
        alreadyWords.push(currentWord);

        // 다음 사람으로 이동
        currentNumber++;
        if (currentNumber > n) {
            currentNumber = 1;
            currentSequence++;
        }
    }
    
    return [0, 0];
}