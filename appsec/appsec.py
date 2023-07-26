import os,sys,time
from util import adaptor

class appsec:
    def __init__(self, ext):
        self._ext = ext
        self._adaptor = adaptor()
    
    def connect(self, ip,  user = "admin", password = "admin", version=None):
        try:
            self._adaptor.connection(self._ext, ip, version, user, password)
            #self._adaptor= adaptor(self._ext, ip, version, user, password)
        except Exception as err:
            return err
        return 
    
    def load(self, config_file):
        try:
            # self._adaptor.invoke("load", config_file=config_file)
            self._adaptor.bps_load(config_file)
        except Exception as err:
            return err
        return 
    
    def assign_ports(self, port_list, group=1):
        try:
            # self._adaptor.invoke("load", config_file=config_file)
            self._adaptor.bps_add_ports(port_list, group)
        except Exception as err:
            return err
        return 

    def port_status(self, type="all"):
        try:
            # self._adaptor.invoke("load", config_file=config_file)
            return(self._adaptor.bps_port_status(type))
        except Exception as err:
            return err
        return 

    def run(self, model=None, group=None):
        try:
            # self._adaptor.invoke("load", config_file=config_file)
            return(self._adaptor.bps_run(model, group))
        except Exception as err:
            return err
        return 

    def get_test_status(self, run_id=None):
        try:
            # self._adaptor.invoke("load", config_file=config_file)
            progress = self._adaptor.bps_get_test_status(run_id)
        except Exception as err:
            return err
        return progress
    
    def get_stats(self, type, run_id = None):
        try:
            stats = self._adaptor.bps_get_stats(type, run_id)
        except Exception as err:
            return err
        return stats
    
    def unassign_ports(self, port_list, group=1):
        try:
            
            # self._adaptor.invoke("load", config_file=config_file)
            self._adaptor.bps_unassign_ports(port_list)
        except Exception as err:
            return err
        return 

    def stop(self, run_id):
        try:
            self._adaptor.bps_stop(run_id)
        except Exception as err:
            return err
        return 
    
    def disconnect(self):
        try:
            self._adaptor.bps_disconnect()
        except Exception as err:
            return err
        return 
            

    