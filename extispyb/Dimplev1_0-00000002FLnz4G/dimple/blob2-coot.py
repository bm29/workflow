# coot script generated by dimple
#set_nomenclature_errors_on_read("ignore")
molecule = read_pdb('/users/opd29/passerelle-edm/scripts/extispyb/Dimplev1_0-00000002FLnz4G/dimple/final.pdb')
set_rotation_centre(-8.18, -25.96, 10.45)
set_zoom(30.)
set_view_quaternion(0.17608, 0.048163, 0, 0.983197)
mtz = '/users/opd29/passerelle-edm/scripts/extispyb/Dimplev1_0-00000002FLnz4G/dimple/final.mtz'
map21 = make_and_draw_map(mtz, "2FOFCWT", "PH2FOFCWT", "", 0, 0)
map11 = make_and_draw_map(mtz, "FOFCWT", "PHFOFCWT", "", 0, 1)