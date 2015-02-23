"""
Calculation module for setting the normalisation factor to absolute or scaled_absolute using water
	
author: Adam Round
Date: 16/02/2015
"""


class Normalisation_Factor_Calculator:

	# I0_sensitivity = 5
	
	"""
	Constants
	"""
	
	# look up dictionary for theoretical I0 values fo water scattering
	I0_t = {
		4 : 0.01670, 5 : 0.01665, 6 : 0.01661, 7 : 0.01657, 8 : 0.01653, 9 : 0.0165, 10 : 0.01647, 11 : 0.01645, 12 : 0.01642, 13 : 0.0164, \
		14 : 0.01638, 15 : 0.01637, 16 : 0.01635, 17 : 0.01634, 18 : 0.01633, 19 : 0.01633, 20 : 0.01632, 21 : 0.01632, 22 : 0.01632, 23 : 0.01632, \
		24 : 0.01632, 25 : 0.01633, 26 : 0.01634, 27 : 0.01635, 28 : 0.01636, 29 : 0.01637, 30 : 0.01638, 31 : 0.01640, 32 : 0.01641, 33 : 0.01643, \
		34 : 0.01645, 35 : 0.01647, 36 : 0.01650, 37 : 0.01620, 38 : 0.01655, 39 : 0.01658, 40 : 0.01660, 41 : 0.01663, 42 : 0.01666, 43 : 0.01670, \
		44 : 0.01673, 45 : 0.01677, 46 : 0.01680, 47 : 0.01684, 48 : 0.01688, 49 : 0.01692, 50 : 0.01696, 51 : 0.01700, 52 : 0.01704, 53:  0.01709, \
		54 : 0.01713, 55 : 0.01718, 56 : 0.01723, 57 : 0.01728, 58 : 0.01732, 59 : 0.01738, 60 : 0.01743,
	}
	#Scattering contrast per mass (Average Protein - Standard buffer)
	Scat_cont_Prot = 4.83376253809983E+20	
	
	# Scattering contrast per mass could be added for neucleic acids
			
	#Protein Partial specific volume (cm3/g)
	Prot_Partial_specific_volume = 0.735	
			
	#Avogadro constant (mol-1)	
	Avogadro_constant = 6.023E+23	
	
	"""
	Calculation of values for protein: could be updated to include nucleic acids as well
	"""		
						
	def calculate_absolute_normalisation(self):
		#New normalization for absolute scale (cm-1)	
		return (self.I0_t.get(self.T_c)/ self.I0_m) * self.NF	
	
	def calculate_scaled_normalisation(self, NF_abs):
		#New normalization for scale to give I0 as Mw (kD)	(for average protein in standard buffer
		return (NF_abs * self.Avogadro_constant) / self.Scat_cont_Prot
	
	#print "New normalization for absolute scale (cm-1) : %s" % (new_NF_abs)
	#print "New normalization to give I0 as Mw (kD)	(for average protein in standard buffer) : %s" % (new_NF_scale)
	
	
	
	"""
	TEST
	"""
	def Check_NF(self, T_c, NF, I0_m, I0_sensitivity):
		# Temperature : accepted temperatures only achievable by BioSAXSSC (in the range of 4 to 60 degrees C)
		self.T_c = T_c
		#current Normalisation factor
		self.NF = NF
		#measured I0 of water
		self.I0_m = I0_m
		#sensitivity in terms of percent
		self.I0_sensitivity = I0_sensitivity
		
		# expected correctly normalized I0 for Water
		I0_expected = self.I0_t.get(self.T_c)
		I0_scale_expected = self.calculate_scaled_normalisation(I0_expected)
		I0_scale_diff = self.I0_m - I0_scale_expected
		I0_abs_diff = self.I0_m - self.I0_t.get(self.T_c)
		I0_scale_diff_percent = (abs(I0_scale_diff) / I0_scale_expected) * 100
		I0_abs_diff_percent = (abs(I0_abs_diff) / I0_scale_expected) * 100
		
		if I0_scale_diff_percent <= self.I0_sensitivity:
			print "I0 of %s is within %s percent sensitivity of expected scaled value of %s" % (self.I0_m, self.I0_sensitivity, I0_scale_expected)
			print "No action required for I0 as Mw (kD)"
			print
			print "New normalization factor for absolute scale (cm-1) : %s" % (self.calculate_absolute_normalisation())
			SF = {"results" : "No action required for I0 as Mw (kD)", "ScaledNF" : self.NF, "AbsoluteNF" : self.calculate_absolute_normalisation()}
			return  SF
		elif I0_abs_diff_percent <= self.I0_sensitivity:
			print "I0 of %s is within %s percent sensitivity of expected absolute value of %s" % (self.I0_m, self.I0_sensitivity, self.I0_t.get(self.T_c))
			print "No action required for absolute scale (cm-1)"
			print
			print "New normalization factor for for I0 as Mw (kD) : %s" % (self.calculate_scaled_normalisation(self.calculate_absolute_normalisation()))
			SF = {"results" :"No action required for absolute scale (cm-1)", "ScaledNF": self.calculate_scaled_normalisation(self.calculate_absolute_normalisation()), "AbsoluteNF" : self.NF}
			return  SF
		else:
			print "I0 of %s is not within %s percent sensitivity of expected values of %s (abs) or %s (scaled)" % (self.I0_m, self.I0_sensitivity, self.I0_t.get(self.T_c), I0_scale_expected)
			print
			print "New normalization factor for absolute scale (cm-1) : %s" % (self.calculate_absolute_normalisation())
			print "New normalization factor for for I0 as Mw (kD) : %s" % (self.calculate_scaled_normalisation(self.calculate_absolute_normalisation()))
			SF = {"results" : "NF does not match either Absolute or Scaled: Please update", "ScaledNF" : self.calculate_scaled_normalisation(self.calculate_absolute_normalisation()), "AbsoluteNF" : self.calculate_absolute_normalisation()}
			return SF
	
	


	
