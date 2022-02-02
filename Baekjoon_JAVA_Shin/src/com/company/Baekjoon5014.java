package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Baekjoon5014 {

    static int F, S, G, U, D;
    static int[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        F = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());
        G = Integer.parseInt(st.nextToken());
        U = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());
        visited = new int[F+1];
        visited[S] = 1;
        int result = bfs();
        if (result == -1) {
            System.out.println("use the stairs");
        } else {
            System.out.println(result);
        }
    }

    static Integer bfs() {
        int cur = 0;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(S);
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i=0; i<size; i++) {
                int s = queue.poll();
                if (s == G) {
                    return cur;
                }
                if (s + U < F + 1 && visited[s + U] == 0) {
                    queue.add(s + U);
                    visited[s + U] = 1;
                }
                if (0 < s - D && visited[s - D] == 0) {
                    queue.add(s - D);
                    visited[s - D] = 1;
                }
            }
            cur++;
        }
        return -1;
    }
}
