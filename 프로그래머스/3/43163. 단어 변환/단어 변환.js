function solution(begin, target, words) {
    
    // 1. 두 단어가 한 글자만 다른지 확인
    function isOneCharDiff(word1, word2) {
        let diffCount = 0;
        for (let i = 0; i < word1.length; i++) {
            if (word1[i] !== word2[i]) {
                diffCount ++;
            }
        }
        return diffCount === 1;
    }
    
    // 2. BFS 탐색
    const queue = [[begin, 0]];
    
    const visited = new Set();
    visited.add(begin);
    
    while (queue.length > 0) {
        const [currentWord, steps] = queue.shift();
        
        // 현재 단어가 target과 같으면 최단 경로
        if (currentWord == target) {
            return steps;
        }
        
        for (const word of words) {
            // 현재 단어와 한 글자만 다르고, 아직 방문하지 않은 단어라면
            if (isOneCharDiff(currentWord, word) && !visited.has(word)) {
                visited.add(word); // 방문 기록
                queue.push([word, steps + 1]); // 큐 추가
            }
        }
    }
    
    return 0;
}