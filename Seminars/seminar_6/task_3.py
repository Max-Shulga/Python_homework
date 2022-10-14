# дан список, вывести отдельно буквы и цифры
a = ( "a", 'b', '2', '3' ,'c')
b = ( 'a' , 'b' , 'c')
c = ( '1', '2', '3')
 

b= filter(str.isalpha, a)
c= filter(str.isdigit, a)

print(*b)
print(*c)
