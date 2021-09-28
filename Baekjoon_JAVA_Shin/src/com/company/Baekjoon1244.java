package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Baekjoon1244 {

    static int N, M;
    static Integer[] switchs;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        switchs = new Integer[N];
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        for (int i=0; i < N; i++) {
            switchs[i] = Integer.parseInt(st.nextToken());
        }
        M = Integer.parseInt(br.readLine());
        for (int i=0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int sex = Integer.parseInt(st.nextToken());
            int idx = Integer.parseInt(st.nextToken());
            if (sex == 1) {
                int plus = idx;
                while (idx <= N) {
                    switchs[idx-1] = (switchs[idx-1] + 1) % 2;
                    idx += plus;
                }
            } else {
                idx -= 1;
                int left = idx - 1;
                int right = idx + 1;
                switchs[idx] = (switchs[idx] + 1) % 2;
                while (0 <= left && right < N && switchs[left] == switchs[right]) {
                    switchs[left] = (switchs[left] + 1) % 2;
                    switchs[right] = (switchs[right] + 1) % 2;
                    left -= 1;
                    right += 1;
                }
            }
        }

        for (int i=0; i < N; i++) {
            System.out.print(switchs[i] + " ");
            if ((i+1) % 20 == 0) {
                System.out.println();
            }
        }
    }
}
