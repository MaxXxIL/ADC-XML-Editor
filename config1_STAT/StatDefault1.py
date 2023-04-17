from source.services.apply_adc.PostProcessBaseClass import PostProcessBaseClass
import numpy as np


class StatDefault1(PostProcessBaseClass):
    def run(self):
        for self.i_image, self.image_path in enumerate(self.defect_key):
            # Near pad
            if self.eng_passed('Near_pad'):
                continue
            # chipping_touching

            # corner
            if self.eng_passed('corner'):
                continue
            # pads
            if self.eng_passed('pads'):
                continue
            # Non_cis
            if self.eng_passed('Non_CIS'):
                continue
            # cis
            if self.eng_passed('CIS'):
                continue
            # chippinh
            if self.eng_passed('chipping'):
                continue