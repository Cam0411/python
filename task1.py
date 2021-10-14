import datetime
day = datetime.datetime.now()
name = (input("ten"))
sang = int(input("calo sang"))
trua = int(input("calo trua"))
chieu = int(input("calo toi"))
trongngay = int(input("so van dong"))
sum = sang + trua + chieu - trongngay 
a = ("{} {} co luong calo trong ngay la {} ")
print(a.format(day,name,round(sum)))
