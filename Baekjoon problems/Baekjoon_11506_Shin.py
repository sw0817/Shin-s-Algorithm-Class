# 백준 11506 占쏙옙
# Baekjoon 11506

# Created by sw0817 on 2021. 09. 19..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/11506

'''
힌트
占쏙이옙占쏙옙占쏙옙占쏙옙占쏙문옙占쏙옙占쏙옙占쏙옙占쏙제옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙는옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙예占쏙옙占제쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙를옙占쏙옙占쏙옙占쏙옙占쏙옙채占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙점占쏙옙占쏙옙占쏙옙占쏙옙占쏙하옙占지쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙않옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙습옙占쏙옙占쏙옙占쏙니옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙다占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙.
占쏙옙데占쏙옙占쏙옙占쏙옙占쏙옙占쏙이옙占쏙옙占쏙터옙占쏙옙占는쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙한占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙개옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙입占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙니占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙다옙
占쏙옙占쏙옙占쏙옙입占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙력占쏙옙占쏙옙占쏙옙占쏙옙을占쏙옙占쏙옙占쏙옙占쏙옙占쏙받옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占을쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙필占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙요占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙는옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙없占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占쏙옙占다쏙옙占쏙옙
'''

# 힌트에서 '占쏙옙' 을 모두 제거하면,
# '이문제는예제를채점하지않습니다.
# 데이터는한개입니다.
# 입력을받을필요는없다.'
# 라는 힌트를 얻게 되고, 데이터는 1개라는 사실을 알게 됩니다.
# '占쏙옙'의 각 문자를 'EUC-KR'로 인코딩 하면, 각각 16진수로
# EFBF, BDEF, BFBD 가 되고
# 하나로 이어 붙이면 'EFBFBDEFBFBD' 가 됩니다.
# 이는 'EFBFBD' 가 두 번 반복되는 형태이므로
# 'EFBFBD'를 'UTF-8'로 인코딩 하면
# � 문자가 나오게 됩니다.

print('�')