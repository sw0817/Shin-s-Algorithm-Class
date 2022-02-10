package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Baekjoon1004 {

    static int T, x1, x2, y1, y2, cx, cy, r, n, result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        T = Integer.parseInt(br.readLine());
        for (int t=0; t<T; t++) {
            st = new StringTokenizer(br.readLine());
            x1 = Integer.parseInt(st.nextToken());
            y1 = Integer.parseInt(st.nextToken());
            x2 = Integer.parseInt(st.nextToken());
            y2 = Integer.parseInt(st.nextToken());
            n = Integer.parseInt(br.readLine());
            result = 0;
            for (int i=0; i<n; i++) {
                st = new StringTokenizer(br.readLine());
                cx = Integer.parseInt(st.nextToken());
                cy = Integer.parseInt(st.nextToken());
                r = Integer.parseInt(st.nextToken());
                int s = 0;
                if (Math.sqrt(Math.pow((cx - x1), 2) + Math.pow((cy - y1), 2)) < r) {
                    s++;
                }
                if (Math.sqrt(Math.pow((cx - x2), 2) + Math.pow((cy - y2), 2)) < r) {
                    s++;
                }
                if (s == 1) {
                    result++;
                }
            }
            System.out.println(result);
        }
    }
}
