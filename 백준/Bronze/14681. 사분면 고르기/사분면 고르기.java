import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int x = Integer.parseInt(br.readLine());
        int y = Integer.parseInt(br.readLine());

        int Quadrant1 = 1, Quadrant2 = 2, Quadrant3 = 3, Quadrant4 = 4;

        if (x > 0 && y > 0) {
            System.out.print(Quadrant1);
        } else if (x < 0 && y > 0) {
            System.out.print(Quadrant2);
        } else if (x < 0 && y < 0) {
            System.out.print(Quadrant3);
        } else if (x > 0 && y < 0) {
            System.out.print(Quadrant4);
        }
    }
}
