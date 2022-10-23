#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : update.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/6
import re
from time import time as getTime
import sys
import requests
import os
import zipfile
import shutil # https://blog.csdn.net/weixin_33130113/article/details/112336581
from utils.log import logger
from utils.web import get_interval
from utils.htmlParser import jsoup

headers = {
        'Referer': 'https://gitcode.net/',
       # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
  'X-T5-Auth': 'ZjQxNDIh',
        'User-Agent': 'baiduboxapp',
}
proxies={"https":"http://cloudnproxy.baidu.com:443","http":"http://cloudnproxy.baidu.com:443"}
def getHotSuggest(url='http://4g.v.sogou.com/hotsugg'):
    jsp = jsoup(url)
    pdfh = jsp.pdfh
    pdfa = jsp.pdfa
    pd = jsp.pd
    try:
        r = requests.get(url,headers=headers,timeout=2)
        html = r.text
        data = pdfa(html,'ul.hot-list&&li')
        suggs = [{'title':pdfh(dt,'a&&Text'),'url':pd(dt,'a&&href')} for dt in data]
        # print(html)
        # print(suggs)
        return suggs
    except:
        return []

def getLocalVer():
    base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # 上级目录
    version_path = os.path.join(base_path, f'js/version.txt')
    if not os.path.exists(version_path):
        with open(version_path,mode='w+',encoding='utf-8') as f:
            version = '1.0.0'
            f.write(version)
    else:
        with open(version_path,encoding='utf-8') as f:
            version = f.read()
    return version

def getOnlineVer():
    ver = '1.0.1'
    msg = ''
    try:
        r = requests.get('https://gitcode.net/qq_32394351/dr_py/-/raw/master/js/version.txt',timeout=(2,2),proxies=proxies)
        ver = r.text
    except Exception as e:
        # print(f'{e}')
        msg = f'{e}'
        logger.info(msg)
    return ver,msg

def checkUpdate():
    local_ver = getLocalVer()
    online_ver,msg = getOnlineVer()
    if local_ver != online_ver:
        return True
    return False


def del_file(filepath):
    """
    删除execl目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)

def copytree(src, dst, ignore=None):
    if ignore is None:
        ignore = []
    dirs = os.listdir(src)  # 获取目录下的所有文件包括文件夹
    logger.info(f'{dirs}')
    for dir in dirs:  # 遍历文件或文件夹
        from_dir = os.path.join(src, dir)  # 将要复制的文件夹或文件路径
        to_dir = os.path.join(dst, dir)  # 将要复制到的文件夹或文件路径
        if os.path.isdir(from_dir):  # 判断是否为文件夹
            if not os.path.exists(to_dir):  # 判断目标文件夹是否存在,不存在则创建
                os.mkdir(to_dir)
            copytree(from_dir, to_dir,ignore)  # 迭代 遍历子文件夹并复制文件
        elif os.path.isfile(from_dir):  # 如果为文件,则直接复制文件
            if ignore:
                regxp = '|'.join(ignore).replace('\\','/') # 组装正则
                to_dir_str = str(to_dir).replace('\\','/')
                if not re.search(rf'{regxp}', to_dir_str, re.M):
                    shutil.copy(from_dir, to_dir)  # 复制文件
            else:
                shutil.copy(from_dir, to_dir)  # 复制文件


def force_copy_files(from_path, to_path, exclude_files=None):
    # print(f'开始拷贝文件{from_path}=>{to_path}')
    if exclude_files is None:
        exclude_files = []
    logger.info(f'开始拷贝文件{from_path}=>{to_path}')
    if not os.path.exists(to_path):
        os.makedirs(to_path,exist_ok=True)
    try:
        if sys.version_info < (3, 8):
            copytree(from_path, to_path,exclude_files)
        else:
            if len(exclude_files) > 0:
                shutil.copytree(from_path, to_path, dirs_exist_ok=True,ignore=shutil.ignore_patterns(*exclude_files))
            else:
                shutil.copytree(from_path, to_path, dirs_exist_ok=True)

    except Exception as e:
        logger.info(f'拷贝文件{from_path}=>{to_path}发生错误:{e}')

def copy_to_update():
    base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # 上级目录
    tmp_path = os.path.join(base_path, f'tmp')
    dr_path = os.path.join(tmp_path, f'dr_py-master')
    if not os.path.exists(dr_path):
        # print(f'升级失败,找不到目录{dr_path}')
        logger.info(f'升级失败,找不到目录{dr_path}')
        return False
    # 千万不能覆盖super，base
    paths = ['js','models','controllers','libs','static','templates','utils','txt','jiexi','py','whl']
    exclude_files = ['txt/pycms0.json','txt/pycms1.json','txt/pycms2.json','base/rules.db','utils/update.py']
    for path in paths:
        force_copy_files(os.path.join(dr_path, path),os.path.join(base_path, path),exclude_files)
    try:
        shutil.copy(os.path.join(dr_path, 'app.py'), os.path.join(base_path, 'app.py'))  # 复制文件
    except Exception as e:
        logger.info(f'更新app.py发生错误:{e}')
    logger.info(f'升级程序执行完毕,全部文件已拷贝覆盖')
    return True

def download_new_version():
    t1 = getTime()
    base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # 上级目录
    tmp_path = os.path.join(base_path, f'tmp')
    os.makedirs(tmp_path,exist_ok=True)
    url = 'https://gitcode.net/qq_32394351/dr_py/-/archive/master/dr_py-master.zip'
    # tmp_files = os.listdir(tmp_path)
    # for tp in tmp_files:
    #     print(f'清除缓存文件:{tp}')
    #     os.remove(os.path.join(tmp_path, tp))
    del_file(tmp_path)
    msg = ''
    try:
        # print(f'开始下载:{url}')
        logger.info(f'开始下载:{url}')
        r = requests.get(url,headers=headers,timeout=(20,20),proxies=proxies)
        rb = r.content
        download_path = os.path.join(tmp_path, 'dr_py.zip')
        with open(download_path,mode='wb+') as f:
            f.write(rb)
        # print(f'开始解压文件:{download_path}')
        logger.info(f'开始解压文件:{download_path}')
        f = zipfile.ZipFile(download_path, 'r')  # 压缩文件位置
        for file in f.namelist():
            f.extract(file, tmp_path)  # 解压位置
        f.close()
        # print('解压完毕,开始升级')
        logger.info('解压完毕,开始升级')
        ret = copy_to_update()
        logger.info(f'升级完毕,结果为:{ret}')
        # print(f'升级完毕,结果为:{ret}')
        msg = '升级成功'
    except Exception as e:
        msg = f'升级失败:{e}'
    logger.info(f'系统升级共计耗时:{get_interval(t1)}毫秒')
    return msg

def download_lives(live_url:str):
    t1 = getTime()
    base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # 上级目录
    live_path = os.path.join(base_path, f'base/直播.txt')
    logger.info(f'尝试同步{live_url}远程内容到{live_path}')
    try:
        r = requests.get(live_url,headers=headers,timeout=3)
        auto_encoding = r.apparent_encoding
        if auto_encoding.lower() in ['utf-8','gbk','bg2312','gb18030']:
            r.encoding = auto_encoding
        # print(r.encoding)
        html = r.text
        # print(len(html))
        if re.search('cctv|.m3u8',html,re.M|re.I) and len(html) > 1000:
            logger.info(f'直播源同步成功,耗时{get_interval(t1)}毫秒')
            with open(live_path,mode='w+',encoding='utf-8') as f:
                f.write(html)
            return True
        else:
            logger.info(f'直播源同步失败,远程文件看起来不是直播源。耗时{get_interval(t1)}毫秒')
            return False
    except Exception as e:
        logger.info(f'直播源同步失败,耗时{get_interval(t1)}毫秒\n{e}')
        return False