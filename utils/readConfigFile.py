import configparser

class ReadConfigFile():
    def readFile(self,filepath):
        self.config = configparser.RawConfigParser()
        self.config.read(filenames=filepath)
        return self.config


class ConfigFileOperations():
    @staticmethod
    def getValueFromConfig(filepath, sectionname, keyname):
        file = ReadConfigFile()
        config = file.readFile(filepath=filepath)
        value = config.get(sectionname, keyname)
        return value
