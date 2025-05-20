import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // N, M: 행, 열
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());


        // 격자
        // 가장 왼쪽 윗 칸은 (1, 1)
        // 가장 오른쪽 아랫 칸 : (N, N)
        int[][] map = new int[N+1][N+1];
        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // moves[][0] = 방향
        // moves[][0] = 거리
        int[][] moves = new int[M][2];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            moves[i][0] = Integer.parseInt(st.nextToken());
            moves[i][1] = Integer.parseInt(st.nextToken());
        }


//        for (int i = 1; i < N+1; i++) {
//            for (int j = 1; j < N+1; j++) {
//                System.out.print(map[i][j]);
//            }
//            System.out.println();
//        }
//
//        for (int i = 0; i < M; i++) {
//            System.out.print(moves[i][0]);
//            System.out.print(moves[i][1]);
//            System.out.println();
//        }

        // 8방향
        // 1부터 순서대로
        int[] dr = {0, 0, -1, -1, -1, 0, 1, 1, 1};
        int[] dc = {0, -1, -1, 0, 1, 1, 1, 0, -1};

        // 대각선 방향 (물복사버그)
        int[] diagR = {-1, -1, 1, 1};
        int[] diagC = {-1, 1, 1, -1};

        // 초기 구름 위치
        List<int[]> cloud = new ArrayList<>();
        cloud.add(new int[]{N, 1});
        cloud.add(new int[]{N, 2});
        cloud.add(new int[]{N - 1, 1});
        cloud.add(new int[]{N - 1, 2});

        // 1. 모든 구름이 move[i][0] 방향으로 move[i][1]칸 이동한다.
        for (int i = 0; i < M; i++) {
            int dir = moves[i][0];
            int dist = moves[i][1];

            // 1. 모든 구름 이동
            for (int[] c : cloud) {
                // 실제 이동 거리는 N으로 나눈 나머지
                int actualDist = dist % N;

                c[0] = c[0] + dr[dir] * actualDist;
                c[1] = c[1] + dc[dir] * actualDist;

                // 1-indexed 배열에서 범위를 벗어날 경우 처리
                while (c[0] <= 0) c[0] += N;
                while (c[0] > N) c[0] -= N;
                while (c[1] <= 0) c[1] += N;
                while (c[1] > N) c[1] -= N;
            }

            // 2. 구름이 있는 칸에 비 내리기
            for (int[] c : cloud) {
                map[c[0]][c[1]] += 1;
            }

            // 3. 구름 사라짐 (위치 기록)
            boolean[][] visited = new boolean[N + 1][N + 1];
            for (int[] c : cloud) {
                visited[c[0]][c[1]] = true;
            }

            // 4. 물복사 버그
            for (int[] c : cloud) {
                int r = c[0];
                int c1 = c[1];
                int cnt = 0;

                // 대각선 4방향 검사
                for (int d = 0; d < 4; d++) {
                    int nr = r + diagR[d];
                    int nc = c1 + diagC[d];

                    // 범위 체크 및 물이 있는지 확인
                    if (nr >= 1 && nr <= N && nc >= 1 && nc <= N && map[nr][nc] > 0) {
                        cnt++;
                    }
                }

                map[r][c1] += cnt;
            }

            // 5. 새로운 구름 생성
            List<int[]> newCloud = new ArrayList<>();
            for (int r = 1; r <= N; r++) {
                for (int c1 = 1; c1 <= N; c1++) {
                    if (!visited[r][c1] && map[r][c1] >= 2) {
                        newCloud.add(new int[]{r, c1});
                        map[r][c1] -= 2;
                    }
                }
            }

            // 구름 갱신
            cloud = newCloud;
        }

        int water = 0;

        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                water += map[i][j];
            }
        }

        System.out.println(water);

    }
}
