def solution(n, words):
    turn = 1
    answer = [words[0]]

    for i in range(1, len(words)):
        if words[i] in answer:
            print("a")
            return [i % n + 1, turn]
        
        if words[i-1][-1] != words[i][0]:
            print("b")
            return [i % n + 1, turn]
        
        
        answer.append(words[i])
        print(answer)
        
        if (i + 1) % n == 0:
            turn += 1
        
    return [0, 0]


print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))