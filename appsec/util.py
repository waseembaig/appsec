import os,sys,time
from bps.bps_restpy.bps import BPS,pp
#from bps.bps_restpy.bps_restpy_admin.bpsRest import BPS

class adaptor:
    _BPS = {
        "load": "uploadBPT",
    }

    def __init__(self):
        self._ext = None
        pass

        #self._ext = ext
        #  self.connection(ip, version, user, password)

    def connection(self, ext , ip, version, user, password):
        self._ext = ext
        if self._ext == "bps":
            bps = BPS(ip, user, password)
            bps.login()
            self._obj = bps
        elif self._ext == "ixload":
            pass
    

    def invoke(self, method, **args):
        method = self._ext+"_"+method
        method = self.get_method(method)
        func = getattr(self, method)
        responce = func(args)
        print (responce)
    
    def bps_load(self, args):
        #importAsTestName = args.split(".")[0]
        #bpt_filename_to_import = args
        #pp(self._obj.testmodel.importModel(importAsTestName, bpt_filename_to_import, True))
        return(self._obj.testmodel.load(template=args))


    def bps_add_ports(self, port_list, group):
        for port in port_list:
            slot_number = port.split("/")[0]
            port_number = port.split("/")[-1]
            #self._obj.testmodel.save()
            self._obj.topology.reserve([{'slot': int(slot_number), 'port': int(port_number), 'group': group}])
    
    def bps_port_status(self, type):
        data = self._obj.topology.portstate()
        return (self.parse_data(type, data))
    
    def parse_data(self, type, data):
        if type == "runningtest":
            return data['runningTest']
        elif type == "slot":
            return data['slot']
        else:
            return data
    
    def bps_run(self, model, group):
        #self._obj.testmodel.saveAs(name=model, force=True)
        #self._obj.testmodel.save()
        test_id_json = self._obj.testmodel.run(modelname=model, group=group)
        return test_id_json["runid"]

    def bps_get_test_status(self, run_id):
        if run_id != None:
            return(int(self._obj.topology.runningTest['TEST-%s'%run_id].progress.get()))
        else:
            self._obj.topology.runningTest()
            raise Exception("Please input run_id for test status")
    
    def bps_get_stats(self, type, run_id):
        if run_id != None:
            return(self._obj.testmodel.realTimeStats(int(run_id), type, -1))
        else:
            raise Exception("Please input run_id for test stats")
    
    def bps_unassign_ports(self,port_list):
        for port in port_list:
            slot_number = port.split("/")[0]
            port_number = port.split("/")[-1]
            self._obj.topology.unreserve([{'slot': slot_number, 'port': port_number}])
    
    def bps_disconnect(self):
        return(self._obj.testmodel.logout())

    def bps_delete_report(self, type , limit):
        status = ["passed", "failed", "error", "canceled"]
        for state in status:
            data = self._obj.reports.search(searchString=state, limit=limit, sort=type, sortorder="ascending")
            if data:
                for item in data:
                    self._obj.reports.delete(runid = item['runid'])
        

    def get_method(self, name):
        if self._ext == "bps":
            for key in self._BPS.keys():
                if key == name:
                    return self._BPS[key]
    


    def bps_stop(self, run_id):
        #self._obj.testmodel.saveAs(name=model, force=True)
        #self._obj.testmodel.save()
        self._obj.topology.stopRun(run_id)
        return