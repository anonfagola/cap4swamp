import calendar
import os
import sys #SYS SCUM CHECK YOUR PRIVILEGE
import time
import traceback

try:
	import pyscreenshot
except Exception:
	print "Pyscreenshot not installed. You didn't read the README, retard."
	
	sys.exit()

from datetime import date, datetime

print "Cap4Swamp v1.0"

dir = os.path.dirname(os.path.realpath(__file__)) + "\\" + date.today().isoformat()

if not os.path.exists(dir):
	os.makedirs(dir)

print "Using directory %s" % dir

while True:
	try:
		unixtime = calendar.timegm(datetime.utcnow().utctimetuple())
		print("Saving to %s\\%s.png" % (dir, unixtime))
		pyscreenshot.grab_to_file("%s\\%s.png" % (dir, unixtime))
	except Exception:
		print "Error saving image."
		traceback.print_exc()
	
	print "Screencapped! Next screencap will be in 60 seconds."
	
	time.sleep(60)
