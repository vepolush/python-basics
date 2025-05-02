import requests


# url =  'https://www.ukr.net'
#
# response = requests.get(url)
# # print(response.content)
# print(response.text)
# with open('ukr.html', mode='w', encoding='utf-8') as file:
#     file.write(response.text)


# url = 'https://cdn.pixabay.com/photo/2014/12/04/14/46/magnolia-trees-556718_1280.jpg'
# response = requests.get(url)
# content = response.content
# with open('spring.jpeg', mode='bw') as file:
#     file.write(content)


# url2 = 'https://github.com/progit/progit2/releases/download/2.1.447/progit.pdf'
# response2 = requests.get(url2)
# content2 = response2.content
# with open('git.pdf', mode='bw') as file:
#     file.write(content2)


# with open('spring.jpeg', mode='br') as file, open('spring2.jpeg', mode='bw') as file2:
#     content = file.read()
#     file2.write(content + b'hello there')

with open('spring2.jpeg', mode='br') as file2:
    content = file2.read()
    print(content)