package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Baekjoon3541 {

    static int n, m;
    static long result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        result = (long)n * 1000;
        for (int i=0; i<m; i++) {
            st = new StringTokenizer(br.readLine());
            int up = Integer.parseInt(st.nextToken());
            int down = -1 * Integer.parseInt(st.nextToken());
            int l = 1;
            int h = n + 1;

            while (l < h) {
                int mid = (l + h) / 2;
                long upFloor = (long)up * mid;
                long downFloor = (long)down * (n - mid);
                if (0 < upFloor + downFloor) {
                    h = mid;
                    result = Math.min(result, (upFloor + downFloor));
                } else {
                    l = mid + 1;
                }
            }
        }

        System.out.println(result);
    }
}
