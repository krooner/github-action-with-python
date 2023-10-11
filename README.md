# github-action-with-python

## Contents

### 서울특별시 청년안심주택 모집공고 정보 가져오기

- 목표: [서울특별시 > 청년안심주택 > 모집공고](https://soco.seoul.go.kr/youth/bbs/BMSR00015/list.do?menuNo=400008) 페이지 하단 테이블에 있는 정보를 Repository의 Issue에 주기적으로 업로드한다.
    - 추가 구현 기능 (예정)
        1. 현재 날짜 기준 청약 시작일이 지났는지 여부를 판단해서 현재 청약 가능 공고만 필터링하여 보여준다.
        2. 이전 Issue에서 업로드한 공고와 비교하여 최신 공고만 보여준다.
     
## Instruction

### 1. Prepare files
실행 파일
- `main.py`: 웹 페이지에 대한 크롤링으로 필요한 데이터를 추출 및 전처리하고, 현재 Repository의 Issue에 데이터를 업로드하는 Python Script
- `github_utils.py`: PyGithub 라이브러리를 활용하여 현재 Repository에 대한 작업을 수행하도록 돕는 기능들을 함수화함

워크플로우 설정 파일
- `.github/workflows/`: 워크플로우 설정 파일 폴더 (여러 개의 워크플로우 설정 가능)
    - action.yaml`: 청년안심주택 모집공고 정보 크롤링 작업에 대한 설정 파일
- `requirements.txt`: 추가적으로 설치해야할 PIP 패키지 목록 (`.yaml` 파일에서 목록에 해당하는 패키지를 설치하도록 할 수 있음) 

### 2. Set GitHub Action
1. Repository 첫 화면 상단에 있는 Actions 클릭
2. Workflow 선택 검색 창에 Simple workflow 검색 후 Configure
3. 필요한 작업을 수행하는 `.yaml` 파일을 작성 및 Commit

## Consideration
1. 가져오려는 정보가 동적 웹페이지로 구성되어 있는 경우 Beautiful4soup로는 크롤링이 안 된다.
    - [Selenium 라이브러리 활용하기](https://selenium-python.readthedocs.io/getting-started.html)
    - [WebElement 객체에서 정보 추출하기](https://selenium-python.readthedocs.io/api.html?highlight=webelement#module-selenium.webdriver.remote.webelement)
2. Github Issue를 날리려면 Token이 필요한데, 민감한 정보이기 때문에 안 보이도록 해야 된다.
    - [Token 발급하기](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)
    - [Secrets에 Token 변수 등록하기](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository)


## Reference

1. [zzsza/github-action-with-python](https://github.com/zzsza/github-action-with-python)
2. [MarketingPipeline/Python-Selenium-Action](https://github.com/MarketingPipeline/Python-Selenium-Action)
