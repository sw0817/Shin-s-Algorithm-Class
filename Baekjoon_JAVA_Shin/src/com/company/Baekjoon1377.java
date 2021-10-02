package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Baekjoon1377 {

    static int N;
    static Point[] arr;
    static boolean changed;

    static class Point implements Comparable<Point> {
        int num;
        int idx;

        Point(int num, int idx) {
            this.num = num;
            this.idx = idx;
        }

        @Override
        public int compareTo(Point o) {
            return num - o.num;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new Point[N];
        for (int i=0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());
            arr[i] = new Point(num, i);
        }
        Arrays.sort(arr);

        int result = 0;
        for (int i=0; i < N; i++) {
            result = Math.max(result, arr[i].idx - i + 1);
        }

        System.out.println(result);
    }
}
