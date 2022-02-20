package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Baekjoon10476 {

    static int N, k;
    static int[][] gallery;
    static int[][][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        gallery = new int[N+1][2];
        dp = new int[N+2][N+2][3];
        for (int i=1; i<=N; i++) {
            st = new StringTokenizer(br.readLine());
            gallery[i][0] = Integer.parseInt(st.nextToken());
            gallery[i][1] = Integer.parseInt(st.nextToken());
        }
        dp[1][1][0] = gallery[1][1];
        dp[1][1][1] = gallery[1][0];
        dp[1][0][2] = gallery[1][0] + gallery[1][1];

        for (int i=2; i <= N; i++) {
            for (int j=0; j <= k; j++) {
                if (1 <= j) {
                    dp[i][j][0] = Math.max(dp[i-1][j-1][0], dp[i-1][j-1][2]) + gallery[i][1];
                    dp[i][j][1] = Math.max(dp[i-1][j-1][1], dp[i-1][j-1][2]) + gallery[i][0];
                }
                if (i != j) {
                    dp[i][j][2] = Math.max(Math.max(dp[i-1][j][0], dp[i-1][j][1]), dp[i-1][j][2]) + gallery[i][0] + gallery[i][1];
                }
            }
        }

        System.out.println(Math.max(Math.max(dp[N][k][0], dp[N][k][1]), dp[N][k][2]));
    }
}
