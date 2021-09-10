def HelloGamePlayer():
    print("欢迎来到《自旅》游戏，旅行者。。。\n")

def CheckPlayerInformation():
    f = open("Storage/PlayerInfomation")
    line = f.readline()  # 调用文件的 readline()方法
    print("当前人物信息：")
    while line:
        print(line.strip("\n"))
        line = f.readline()
    print("\n")
    f.close()

def CheckJob():
    print("当前未完成的任务：")
    with open("Storage/Job.csv") as file:
        for line in file:
            # 只打印出状态为未完成的状态
            line_list = line.strip("\n").split(",")
            if line_list[0] == "任务编号" or line_list[5] == "0":
                print(line.strip("\n"))

def CheckWorkJob():
    print("当前未完成的工作任务：")
    with open("Storage/WorkJob.csv") as file:
        for line in file:
            # 只打印出状态为未完成的状态
            line_list = line.strip("\n").split(",")
            if line_list[0] == "任务编号" or line_list[5] == "0":
                print(line.strip("\n"))

if __name__ == '__main__':
    HelloGamePlayer()
    CheckPlayerInformation()
    CheckJob()
    print("\n")
    CheckWorkJob()