def solution(my_strings, parts):
    result = []
    
    for i in range(len(my_strings)):
        s, e = parts[i]
        string = my_strings[i]
        
        # 부분 문자열을 추출하여 이어 붙임
        substring = string[s:e+1]
        result.append(substring)
    
    return ''.join(result)

print(solution(["progressive", "hamburger", "hammer", "ahocorasick"],[[0, 4], [1, 2], [3, 5], [7, 7]]))