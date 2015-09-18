import sys
sys.path.append("/opt/pxsoft/EDNA/vMX/edna/kernel/src")

from EDFactoryPluginStatic import EDFactoryPluginStatic

from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile

EDFactoryPluginStatic.loadModule("XSDataCCP4v1_0")
from XSDataCCP4v1_0 import XSDataInputDimple

xsDataInputDimple = XSDataInputDimple()
xsDataInputDimple.mtz = XSDataFile(XSDataString("/mntdirect/_sware/exp/pxsoft/EDNA/vMX/edna/tests/data/images/dimple_noanom_aimless.mtz"))
xsDataInputDimple.pdb = XSDataFile(XSDataString("/mntdirect/_sware/exp/pxsoft/EDNA/vMX/edna/tests/data/images/dimple_model.pdb"))

edPluginExecDimple = EDFactoryPluginStatic.loadPlugin("EDPluginExecDimplev1_0")
edPluginExecDimple.dataInput = xsDataInputDimple
edPluginExecDimple.executeSynchronous()
print(edPluginExecDimple.dataOutput.marshal())


print edPluginExecDimple.dataOutput.refmac5restrLog
