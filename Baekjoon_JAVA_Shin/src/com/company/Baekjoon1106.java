package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Baekjoon1106 {

    static int C, N;
    static int[] cost;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        C = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        cost = new int[C+101];
        Arrays.fill(cost, 101 * (C + 101));
        cost[0] = 0;
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            int c = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());
            for (int j=p; j<C+101; j++) {
                int prev = cost[j-p];
                if (prev != 101 * (C + 101)) {
                    cost[j] = Math.min(cost[j], c + prev);
                }
            }
        }
        int result = 101 * (C + 101);
        for (int i=C; i<C+101; i++) {
            result = Math.min(result, cost[i]);
        }
        System.out.println(result);
    }
}
