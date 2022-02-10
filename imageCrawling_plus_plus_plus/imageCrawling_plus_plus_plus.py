import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time
import os
from concurrent.futures import ThreadPoolExecutor

headers = {
    'User-Agent': UserAgent().random
}

# 选择下载壁纸类型
def selectType(opt):
    # menu()
    type = ''
    page = 0
    while True:
        if 1 <= opt <= 19:
            if opt == 1:
                type = 'MV'
                page = 38
            elif opt == 2:
                type = 'MX'
                page = 11
            elif opt == 3:
                type = 'YS'
                page = 17
            elif opt == 4:
                type = 'DM'
                page = 51
            elif opt == 5:
                type = 'KT'
                page = 11
            elif opt == 6:
                type = 'QC'
                page = 13
            elif opt == 7:
                type = 'AQ'
                page = 3
            elif opt == 8:
                type = 'YX'
                page = 9
            elif opt == 9:
                type = 'TY'
                page = 5
            elif opt == 10:
                type = 'CM'
                page = 7
            elif opt == 11:
                type = 'FJ'
                page = 33
            elif opt == 12:
                type = 'PP'
                page = 4
            elif opt == 13:
                type = 'KA'
                page = 3
            elif opt == 14:
                type = 'JR'
                page = 2
            elif opt == 15:
                type = 'JZ'
                page = 3
            elif opt == 16:
                type = 'ZW'
                page = 3
            elif opt == 17:
                type = 'DW'
                page = 6
            elif opt == 18:
                type = 'CY'
                page = 10
            else:
                type = 'JM'
                page = 16
            break
        else:
            print('\t\t输入错误，请重新输入!')
            continue
    return type, page


# 下载图片
def download(url):
    response = requests.get(url, headers=headers)
    url_text = response.text
    # print(response.text)

    # 数据解析
    page = BeautifulSoup(url_text, 'html.parser')
    li_list = page.find('div', class_='contlistw').find_all('li')
    for li in li_list:
        img_url = li.find('a', class_='imgw').get('href')
        # print(img_url)
        img_response = requests.get(img_url, headers=headers)
        # print(img_response.text)
        page2 = BeautifulSoup(img_response.text, 'html.parser')
        a_html = page2.find('div', class_='morew').find_all('a')
        # print(a_html)
        download_url = a_html[0].get('href')
        # print(download_url)
        img_name = page2.find('div', class_='showtitle').find('h2').text
        # print(img_name)

        # 下载图片
        imgSave(download_url, img_name)
    # print(li_list)
    response.close()


# 图片本地化存储
def imgSave(download_url, img_name):
    path = 'E:/PyCharm/python_code/courseDesign/img'
    if not os.path.exists(path):
        os.makedirs(path)
    img_resp = requests.get(download_url, headers=headers)
    with open('img/' + img_name + '.jpg', 'wb') as f:
        f.write(img_resp.content)
        print(img_name + '   下载成功！')
    # time.sleep(1)


def img_download(type,page):
    url = 'https://www.3gbizhi.com/wall'
    # type, page = selectType()
    page_url1 = url + type + '/'
    page_url = url + type + '/index_{}.html'
    # for i in range(1, page + 1):
    #     print(page_url.format(i) if i > 1 else page_url1)
    with ThreadPoolExecutor(50) as t:
        for i in range(1, page + 1):
            t.submit(download, page_url.format(i) if i > 1 else page_url1)
    print('全部爬取完毕！！！')


if __name__ == '__main__':
    img_download('MV',38)

    # python3: input("please input any key to exit!")
