import pandas as pd
import streamlit as st
import requests
from bs4 import BeautifulSoup
import extra_streamlit_components as stx
from pricedblib import *

def init_router():
    return stx.Router({"/":home,"/home": home, "/add": new_product, "/delete": delete_productinfo})


def home():
    st.title("제품 최저가 시스템")
    st.write("<hr>", unsafe_allow_html=True)
    use = st.expander("<사용법>")
    use.write("1. '추가하기' 버튼 클릭\n2. 네이버 -> 쇼핑으로 가서 원하는 제품 검색\n3. 그 제품에 들어가서 URL 복사 **(브랜드 카탈로그라고 표시된 제품만 가능)**\n4. 복사한 URL을 제품 추가 화면에 붙여넣기")
    st.write("<hr>", unsafe_allow_html=True)
    products = fetch_products()
    for p in products:
        url = p['url']
        title = p['name']
        response = requests.get(url)
        
        if response.status_code == 200:
            htmlsource = response.content
            soup = BeautifulSoup(htmlsource, 'html.parser')
            
            low_price = soup.find(class_ = "lowestPrice_low_price__Ypmmk").find('em').text
            image = soup.find(class_="image_thumb__IB9B3").find('img').attrs['src']
            # print(low_price)
            p['price'] = low_price
        else:
            print('error')
        st.subheader(title)
        col1, col2 = st.columns(2)
        col1.image(image, width=250)
        col2.write(f"{url}")
        price, link = st.columns(2)
        price.subheader(f"최저가: {p['price']}원")
        st.write("<hr>", unsafe_allow_html=True)
    b1, b2 = st.columns(2)
    add = b1.button("추가", use_container_width=True)
    if add:
        router.route("/add")
    delete = b2.button("삭제", use_container_width=True)
    if delete:
        router.route("/delete")
    

def new_product():
    products = fetch_products()
    st.title("제품 추가")
    url = st.text_input("URL 입력")
    submitted = st.button("추가하기")
    if url != '':
        response = requests.get(url)

        if response.status_code == 200:
            htmlsource = response.content
            soup = BeautifulSoup(htmlsource, 'html.parser')
            
            low_price = soup.find(class_ = "lowestPrice_low_price__Ypmmk").find('em').text
            p_name = soup.find(class_ = "top_summary_title__ViyrM").find('h2').text
            # print(low_price)

        else:
            print('error')
    if submitted:
        if len(products) == 0:
            product = {'id':1, 'name':p_name, 'url': url, 'price':low_price}
            insert_product(product)
        else:
            product = {'id':get_new_id(), 'name':p_name, 'url': url, 'price':low_price}
            insert_product(product)
        router.route("/home")
    if st.button("제품 목록", use_container_width=True):
        router.route("/home")

def delete_productinfo():
    st.title("제품 삭제")
    products = fetch_products()
    df = pd.DataFrame(products, columns=['id', 'name', 'url', 'price'])
    st.dataframe(df, use_container_width=True, hide_index=True)
    df["id_name"] = df["id"].astype(str)+":" + df["name"]
    selected = st.selectbox("제품 선택", df["id_name"])
    product = fetch_product_by_id(int(selected.split(":")[0]))
    with st.form(key='product_form'):
        submitted = st.form_submit_button(label='삭제하기', use_container_width=True)
        if submitted:
            delete_product(product["id"])
            st.success("삭제되었습니다.")
            router.route("/home")
    if st.button("제품 목록", use_container_width=True):
        router.route("/home")


router = init_router()
router.show_route_view()