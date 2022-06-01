import json
import os
import hashlib

def get_hash(file_name):
    blockchain_dir = os.curdir + '/transactions/'
    file = open(blockchain_dir + str(file_name), 'rb').read()
    return hashlib.md5(file).hexdigest()

def check():
    blockchain_dir = os.curdir + '/transactions/'
    files = os.listdir(blockchain_dir)
    files = sorted([int(i) for i in files])
    resultt = list()
    for file in files[1:]:
        f = open(blockchain_dir + str(file))
        h = json.load(f)['hash']
        prev_file = str(file - 1)
        act_hash = get_hash(prev_file)

        if h == act_hash:
            result = 'OK'
        else:
            result = 'Was changed data'
        resultt.append({'block': prev_file, 'result':result})
    return resultt

        # print(f'Block {prev_file} is {result}')
        # return f'Block {prev_file} is {result}'


def write_block(name, amount, to_whom):
    blockchain_dir = os.curdir + '/transactions/'

    files = os.listdir(blockchain_dir)
    files = sorted([int(i) for i in files])
    last_file = files[-1]
    file_name = last_file + 1
    prev_hash = get_hash(last_file)
    data = {
        'name' : name,
        'amount' : amount,
        'to_whom' : to_whom,
        'hash' : prev_hash
    }
    with open(blockchain_dir + f'{file_name}', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def main():
    pass
    # write_block('Alina', 200, 'Aijana')
    # print(get_hash(1))
    # check()

if __name__ == '__main__':
    pass
    # main()
