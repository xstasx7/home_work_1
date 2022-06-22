import requests

URL = 'https://gbcdn.mrgcdn.ru/uploads/asset/2729331/attachment/e84f9ad49c706008fba3b58e2a1e5b09.txt'
response = requests.get(URL)
file_1 = open('pars.txt', 'w', encoding='utf-8')
file_1.write(response.text)
file_1.close()

file_2 = open('pars.txt', 'r+', encoding='utf-8')
result = []
for line in file_2:
    c = line.split()
    line_pars = (c[0], c[5][1:], c[6])
    result.append(line_pars)
print(result)
file_2.close()
