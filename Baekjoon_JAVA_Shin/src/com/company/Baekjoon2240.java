package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Baekjoon2240 {

    static int T, W;
    static int[] info;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        T = Integer.parseInt(st.nextToken());
        W = Integer.parseInt(st.nextToken());
        info = new int[T+1];
        for (int i=1; i<=T; i++) {
            info[i] = Integer.parseInt(br.readLine());
        }
        dp = new int[T+1][W+1];

        // 초기값 (위치 안 바꿈)
        for (int i=1; i<=T; i++) {
            dp[i][0] = dp[i-1][0];
            if (info[i] == 1) {
                dp[i][0]++;
            }
        }

        for (int i=1; i<=T; i++) {
            for (int j=1; j<=W; j++) {
                if (i < j) {
                    break;
                }
                dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-1]);
                if (j % 2 == 0 && info[i] == 1) {
                    dp[i][j]++;
                } else if (j % 2 == 1 && info[i] == 2) {
                    dp[i][j]++;
                }
            }
        }

        int result = 0;
        for (int j=0; j<=W; j++) {
            result = Math.max(result, dp[T][j]);
        }

        System.out.println(result);
    }
}
