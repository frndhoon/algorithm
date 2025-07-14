function solution(n, works) {
    
    // 1. 총 작업량 확인: 모든 작업을 n시간 안에 끝낼 수 있으면 피로도는 0
    const totalWork = works.reduce((sum, work) => sum + work, 0);
    if (totalWork <= n) {
        return 0;
    }
    
    // 2. 작업량 분포 카운팅: 각 작업량별로 몇 개의 일이 있는지 기록
    // works의 원소는 최대 50000이므로, 50001 크기의 배열 사용
    const workCounts = new Array(50001).fill(0);
    let maxWorkValue = 0;

    for (const work of works) {
        workCounts[work]++;
        if (work > maxWorkValue) {
            maxWorkValue = work; // 최대 작업량 갱신
        }
    }

  // 3. n 시간 동안 야근하며 작업량 줄이기
    for (let i = 0; i < n; i++) {
        if (maxWorkValue <= 0) {
            // 모든 작업량이 0이 되면 더 이상 줄일 일이 없음
            break;
        }

        // 현재 가장 큰 작업량을 가진 일이 남아있는 경우
        if (workCounts[maxWorkValue] > 0) {
            workCounts[maxWorkValue]--;
            workCounts[maxWorkValue - 1]++;
        } else {
            maxWorkValue--;
            i--;
            continue;
        }

        // 만약 현재 maxWorkValue를 가진 모든 일을 처리하여 개수가 0이 되었다면,
        // 다음 야근 시간에는 그 다음으로 큰 작업량을 처리해야 하므로 maxWorkValue 감소
        if (workCounts[maxWorkValue] === 0) {
            maxWorkValue--;
        }
    }

    // 4. 최종 야근 피로도 계산
    let pirodo = 0;
    // 0부터 maxWorkValue까지 (최대 50000) 순회하며 피로도 계산
    for (let i = 0; i <= maxWorkValue; i++) {
        if (workCounts[i] > 0) {
            pirodo += i * i * workCounts[i];
        }
    }
    return pirodo;
}