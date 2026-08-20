#######################################################
# @Author       JachynRen                             #
# @Version      0.1                                   #
# @Description  替换Folium和Leaflet资源地址加速网页加载    #
#######################################################


import os
import re
import json
import urllib.request
from urllib.error import HTTPError

TOOLTIPS = True  # 改为False禁用提示信息

MODEL_NAME = "foliumacc.py"
MODEL_VERSION = 0.3

VERSION_URL = "http://121.196.36.104/res/version.json"
RESOURCE_URL = "http://121.196.36.104/res/list.json"
MODEL_URL = "http://121.196.36.104/res/foliumacc.py"
SUBMIT_URL = "http://115.29.204.15:8080/Demo1/saveLog?log="
LOCAL_CACHE = "res/list.json"
REGX = r'(?:<script src="|<link rel="stylesheet" href=")' \
       r'((?:https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+' \
       r'[-A-Za-z0-9+&@#/%=~_|])(?:"></script>|"/>)'

# 能正常访问的资源加入白名单
WHITE_LIST = [
    "https://cdn.jsdelivr.net/npm/leaflet@1.6.0/dist/leaflet.js",
    "https://cdn.jsdelivr.net/npm/leaflet@1.6.0/dist/leaflet.css",
    "https://cdn.jsdelivr.net/npm/leaflet@1.2.0/dist/leaflet.js",
    "https://cdn.jsdelivr.net/npm/leaflet@1.2.0/dist/leaflet.css",
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.1.0/MarkerCluster.Default.css",
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.1.0/MarkerCluster.css",
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.1.0/leaflet.markercluster.js"
]


# ReplaceResource
def rr(htmlpath):
    update()
    if not os.path.isfile(LOCAL_CACHE):
        print("资源列表不存在,请检查网络")
        return
    else:
        json_data = json.load(open(LOCAL_CACHE))

    list_version = json_data["LIST_VERSION"]
    resource_list = json_data["LIST"]
    if TOOLTIPS:
        print("FoliumAccelerator " + str(MODEL_VERSION) + "\nResourceList " + str(list_version))

    fr = open(htmlpath)
    html = fr.read()

    # submit&replace
    reg = re.compile(REGX)
    local_url = reg.findall(html)
    for url in resource_list:
        if url[1] in local_url:
            local_url.remove(url[1])
        elif url[2] in local_url:
            local_url.remove(url[2])
        html = html.replace(url[1], url[2], 1)
    for url in local_url:
        if url not in WHITE_LIST:
            submitUnknownUrl(url)

    fw = open(htmlpath, "w")
    fw.write(html)

    fw.close()
    fr.close()


def update():
    list_local_version = 0.0
    json_data = getJsonFromUrl(VERSION_URL)

    if os.path.isfile(LOCAL_CACHE):
        f = open(LOCAL_CACHE).read()
        if f:
            list_local_version = float(json.loads(f)["LIST_VERSION"])
    else:
        if not os.path.exists("res"):
            os.mkdir("res")

    if json_data:
        list_version_code = float(json_data["LIST_VERSION"])
        model_version_code = float(json_data["MODEL_VERSION"])

        if model_version_code != MODEL_VERSION:
            print("正在更新模块...")
            open(MODEL_NAME, "wb").write(urllib.request.urlopen(MODEL_URL).read())
            print("模块更新成功 下次启动生效 Model Version " + str(model_version_code))

        if list_version_code != list_local_version:
            print("正在更新资源列表...")
            json.dump(getJsonFromUrl(RESOURCE_URL), open(LOCAL_CACHE, "w"))
            print("List更新成功 List Version " + str(list_version_code))
    else:
        print("更新列表失败→尝试使用本地资源...")


def getJsonFromUrl(url):
    try:
        json_data = urllib.request.urlopen(url)
    except HTTPError:
        print("JSON文件获取失败：" + str(url))
        return None
    else:
        return json.load(json_data)


def submitUnknownUrl(url):
    try:
        flag = urllib.request.urlopen(SUBMIT_URL + url)
    except HTTPError:
        print("Unknown Urls update failed...")
        return None
    else:
        return flag
