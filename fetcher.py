import requestmaker
import tui

def top():
    top_id = requestmaker.top()
    results = []
    fetch_count = 10

    file = open("./data/sel.txt", "w")

    filedata = ""
    for i in range(fetch_count):
        tui.fetch_progress(i+1, fetch_count)
        result = requestmaker.item(top_id[i])
        results.append(result)
        filedata += str(result["id"])+"\n"

    file.write(filedata)
    file.close()

    return results

def sel(selector):
    id_lists = []

    with open("./data/sel.txt", "r") as file:
        id_lists.extend(file.read().split("\n"))

    return requestmaker.item(int(id_lists[selector]))

def comments(comments_list: list):
    fetch_count = len(comments_list)
    current_count = 0
    results = []
    for i in comments_list:
        current_count += 1
        results.append(requestmaker.comment(i))
        tui.fetch_progress(current_count, fetch_count)
    return results