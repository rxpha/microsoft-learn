def process_numbers(unproc_list):
    proc_list = []
    if isinstance(unproc_list, list) == False:
        return proc_list
    for item in unproc_list:
        if isinstance(item, int):
            proc_list.append(item)
        elif isinstance(item, str):
            if item.isnumeric():
                convert = int(item)
                proc_list.append(convert)
    proc_list.sort()
    return proc_list

def process_names(unproc_list):
    proc_list = []
    if isinstance(unproc_list, list) == False:
        return proc_list
    for item in unproc_list:
        if isinstance(item, str):
            if item.isnumeric() == False:
                proc_list.append(item)
    proc_list.sort()
    return proc_list