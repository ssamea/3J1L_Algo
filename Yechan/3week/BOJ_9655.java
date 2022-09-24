import java.io.*;

public class BOJ_9655 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println((Integer.parseInt(br.readLine()) % 2 == 0) ? "CY" : "SK");
    }
}
