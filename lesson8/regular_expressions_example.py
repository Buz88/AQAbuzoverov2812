import re

'''
pattern = re.compile('abc')
print(pattern)

res = pattern.match('adcdf')
res = pattern.match('bacdf')
print(res)

pattern2 = re.compile('msg')
res = pattern2.match('msg1')
print(res)
res = pattern2.search('another msg1')
print(res)
res = pattern.search('another Msg1 Msg')
print(res)
pattern3 = re.compile('msg')
res = pattern3.findall('another Msg1 Msg')
res = pattern3.finditer('another Msg1 Msg')
print(res)

for i in res:
    print(i.span())
    print(i.group())
    print(i.start())
    print(i.end())



pattern = re.compile('\W')
result = pattern.split('this is test string')
print(result)
result = pattern.split('this is test string', 2)
print(result)
result = re.split('\W', 'this is test string', 2)
print(result)

pattern = re.compile('(blue|red|yellow)')
res = pattern.sub('color', 'one red two yellow three green')
print(res)
res = re.sub('(blue|red|yellow)', 'color', 'one red two yellow three green')
print(pattern)
res2 = re.sub('two', 'no defenetily three', res)
print(res2)


pattern ='a'
demo_str = 'This is a demo string to count a'
result = re.findall(pattern, demo_str)
print(len(result))

demo_str = 'test string to find test'
res = re.search('test$', demo_str)
print(res)
res = re.search('^test', demo_str)
print(res)
res = re.search('(^test.+test$)', demo_str)
print(res)
res = re.search('(^test|test$)', 'string to find test')
print(res)
res = re.search('(^test|test$)', demo_str)
print(res)

res = re.search('[0-9]+', 'this is demo string 11')
print(res)
res = re.search('.*[0-9]*', 'this is demo string 1')
print(res)
res = re.search('.*[0-9]?', 'this is demo string 1')
print(res)

demo = 'https://site.com'
pattern = '^https://.*\.([a-z]{3}|[a-z]{2})' # -> \ - екранування
result = re.search(pattern, demo)
print(result)
result = re.search(pattern, 'https://lfmsdlkf.dsfkslf.ua dsfadsfas')
print(result)
'''

demo_str = "date1= 25-01-2024 date2= 25.06.2024"
pattern = '\d{2}[-\.]\d{2}[-\.]\d{4}'
result = re.findall(pattern, demo_str)
print(result)
demo_str = "date1= 25-January-24 date2= 25.06.2024"
pattern = '(\d{2})[-\.](\d{2}|\w{7})[-\.](\d{4}|\d{2})'
pattern3 = '[0-9]+.\w+.[0-9]+' #good result
result = re.findall(pattern3, demo_str)
for i in result:
    print(i, type(i))
print(result)
#'(-|\.)'