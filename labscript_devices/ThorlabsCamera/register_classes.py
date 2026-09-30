from labscript_devices import register_classes

register_classes(
    'ThorlabsCamera',
    BLACS_tab='labscript_devices.ThorlabsCamera.blacs_tabs.ThorlabsCameraTab',
    runviewer_parser=None,
)
