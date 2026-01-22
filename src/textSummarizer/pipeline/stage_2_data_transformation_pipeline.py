from src.textSummarizer.logging import logger
from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_transformation import DataTransformation


class DataTransformationPipeline:
    def __init__(self):
        pass

    def init_data_transformation(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transormation = DataTransformation(config=data_transformation_config)
        data_transormation.convert()
