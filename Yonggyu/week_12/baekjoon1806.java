package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon1806 {
	static int[] arr;
	static int N;
	static int S;

	public static void main(String[] args) throws IOException {
		// 부분합
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken()); // 수열 개수
		S = Integer.parseInt(st.nextToken()); // 구하고자 하는 부분합

		arr = new int[N];

		st = new StringTokenizer(br.readLine());

		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}

		int result = subTotal();

		System.out.println(result);
	}

	private static int subTotal() {
		int lt = 0, rt = 0;
		int sum = 0;
		int min = Integer.MAX_VALUE;
		int pnum = 0;

		while (rt < arr.length) {
			if (sum >= S) {
				pnum = rt - lt;

				min = Math.min(min, pnum);

				sum -= arr[lt++];
			} else if (sum < S) {
				sum += arr[rt++];
			}
		}

		if (min == Integer.MAX_VALUE) {
			return 0;
		}

		return min;
	}

}
