from source.services.apply_adc.LogicalEngineBaseClass import LogicalEngineBaseClass


class LogicalModelImageType(LogicalEngineBaseClass):
    def run(self):
        for self.i_image, self.image_path in enumerate(self.image_names):
            self.set_image_type()
            
