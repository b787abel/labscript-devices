import labscript_utils.h5_lock
import h5py
from sipyco.pc_rpc import Client
from blacs.tab_base_classes import Worker
from labscript_utils.shared_drive import path_to_local

class ThorlabsCamera(object): 

    def __init__(self): 

        print('Connecting to camera')
        cli = Client('::1', 10337) 
        cli.message_test() 
        cli.close_rpc()
        print('Tried messaging')

    def arm(self, exposure_duration_us): 
        print('Arming camera')
        cli = Client('::1', 10337) 
        cli.arm(exposure_duration_us, 2)
        cli.close_rpc()

class ThorlabsCameraWorker(Worker):  

    def init(self): 
        self.camera = ThorlabsCamera() 

    def arm(self): 
        pass 

    def transition_to_buffered(self, device_name, h5_filepath, initial_values, fresh):
        cli = Client('::1', 10337) 
        cli.log_message('Transitioning to buffered for the camera')
        if getattr(self, 'is_remote', False):
            h5_filepath = path_to_local(h5_filepath)
        self.h5_filepath = h5_filepath
        cli.log_message('h5 path: {}'.format(self.h5_filepath))
        with h5py.File(self.h5_filepath, 'r') as f:
            self.use_camera = f['globals/thorlabs_camera'].attrs['use_camera']
            self.exposure_duration_us = int(f['globals/thorlabs_camera'].attrs['exposure_duration'])
        cli.log_message('Use camera: {}'.format(self.use_camera))
        cli.log_message('Exposure duration: {}'.format(self.exposure_duration_us))
        if self.use_camera:
            cli.arm(self.exposure_duration_us, 2)
        cli.close_rpc()
        return {}

    def transition_to_manual(self):
        cli = Client('::1', 10337)
        cli.log_message('Transitioning to manual for the camera')
        cli.log_message('Use camera: {}'.format(self.use_camera))
        cli.log_message('Exposure duration: {}'.format(self.exposure_duration_us))
        if self.use_camera:
            cli.get_picture(False)
            cli.disarm()
            cli.save_picture(self.h5_filepath)
        cli.close_rpc()
        return True

    def program_manual(self, values):
        return {}


    def abort_transition_to_buffered(self):
        return True