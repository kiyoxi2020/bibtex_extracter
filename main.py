from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def extract_href(input_file, output_file, chrome_driver):
    scholars = open(input_file)
    scholars = scholars.readlines()
    browser = webdriver.Chrome(executable_path=chrome_driver)
    print(By.ID)
    url = "https://scholar.google.com"
    browser.get(url)
    # time.sleep(1)
    links = []
    file_out = open(output_file,'a')
    file_bib_out = open('bib.txt', 'a')
    bibs = []
    # cc = 0
    # st = 64
    failed = []
    for tt in scholars:
        # cc += 1
        # if not (cc <= 64-18+1 and cc>=44-18+1):
        #     continue
        tt = tt.strip().split('\t')
        print(tt[0])
        tt = tt[-1]
        browser.get(url)
        time.sleep(0.5)
        browser.find_element_by_xpath('//*[@name="q"]').send_keys(tt)
        # time.sleep(1)

        try:
            # el.send_keys(Keys.ENTER)
            browser.find_element_by_xpath('//*[@name="btnG"]').click()
            # time.sleep(1)

            browser.find_element_by_xpath('//*[@class="gs_or_cit gs_or_btn gs_nph"]').click()
            time.sleep(1)
            link = browser.find_element_by_xpath('//*[@class="gs_citi"]').get_attribute('href')
            print(link)
            if link not in links:
                links.append(link)
                file_out.write(link+'\n')
            
            browser.get(link)
            text = browser.find_element_by_xpath('/html/body/pre')
            text = text.text + '\n'
            file_bib_out.writelines(text)
            bibs.append(text)
        except:
            print('[*****************************]')
            failed.append(tt)
            continue
        # time.sleep(3)

    print(links)
    print(bibs)
    file_out.close()
    file_bib_out.close()
        

if __name__ == '__main__':
    input_file = 'scholars.txt'
    output_file = 'links.txt'
    extract_href(input_file, output_file, "E:\我的文章\博士论文\crawl\chromedriver.exe")


