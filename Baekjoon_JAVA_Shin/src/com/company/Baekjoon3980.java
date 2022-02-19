package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Baekjoon3980 {

    static int T, result;
    static int[][] ability;
    static int[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        T = Integer.parseInt(br.readLine());
        for (int t=0; t<T; t++) {
            result = 0;
            visited = new int[11];
            ability = new int[11][11];
            for (int i=0; i<11; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j=0; j<11; j++) {
                    ability[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            findMax(0, 0);
            System.out.println(result);
        }
    }

    static void findMax(int cur, int idx) {
        if (idx == 11) {
            result = Math.max(result, cur);
            return;
        }

        for (int j=0; j<11; j++) {
            if (visited[j] == 0 && 0 < ability[idx][j]) {
                visited[j] = 1;
                findMax(cur + ability[idx][j], idx + 1);
                visited[j] = 0;
            }
        }
    }
}
