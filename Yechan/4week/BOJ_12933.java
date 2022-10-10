import java.io.*;
import java.util.*;

public class BOJ_12933 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] str = br.readLine().toCharArray();
        char[] duck = {'q', 'u', 'a', 'c', 'k'};
        boolean[] cry = new boolean[str.length];
        int k = 0;
        int cnt = 0;

        if (str[0] != 'q' || str.length % 5 != 0) {
            System.out.println(-1);
            return;
        }

        for (int i = 0; i < str.length; i++) {
            ArrayList<Character> list = new ArrayList<>();
            for (int j = 0; j < str.length; j++) {
                if (!cry[j] && str[j] == duck[k]) {
                    k++;
                    list.add(str[j]);
                    cry[j] = true;
                    if (k == 5) k = 0;
                }
            }

            if (list.size() != 0) {
                if (list.get(list.size() - 1) != 'k') {
                    System.out.println(-1);
                    return;
                }
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}
