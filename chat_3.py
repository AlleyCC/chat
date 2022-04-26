lines = []
with open('3.txt','r', encoding = 'utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())


for line in lines:     #字串可以當作清單來看待
    s = line.split(' ')  
    time = s[0][:5]       #結尾值不包含
    name = s[0][5:]
    print(name)

    