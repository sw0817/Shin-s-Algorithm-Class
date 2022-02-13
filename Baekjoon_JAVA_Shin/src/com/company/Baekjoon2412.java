package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Baekjoon2412 {

    static int n, T;
    static int[][] info;
    static ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
    static int[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());
        adj.add(new ArrayList<>());
        info = new int[n+1][2];
        for (int i=1; i<=n; i++) {
            st = new StringTokenizer(br.readLine());
            info[i][0] = Integer.parseInt(st.nextToken());
            info[i][1] = Integer.parseInt(st.nextToken());
            adj.add(new ArrayList<>());
//            for (int j=0; j<i; j++) {
//                if (Math.abs(info[i][0] - info[j][0]) <= 2 && Math.abs(info[i][1] - info[j][1]) <= 2) {
//                    adj.get(i).add(j);
//                    adj.get(j).add(i);
//                }
//            }
        }
        // 정렬 후 인접리스트 만들기



        visited = new int[n+1];
        for (int i=1; i<=n; i++) {
            visited[i] = n+1;
        }

        Queue<Integer> queue = new LinkedList<>();
        queue.add(0);
        int cnt = 0;
        while (!queue.isEmpty()) {
            int q_size = queue.size();
            for (int i=0; i<q_size; i++) {
                int v = queue.poll();
                if (T == info[v][1]) {
                    System.out.println(cnt);
                    return;
                }
                for (int j=0; j<adj.get(v).size(); j++) {
                    int n_v = adj.get(v).get(j);
                    if (cnt < visited[n_v]) {
                        visited[n_v] = cnt;
                        queue.add(n_v);
                    }
                }
            }
            cnt++;
        }
        System.out.println(-1);
    }
}
