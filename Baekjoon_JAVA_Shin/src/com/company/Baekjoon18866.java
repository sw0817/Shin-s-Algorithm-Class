package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Baekjoon18866 {

    static int N, inf, min, max, result;
    static int[][] info, young, old;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        inf = 1000000001;
        N = Integer.parseInt(br.readLine());
        min = inf;
        max = 0;
        info = new int[N][2];
        young = new int[N][2];
        old = new int[N][2];
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            info[i][0] = Integer.parseInt(st.nextToken());
            info[i][1] = Integer.parseInt(st.nextToken());

            if (info[i][0] == 0) {
                young[i][0] = min;
            } else {
                min = Math.min(info[i][0], min);
                young[i][0] = min;
            }

            max = Math.max(info[i][1], max);
            young[i][1] = max;
        }

        min = inf;
        max = 0;
        for (int i=N-1; 0<=i; i--) {
            if (info[i][1] == 0) {
                old[i][1] = min;
            } else {
                min = Math.min(info[i][1], min);
                old[i][1] = min;
            }

            max = Math.max(info[i][0], max);
            old[i][0] = max;
        }

        for (int i=1; i<N; i++) {
            if (young[i-1][0] > old[i][0] && young[i-1][1] < old[i][1]) {
                result = i;
            }
        }

        if (result == 0) {
            System.out.println(-1);
        } else {
            System.out.println(result);
        }
    }
}
