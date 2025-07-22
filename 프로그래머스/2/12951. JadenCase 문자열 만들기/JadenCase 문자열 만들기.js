function solution(s) {
    var answer = '';
    // 모든 단어의 첫 문자가 대문자
    // 그 외의 알파벳은 소문자
    // 첫 문자가 아닐 때 이어지는 알파벳은 소문자
    
    // 띄어쓰기 기준으로 단어 나누기
    const words = s.split(' ');
    const newWords = [];
    
    for (word of words) {
        
        let newWord = '';
        
        for (let i = 0; i < word.length; i++) {
            // 첫 문자일 경우, 대문자로 변경
            if (i === 0 && typeof word[i] === 'string') {
                newWord += word[i].toUpperCase();
            } else if (i !== 0 && typeof word[i] === 'string') {
                newWord += word[i].toLowerCase();                
            } else {
                newWord += word;
            }
        }
        newWords.push(newWord);
    }
    
    answer = newWords.join(' ');
    
    return answer;
}