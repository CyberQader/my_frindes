my_frindes = ['ahmed','jamal','natalia','iyad','abd','mazen','abood','lana','roua','ashref']
a = 0
while a < len(my_frindes):
    print(f'#{str(a+1).zfill(2)} {my_frindes[a]}')
    a+=1
else:
    print('*'*15)
    print('<<<All My Frindes>>>')
