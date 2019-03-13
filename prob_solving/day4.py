# https://www.hackerrank.com/challenges/nested-list/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    n = int(input())
    ans_dict = {}
    for _ in range(n):
        name = input()
        score = float(input())
        ans_dict.update({name: score})

    scores = list(ans_dict.values())

    scores.sort(reverse=True)

    runner_up = n - 2
    while scores[runner_up] == scores[runner_up + 1]:
        runner_up -= 1

    ans = []
    for key in reversed(list(ans_dict.keys())):
        if ans_dict[key] == scores[runner_up]:
            ans.append(key)

    for ans_i in sorted(ans):
        print(ans_i)
