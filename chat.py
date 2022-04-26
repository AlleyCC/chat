


#讀取檔案
def read_file(filename):
    chat_record = []
    with open(filename,'r', encoding = 'utf-8-sig') as f:
        for line in f:
            chat_record.append(line.strip())
    return chat_record


#將Allen,Tom加入name清單

#將chat內容加入chat清單
def convert(chat_record):
    new = []
    person = None #先宣告，但仍沒有值
    for line in chat_record: #一行一行讀取，所以用continu把名字找出來取代成person
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:  #如果person有值，才執行下面的步驟
            new.append(person + ':' + line)  #字串的合併，最後全部變成一個字串
    return new  #回傳出new清單


        

#寫出檔案
def write_file(filename,chat_record): #多設計chat_record為了寫入chat_record清單
    with open(filename,'w', encoding='utf-8-sig') as f:
        for line in chat_record:
            f.write(line + '\n')

def main():
    chat_record = read_file('input.txt')
    chat_record = convert(chat_record)
    write_file('output.txt', chat_record)

main()
