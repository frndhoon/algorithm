const fs = require("fs");
// ("/dev/stdin")
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

// 테스트 케이스가 여러 개이므로, 현재 어디를 가리키고 있는 지 저장할 변수
let currentIndex = 0;

// while 내부에 offset을 선언하지 않는 이유는, 반복하면서 계속해서 선언할 경우 메모리 낭비가 있을 것이라고 판단하여
// 전역적으로 선언하였음
// 순서) 동 서 남 북 상 하 (6번)
const numOffsets = 6;
const layerOffsets = [0, 0, 0, 0, -1, +1];
const RowOffsets = [-1, +1, 0, 0, 0, 0];
const ColOffsets = [0, 0, -1, +1, 0, 0];

while (true) {
  const [numLayers, numRows, numCols] = input[currentIndex]
    .split(" ")
    .map(Number);

  // 1. L, R, C가 0일 때까지 테스트 케이스 반복
  if (numLayers === 0 && numRows === 0 && numCols === 0) {
    break;
  }

  // 다음 인덱스로 이동
  currentIndex++;

  // 정육면체 초기화
  // 정육면체는 string을 받아야하므로 '' 할당
  const cube = Array.from({ length: numLayers }, () =>
    Array.from({ length: numRows }, () => new Array(numCols).fill(""))
  );

  // 2. L번 반복, R번 반복하면서 빈 정육면체에 기록
  for (let l = 0; l < numLayers; l++) {
    for (let r = 0; r < numRows; r++) {
      // 해당 행의 0열부터 c열까지 기록
      cube[l][r] = input[currentIndex].split("");
      // 다음 행으로 이동
      currentIndex++;
    }

    // 3. l번 반복 시 중간에 공백이 있으므로 건너뛰기
    currentIndex++;
  }

  // 최단 시간이므로 bfs로 너비 우선으로 탐색하면서 도착했을 때, 최단 시간을 구해야겠다는 생각을 함
  // 시간 제한 1초, L, R, C 각각 30
  // 30 x 30 x 30 = 27000
  // 시간 복잡도 : O(L * R * C)
  // 공간 복잡도 : O(L * R * C)

  // 중복 방문 체크
  const visited = Array.from({ length: numLayers }, () =>
    Array.from({ length: numRows }, () => new Array(numCols).fill(false))
  );

  // l: 층 좌표
  // r: 행 좌표
  // c: 열 좌표
  // EscapedTime: 탈출에 걸리는 시간(0초부터 시작)
  function bfs(l, r, c, EscapedTime = 0) {
    // bfs는 너비 우선 탐색을 해야하니, 선입선출의 특성을 가진 큐 자료구조를 이용하여 구현
    const queue = [[l, r, c, EscapedTime]];
    // 처음 좌표 방문 체크
    visited[l][r][c] = true;

    while (queue.length) {
      // 선입선출 좌표 탐색 시작
      const [currL, currR, currC, EscapedTime] = queue.shift();

      // 출구(E)인지 확인
      if (cube[currL][currR][currC] === "E") {
        return `Escaped in ${EscapedTime} minute(s).`;
      }

      // 동 서 남 북 상 하 순으로 탐색
      for (let i = 0; i < numOffsets; i++) {
        const nextL = currL + layerOffsets[i];
        const nextR = currR + RowOffsets[i];
        const nextC = currC + ColOffsets[i];

        // 갈 수 없는 조건
        // 갈 수 없는 조건을 한 이유는, 개인적으로 디버깅이 용이하다고 생각한다.
        // 잘못 조건을 선언했더라도, 조건을 나눠놓으면 해당 조건만 디버깅하면 되기 때문

        // 1순위. 정육면체(빌딩) 밖에 있나?
        if (
          nextL < 0 ||
          nextL >= numLayers ||
          nextR < 0 ||
          nextR >= numRows ||
          nextC < 0 ||
          nextC >= numCols
        ) {
          continue;
        }

        // 2순위. 지나갈 수 없는 칸인가?(#)
        if (cube[nextL][nextR][nextC] === "#") {
          continue;
        }

        // 3순위. 이미 방문했나?
        if (visited[nextL][nextR][nextC]) {
          continue;
        }

        // 갈 수 없는 조건을 통과했다면, 큐에 해당 좌표 추가
        // 탈출 시간 + 1
        // 왜냐하면, 너비 우선 탐색이기 때문에 해당 경로에서 갈 수 있는 모든 경로는 1초 더 걸림
        queue.push([nextL, nextR, nextC, EscapedTime + 1]);
        visited[nextL][nextR][nextC] = true;
      }
    }

    // 다 탐색했는데, 출구(E)를 발견하지 못했다.
    return "Trapped!";
  }

  for (let l = 0; l < numLayers; l++) {
    for (let r = 0; r < numRows; r++) {
      for (let c = 0; c < numCols; c++) {
        // 시작 지점 탐색 후 bfs 탐색 시작
        if (cube[l][r][c] === "S") {
          console.log(bfs(l, r, c));
        }
      }
    }
  }
}
