import data

class Core:
	def __init__(self, number, version, active = False):
		self.number = number
		self.version = version
		self.active = active
	
data.cores = []

if (data.mode == 0 or data.mode == 1):
	data.cores += [
		Core("F1-01", "Falcon 1"),
		Core("F1-02", "Falcon 1"),
		Core("F1-03", "Falcon 1"),
		Core("F1-04", "Falcon 1"),
		Core("F1-05", "Falcon 1"),
		
		Core("B0001", "Falcon 9 v1.0"),
		Core("B0002", "Falcon 9 v1.0"),
		Core("B0003", "Falcon 9 v1.0"),
		Core("B0004", "Falcon 9 v1.0"),
		Core("B0005", "Falcon 9 v1.0"),
		Core("B0006", "Falcon 9 v1.0"),
		Core("B0007", "Falcon 9 v1.0"),
		
		Core("B1001", "Falcon 9 v1.1"),
		Core("B1002", "Falcon 9 v1.1"),
		Core("B1003", "Falcon 9 v1.1"),
		Core("B1004", "Falcon 9 v1.1"),
		Core("B1005", "Falcon 9 v1.1"),
		Core("B1006", "Falcon 9 v1.1"),
		Core("B1007", "Falcon 9 v1.1"),
		Core("B1008", "Falcon 9 v1.1"),
		Core("B1009", "Falcon 9 v1.1"),
		Core("B1010", "Falcon 9 v1.1"),
		Core("B1011", "Falcon 9 v1.1"),
		Core("B1012", "Falcon 9 v1.1"),
		Core("B1013", "Falcon 9 v1.1"),
		Core("B1014", "Falcon 9 v1.1"),
		Core("B1015", "Falcon 9 v1.1"),
		Core("B1016", "Falcon 9 v1.1"),
		Core("B1017", "Falcon 9 v1.1"),
		Core("B1018", "Falcon 9 v1.1"),
	]
	
if (data.mode == 0 or data.mode == 2):
	data.cores += [
		Core("B1019", "F9 FT Block 1"),
		Core("B1020", "F9 FT Block 1"),

		Core("B1021", "F9 FT Block 2"),
		Core("B1022", "F9 FT Block 2"),
		Core("B1023", "F9 FT Block 2"),
		Core("B1024", "F9 FT Block 2"),
		Core("B1025", "F9 FT Block 2"),
		Core("B1026", "F9 FT Block 2"),
		Core("B1027", "F9 FT Block 2"),

		Core("B1028", "F9 FT Block 3"),
		Core("B1029", "F9 FT Block 3"),
		Core("B1030", "F9 FT Block 3"),
		Core("B1031", "F9 FT Block 3"),
		Core("B1032", "F9 FT Block 3"),
		Core("B1033", "F9 FT Block 3"),
		Core("B1034", "F9 FT Block 3"),
		Core("B1035", "F9 FT Block 3"),
		Core("B1036", "F9 FT Block 3"),
		Core("B1037", "F9 FT Block 3"),
		Core("B1038", "F9 FT Block 3"),

		Core("B1039", "F9 FT Block 4"),
		Core("B1040", "F9 FT Block 4"),
		Core("B1041", "F9 FT Block 4"),
		Core("B1042", "F9 FT Block 4"),
		Core("B1043", "F9 FT Block 4"),
		Core("B1044", "F9 FT Block 4"),
		Core("B1045", "F9 FT Block 4"),

		Core("B1046", "F9 FT Block 5", True),
		Core("B1047", "F9 FT Block 5", True),
		Core("B1048", "F9 FT Block 5", True),
		Core("B1049", "F9 FT Block 5", True),
		Core("B1050", "F9 FT Block 5"),
		Core("B1051", "F9 FT Block 5", True),
		Core("B1052", "F9 FT Block 5", True),
		Core("B1053", "F9 FT Block 5", True),
		Core("B1054", "F9 FT Block 5"),
		Core("B1055", "F9 FT Block 5", True),
		Core("B1056", "F9 FT Block 5", True)
	]