package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Baekjoon17089 {

    static int N, M, result;
    static ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
    static int[] visited, friends;

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
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            adj.get(a).add(b);
            adj.get(b).add(a);
        }

        visited = new int[N+1];
        friends = new int[3];
        result = 100000;
        for (int i=1; i<N+1; i++) {
            friends[0] = i;
            visited[i] = 1;
            findRelation(i, 1);
            friends[0] = 0;
            visited[i] = 0;
        }
        if (result == 100000) {
            System.out.println(-1);
        } else {
            System.out.println(result);
        }
    }

    static void findRelation(int idx, int cnt) {
        if (cnt == 3) {
            result = Math.min(result, adj.get(friends[0]).size() + adj.get(friends[1]).size() + adj.get(idx).size() - 6);
            return;
        }

        int l = adj.get(idx).size();
        for (int i=0; i<l; i++) {
            int nxt = adj.get(idx).get(i);
            if (visited[nxt] == 0) {
                boolean have = true;
                for (int j=0; j<cnt; j++) {
                    if (!adj.get(nxt).contains(friends[j])) {
                        have = false;
                        break;
                    }
                }
                if (!have) {
                    continue;
                }
                visited[nxt] = 1;
                friends[cnt] = nxt;
                findRelation(nxt, cnt+1);
                friends[cnt] = 0;
                visited[nxt] = 0;
            }
        }
    }
}
