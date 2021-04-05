import pygeoip

loc = pygeoip.GeoIP("GeoLiteCity.dat")
res = loc.record_by_addr('The IP address')
for key, val in res.items():
    print('%s : %s' % (key,val))
