from bs4 import BeautifulSoup
import requests
import streamlit as st

st.markdown("<h1 style='text-align: center;'>LeapCode</h1>", unsafe_allow_html=True)

# url_leet=st.text_input("Enter the URL of the problem")
url_leet=st.text_input("Enter the URL of the problem: ")
if url_leet:
    response = requests.get(url_leet)
    soup = BeautifulSoup(response.content, 'html.parser')
    code_element = soup.find('span', class_='mr-2 text-lg font-medium text-label-1 dark:text-dark-label-1')
    code = code_element.text.strip()
    # find and separate the number and remove '.' from the string
    a=[]
    for i in range(len(code)):
        if code[i].isalpha():
            break
        else:
            
            a.append(code[i])
            continue
    number = ''.join(a)
    number = number.replace('.','')
    #remove all spaces
    number = number.replace(' ','')
    #turn number into a 4 digit string using 0 before the number
    number = number.zfill(4)
    print(number)
    # # Make a GET request to the webpage
    url = 'https://walkccc.me/LeetCode/problems/{}/'.format(number)
    
    response = requests.get(url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the code element and get its text content
    code_element = soup.find('code')
    code = code_element.text.strip()
    st.code(code)
    print(code)