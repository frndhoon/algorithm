import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[][] matrix;
    static boolean[][] visited;
    static boolean top;
    static int ROW, COL;
    static int[] dr = {-1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dc = {0, 1, 1, 1, 0, -1, -1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        ROW = Integer.parseInt(st.nextToken());
        COL = Integer.parseInt(st.nextToken());
        matrix = new int[ROW][COL];
        visited = new boolean[ROW][COL];
        int count = 0;

        for (int r = 0; r < ROW; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < COL; c++) {
                matrix[r][c] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < ROW; i++) {
            for (int j = 0; j < COL; j++) {
                if (!visited[i][j] && matrix[i][j] != 0) {
                    top = true;
                    dfs(i, j);
                    if(top) count++;
                }
            }
        }
        System.out.println(count);
    }

    public static void dfs(int x, int y) {
        visited[x][y] = true;

        for (int i = 0; i < 8; i++) {
            int nr = x + dr[i];
            int nc = y + dc[i];

            if (nr >= 0 && nc >= 0 && nr < ROW && nc < COL) {
                if (matrix[x][y] < matrix[nr][nc]) {
                    top = false;
                } if (!visited[nr][nc] && matrix[nr][nc] == matrix[x][y]) {
                    dfs(nr, nc);
                }
            }

        }
    }
}
