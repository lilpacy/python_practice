def grow(s,r):
    n=len(s)
    ss=' '
    for i in range(n):
        if s[i]=='f': # 'f'を'fg'に置き換え
            ss=ss+'fg'
        else:
            if s[i]=='g': #'g'を'gh'に置き換え
                ss=ss+'gh'
            else:
                ss=ss+'h' # その他の文字(h)の時そのまま
    print(ss)
    r -= 1
    if r > 0: # 残り回数が0回出ない時自分自身を呼び出す
        grow(ss,r)
        return ss

grow('fgh',2) # growを2回実行
