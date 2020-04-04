print('=' * 16 + '\t你好，欢迎来到古灵阁\t' + '=' * 16)
print('2' * 3)

question_one = input('请问您需要帮助吗？[y or n]：')
if question_one == 'y':
    print('请问您需要什么帮助呢？')
    print('\t1、存取款')
    print('\t2、货币兑换')
    print('\t3、咨询')
    question_two = input('请选择[1-3]：')
    if question_two == '1':
        print('推荐去存取款窗口')
    elif question_two == '2':
        print('金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币')
        money = input('请问您要兑换多少金加隆呢？：')
        print(f'好的，我知道了，您需要兑换{money}金加隆')
        money = float(money) * 51.3
        print(f'那么，您需要付给我{money}人民币')
    elif question_two == '3':
        print('推荐你去咨询窗口')
    else:
        print('您输入的信息有误')
else:
    print('好的，再见！')
