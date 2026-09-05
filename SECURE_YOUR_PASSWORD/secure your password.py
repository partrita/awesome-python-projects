          'z' : '|',
          }
inp = 'alphabet'
password = ''

for i in inp:
        for key, val in sym.items():
                if i in key:
                        password = password + val
print("Name you entered : ", inp)