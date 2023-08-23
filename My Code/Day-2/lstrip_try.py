demo3 = '     Bangladesh     '
print('My country is',demo3,'.')

rm_space3 = demo3.lstrip()
print('My country is',rm_space3,'.')

demo4= ',,,,,,,,,,gggggyyytt ...    Bangladeshy.....yyttt'
print('My country is',demo4,'.')

rm_space4= demo4.lstrip(',.gyt ')
print('My country is',rm_space4,'.')
