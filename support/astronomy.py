from crontab import CronTab
import urllib3, codecs, json, sqlite3, datetime
proxy = urllib3.ProxyManager('http://proxy.server:3128', maxsize=10)
reader = codecs.getreader('utf-8')
#http = urllib3.PoolManager()
r = proxy.request('GET',
                 'http://api.wunderground.com/api/<api key>/astronomy/1/q/pws:IONTARIO1075.json',
                 preload_content=False)
data = json.load(reader(r))
r.release_conn()
srhour = data['sun_phase']['sunrise']['hour']
srmin = data['sun_phase']['sunrise']['minute']
sshour = data['sun_phase']['sunset']['hour']
ssmin = data['sun_phase']['sunset']['minute']

my_cron = CronTab(user='your user id')
#my_cron = CronTab()
for job in my_cron:
    if job.comment == 'sunrise':
        job.minute.on(srmin)
        job.hour.on(srhour)
        my_cron.write()
#  #     print(job)
    if job.comment == 'sunset':
        job.minute.on(ssmin)
        job.hour.on(sshour)
        my_cron.write()
#  #  print(job)

sunrise = srhour + ":" + srmin
sunset = sshour + ":" + ssmin

currtime = str(datetime.datetime.now())

conn = sqlite3.connect('/path/to/suntimes.sdb')

conn.execute("INSERT into suntimes(today,sunrise,sunset) VALUES (?,?,?)", [currtime, sunrise, sunset])

conn.commit()

conn.close()