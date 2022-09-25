import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class BOJ_2667 {
    static int danzi[][];
    static int dr[] = {-1,1,0,0,-1,-1,1,1};
    static int dc[] = {0,0,-1,1,-1,1,-1,1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int size = Integer.parseInt(st.nextToken());
        danzi = new int[size][size];
        int N = 0;
        String[] input = new String[size];
        while (N != size) {
            input[N] = br.readLine();
            N++;
        }
        int i, j;
        for (i = 0; i < size; i++) {
            for (j = 0; j < size; j++)
                danzi[i][j] = Integer.parseInt(String.valueOf(input[i].charAt(j)));
        }

        int r = 0, c = 0, l = 0;
        int danzis = 0;
        for (int k= 0 ; k < 8; k++) {
            int nr = r + dr[k];
            int nc = c + dc[k];
            if (nr >= 0 && nc < 5 && nc >= 0 && nc <5) {
                for (l = 0; l < size; l++) {
                    if (danzi[k][l] != 0 && danzi[k+1][l] != 0)
                        danzis += 1;
                    else if (danzi[k][l] != 0 && danzi[k-1][l] != 0)
                        danzis += 1;
                    else if (danzi[k][l] != 0 && danzi[k][l+1] != 0)
                        danzis += 1;
                    else if (danzi[k][l] != 0 && danzi[k][l-1] != 0)
                        danzis += 1;
                }
                System.out.println(danzis);
            }
        }

        print(size);
    }

    private static void print(int N) {
        for (int i = 0; i < N; i++) {
            System.out.println(Arrays.toString(danzi[i]));
        }
    }


}
