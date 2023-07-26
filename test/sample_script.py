import time
import os
import sys
from appsec import appsec
import pdb;pdb.set_trace()
#ixload_obj = appsec("ixload")
obj = appsec("bps")
bps_system  = '10.39.68.79'
bpsuser     = 'admin'
bpspass     = 'admin'
port_list = ["2/1","2/3"] #[slot/portno]
group = 3


obj.connect(bps_system, bpsuser, bpspass)

obj.load(config_file = "AppSim")
obj.assign_ports(port_list, group)
run_id = obj.run(model = "AppSim", group=group)

stats = obj.get_stats(type="summary", run_id=run_id)
print(run_id)

time.sleep(10)

#progress = obj.get_test_status(run_id)
run_data = obj.port_status(type="runningtest")
slot_data = obj.port_status(type="slot")
data = obj.port_status(type="all")

print(run_data)
print(slot_data)
print(data)
print("~Test is running. Get stats at every 10 seconds.") 
progress = obj.get_test_status(run_id)
while(type(progress) == int and int(progress) <= 100):
    stats = obj.get_stats(type="summary", run_id=run_id)
    print("******************")
    print(stats)
    print("******************")
    progress = obj.get_test_status(run_id)
    time.sleep(10)
obj.stop(run_id)
obj.unassign_ports(port_list)
obj.disconnect()





