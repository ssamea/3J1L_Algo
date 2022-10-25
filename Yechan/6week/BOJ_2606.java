import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2606 {
    static int[][] arr;
    static boolean[] brr;
    static int count = 0;
    static int N, L;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        L = Integer.parseInt(br.readLine());
        arr = new int[N+1][N+1];
        brr = new boolean[N+1];

        for (int i = 0; i < L; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a][b] = arr[b][a] = 1;
        }

        System.out.println(dfs(1));

    }

    private static int dfs(int i) {
        brr[i] = true;
        for (int j = 0; j <= N; j++) {
            if (arr[i][j] == 1 && !brr[j]) {
                count++;
                dfs(j);
            }
        }
        return count;
    }
}
