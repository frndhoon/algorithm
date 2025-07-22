const fs = require("fs");
// ("/dev/stdin")
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

// splice 메소드는 O(N)의 시간복잡도
// O(500,000 * N) => 시간 초과

// 스택 자료구조 이용

const leftStack = input[0].trim().split("");
const rightStack = [];

const cmdCnt = Number(input[1]);

// 셋째 줄부터 cmdCnt줄 까지 입력할 명령어 출력
for (let i = 0; i < cmdCnt; i++) {
  const [cmd, addWord] = input[i + 2].split(" ");

  // 커서를 왼쪽으로 한 칸 옮김(맨 앞이면 무시)
  if (cmd === "L" && leftStack.length) {
    rightStack.push(leftStack.pop());
  }

  // 커서를 오른쪽으로 한 칸 옮김(맨 뒤면 무시)
  if (cmd === "D" && rightStack.length) {
    leftStack.push(rightStack.pop());
  }

  // 커서 왼쪽에 있는 문자를 삭제함 (맨 앞이면 무시)
  if (cmd === "B" && leftStack.length) {
    leftStack.pop();
  }

  if (cmd === "P") {
    leftStack.push(addWord);
  }
}

let answer = leftStack.join("");
answer += rightStack.reverse().join("");

console.log(answer);
