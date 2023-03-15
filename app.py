from flask import Flask,jsonify, redirect, render_template
import openai
from transformers import pipeline
import json
pipe = pipeline('summarization', "dominguesm/positive-reframing-en")

app = Flask(__name__)

openai.api_key = "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"
transformation_type = "['growth']"
text = input("Enter your text:")
final_input = transformation_type + text

@app.route('/getAnswer/<string:input>/<string:decision>',methods = ['GET','POST'])
def reply(input,decision):
    if decision == True:
        if " " in text:
            answer = pipe(input, max_length=1024)
            return jsonify("reply",answer)

        else:
            return jsonify("reply","Hey....How can i help you?")
    else:
        ask = input
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=ask,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )
        reply = response["choices"][0]["text"]

        return jsonify("reply",reply)


    

if __name__ == '__main__':
    app.run(host = "127.0.0.1", port = "3000",debug=True)

# import requests
# from bs4 import BeautifulSoup

# query = "Face+Recognition+System+using+Machine+Learning"
# res = list()
# for i in range(0, 100, 10):
#   headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
#   url = f'https://scholar.google.com/scholar?start={i}&q={query}&hl=en&as_sdt=2007&as_ylo=2000&as_yhi=2023'
#   print(url)
#   # url = f"https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q={query}&btnG="

#   # response = requests.get(url, headers = headers)
#   response = requests.get(url)
#   #print("====================================================================================================================================")
#   soup = BeautifulSoup(response.content, "html.parser")
#   # print(soup.prettify())
#   print("====================================================================================================================================")
#   results = soup.find_all("div", {"class": "gs_r gs_or gs_scl"})
#   for result in results:
#     try:
#         title = result.find("h3", {"class": "gs_rt"}).get_text().strip()
#     except:
#         title = ""
          
#     try:
#         author = result.find("div", {"class": "gs_a"} ).get_text().strip()
              
#     except:
#         author = ""
          
#     try:
#         summary = result.find("div", {"class": "gs_rs"}).get_text().strip()
#     except:
#         summary = ""
          
#     try:
#         publisher = result.find("div", {"class": "gs_pub"}).get_text().strip()
#     except:
#         publisher = ""
              
#     try:
#         link = result.find("a")["href"]
#     except:
#         link = ""
          
#     res.append([title, author, summary, link])

# print("=============================================================================================================================================")
# print(len(res))
# print("=============================================================================================================================================")
# print()
# print()
# print()
# for i in range(len(res)):
#     print(res[i])
#     print("=============================================================================================================================================")

