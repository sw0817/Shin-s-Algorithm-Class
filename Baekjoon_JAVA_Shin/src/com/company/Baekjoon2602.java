package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baekjoon2602 {

    static int l1, l2, result;
    static String str, angel, demon;
    static int[][][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        str = br.readLine();
        demon = br.readLine();
        angel = br.readLine();
        l1 = str.length();
        l2 = angel.length();
        result = 0;

        dp = new int[2][l2][l2];
        for (int i=0; i<2; i++) {
            for (int j=0; j<l2; j++) {
                for (int k=0; k<l2; k++) {
                    dp[i][j][k] = -1;
                }
            }
        }

        char iniChar = str.charAt(0);
        for (int j=0; j<l2; j++) {
            if (demon.charAt(j) == iniChar) {
                result += bridge(0, 0, j);
            }
            if (angel.charAt(j) == iniChar) {
                result += bridge(0, 1, j);
            }
        }

        System.out.println(result);
    }

    static int bridge(int idx, int r, int c) {
        if (dp[r][c][idx] != -1) {
            return dp[r][c][idx];
        }

        dp[r][c][idx] = 0;
        if (idx == l1-1) {
            dp[r][c][idx] = 1;
            return 1;
        }

        if (c == l2-1) {
            return 0;
        }

        char nxt = str.charAt(idx+1);
        if (r == 0) {
            for (int j=c+1; j<l2; j++) {
                if (angel.charAt(j) == nxt) {
                    dp[r][c][idx] += bridge(idx+1, 1, j);
                }
            }
        } else {
            for (int j=c+1; j<l2; j++) {
                if (demon.charAt(j) == nxt) {
                    dp[r][c][idx] += bridge(idx+1, 0, j);
                }
            }
        }

        return dp[r][c][idx];
    }
}
