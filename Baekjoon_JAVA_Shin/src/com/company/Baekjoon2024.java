package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Baekjoon2024 {

    static int M, result;
    static ArrayList<Node> lines = new ArrayList<>();
    static HashMap<Integer, Integer> line_map = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        M = Integer.parseInt(br.readLine());
        while (true) {
            st = new StringTokenizer(br.readLine());
            int l = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());
            if (l == 0 && r == 0) {
                break;
            }
            if (r < 0 || M < l) {
                continue;
            }
            if (line_map.containsKey(l)) {
                line_map.put(l, Math.max(line_map.get(l), r));
            } else {
                line_map.put(l, r);
            }
        }

        for (Integer i : line_map.keySet()) {
            lines.add(new Node(i, line_map.get(i)));
        }

        Collections.sort(lines, new NodeComparator());

        result = 0;

        int cur_r = 0;
        int cnt = lines.size();
        int idx = 0;
        int max_r = 0;
        while (idx < cnt) {
            while (idx < cnt && lines.get(idx).l <= cur_r) {
                max_r = Math.max(max_r, lines.get(idx).r);
                idx++;
            }
            if (cur_r < max_r) {
                cur_r = max_r;
                result++;
            } else {
                result = 0;
                break;
            }
            if (M <= max_r) {
                break;
            }
        }

        System.out.println(result);
    }

    static class Node {

        int l, r;

        Node(int l_, int r_) {
            this.l = l_;
            this.r = r_;
        }
    }

    static class NodeComparator implements Comparator<Node> {
        @Override
        public int compare(Node n1, Node n2) {
            if (n1.l > n2.l) {
                return 1;
            } else if (n1.l < n2.l) {
                return -1;
            }
            return 0;
        }
    }
}
