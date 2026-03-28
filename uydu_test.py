from sgp4.api import Satrec, jday

tle1 = "1 25544U 98067A   19343.69339541  .00001764  00000-0  38792-4 0  9991"
tle2 = "2 25544  51.6439 211.2001 0007417  17.6667  85.6398 15.50103472202482"

uydu = Satrec.twoline2rv(tle1, tle2)
jd, fr = jday(2026, 3, 28, 12, 0, 0)

hata, konum, hiz = uydu.sgp4(jd, fr)

print("Hata:", hata)
print("Konum:", konum)
print("Hız:", hiz)