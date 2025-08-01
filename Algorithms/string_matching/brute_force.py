def brute_force(str, pattern):
    if not pattern:
        return 0
    for i in range(len(str)-len(pattern)+1):
        str_i = i
        pattern_i = 0
        print(str_i, pattern_i, 'i')
        while str_i<len(str) and pattern_i<len(pattern) and str[str_i]==pattern[pattern_i]:
            print(str[str_i], 'aur' ,pattern[pattern_i])

            str_i+=1
            pattern_i+=1
        if pattern_i==len(pattern):
            return str[i:] 
    return -1

print(brute_force('iamyash', 'sh'))
