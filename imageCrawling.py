import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time
import os

headers = {
    'User-Agent': UserAgent().random
}

def download(url):
    for page_numble in range(1, 191):
        page_url = url.format(page_numble)
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
            imgSave(download_url,img_name)

        print('======================================第{}页壁纸爬取完毕！======================================'.format(page_numble))
        # print(li_list)
    response.close()

def imgSave(download_url,img_name):
    path = 'E:/PyCharm/python_code/courseDesign/img'
    if not os.path.exists(path):
        os.makedirs(path)
    img_resp = requests.get(download_url, headers=headers)
    with open('E:/PyCharm/python_code/courseDesign/img/'+img_name + '.jpg', 'wb') as f:
        f.write(img_resp.content)
        print(img_name + '   下载成功！')
    

if __name__ == '__main__':
    url = 'https://www.3gbizhi.com/sjbz/index_{}.html'
    download(url)

