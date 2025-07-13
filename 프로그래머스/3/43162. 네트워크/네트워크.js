function solution(n, computers) {
    var answer = 0;
    
    const visited = new Array(n).fill(false);
    
    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            answer++;
            dfs(i);
        }
    }
    
    function dfs(computerIndex) {
        visited[computerIndex] = true;
        
        for (let i = 0; i < n; i++) {
            if (computers[computerIndex][i] === 1 && !visited[i]) {
                dfs(i);
            }
        }
    }
    
    return answer;
}