function solution(k, dungeons) {
    let maxDungeons = 0;
    
    const visited = new Array(dungeons.length).fill(false);
    
    // dfs, 백트래킹
    const dfs = (currentK, cnt) => {
        
        // 현재까지 탐험한 던전 수가 최대값보다 크다면 업데이트
        maxDungeons = Math.max(maxDungeons, cnt);
        
        for (let i = 0; i < dungeons.length; i++) {
            const [minRequiredPirodo, consumedPirodo] = dungeons[i];
            
            // 방문하지 않은 던전인지?
            // 현재 피로도가 해당 던전 최소 필요 피로도보다 이상인지?
            if (!visited[i] && currentK >= minRequiredPirodo) {
                
                // 던전 방문 처리
                visited[i] = true;
                
                // 해당 던전 탐험 후 피로도 소모, 던전 수 + 1
                dfs(currentK - consumedPirodo, cnt + 1);
                
                // 백트래킹
                visited[i] = false;
            }
        }
    }
    
    dfs(k, 0);
    
    return maxDungeons;
}