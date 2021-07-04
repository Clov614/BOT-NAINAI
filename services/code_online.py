import requests

def code_online(name,code):

    middle_code = code.strip()
    fin_code = middle_code.replace("&#91;","[").replace("&#93;","]")
    error_json = {
        "stdout":" ",
        "error":"并未支持此语言 or 语法错误",
        "stderr":" ",

    }

    headers = {
        "Authorization":"4509b94e-6464-4f87-aacc-a02bba172ae3",
        "Content-type":"application/json",


    }
    if name[-3:] == ".py":
        url = "https://glot.io/api/run/python/latest"
    elif name[-3:] == ".kt":
        url = "https://glot.io/api/run/kotlin/latest"
    elif name[-3:] == ".js":
        url = "https://glot.io/api/run/javascript/latest"
    elif name[-5:] == ".java":
        url = "https://glot.io/api/run/java/latest"
    else:
        return error_json
    data = {
        "files":[{
          "name": name,
          "content": fin_code,
        }]
    }

    # if input != "None":
    #     data = {
    #         "stdin": input,
    #         "files":[{
    #         "name": name,
    #         "content": code,
    #     }]
    # }

    response = requests.post(url=url,headers=headers,json=data)
    data_json = response.json()
    # print(data_json)
    return data_json
