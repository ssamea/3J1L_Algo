import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_20310 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] arr = br.readLine().toCharArray();
        StringBuilder sb = new StringBuilder();
        int zero = 0, one = 0;

        if (arr.length % 4 != 0) return;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == '1' && (i+1) % 2 != 0) one++;
            if (arr[i] == '0' && (i+1) % 2 == 0) zero++;
        }

        for (int i = 1; i <= zero/2; i++) sb.append(0);
        for (int i = 1; i <= one/2; i++) sb.append(1);

        System.out.println(sb);
    }
}
