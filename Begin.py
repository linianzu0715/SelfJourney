def HelloGamePlayer():
    print("欢迎来到《自旅》游戏，旅行者。。。\n")

def CheckPlayerInformation():
    f = open("Storage/PlayerInfomation")
    line = f.readline()  # 调用文件的 readline()方法
    print("当前人物信息：")
    while line:
        print(line.strip("\n"))
        line = f.readline()

if __name__ == '__main__':
    HelloGamePlayer()
    CheckPlayerInformation()