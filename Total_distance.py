'''
If I leave my house at 6:52 am and run 1 mile at an easy pace( 8.15 per mile ), then 3 miles at tempo( 7:12 per mile)
and 1 mile at easy pace again, what is the time do i get home for breakfast?
'''
h, m, s = 6, 52, 0
em, es, erm, ers = 8*2, 15*2, 8*2, 15*2
tm, ts, trm, trs = 7*3, 12*3, 7*3, 12*3

ts = s + es + ers + ts + trs
sec = ts % 60
tm = m + em + erm + tm + trm + ts//60
min = tm % 60
hr = h + tm // 60
print(str(hr)+" : "+str(min)+" : "+str(sec))