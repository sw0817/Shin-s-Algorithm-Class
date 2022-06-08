package com.company;

import java.io.IOException;

public class Programmers42842 {
    static class Solution {
        public int[] solution(int brown, int yellow) {
            int[] answer = new int[2];
            int s = brown + yellow;
            for (int i=s; 2<=i; i--) {
                if (0 == s % i) {
                    int v = s / i;
                    if (yellow == (i-2) * (v-2)) {
                        answer[0] = i;
                        answer[1] = v;
                        return answer;
                    }
                }
            }
            return answer;
        }
    }

    public static void main(String[] args) throws IOException {
        Programmers42842.Solution s = new Programmers42842.Solution();
    }
}
