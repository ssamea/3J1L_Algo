import java.io.*;
import java.util.*;
public class BOJ_20154 {
    static Map<String, Integer> map = new HashMap<>();
    static int[] arr = {3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1};
    public static void main(String[] args) throws IOException {
        /*map.put("A",3);map.put("B",2);map.put("C",1);map.put("D",2);map.put("E",3);map.put("F",3);
        map.put("G",3);map.put("H",3);map.put("I",1);map.put("J",1);map.put("K",3);map.put("L",1);
        map.put("M",3);map.put("N",3);map.put("O",1);map.put("P",2);map.put("Q",2);map.put("R",2);
        map.put("S",1);map.put("T",2);map.put("U",1);map.put("V",1);map.put("W",2);map.put("X",2);
        map.put("Y",2);map.put("Z",1);*/
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int sum = 0;

        for (int i = 0; i < str.length(); i++) {
            sum += arr[str.charAt(i) - 'A'];
            //sum += map.get((String.valueOf(str.charAt(i))));
        }
        System.out.println((sum % 2 != 0) ? "I`m a winner!" : "You`re the winner?");
    }
}
