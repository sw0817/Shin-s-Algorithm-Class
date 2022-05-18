package com.company;

import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;

public class Programmers81302 {
    static class Solution {
        public int[] solution(String[][] places) {
            int[] answer = new int[5];
            for (int i=0; i<5; i++) {
                answer[i] = bfs(places[i]);
            }
            return answer;
        }

        static int bfs(String[] place) {
            int[][] visited = new int[5][5];
            int[] dr = {1, 0, -1, 0}, dc = {0, 1, 0, -1};

            Queue<Node> queue = new LinkedList<>();

            for (int i=0; i<5; i++) {
                for (int j=0; j<5; j++) {
                    if (place[i].charAt(j) == 'P') {
                        queue.add(new Node(i, j));
                    }
                }
            }

            while (!queue.isEmpty()) {
                Node node = queue.poll();
                int r = node.r;
                int c = node.c;
                visited[r][c] = 1;
                for (int k=0; k<4; k++) {
                    int nr = r + dr[k];
                    int nc = c + dc[k];
                    if (0 <= nr && nr < 5 && 0 <= nc && nc < 5) {
                        if (visited[nr][nc] == 1 || place[nr].charAt(nc) == 'P') {
                            return 0;
                        } else if (place[nr].charAt(nc) == 'O') {
                            visited[nr][nc] = 1;
                        }
                    }
                }
            }
            return 1;
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
        Programmers81302.Solution s = new Programmers81302.Solution();
    }
}
