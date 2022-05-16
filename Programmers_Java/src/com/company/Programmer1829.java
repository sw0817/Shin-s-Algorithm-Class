package com.company;

import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;

public class Programmer1829 {
    static int[][] visited;
    static int[] dr = {1, 0, -1, 0}, dc = {0, 1, 0, -1};

    static class Solution {
        public int[] solution(int m, int n, int[][] picture) {
            visited = new int[m][n];

            int max = 0;
            int cnt = 0;

            for (int i=0; i<m; i++) {
                for (int j=0; j<n; j++) {
                    if (visited[i][j] == 0 && picture[i][j] != 0) {
                        int num = picture[i][j];
                        cnt++;
                        Queue<Node> queue = new LinkedList<>();
                        queue.add(new Node(i, j));
                        visited[i][j] = 1;
                        int cur = 1;
                        while (!queue.isEmpty()) {
                            Node node = queue.poll();
                            int r = node.r;
                            int c = node.c;
                            for (int k=0; k<4; k++) {
                                int nr = r + dr[k];
                                int nc = c + dc[k];
                                if (0 <= nr && nr < m && 0 <= nc && nc < n && visited[nr][nc] == 0 && picture[nr][nc] == num) {
                                    queue.add(new Node(nr, nc));
                                    visited[nr][nc] = 1;
                                    cur++;
                                }
                            }
                        }
                        max = Math.max(max, cur);
                    }
                }
            }

            int[] answer = new int[2];
            answer[0] = cnt;
            answer[1] = max;
            return answer;
        }

        static class Node {
            int r;
            int c;

            Node(int r, int c) {
                this.r = r;
                this.c = c;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        Programmer1829.Solution s = new Programmer1829.Solution();
    }
}
