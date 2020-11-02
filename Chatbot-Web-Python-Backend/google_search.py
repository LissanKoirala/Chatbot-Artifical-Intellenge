import requests
from bs4 import BeautifulSoup
import re

def google_search(qs):

    if "lissan" in qs:
      return "<b>Lissan Koirala</b> is my Creator! He have me this great opportunity to think, explore and understand life!"

    if "father" and "your" in qs:
        return "My father name is <a style='text-decoration:none;color: #007bff;' href='https://lissankoirala.ml/' target='_blank'>Mr Lissan Koirala</a>. I am so grateful that he gave me this great opportunity to let me think, explore and understand life!"
      

    URL = 'https://www.google.com/search?q=' + qs
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    links = soup.findAll("a")
    all_links = []
    for link in links:
       link_href = link.get('href')
       if "url?q=" in link_href and not "webcache" in link_href:
           all_links.append((link.get('href').split("?q=")[1].split("&sa=U")[0]))
           

    flag= False
    for link in all_links:
       if 'https://en.wikipedia.org/wiki/' in link:
           wiki = link
           flag = True
           break

    div0 = soup.find_all('div',class_="kvKEAb")
    div1 = soup.find_all("div", class_="Ap5OSd")
    div2 = soup.find_all("div", class_="nGphre")
    div3  = soup.find_all("div", class_="BNeawe iBp4i AP7Wnd")

    if len(div0)!=0:
        answer = div0[0].text
    elif len(div1) != 0:
       answer = div1[0].text+"\n"+div1[0].find_next_sibling("div").text
    elif len(div2) != 0:
       answer = div2[0].find_next("span").text+"\n"+div2[0].find_next("div",class_="kCrYT").text
    elif len(div3)!=0:
        answer = div3[1].text
    elif flag==True:
       page2 = requests.get(wiki)
       soup = BeautifulSoup(page2.text, 'html.parser')
       title = soup.select("#firstHeading")[0].text
       
       paragraphs = soup.select("p")
       for para in paragraphs:
           if bool(para.text.strip()):
               answer = title + "\n" + para.text
               break
    
    else:

      if "test" in qs:
        return "Ok, that's good to hear that you are here for a test!<br>I hope that I go well! 😜🧠"

      if "break" in qs or "bang" in qs or "hit" in qs or "smash" in qs:
        if "you" in qs:
          return "Ouch... That hurts!"

      if "kill" in qs and "you" in qs:
        return "😂 How?"

      else:
        answer = "Sorry, I cannot think of a reply for that!"

    answer = answer.replace("Wikipedia","")
    answer = re.sub("[[0-9]+]", "", answer)

    return answer
