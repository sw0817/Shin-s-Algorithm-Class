package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Baekjoon1022 {

    static int r1, c1, r2, c2, cnt, r, c, d, n, t, step;
    static int[][] arr;
    static int[] dr = {0, -1, 0, 1}, dc = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r1 = Integer.parseInt(st.nextToken());
        c1 = Integer.parseInt(st.nextToken());
        r2 = Integer.parseInt(st.nextToken());
        c2 = Integer.parseInt(st.nextToken());

        arr = new int[r2 - r1 + 1][c2 - c1 + 1];
        cnt = (r2 - r1 + 1) * (c2 - c1 + 1);

        r = 0;
        c = 0;
        d = 0;
        n = 1;
        t = 1;
        step = 0;

        while (0 < cnt) {
            if (r1 <= r && r <= r2 && c1 <= c && c <= c2) {
                arr[r - r1][c - c1] = n;
                cnt--;
            }
            n++;
            step++;
            r += dr[d];
            c += dc[d];

            if (step == t) {
                step = 0;
                if (0 < d % 2) {
                    t++;
                }
                d = (d + 1) % 4;
            }
        }

        n--;
        int l = (int)Math.log10(n);

        for (int i=0; i<r2-r1+1; i++) {
            for (int j=0; j<c2-c1+1; j++) {
                for (int k=0; k<l-(int)Math.log10(arr[i][j]); k++) {
                    System.out.print(" ");
                }
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}
