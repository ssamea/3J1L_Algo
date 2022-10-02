import java.io.*;
import java.util.*;

public class BOJ_10825 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[][] stu = new String[N][4];

        for (int i = 0; i < N ; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            stu[i][0] = st.nextToken();
            stu[i][1] = st.nextToken();
            stu[i][2] = st.nextToken();
            stu[i][3] = st.nextToken();
        }

        Arrays.sort(stu, (o1, o2) -> {
            if (o1[1].equals(o2[1])){
                if (o1[2].equals(o2[2])){
                    if (o1[3].equals(o2[3])){
                        return o1[0].compareTo(o2[0]);
                    } return Integer.parseInt(o2[3]) - Integer.parseInt(o1[3]);
                } return Integer.parseInt(o1[2]) - Integer.parseInt(o2[2]);
            } return Integer.parseInt(o2[1]) - Integer.parseInt(o1[1]);
        });

        for (int i = 0; i < N; i++) System.out.println(stu[i][0]);
    }
}
