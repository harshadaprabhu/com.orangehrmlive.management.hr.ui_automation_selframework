import logging
from utils.readConfigFile import ConfigFileOperations as cf

class GetLog():
    @staticmethod
    def getLogger():
        logger = logging.getLogger()
        configFilePath ="C:\\Workspace\\Python_Workspace\\com.orangehrmlive.management.hr.ui_automation_selframework\\config_files\\config.ini"
        filePath = cf.getValueFromConfig(configFilePath,"directory_path","log_filepath")
        fhandler = logging.FileHandler(filename=filePath, mode='a')
        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger

