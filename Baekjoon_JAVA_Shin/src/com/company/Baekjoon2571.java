package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Baekjoon2571 {

    static int[][] board = new int[101][101];
    static int N, result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            board[n1][n2] += 1;
            board[n1+10][n2] += -1;
            board[n1][n2+10] += -1;
            board[n1+10][n2+10] += 1;
        }
        for (int i=0; i<100; i++) {
            for (int j=1; j<100; j++) {
                board[i][j] += board[i][j-1];
            }
        }
        for (int j=0; j<100; j++) {
            for (int i=1; i<100; i++) {
                board[i][j] += board[i-1][j];
            }
        }
        result = 0;

        for (int i=0; i<100; i++) {
            for (int j=0; j<100; j++) {
                if (0 < board[i][j]) {
                    check(i, j);
                }
            }
        }
        System.out.println(result);
    }

    static void check(int x, int y) {
        for (int i=0; i<100-x; i++) {
            for (int j=0; j<100-y; j++) {
                if (isSquare(x, y, x+i, y+j)) {
                    result = Math.max(result, (i+1) * (j+1));
                }
            }
        }
    }

    static boolean isSquare(int x, int y, int endx, int endy) {
        for (int i=x; i<=endx; i++) {
            for (int j=y; j<=endy; j++) {
                if (board[i][j] < 1) {
                    return false;
                }
            }
        }
        return true;
    }
}
