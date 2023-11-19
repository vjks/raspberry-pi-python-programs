# This will make a HTTP request and save the response to a file. 

import requests

url = "https://www.nytimes.com/2023/11/18/technology/open-ai-sam-altman-what-happened.html"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Open a file in binary write mode
    with open("response_content.txt", "wb") as file:
        # Write the content of the response to the file
        file.write(response.content)
    print("Response content saved to response_content.txt")
else:
    print("Error: Failed to retrieve content. Status code:", response.status_code)