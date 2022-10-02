import java.io.*;
import java.util.*;

public class BOJ_20546 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int asset = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] stock = new int[14];

        for (int i = 0; i < 14; i++) {
            stock[i] = Integer.parseInt(st.nextToken());
        }

        int jun_earn = BNP(stock, asset);
        int sung_earn = TIMING(stock, asset);

        if (jun_earn > sung_earn) System.out.println("BNP");
        else if (jun_earn < sung_earn) System.out.println("TIMING");
        else System.out.println("SAMESAME");
    }

    private static int BNP(int[] stock, int asset) {
        int count = 0;
        int earn = asset;

        for (int i = 0; i < 14; i++) {
            int now = earn / stock[i];
            count += now;
            earn -= now * stock[i];
        }
        return earn + count * stock[13];
    }

    private static int TIMING(int[] stock, int asset) {
        int count = 0;
        int earn = asset;
        int up = 0;
        int down = 0;

        for (int i = 1; i < 14; i++) {
            int yesterday = stock[i-1];
            int today = stock[i];

            if (today > yesterday) {
                up++;
                down = 0;
            }
            else if (today < yesterday) {
                down++;
                up = 0;
            }
            else {
                up = 0;
                down = 0;
            }

            if (up == 3) {
                if (count != 0) {
                    earn += today * count;
                }
                up = 0;
                count = 0;
            }
            else if (down == 3) {
                int now = earn / today;
                count += now;
                earn -= now * today;
            }
        }
        return earn + count * stock[13];
    }
}
