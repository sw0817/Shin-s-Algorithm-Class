package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Baekjoon1388 {

    static Integer N, M, ans;
    static Integer[][] visited;
    static Character[][] arr;

    static class Node{
        int r;
        int c;

        Node(int _r, int _c) {
            this.r = _r;
            this.c = _c;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        ans = 0;
        arr = new Character[N][M];
        visited = new Integer[N][M];
        for (int i=0; i < N; i++) {
            String row = br.readLine();
            for (int j=0; j < M; j++) {
                arr[i][j] = row.charAt(j);
                visited[i][j] = 0;
            }
        }
        BFS();
        System.out.println(ans);
    }

    static void BFS() {
        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, 1, -1};
        for (int i=0; i < N; i++) {
            for (int j=0; j < M; j++) {
                if (visited[i][j] == 0) {
                    Queue<Node> q = new LinkedList<>();
                    q.add(new Node(i, j));
                    ans += 1;
                    visited[i][j] = 1;
                    Character temp = arr[i][j];
                    while (!q.isEmpty()) {
                        Node node = q.poll();
                        for (int k=0; k < 4; k++) {
                            if (temp == '-' && k < 2) {
                                continue;
                            }
                            else if (temp == '|' && 2 <= k) {
                                continue;
                            }
                            int nr = node.r + dr[k];
                            int nc = node.c + dc[k];
                            if (0 <= nr && nr < N && 0 <= nc && nc < M && visited[nr][nc] == 0 && arr[nr][nc] == temp) {
                                visited[nr][nc] = 1;
                                q.add(new Node(nr, nc));
                            }
                        }
                    }
                }
            }
        }
    }
}
