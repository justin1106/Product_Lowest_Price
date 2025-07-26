# 제품 최저가 시스템

브랜드 카탈로그 제품의 네이버 쇼핑 최저가를 자동으로 수집하고 표시하는 Streamlit 기반 웹 애플리케이션입니다. 사용자는 제품 URL만 추가하면, 시스템이 이미지와 함께 실시간 최저가 정보를 표시합니다.

## 주요 기능

* 브랜드 카탈로그 제품 URL로 제품 등록
* 실시간 최저가 및 대표 이미지 출력
* 등록된 제품 목록에서 선택 후 삭제 기능 제공
* Streamlit 라우팅을 이용한 간단한 화면 전환

## 실행 환경

* Python 3.10 이상
* Streamlit
* requests + BeautifulSoup (웹 크롤링)
* pricedblib (데이터 저장/조회 로직 포함한 별도 모듈)

## 필수 패키지 설치

```bash
pip install streamlit requests beautifulsoup4 pandas extra-streamlit-components
```

## 디렉토리 구조 예시

```
lowest_price_tracker/
├── app.py                      # 메인 실행 파일
├── pricedblib.py              # 제품 정보 insert, fetch, delete 등의 DB 처리 모듈
├── data.json                  # (예시) 제품 정보 저장 파일
└── README.md
```

## 사용법

```bash
streamlit run app.py
```

1. 메인 화면에서 현재 등록된 제품들의 이미지, 링크, 최저가를 확인할 수 있습니다.
2. '추가' 버튼을 누르면 제품 URL을 입력할 수 있는 화면으로 이동합니다.

   * 네이버 쇼핑에서 브랜드 카탈로그가 붙은 제품의 상세페이지 URL만 가능
3. '삭제' 버튼을 누르면 등록된 제품 목록을 보고 선택적으로 삭제할 수 있습니다.

## 사용 예시

* URL 입력 예시: `https://smartstore.naver.com/...` (브랜드 카탈로그가 있는 상품)
* 이미지 및 최저가 정보는 네이버 쇼핑 HTML 구조를 기준으로 크롤링합니다.

## 주의 사항

* BeautifulSoup 파싱은 네이버 쇼핑 구조에 따라 동작하므로, 페이지 구조 변경 시 코드 수정 필요
* 브랜드 카탈로그가 없는 일반 상품은 파싱이 실패하거나 정보가 정확하지 않을 수 있음

## 링크
https://lowest-price.streamlit.app/

## 라이선스

MIT License


