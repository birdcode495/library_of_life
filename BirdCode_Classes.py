

# -------------------------------------------------------------------------------------------------------------------------------


#                                                     LIBRARY OF LIFE

#                                            Construction of BirdCode Classes



# -------------------------------------------------------------------------------------------------------------------------------


import datetime

class Milvus_migrans():

	scientific_name = 'Milvus migrans'
	english_name = 'Black kite'
	chinese_name = '黑鸢'
	kingdom = 'Animalia'
	phylum = 'Chordata'
	classs = 'Aves'
	order = 'Accipitriformes'
	family = 'Accipitridae'
	genus = 'Milvus'
	mean_number_mature_individuals = 4800000
	global_assessment = 'LC'
	lower_elevation_limit = 0
	upper_elevation_limit = 4900
	size_cm = 60
	wingspan_cm = 150
	mean_weight_g = 875
	movement_patterns = 'Full migrant'
	ability_to_fly = True
	breeding_season_start = 1
	breeding_season_finish = 2

	def breeding_timer(self):

		x = datetime.datetime.now()
		
		if self.breeding_season_start < self.breeding_season_finish:

			if x.month < self.breeding_season_start or x.month > self.breeding_season_finish:

				print('Now is not breeding season for this species')

			else:

				print('Now is the breeding season for this species ')


		elif self.breeding_season_start > self.breeding_season_finish:

			if x.month >= self.breeding_season_start:

				print('Now is the breeding season for this species')

			elif x.month <= self.breeding_season_finish:

				print('Now is the breeding season for this species')

			else:

				print('Now is not breeding season for this species')




# -------------------------------- Creation of this first object for this species --------------------------

MilvusMigrans1 = Milvus_migrans()


# -------------------------------- Creation of the initial report for the generated object ------------------


print('--------------------------------------- SPECIES REPORT -----------------------------------------------')

print()
print()
print('The scientific name of this species is: ', MilvusMigrans1.scientific_name)
print('The english name for this species is: ', MilvusMigrans1.english_name)
print('The chinese name for this species is: ', MilvusMigrans1.chinese_name)
print('This species movement patterns are: ', MilvusMigrans1.movement_patterns)
print()
MilvusMigrans1.breeding_timer()

