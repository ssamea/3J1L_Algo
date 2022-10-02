import java.io.*;
import java.util.*;

public class BOJ_1929 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        StringBuilder sb = new StringBuilder();
        boolean[] prime = new boolean[N + 1];

        prime[0] = true;
        prime[1] = true;

        for (int i = 2; i * i <= N; i++) {
            if (!prime[i]) {
                for (int j = i * i; j <= N; j += i) prime[j] = true;
            }
        }

        for (int i = M; i <= N; i++) {
            if (!prime[i]) sb.append(i).append('\n');
        }
        System.out.println(sb);
    }
}
