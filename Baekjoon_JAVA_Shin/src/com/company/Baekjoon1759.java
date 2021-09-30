package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Baekjoon1759 {

    static int L, C;
    static Character[] alps;
    static Set<Character> charSet = new HashSet<Character>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        alps = new Character[C];
        for (int i=0; i < C; i++) {
            char temp = st.nextToken().charAt(0);
            alps[i] = temp;
        }
        Arrays.sort(alps);
        charSet.add('a');
        charSet.add('e');
        charSet.add('i');
        charSet.add('o');
        charSet.add('u');
        makeWords(0, 0, new StringBuilder());
    }

    static void makeWords(int k, int idx, StringBuilder word) {
        if (k == L) {
            int cnt = k;
            for (int i=0; i < k; i++) {
                if (charSet.contains(word.charAt(i))) {
                    cnt--;
                }
            }
            if (2 <= cnt && cnt < k) {
                System.out.println(word);
            }
            return;
        } else if (idx == C) {
            return;
        }
        makeWords(k+1, idx+1, word.append(alps[idx]));
        word.deleteCharAt(word.length()-1);
        makeWords(k, idx+1, word);
    }
}
