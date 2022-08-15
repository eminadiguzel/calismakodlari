x = 10
y = 100
z = 100


#GİRİLEN RAKAMLAR AYNI MI DİYE KONTROL EDELİM
if x==y==z:
  print("Üç rakamda birbiriyle aynı x==y==z")
elif y==z:
  print("sadece x rakamı farklı (y ve z aynı)")
elif x==z:
  print("sadece y rakamı farklı (x ve z aynı)")
elif y==x:
  print("sadece z rakamı farklı (y ve x aynı)")

  
#EN BÜYÜK RAKAMI BULALIM
  
#Bütün rakamlar birbiriyle benzer mi kontrol edelim
if x==y==z:
  print("bütün rakamlar aynı x==y==z")
  
#x, y'den büyük yada eşitse, y'de z'den büyük yada eşitse
elif x>=y>=z: 
  print("1.sıra çalıştı - x en büyük rakam:",x)

#x, z'den büyük yada eşitse, z'de y'den büyük yada eşitse
elif x>=z>=y:
  print("2.sıra çalıştı - x en büyük rakam:",x)
  
#y, z'den büyük yada eşitse, z'de x'den büyük yada eşitse
elif y>=z>=x:
  print("3.sıra çalıştı - y en büyük rakam:",y)

#y, x'den büyük yada eşitse, z'de x'den büyük yada eşitse
elif y>=x>=z:
  print("4.sıra çalıştı - y en büyük rakam:",y)

#z, x'den büyük yada eşitse, x'de y'den büyük yada eşitse
elif z>=x>=y:
  print("5.sıra çalıştı - z en büyük rakam:",z)
  
#z, x'den büyük yada eşitse, x'de y'den büyük yada eşitse
elif z>=y>=x:
  print("6.sıra çalıştı - z en büyük rakam:",z)



  

#EN KÜÇÜK RAKAMI BULALIM
  
#Bütün rakamlar birbiriyle benzer mi kontrol edelim
if x==y==z:
  print("bütün rakamlar aynı x==y==z")
  
#x, y'den küçük yada eşitse, y'de z'den küçük yada eşitse
elif x<=y<=z: 
  print("1.sıra çalıştı - x en küçük rakam:",x)

#x, z'den küçük yada eşitse, z'de y'den küçük yada eşitse
elif x<=z<=y:
  print("2.sıra çalıştı - x en küçük rakam:",x)
  
#y, z'den küçük yada eşitse, z'de x'den küçük yada eşitse
elif y<=z<=x:
  print("3.sıra çalıştı - y en küçük rakam:",y)

#y, x'den küçük yada eşitse, z'de x'den büyük yada eşitse
elif y<=x<=z:
  print("4.sıra çalıştı - y en küçük rakam:",y)

#z, x'den küçük yada eşitse, x'de y'den küçük yada eşitse
elif z<=x<=y:
  print("5.sıra çalıştı - z en küçük rakam:",z)
  
#z, x'den küçük yada eşitse, x'de y'den küçük yada eşitse
elif z<=y<=x:
  print("6.sıra çalıştı - z en küçük rakam:",z)
