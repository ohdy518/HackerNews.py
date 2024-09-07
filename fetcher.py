import requestmaker
import tui

def top():
    # TODO: Fetch the top board of HN.
    # DEBUG: For now, the code uses a sample data.
    TOP_ID = requestmaker.top()
    results = []
    FETCH_COUNT = 10

    file = open("./data/sel.txt", "w")

    filedata = ""
    for i in range(FETCH_COUNT):
        tui.fetch_progress(i+1, FETCH_COUNT)
        result = requestmaker.item(TOP_ID[i])
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