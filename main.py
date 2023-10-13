import os
from datetime import datetime
from pytz import timezone

from github_utils import get_github_repo, upload_github_issue

from selenium import webdriver 
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

"""
    Needed for using selenium in Virtual Machine
"""
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))
display.start()

chromedriver_autoinstaller.install()

chrome_options = webdriver.ChromeOptions()
options = [
    "window-size=1200,1200",
    "ignore-certificate-errors" # for connection to https URL
]

for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(options=chrome_options)

if __name__ == "__main__":
    access_token = os.environ["MY_GITHUB_TOKEN"]
    repo_name = "github-action-with-python"

    seoul_timezone = timezone('Asia/Seoul')
    today = datetime.now(seoul_timezone)
    today_date = today.strftime("%Y년 %m월 %d일")

    target_url = "https://soco.seoul.go.kr/youth/bbs/BMSR00015/list.do?menuNo=400008"

    driver.get(target_url)

    elem = driver.find_element(By.CLASS_NAME, "boardTable")
    
    target_string = elem.text
    text_list = target_string.split("\n")
    column_list = text_list[0].split()

    # Table Markdown format
    markdown_table = ""
    column_text = "|" + "|".join(column_list) + "|\n"
    middle_text = "---".join(["|" for _ in range(column_text.count("|"))]) + "\n"
    markdown_table += column_text + middle_text

    link_address_list = [item.get_attribute("href") for item in elem.find_elements(By.TAG_NAME, 'a')]

    contents_list = []
    
    for index in range(1, len(text_list), 3):
        link_address = link_address_list[index//3]
        content = text_list[index].split() + [f"[{text_list[index+1]}]({link_address})"]
        
        post_date, apply_date, *management = text_list[index+2].split()

        if post_date != today.strftime("%Y-%m-%d"): continue

        management = " ".join(management)

        content += [post_date, apply_date, management]

        insert_text = "|" + "|".join(content) + "|\n"

        contents_list.append(insert_text)

    
    if len(contents_list) == 0:
        print("No Updated Post.")
        exit()

    markdown_table = markdown_table + "\n" + "".join(contents_list)
    upload_contents = markdown_table

    issue_title = f"청년안심주택 최신 공고 알림 ({today_date})"
    repo = get_github_repo(access_token, repo_name)
    upload_github_issue(repo, issue_title, upload_contents)
    print("Upload Github Issue Success!")
    
