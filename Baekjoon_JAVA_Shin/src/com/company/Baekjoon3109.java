package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Baekjoon3109 {

    static int R, C, result;
    static int[][] arr, visited;
    static int[] dr = {-1, 0, 1};
    static boolean checked;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        arr = new int[R][C];
        visited = new int[R][C];
        for (int i=0; i<R; i++) {
            String info = br.readLine();
            for (int j=0; j<C; j++) {
                char cur = info.charAt(j);
                if (cur == 'x') {
                    arr[i][j] = 1;
                }
            }
        }

        result = 0;
        for (int i=0; i<R; i++) {
            checked = false;
            visited[i][0] = 1;
            dfs(i, 0);
        }

        System.out.println(result);
    }

    static void dfs(int r, int c) {
        if (checked) {
            return;
        }

        if (c == C-1) {
            checked = true;
            result++;
            return;
        }

        for (int i=0; i<3; i++) {
            if (checked) {
                continue;
            }
            int nr = r + dr[i];
            int nc = c + 1;
            if (0 <= nr && nr < R && nc < C && arr[nr][nc] == 0 && visited[nr][nc] == 0) {
                visited[nr][nc] = 1;
                dfs(nr, nc);
            }
        }
    }
}
