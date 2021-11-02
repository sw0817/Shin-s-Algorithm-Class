package com.company;

import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        List<String> lst = new ArrayList<>();

        Arrays.stream(strings).forEach(el -> {
            lst.add(el.charAt(n) + el);
        });

        Collections.sort(lst);

        int l = lst.size();
        String[] answer = new String[l];

        for (int i=0; i < l; i++) {
            answer[i] = lst.get(i).substring(1, lst.get(i).length());
        }

        return answer;
    }
}