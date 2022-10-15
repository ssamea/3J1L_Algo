import java.io.*;
import java.util.Arrays;

public class BOJ_2309 {
    static int[] arr = new int[9];
    static int sum, other1, other2  = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 9; i++) {
            arr[i] = Integer.parseInt(br.readLine());
            sum += arr[i];
        }

        Arrays.sort(arr);

        for (int i = 0; i < arr.length-1; i++) {
            for (int j = i+1; j < arr.length; j++) {
                if (sum - arr[i] - arr[j] == 100) {
                    other1 = arr[i];
                    other2 = arr[j];
                }
            }
        }

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == other1 || arr[i] == other2) continue;
            System.out.println(arr[i]);
        }
    }
}
