import fileinput
def CheckPlayerInformation():
    f = open("Storage/PlayerInfomation")
    line = f.readline()  # 调用文件的 readline()方法
    print("当前人物信息：")
    while line:
        print(line.strip("\n"))
        line = f.readline()
    f.close()


def finishJob(url,JobNumber):
    EXP_GODEN = alter(url, JobNumber, "0","1")
    EXP = EXP_GODEN[0]
    GODEN = EXP_GODEN[1]
    file_data = ""
    with open("Storage/PlayerInfomation", "r") as f:
        for line in f:
            line_list = line.strip("\n").split(":")
            if line_list[0] == "经验值":
                newEXP = int(line_list[1]) + int(EXP)
                new_line = "经验值:" + str(newEXP) + "\n"
                file_data += new_line
            elif line_list[0] == "金币":
                newGODEN = int(line_list[1]) + int(GODEN)
                new_line = "金币:" + str(newGODEN) + "\n"
                file_data += new_line
            else:
                file_data += line
    with open("Storage/PlayerInfomation","w") as f:
        f.write(file_data)
    CheckPlayerInformation()



def unfinishJOb(JobNumber):
    EXP_GODEN = alter("Storage/Job.csv", JobNumber, "1","0")
    EXP = EXP_GODEN[0]
    GODEN = EXP_GODEN[1]
    if EXP != 0:
        print("要减少的经验值为"+str(EXP))
    if GODEN != 0:
        print("要减少的金币为" + str(GODEN))

def alter(file,JobNumber,oldStatus,newStatsu):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:旧字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    EXP = 0
    GODEN = 0
    with open(file, "r") as f:
        for line in f:
            line_list = line.strip("\n").split(",")
            if line_list[0] == str(JobNumber) and line_list[5] == oldStatus:
                EXP = line_list[3]
                GODEN = line_list[4]
                line_list[5] = newStatsu
                newLine = ",".join(line_list)
                line = line.replace(line, newLine) + "\n"
                print("恭喜你完成任务：")
                print("No：" + line_list[0] + " 任务名称：《" + line_list[1] + "》")
                print("任务状态更新完成\n")
            file_data += line
    with open(file,"w") as f:
        f.write(file_data)
    returnData = [];
    returnData.append(EXP)
    returnData.append(GODEN)
    return returnData


if __name__ == '__main__':
    #如果要完成某个JOB，就在方法中填入JOBID，否则就填入0
    finishJob("Storage/Job.csv",3)
    finishJob("Storage/WorkJob.csv", 3)

    #如果要将JOB回退为未完成状态，就在方法中填入JOBID，否则就填入0
    #unfinishJOb(1)

    #失效任务

