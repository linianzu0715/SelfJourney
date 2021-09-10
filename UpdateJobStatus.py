import fileinput

def finishJob(JobNumber):
    EXP_GODEN = alter("Storage/Job.csv", JobNumber)
    EXP = EXP_GODEN[0]
    GODEN = EXP_GODEN[1]
    print("要增加的经验值为"+str(EXP))
    print("要增加的金币为" + str(GODEN))

def alter(file,JobNumber):
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
            if line_list[0] == str(JobNumber) and line_list[5] == "0":
                EXP = line_list[3]
                GODEN = line_list[4]
                line_list[5] = "1"
                newLine = ",".join(line_list)
                line = line.replace(line, newLine) + "\n"
                print(line)
            file_data += line
    with open(file,"w") as f:
        f.write(file_data)
    returnData = [];
    returnData.append(EXP)
    returnData.append(GODEN)
    return returnData


if __name__ == '__main__':
    finishJob(1)
