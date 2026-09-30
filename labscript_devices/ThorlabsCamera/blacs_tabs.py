from blacs.device_base_class import DeviceTab
from qtutils.qt import QtWidgets

class ThorlabsCameraTab(DeviceTab):

    worker_class = 'labscript_devices.ThorlabsCamera.blacs_workers.ThorlabsCameraWorker' 

    def initialise_GUI(self):
        label = QtWidgets.QLabel("Thorlabs camera tab — test display")
        self.get_tab_layout().addWidget(label)

    def initialise_workers(self):

        print('Initialising workers for the camera')
        self.create_worker(
            'main_worker', self.worker_class, {}
        )
        self.primary_worker = "main_worker"