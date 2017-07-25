import sys
with open(sys.argv[1],'rt',encoding='utf-8') as f:
    with open(sys.argv[2],'a+',encoding='gbk') as outF:
        for ln in f:
            print(ln)
            outF.write(ln)
        