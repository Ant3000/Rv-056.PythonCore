# Homework on lesson 1 Vadym Horval
step = 2
lenght = 18
lenght_1 = 18

while lenght > 0: # draving top range
    if lenght == lenght_1:
        print(' '*lenght,'****')
        lenght -= step
    elif lenght == 6:
        print(' '*lenght,'*',' '*7,'*',' '*7,'*',' '*2*step,'*')
        lenght -= step
    else:
        print(' '*lenght,'*',' '*(lenght_1-lenght)*step,'*')
        lenght -= step

while lenght <= lenght_1: # draving bottom range
    if lenght == 0:
        print(' '*lenght,'*',' '*5,'*'*25,' '*step*2,'*')
        lenght += step
    elif lenght == lenght_1:
        print(' '*lenght,'****')
        lenght += step
    else:
        print(' '*lenght,'*',' '*(lenght_1-lenght)*step,'*')
        lenght += step