#!/bin/bash
cd /users/opd29/passerelle-edm/scripts/extispyb/Dimplev1_0-00000002sZ7J4K
/opt/pxsoft/bin/dimple  /mntdirect/_sware/exp/pxsoft/EDNA/vMX/edna/tests/data/images/dimple_noanom_aimless.mtz /mntdirect/_sware/exp/pxsoft/EDNA/vMX/edna/tests/data/images/dimple_model.pdb /users/opd29/passerelle-edm/scripts/extispyb/Dimplev1_0-00000002sZ7J4K/dimple > Dimplev1_0-00000002sZ7J4K.log 2> Dimplev1_0-00000002sZ7J4K.err &
ednaJobPid=$!
ednaJobHostName=$(hostname)
echo "$ednaJobHostName $ednaJobPid" > /users/opd29/passerelle-edm/scripts/extispyb/Dimplev1_0-00000002sZ7J4K/dimple_hostNamePid.txt
wait $ednaJobPid
