import sys

N, new_score, P = map(int, sys.stdin.readline().split())

rank = 0 #초기값

if N > 0:
    rank_list = list(map(int, sys.stdin.readline().split()))
    # rank_list에 new_score가 있는지 확인
    for i in range(len(rank_list)):
        if rank_list[i] == new_score:
            rank = i + 1  # 같은 점수가 있을 때는 그러한 점수의 등수 중에 가장 작은 등수가 된다.
            if rank == P:
                rank = -1  # 만약, 랭킹 리스트가 꽉 차있을 때, 새 점수가 이전 점수보다 더 좋을 때만 점수가 바뀐다.
            break

    # rank_list에 같은 수가 없다면 new_score를 rank_list에 입력해서 rank 확인
    if rank == 0:
        rank_list.append(new_score)
        # 내림차순 정렬
        rank_list.sort(reverse=True)

        # 랭킹 계산
        for i in range(len(rank_list)):
            if rank_list[i] == new_score:
                rank = i + 1  # 같은 점수가 있을 때는 그러한 점수의 등수 중에 가장 작은 등수가 된다.
                break
            elif rank_list[i] < new_score:
                rank = i + 1  # 같은 점수가 있을 때는 그러한 점수의 등수 중에 가장 작은 등수가 된다.
                break
else:
    rank = 1


print(rank)