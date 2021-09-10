

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

def addWorkJob(jobName,jobType,jobExp,jobGoden):
    file_data = ""
    num = 0
    with open("Storage/WorkJob.csv", "r") as f:
        for line in f:
            line_list = line.strip("\n").split(",")
            if line_list[0] != "任务编号":
                num = int(line_list[0])
            file_data += line
    with open("Storage/WorkJob.csv","w") as f:
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
    print("工作任务增加完成！")
    print("工作任务编号：" + str(num+1) + " 任务名称：《" + jobName + "》")


if __name__ == '__main__':
    jobName = "新增等级系统"
    jobType = "基础任务"
    jobExp = 50
    jobGoden = 50
    #addJob(jobName, jobType, jobExp, jobGoden)

    workJobName = "检查一下昨天合并到qa分支的换签自动化执行状态"
    workJobType = "普通任务"
    workJobExp = 0
    workJobGoden = 5
    addWorkJob(workJobName, workJobType, workJobExp, workJobGoden)




