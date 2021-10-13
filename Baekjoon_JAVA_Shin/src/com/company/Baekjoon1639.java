package com.company;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Baekjoon1639 {

    static int[] numList, subSum;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        int n = input.length();
        numList = new int[n];
        subSum = new int[n+1];
        for (int i=0; i < n; i++) {
            numList[i] = input.charAt(i) - 48;
        }
        for (int i=1; i < n+1; i++) {
            subSum[i] = subSum[i-1] + numList[i-1];
        }
        int result = 0;
        int l = n / 2;
        while (0 < l) {
            int idx = 0;
            while (idx + (l * 2) < n+1) {
                int left = subSum[idx+l] - subSum[idx];
                int right = subSum[idx+(l*2)] - subSum[idx+l];
                if (left == right) {
                    result = l*2;
                    l = 0;
                    break;
                }
                idx++;
            }
            l--;
        }
        System.out.println(result);
    }
}
