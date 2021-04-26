# check whether given year is a leap year or not

a = int(input('Enter year : '))

if( ( a % 400 == 0 ) or (( a % 4 == 0 )) and (( a % 100 != 0 )) ) :
    print(a ,' is a leap year '))
else :
    print(a,'is NOT a leap year'))

    
    
