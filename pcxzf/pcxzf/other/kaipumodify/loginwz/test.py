import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = "http://www.scpc.gov.cn/content/article/13938326"

# Send an HTTP request to fetch the webpage content
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the element containing the message ID
message_id_element = soup.find("td", class_="nr")

# Extract the message ID
message_id = message_id_element.text.strip()

# Print the extracted message ID
print("Message ID:", message_id)
shuji_el = soup.find("a", title="书记信箱")
xianzhang_el = soup.find("a", title="县长信箱")

# Extract the text
if shuji_el:
    result = shuji_el.text
elif xianzhang_el:
    result = xianzhang_el.text
else:
    result = "Not found"

print(result)