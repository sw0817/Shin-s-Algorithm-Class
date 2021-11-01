package com.company;

import java.util.*;

public class Programmers68644 {

    static Set<Integer> numSet;

    static class Solution {
        public int[] solution(int[] numbers) {
            numSet = new HashSet<>();
            for (int i=0; i < numbers.length - 1; i++) {
                for (int j=i+1; j < numbers.length; j++) {
                    numSet.add(numbers[i] + numbers[j]);
                }
            }

            List<Integer> lst = new ArrayList<>();

            numSet.stream().forEach(el -> {
                lst.add(el);
            });

            lst.sort((o1, o2) -> o1 - o2);

            return lst.stream().mapToInt(el -> el).toArray();
        }
    }

    public static void main(String[] args) throws Exception {
        Solution s = new Solution();
    }
}
