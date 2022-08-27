from jproperties import Properties
config = Properties()
with open("C:\\Users\\dell\\PycharmProjects\\testcase\\config.properties","rb") as configFile:
    config.load(configFile)
    print(config.get("browser").data)
