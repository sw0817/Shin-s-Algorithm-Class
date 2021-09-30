package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Baekjoon1926 {

    static int n, m, cnt, result;
    static int[][] arr, visited;
    static int[] dr = {-1, 1, 0, 0}, dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n][m];
        visited = new int[n][m];
        for (int i=0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j < m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        for (int i=0; i < n; i++) {
            for (int j=0; j < m; j++) {
                if (visited[i][j] != 1 && arr[i][j] == 1) {
                    bfs(i, j);
                    cnt++;
                }
            }
        }
        System.out.println(cnt);
        System.out.println(result);
    }

    static void bfs(int r, int c) {
        visited[r][c] = 1;
        int temp = 1;
        Queue<Node> queue = new LinkedList<Node>();
        queue.add(new Node(r, c));
        while (!queue.isEmpty()) {
            Node node = queue.poll();
            for (int i=0; i < 4; i++) {
                int nr = node.r + dr[i];
                int nc = node.c + dc[i];
                if (0 <= nr && nr < n && 0 <= nc && nc < m && visited[nr][nc] != 1 && arr[nr][nc] == 1) {
                    visited[nr][nc] = 1;
                    queue.add(new Node(nr, nc));
                    temp++;
                }
            }
        }
        result = Math.max(result, temp);
    }

    static class Node {
        int r;
        int c;

        Node(int r_, int c_) {
            this.r = r_;
            this.c = c_;
        }
    }
}
