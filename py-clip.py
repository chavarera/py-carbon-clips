# ---------------------------------------------------------#
#   Name    : py-clip.py
#   Author  : Ravishankar Chavare
#   Desc    : This File Accept programing files and make
#             Them into beautiful png images and save it into
#             clips directory with input file name
#   Date    : 04-Jul-2020
# ---------------------------------------------------------#

import os
import glob
from urllib import parse
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options


def get_driver():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(
        executable_path=GeckoDriverManager().install(), options=options)
    return driver


def read_file(file):
    with open(file, 'r') as _f:
        text = _f.read()
    return text


def get_files(path):
    files = glob.glob('{}/*'.format(path))
    for file in files:
        if os.path.isfile:
            yield file


def encode_text(file):
    clip_text = read_file(file)
    uri_encoded_clip_text = parse.quote_plus(clip_text)
    return uri_encoded_clip_text


def take_snapshot(web, file):
    elem = web.find_element_by_xpath("//div[@id='export-container']")
    out_file = os.path.basename(file).split('.')[0]
    if not os.path.isdir(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
    file_path = '{}/{}.png'.format(OUTPUT_DIR, out_file)
    elem.screenshot(file_path)


def main():
    with (get_driver())as web:
        for file in get_files(INPUT_DIR):
            print("{}Processing-{}{}".format('*'*10, file, '*'*10))
            encoded_text = encode_text(file)
            url = "https://carbon.now.sh?code=" + encoded_text
            web.get(url)
            take_snapshot(web, file)


if __name__ == '__main__':
    INPUT_DIR = 'input'
    OUTPUT_DIR = 'clips'
    if os.path.isdir(INPUT_DIR):
        main()
    else:
        os.mkdir(INPUT_DIR)
        msg = '{} is created please put files in {}'
        print(msg.format(INPUT_DIR, os.path.abspath(INPUT_DIR)))
