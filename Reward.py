
def checkReward():
    print("当前可兑换的奖励：")
    with open("Storage/reward.csv") as file:
        for line in file:
            # 只打印出状态为未完成的状态
            line_list = line.strip("\n").split(",")
            if line_list[4] != "0":
                print(line.strip("\n"))

def getReward(rewardNum):
    file_data = ""
    consume = 0
    with open("Storage/reward.csv", "r") as f:
        for line in f:
            line_list = line.strip("\n").split(",")
            if line_list[0] == str(rewardNum) and line_list[4] != "0":
                consume = int(line_list[2])
                line_list[3] = str(int(line_list[3])-1)
                newLine = ",".join(line_list)
                line = line.replace(line, newLine) + "\n"
                print("您兑换的奖励为：")
                print("No：" + line_list[0] + " 奖励：《" + line_list[1] + "》")
            file_data += line
    with open("Storage/reward.csv","w") as f:
        f.write(file_data)

    player_file_data = ""
    with open("Storage/PlayerInfomation", "r") as pf:
        for line in pf:
            line_list = line.strip("\n").split(":")
            if line_list[0] == "金币":
                newGODEN = int(line_list[1]) - int(consume)
                new_line = "金币:" + str(newGODEN) + "\n"
                player_file_data += new_line
            else:
                player_file_data += line
    with open("Storage/PlayerInfomation","w") as pf:
        pf.write(player_file_data)

if __name__ == '__main__':
    getReward(1)
    print("\n")
    checkReward()