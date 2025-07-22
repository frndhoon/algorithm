const fs = require("fs");
// ("/dev/stdin")
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

// n: 세로 크기
// m: 가로 크기
const [numRows, numCols] = input[0].split(" ").map(Number);

// 도화지 그림 input 가져오기(2차원 배열)
const papers = new Array(numRows);

for (let i = 1; i < numRows + 1; i++) {
  papers[i - 1] = input[i].split(" ");
}

// 그림의 개수, 가장 넓은 넓이
let [drawingCount, maxArea] = [0, 0];

// 상, 하, 좌, 우
const rowOffsets = [0, 0, -1, 1];
const colOffsets = [-1, 1, 0, 0];

const visited = Array.from({ length: numRows }, () =>
  new Array(numCols).fill(false)
);

// bfs(너비 우선 탐색)
function bfs(r, c) {
  const queue = [[r, c]];
  visited[r][c] = true;

  let currentArea = 1;

  while (queue.length) {
    const [currR, currC] = queue.shift();

    for (let i = 0; i < 4; i++) {
      const nextR = currR + rowOffsets[i];
      const nextC = currC + colOffsets[i];

      // 도화지 밖이면 pass
      if (nextR < 0 || nextR >= numRows || nextC < 0 || nextC >= numCols) {
        continue;
      }

      // 이미 방문했으면 pass
      if (visited[nextR][nextC]) {
        continue;
      }

      // 도화지가 아니면 pass
      if (papers[nextR][nextC] === "0") {
        continue;
      }

      visited[nextR][nextC] = true;

      // 그림에 포함된 1의 개수를 세아려야 함
      queue.push([nextR, nextC]);
      currentArea++;
    }
  }
  // 탐색이 다 끝났으면 도화지 개수 +1
  drawingCount++;
  return currentArea;
}

for (let i = 0; i < numRows; i++) {
  for (let j = 0; j < numCols; j++) {
    if (visited[i][j]) {
      continue;
    }

    if (papers[i][j] === "1") {
      maxArea = Math.max(maxArea, bfs(i, j, 1));
    }
  }
}

console.log(`${drawingCount}\n${maxArea}`);
