import time
import os
import sys
from appsec import appsec

bps_system  = '10.39.68.79'   # BPS IP
bpsuser     = 'admin'          #Username 
bpspass     = 'admin'          #Password

#API calls to delete all the reports of the specified user.
obj = appsec("bps")
obj.connect(bps_system, bpsuser, bpspass)
import pdb;pdb.set_trace()
#type parameter can be 'name'/'endTime'/'duration'/'result'/'startTime'/'iteration'/'network'/'dut'/'user'/'size'
#limit: how many results has to be deleted, example limit=10 , 
#10 results from each test state("passed", "failed", "error", "canceled", "incomplete") will be deleted 
#by default 100 results will be deleted.
obj.delete_report(type = "admin", limit=4) 
obj.disconnect()





