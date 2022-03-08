package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Baekjoon5972 {

    static int N, M, inf;
    static ArrayList<ArrayList<Node>> adj = new ArrayList<>();
    static int[] visited;
    static Queue<Integer> queue = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        for (int i=0; i<N+1; i++) {
            adj.add(new ArrayList<>());
        }
        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int A_i = Integer.parseInt(st.nextToken());
            int B_i = Integer.parseInt(st.nextToken());
            int C_i = Integer.parseInt(st.nextToken());
            adj.get(A_i).add(new Node(B_i, C_i));
            adj.get(B_i).add(new Node(A_i, C_i));
        }
        inf = 50000 * 1000;
        visited = new int[N+1];
        for (int i=0; i<N+1; i++) {
            visited[i] = inf;
        }
        visited[1] = 0;
        queue.add(1);
        while (!queue.isEmpty()) {
            int v = queue.poll();
            for (int i=0; i<adj.get(v).size(); i++) {
                Node nxt = adj.get(v).get(i);
                if (visited[v] + nxt.c < visited[nxt.n]) {
                    visited[nxt.n] = visited[v] + nxt.c;
                    queue.add(nxt.n);
                }
            }
        }
        System.out.println(visited[N]);
    }

    static class Node {
        int n, c;

        Node(int n, int c) {
            this.n = n;
            this.c = c;
        }
    }
}
