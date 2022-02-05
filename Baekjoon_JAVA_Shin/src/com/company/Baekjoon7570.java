package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Baekjoon7570 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int result = 0;
        int[] dp = new int[N+1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            int n = Integer.parseInt(st.nextToken());
            dp[n] = dp[n-1] + 1;
            result = Math.max(result, dp[n]);
        }
        System.out.println(N - result);
    }
}
