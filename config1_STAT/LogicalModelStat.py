from source.services.apply_adc.LogicalEngineBaseClass import LogicalEngineBaseClass


class LogicalModelStat(LogicalEngineBaseClass):
    def run(self):
        for self.i_image, self.image_path in enumerate(self.defect_key):
            zone, recipe = self.get_zone_recipe()

            if recipe == 1 and zone == 1:
                self.set_results('prob')
                continue

            if recipe == 1 and zone == 2:
                self.set_results('cis')
                continue

            elif recipe == 1 and zone == 3:
                self.set_results('non_cis')
                continue

            elif recipe == 1 and zone == 4:
                self.set_results('pads_sur')
                continue

            elif recipe == 1 and zone == 5:
                self.set_results('zone1')
                continue
            elif recipe == 1 and zone == 6:
                self.set_results('chipping')
                continue

            elif recipe == 1 and zone == 7:
                self.set_results('chipping')
                continue

            elif recipe == 1 and zone == 8:
                self.set_results('cis_edge')
                continue
 
            elif recipe == 1 and zone == 9:
                self.set_results('corner')
                continue
 
            elif recipe == 1 and zone == 10:
                self.set_results('street_FM')
                continue
 
            elif recipe == 1 and zone == 63:
                self.set_results('near_pads')
                continue

            elif recipe == 2 and zone == 1:
                self.set_results('cis')
                continue

            elif recipe == 2 and zone == 2:
                self.set_results('cis_edge')
                continue

            elif recipe == 3 and zone == 1:
                self.set_results('cis')
                continue

            elif recipe == 3 and zone == 2:
                self.set_results('cis_edge')
                continue
            else:
                self.set_results('others')
                continue

