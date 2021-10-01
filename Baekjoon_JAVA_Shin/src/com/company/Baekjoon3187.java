package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Baekjoon3187 {

    static int R, C, S, W;
    static int[][] visited;
    static char[][] arr;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        arr = new char[R][C];
        visited = new int[R][C];
        for (int i=0; i < R; i++) {
            String row = br.readLine();
            for (int j=0; j < C; j++) {
                arr[i][j] = row.charAt(j);
            }
        }
        for (int i=0; i < R; i++) {
            for (int j=0; j < C; j++) {
                if (visited[i][j] != 1) {
                    check(i, j);
                }
            }
        }
        System.out.print(S);
        System.out.print(' ');
        System.out.print(W);
    }

    static void check(int r, int c) {
        int s = 0, w = 0;
        Queue<Node> queue = new LinkedList<Node>();
        visited[r][c] = 1;
        queue.add(new Node(r, c));
        while (!queue.isEmpty()) {
            Node node = queue.poll();
            if (arr[node.r][node.c] == 'v') {
                w++;
            } else if (arr[node.r][node.c] == 'k') {
                s++;
            }
            for (int i=0; i < 4; i++) {
                int nr = node.r + dr[i];
                int nc = node.c + dc[i];
                if (0 <= nr && nr < R && 0 <= nc && nc < C && visited[nr][nc] != 1 && arr[nr][nc] != '#') {
                    visited[nr][nc] = 1;
                    queue.add(new Node(nr, nc));
                }
            }
        }
        if (w < s) {
            S += s;
        } else {
            W += w;
        }
    }

    static class Node {

        int r, c;

        Node(int r_, int c_) {
            this.r = r_;
            this.c = c_;
        }
    }
}
