pages = 100
lines = 50
symbols = 25
byte = 4


Pagesize = lines * symbols * byte
Booksize = Pagesize*pages

Disksize = 1.44 * 1024 * 1024


books = Disksize // Booksize

print("Количество книг, помещающихся на дискету:",round(books))

