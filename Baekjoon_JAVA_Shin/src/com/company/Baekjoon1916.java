package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Baekjoon1916 {

    static int N, M;
    static ArrayList<ArrayList<Edge>> adj;

    static class Edge {
        int v;
        int w;

        Edge(int _v, int _w) {
            this.v = _v;
            this.w = _w;
        }
    }

    static class PriorityNode {
        int v;
        int w;

        PriorityNode(int _v, int _w) {
            this.v = _v;
            this.w = _w;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());

        // 인접리스트 만들기
        adj = new ArrayList<ArrayList<Edge>>();
        for (int i=0; i < N+1; i++) {
            adj.add(new ArrayList<Edge>());
        }

        // 간선, 가중치 등록
        for (int i=0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            adj.get(s).add(new Edge(e, w));
        }

        // 출발 도시 및 도착 도시
        st = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());

        // 다익스트라 구현 (우선순위큐로 다시 구현할 것)
        int[] distance = new int[N+1];
//        boolean[] visited = new boolean[N+1];

        for (int i=0; i < N+1; i++) {
            distance[i] = 1000 * 100000;
        }

        distance[s] = 0;
//        visited[s] = true;

//        Queue<Node> q = new LinkedList<>();
        PriorityQueue<PriorityNode> q = new PriorityQueue<>((o1, o2) -> o1.w - o2.w);
        q.add(new PriorityNode(s, 0));
        while (!q.isEmpty()) {
            PriorityNode priorityNode = q.poll();
            for (int i=0; i < adj.get(priorityNode.v).size(); i++) {
                Edge j = adj.get(priorityNode.v).get(i);
                if (j.w + priorityNode.w < distance[j.v]) {
                    distance[j.v] = j.w + priorityNode.w;
                    q.add(new PriorityNode(j.v, j.w + priorityNode.w));
                }
            }
        }

        System.out.println(distance[e]);
    }
}