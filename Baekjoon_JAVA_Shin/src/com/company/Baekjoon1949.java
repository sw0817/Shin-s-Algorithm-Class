package com.company;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Baekjoon1949 {

    static int N;
    static int[] people, visited;
    static int[][] dp;
    static ArrayList<ArrayList<Integer>> adj;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        dp = new int[N+1][2];
        people = new int[N+1];
        st = new StringTokenizer(br.readLine());
        for (int i=1; i < N+1; i++) {
            people[i] = Integer.parseInt(st.nextToken());
        }
        adj = new ArrayList<>();
        for (int i=0; i < N+1; i++) {
            adj.add(new ArrayList<>());
        }

        for (int i=0; i < N-1; i++) {
            st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());
            adj.get(v1).add(v2);
            adj.get(v2).add(v1);
        }

        visited = new int[N+1];
        dfs(1);
        System.out.println(Math.max(dp[1][0], dp[1][1]));
    }

    static void dfs(int cur) {

        // 방문한 곳은 가지 않는다.
        if (visited[cur] == 1) {
            return;
        }

        // 방문 체크하고,
        // cur 이 일반마을인 경우와 우수 마을인 경우를 따로 체크
        // 사람 수는 우수 마을인 경우에만 셈
        visited[cur] = 1;
        dp[cur][0] = 0;
        dp[cur][1] = people[cur];
        
        // cur의 자식 노드들에 대해
        for (Integer v: adj.get(cur)) {
            if (visited[v] == 1) {
                continue;
            }
            // 방문하지 않았다면 끝까지 타고 들어간다.
            dfs(v);

            // 일반 마을은 자식 마을이 우수거나, 일반이다.
            // 우수 마을 사람 수가 더 큰 쪽을 선택한다.
            dp[cur][0] = dp[cur][0] + Math.max(dp[v][0], dp[v][1]);

            // cur이 우수 마을이면 자식 노드는 모두 일반 마을이다.
            dp[cur][1] = dp[cur][1] + dp[v][0];
        }
    }
}
