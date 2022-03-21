process_1 = ['p1',1,6]
process_2 = ['p2',3,3]
process_3 = ['p3',5,2]
process_4 = ['p4',7,5]
process_5 = ['p5',9,4]
process_7 = ['p7',9,12]
process_8 = ['p8',14,5]

proceccing_list = []

proceccing_list.append(process_1)
proceccing_list.append(process_2)
proceccing_list.append(process_3)
proceccing_list.append(process_4)
proceccing_list.append(process_5)
proceccing_list.append(process_7)
proceccing_list.append(process_8)

total_running_time = 0
for process in proceccing_list:
    total_running_time += process[2]

print(total_running_time)

ready_queue = []

for i in range(1,total_running_time + 1):
    print("-------")
    for process in proceccing_list:

        if process[1] == i:
            print(str(i) + ": " +  str(process[0]))                            #execution
            process[2] = process[2]-1
            if process[2] > 0:
                ready_queue.append(process)
                break
        else:
            continue
        break
    else:
        for process in ready_queue:
            if process[2] == 0:
                ready_queue.remove(process)
        print(str(i) + ": " + str(ready_queue[0][0]))
        ready_queue[0][2] = ready_queue[0][2] - 1
        buffer = ready_queue[0]
        ready_queue.remove(ready_queue[0])
        ready_queue.append(buffer)










# list = [1,2,3,4,5]
# print(str(list[0]))
# buffer = list[0]
# list.remove(list[0])
# list.append(buffer)
# print(list)

