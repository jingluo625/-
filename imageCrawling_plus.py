import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time
import os

headers = {
    'User-Agent': UserAgent().random
}

# 菜单栏
def menu():
    print('\t\t\t\t\t\t\t\t\t\t3G手机壁纸下载\t\t\t\t')
    print('\t\t1.美女\t\t2.明星\t\t3.影视\t\t4.动漫\t\t5.卡通\t\t6.汽车\t\t7.爱情\t\t8.游戏\t\t9.体育\t\t10.车模')
    print('\t\t11.风景\t\t12.品牌\t\t13.可爱\t\t14.节日\t\t15.建筑\t\t16.植物\t\t17.动物\t\t18.创意\t\t19.精美')

# 选择下载壁纸类型
def selectType():
    menu()
    type = ''
    page = 0
    while True:
        opt = int(input('\t\t请输入你想下载的壁纸类型(例：下载美女壁纸，则输入1):'))
        if 1<=opt<=19:
            if opt == 1:
                type = 'MN'
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
    return type,page

# 下载图片
def download(url,type,page):
    type_url = url + type + '/'
    for page_numble in range(1, page+1):
        print('======================================开始爬取第{}页壁纸！======================================'.format(page_numble))
        if page_numble > 1:
            type_url = url + type + '/index_{}.html'
        page_url = type_url.format(page_numble)
        response = requests.get(page_url, headers=headers)
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

        print('======================================第{}页壁纸爬取完毕！======================================'.format(
            page_numble))
        print('\n')
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
   


if __name__ == '__main__':
    url = 'https://www.3gbizhi.com/wall'
    type,page = selectType()
    download(url,type,page)
    # print(type_url)

