package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baekjoon1058 {

    static int N;
    static int[][] dp, friends;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        dp = new int[N][N];
        friends = new int[N][N];
        for (int i=0; i<N; i++) {
            String info = br.readLine();
            for (int j=0; j<N; j++) {
                if (info.charAt(j) == 'Y') {
                    friends[i][j] = 1;
                }
            }
        }

        for (int k=0; k<N; k++) {
            for (int i=0; i<N; i++) {
                for (int j=0; j<N; j++) {
                    if (i == j) {
                        continue;
                    }
                    if (friends[i][j] == 1 || (friends[i][k] == 1 && friends[k][j] == 1)) {
                        dp[i][j] = 1;
                    }
                }
            }
        }
        int result = 0;
        for (int i=0; i<N; i++) {
            for (int j=1; j<N; j++) {
                dp[i][j] += dp[i][j-1];
            }
            result = Math.max(result, dp[i][N-1]);
        }
        System.out.println(result);
    }
}
