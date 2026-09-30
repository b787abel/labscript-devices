from labscript import TriggerableDevice
import h5py
import numpy as np

class ThorlabsCamera(TriggerableDevice):

    def __init__(self, name, parent_device, connection):
        self.BLACS_connection = 'asf'
        TriggerableDevice.__init__(self, name, parent_device, connection)

    def expose(self, t, trigger_duration): 
        self.trigger(t, trigger_duration)

    def generate_code(self, hdf5_file):
        self.do_checks()
        group = self.init_device_group(hdf5_file)
        # vlenstr = h5py.special_dtype(vlen=str)
        # table_dtypes = [
        #     ('t', float),
        #     ('name', vlenstr),
        #     ('frametype', vlenstr),
        #     ('trigger_duration', float),
        # ]
        # data = np.array(self.exposures, dtype=table_dtypes)
        # group = self.init_device_group(hdf5_file)
        # if self.exposures:
        #     group.create_dataset('EXPOSURES', data=data)

    