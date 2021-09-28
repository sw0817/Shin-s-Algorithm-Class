package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Baekjoon1544 {

    static Integer N, ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        ans = 0;
        Set<String> stringSet = new HashSet<>();
        for (int i=0; i < N; i++) {
            String input = br.readLine();
            if (!stringSet.contains(input)) {
                ans++;
                int l = input.length();
                for (int j = 0; j < l; j++) {
                    int idx = j;
                    int cnt = 0;
                    StringBuilder temp = new StringBuilder();
                    while (cnt < l) {
                        temp.append(input.charAt(idx));
                        cnt++;
                        idx = (idx + 1) % l;
                    }
                    String word = temp.toString();
                    stringSet.add(word);
                }
            }
        }
        System.out.println(ans);
    }
}
