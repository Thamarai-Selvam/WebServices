import requests

#uncomment and run app.py

baseURL = "http://localhost:3000/"
# ------------------------------------------------------------------------------
#log1

# print(requests.get(baseURL+'log1?opChoice=0&num3=2&base=2&num=&data=&pow=').content)
# print(requests.get(baseURL+'log1?opChoice=0&num3=21&base=2&num=&data=&pow=').content)
# print(requests.get(baseURL+'log1?opChoice=0&num3=5&base=7&num=&data=&pow=').content)
# print(requests.get(baseURL+'log1?opChoice=0&num3=7&base=9&num=&data=&pow=').content)
# print(requests.get(baseURL+'log1?opChoice=1&num3=&base=&num=22&data=&pow=').content)
# print(requests.get(baseURL+'log1?opChoice=1&num3=&base=&num=14&data=&pow=').content)
# print(requests.get(baseURL+'log1?opChoice=1&num3=&base=&num=0&data=&pow=').content)
# print(requests.get(baseURL+'log1?opChoice=1&num3=&base=&num=76&data=&pow=').content)
# print(requests.get(baseURL+'log1?opChoice=2&num3=2&base=2&num=&data=2&pow=9').content)
# print(requests.get(baseURL+'log1?opChoice=2&num3=2&base=2&num=&data=3&pow=6').content)
# print(requests.get(baseURL+'log1?opChoice=2&num3=2&base=2&num=&data=5&pow=5').content)
# print(requests.get(baseURL+'log1?opChoice=2&num3=2&base=2&num=&data=41&pow=3').content)

# ------------------------------------------------------------------------------

#log2

# print(requests.get(baseURL+'log2?opChoice=0&data=1,2,3,4,5,6&num=&num3=&pow=').content)
# print(requests.get(baseURL+'log2?opChoice=0&data=2,4,6,8,10,17,34,56&num=&num3=&pow=').content)
# print(requests.get(baseURL+'log2?opChoice=0&data=6,12,18,24,36,42,54,60&num=&num3=&pow=').content)
# print(requests.get(baseURL+'log2?opChoice=0&data=11,22,33,44,55,66,77,88,99&num=&num3=&pow=').content)
# print(requests.get(baseURL+'log2?opChoice=1&data=&num=4&num3=&pow=').content)
# print(requests.get(baseURL+'log2?opChoice=1&data=&num=76&num3=&pow=').content)
# print(requests.get(baseURL+'log2?opChoice=1&data=&num=34&num3=&pow=').content)
# print(requests.get(baseURL+'log2?opChoice=1&data=&num=196&num3=&pow=').content)
# print(requests.get(baseURL+'log2?opChoice=2&data=&num=&num3=43&pow=27').content)
# print(requests.get(baseURL+'log2?opChoice=2&data=&num=&num3=24&pow=20').content)
# print(requests.get(baseURL+'log2?opChoice=2&data=&num=&num3=88&pow=44').content)
# print(requests.get(baseURL+'log2?opChoice=2&data=&num=&num3=43&pow=3').content)

# http://localhost:3000/log3?opChoice=2&data=1&degType=0


# ------------------------------------------------------------------------------

#log3

# print(requests.get(baseURL+'log3?opChoice=1&data=1&degType=0').content)
# print(requests.get(baseURL+'log3?opChoice=2&data=12&degType=1').content)
# print(requests.get(baseURL+'log3?opChoice=3&data=30&degType=0').content)
# print(requests.get(baseURL+'log3?opChoice=4&data=45&degType=1').content)
# print(requests.get(baseURL+'log3?opChoice=5&data=15&degType=0').content)
# print(requests.get(baseURL+'log3?opChoice=6&data=90&degType=1').content)
# print(requests.get(baseURL+'log3?opChoice=7&data=15&degType=0').content)
# print(requests.get(baseURL+'log3?opChoice=8&data=30&degType=1').content)
# print(requests.get(baseURL+'log3?opChoice=9&data=65&degType=0').content)
# print(requests.get(baseURL+'log3?opChoice=10&data=70&degType=1').content)
# print(requests.get(baseURL+'log3?opChoice=11&data=90&degType=0').content)
# print(requests.get(baseURL+'log3?opChoice=9&data=0&degType=1').content)

#stat calculator

print(requests.get(baseURL+'statcalc?opChoice=0&data=1,2,3,4,5,6&data1=&data2=').content)
print(requests.get(baseURL+'statcalc?opChoice=0&data=2,5,7,1,4,5,6,7,2,3,4,5,12,4,6&data1=&data2=').content)
print(requests.get(baseURL+'statcalc?opChoice=1&data=1,2,3,4,5,6&data1=&data2=').content)
print(requests.get(baseURL+'statcalc?opChoice=1&data=2,5,7,1,4,5,6,7,2,3,4,5,12,4,56&data1=&data2=').content)
print(requests.get(baseURL+'statcalc?opChoice=2&data=&data1=1,2,3,4,5,6&data2=2,3,4,5,7,8,11').content)
print(requests.get(baseURL+'statcalc?opChoice=2&data=&data1=54,18,57,10&data2=1,3,14,5,57,84,10').content)
