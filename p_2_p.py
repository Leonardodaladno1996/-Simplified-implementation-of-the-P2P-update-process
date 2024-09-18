n, k = map(int, input().split())

#Словарь обновлений к установке
updates = {i + 1: {"number": i + 1, "count": 1, "to_load" : {j + 1 for j in range(n)}, "loaded": set()}for i in range(k)}
#Словарь устройств
devices = {i + 1: {"number": i + 1, "count": 0, "favorites": {j + 1: 0 for j in range(n) if j != i}} for i in range(n)}
devices[1]["count"] = k
for i in range(k):
    updates[i + 1]["to_load"].remove(1)
for i in range(k):
    updates[i + 1]["loaded"].add(1)



answer_list = [] 
answer_list.append((0, 1))
counter = 0
def time_slot_process():
    '''
    Функция реализующий один временной слот запроса обновлений
    '''
    global counter, updates, devices, answer_list
    counter += 1
    operative_set = {i + 1 for i in range(n)}
    requests_dict = {}
    for update in sorted(updates.values(), key=lambda x: (x["count"], x["number"])):
        sorted_loaded = min(updates[update["number"]]["loaded"], key=lambda x: (devices[x]["count"], x))
        if update["to_load"]:
            for device in update["to_load"]:
                if device in operative_set:
                    if sorted_loaded not in requests_dict:
                        requests_dict[sorted_loaded] = [(device, update["number"])]
                    else:
                        requests_dict[sorted_loaded].append((device, update["number"]))
                operative_set.discard(device)
    favorites_dict = {}
    count_dict = {}
    for device in requests_dict:
        if device not in favorites_dict:
            favorites_dict[device] = {}
        for request_device, _ in requests_dict[device]:
            favorites_dict[device][request_device] = devices[device]["favorites"][request_device]
            
    for device in requests_dict:
        for request_device, _ in requests_dict[device]:
            if request_device not in count_dict:
                count_dict[request_device] = 0
            count_dict[request_device] = devices[request_device]["count"]
            
            
        
        
    return requests_dict, favorites_dict, count_dict

def make_updates(requests_dict, favorites_dict, count_dict):
    '''
    Реализация процесса скачивания обновлений за один временной слот
    '''
    global counter, updates, devices, answer_list
    for device in requests_dict.keys():
        max_device, max_favorite = -1, -1
        current_update = -1
        for request_device, update in requests_dict[device]:
            if favorites_dict[device][request_device] > max_favorite:
                max_device = request_device
                max_favorite = favorites_dict[device][request_device]
                current_update = update
            elif favorites_dict[device][request_device] == max_favorite and count_dict[request_device] < count_dict[max_device]:
                max_device = request_device
                current_update = update
            elif favorites_dict[device][request_device] == max_favorite and count_dict[request_device] == count_dict[max_device] and request_device < max_device:
                max_device = request_device
                current_update = update
        
        devices[max_device]["count"] += 1
        if devices[max_device]["count"] == k:
            answer_list.append((counter, max_device))
        devices[max_device]["favorites"][device] += 1
        updates[current_update]["to_load"].remove(max_device)
        updates[current_update]["loaded"].add(max_device)
        updates[current_update]["count"] += 1

        
            
while len(answer_list) < n:
    request_dict, favorites_dict, count_dict = time_slot_process()
    make_updates(request_dict, favorites_dict, count_dict)

    
answer_list.sort(key=lambda x: x[1])
answer_list_to_print = []
for i in range(len(answer_list)):
    answer_list_to_print.append(answer_list[i][0])
    
print(*answer_list_to_print[1:])