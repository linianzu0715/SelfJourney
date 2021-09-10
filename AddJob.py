

def addJob(jobName,jobType,jobExp,jobGoden):
    file_data = ""
    num = 0
    with open("Storage/Job.csv", "r") as f:
        for line in f:
            line_list = line.strip("\n").split(",")
            if line_list[0] != "任务编号":
                num = int(line_list[0])
            file_data += line
    with open("Storage/Job.csv","w") as f:
        new_list = []
        new_list.append(str(num+1))
        new_list.append(jobName)
        new_list.append(jobType)
        new_list.append(str(jobExp))
        new_list.append(str(jobGoden))
        new_list.append("0")
        new_line = ",".join(new_list) + "\n"
        file_data += new_line
        f.write(file_data)
    print("任务增加完成！")
    print("任务编号：" + str(num+1) + " 任务名称：《" + jobName + "》")


if __name__ == '__main__':
    jobName = "基础构建0.1: 任务完成时候增加金币和经验值"
    jobType = "基础构建"
    jobExp = 10
    jobGoden = 10
    addJob(jobName, jobType, jobExp, jobGoden)


