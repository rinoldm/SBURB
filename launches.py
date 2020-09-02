import data
import datetime

class Launch:
	def __init__(self, date, cores, landings = [["No attempt", True]], hop = False, RUD = False, Dragon = False, Starlink = False):
		self.date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
		self.cores = cores
		self.landings = landings
		self.hop = hop
		self.RUD = RUD
		self.Dragon = Dragon
		self.Starlink = Starlink
		
	def getLandings(self):
		landings = []
		for i in range(0, len(self.landings)):
			landings.append({'core': self.cores[i], 'location': self.landings[i][0], 'success': self.landings[i][1]})
		return landings

data.launches = []	

if (data.mode in {'all', 'f1'}):
	data.launches += [
		Launch("2006-03-24", ["F1-01"], RUD=True),
		
		Launch("2007-03-21", ["F1-02"], RUD=True),
		
		Launch("2008-08-03", ["F1-03"], RUD=True),
		Launch("2008-09-28", ["F1-04"]),
		
		Launch("2009-07-14", ["F1-05"]),
	]
	
if (data.mode in {'all', 'f9'}):
	data.launches += [
		Launch("2010-06-04", ["B0003"], landings=[["Land (parachutes)", False]], Dragon=True),
		Launch("2010-12-08", ["B0004"], landings=[["Land (parachutes)", False]], Dragon=True),

		Launch("2012-05-22", ["B0005"], Dragon=True),
		Launch("2012-09-21", ["B0002"], landings=[["McGregor", True]], hop=True),
		Launch("2012-10-07", ["B0006"], Dragon=True),
		Launch("2012-11-01", ["B0002"], landings=[["McGregor", True]], hop=True),
		Launch("2012-12-17", ["B0002"], landings=[["McGregor", True]], hop=True),

		Launch("2013-03-01", ["B0007"], Dragon=True),
		Launch("2013-03-07", ["B0002"], landings=[["McGregor", True]], hop=True),
		Launch("2013-04-17", ["B0002"], landings=[["McGregor", True]], hop=True),
		Launch("2013-06-14", ["B0002"], landings=[["McGregor", True]], hop=True),
		Launch("2013-08-13", ["B0002"], landings=[["McGregor", True]], hop=True),
		Launch("2013-09-29", ["B1003"], landings=[["Ocean", False]]),
		Launch("2013-10-07", ["B0002"], landings=[["McGregor", True]], hop=True),
		Launch("2013-12-03", ["B1004"]),

		Launch("2014-01-06", ["B1005"]),
		Launch("2014-04-17", ["B1002"], landings=[["McGregor", True]], hop=True),
		Launch("2014-04-18", ["B1006"], landings=[["Ocean", True]], Dragon=True),
		Launch("2014-05-01", ["B1002"], landings=[["McGregor", True]], hop=True),
		Launch("2014-06-17", ["B1002"], landings=[["McGregor", True]], hop=True),
		Launch("2014-07-14", ["B1007"], landings=[["Ocean", True]]),
		Launch("2014-08-01", ["B1002"], landings=[["McGregor", True]], hop=True),
		Launch("2014-08-05", ["B1008"]),
		Launch("2014-08-22", ["B1002"], RUD=True, hop=True),
		Launch("2014-09-07", ["B1011"]),
		Launch("2014-09-21", ["B1010"], landings=[["Ocean", True]], Dragon=True),
		
		Launch("2015-01-10", ["B1012"], landings=[["Original JRTI", False]], Dragon=True),
		Launch("2015-02-11", ["B1013"], landings=[["Ocean", True]]),
		Launch("2015-03-01", ["B1014"]),
		Launch("2015-04-14", ["B1015"], landings=[["Original JRTI", False]], Dragon=True),
		Launch("2015-04-27", ["B1016"]),
		Launch("2015-06-28", ["B1018"], landings=[["OCISLY", False]], RUD=True, Dragon=True),

		Launch("2016-01-17", ["B1017"], landings=[["JRTI", False]]),
	]
	
if (data.mode in {'all', 'ft'}):
	data.launches += [
		Launch("2015-12-21", ["B1019"], landings=[["LZ-1", True]]),
		
		Launch("2016-03-04", ["B1020"], landings=[["OCISLY", False]]),
		Launch("2016-04-08", ["B1021"], landings=[["OCISLY", True]], Dragon=True),
		Launch("2016-05-06", ["B1022"], landings=[["OCISLY", True]]),
		Launch("2016-05-27", ["B1023"], landings=[["OCISLY", True]]),
		Launch("2016-06-15", ["B1024"], landings=[["OCISLY", False]]),
		Launch("2016-07-18", ["B1025"], landings=[["LZ-1", True]], Dragon=True),
		Launch("2016-08-14", ["B1026"], landings=[["OCISLY", True]]),
		Launch("2016-09-01", ["B1028"], landings=[["OCISLY", False]], RUD=True),

		Launch("2017-01-14", ["B1029"], landings=[["JRTI", True]]),
		Launch("2017-02-19", ["B1031"], landings=[["LZ-1", True]], Dragon=True),
		Launch("2017-03-16", ["B1030"]),
		Launch("2017-03-30", ["B1021"], landings=[["OCISLY", True]]),
		Launch("2017-05-01", ["B1032"], landings=[["LZ-1", True]]),
		Launch("2017-05-15", ["B1034"]),
		Launch("2017-06-03", ["B1035"], landings=[["LZ-1", True]], Dragon=True),
		Launch("2017-06-23", ["B1029"], landings=[["OCISLY", True]]),
		Launch("2017-06-25", ["B1036"], landings=[["JRTI", True]]),
		Launch("2017-07-05", ["B1037"]),
		Launch("2017-08-14", ["B1039"], landings=[["LZ-1", True]], Dragon=True),
		Launch("2017-08-24", ["B1038"], landings=[["JRTI", True]]),
		Launch("2017-09-07", ["B1040"], landings=[["LZ-1", True]]),
		Launch("2017-10-09", ["B1041"], landings=[["JRTI", True]]),
		Launch("2017-10-11", ["B1031"], landings=[["OCISLY", True]]),
		Launch("2017-10-30", ["B1042"], landings=[["OCISLY", True]]),
		Launch("2017-12-15", ["B1035"], landings=[["LZ-1", True]], Dragon=True),
		Launch("2017-12-22", ["B1036"]),

		Launch("2018-01-07", ["B1043"], landings=[["LZ-1", True]]),
		Launch("2018-01-31", ["B1032"], landings=[["Ocean", True]]),
		Launch("2018-02-06", ["B1033", "B1023", "B1025"], landings=[["OCISLY", False], ["LZ-1", True], ["LZ-2", True]]),
		Launch("2018-02-22", ["B1038"]),
		Launch("2018-03-06", ["B1044"]),
		Launch("2018-03-30", ["B1041"]),
		Launch("2018-04-02", ["B1039"], Dragon=True),
		Launch("2018-04-18", ["B1045"], landings=[["OCISLY", True]]),
		Launch("2018-05-11", ["B1046"], landings=[["OCISLY", True]]),
		Launch("2018-05-22", ["B1043"]),
		Launch("2018-06-04", ["B1040"]),
		Launch("2018-06-29", ["B1045"], Dragon=True),
		Launch("2018-07-22", ["B1047"], landings=[["OCISLY", True]]),
		Launch("2018-07-25", ["B1048"], landings=[["JRTI", True]]),
		Launch("2018-08-07", ["B1046"], landings=[["OCISLY", True]]),
		Launch("2018-09-10", ["B1049"], landings=[["OCISLY", True]]),
		Launch("2018-10-07", ["B1048"], landings=[["LZ-4", True]]),
		Launch("2018-11-15", ["B1047"], landings=[["OCISLY", True]]),
		Launch("2018-12-03", ["B1046"], landings=[["JRTI", True]]),
		Launch("2018-12-05", ["B1050"], landings=[["LZ-1", False]], Dragon=True),
		Launch("2018-12-23", ["B1054"]),

		Launch("2019-01-11", ["B1049"], landings=[["JRTI", True]]),
		Launch("2019-02-21", ["B1048"], landings=[["OCISLY", True]]),
		Launch("2019-03-02", ["B1051"], landings=[["OCISLY", True]], Dragon=True),
		Launch("2019-04-11", ["B1055", "B1052", "B1053"], landings=[["OCISLY", True], ["LZ-1", True], ["LZ-2", True]]),
		Launch("2019-05-04", ["B1056"], landings=[["OCISLY", True]], Dragon=True),
		Launch("2019-05-24", ["B1049"], landings=[["OCISLY", True]], Starlink=True),
		Launch("2019-06-12", ["B1051"], landings=[["LZ-4", True]]),
		Launch("2019-06-25", ["B1057", "B1052", "B1053"], landings=[["OCISLY", False], ["LZ-1", True], ["LZ-2", True]]),
		Launch("2019-07-25", ["B1056"], landings=[["LZ-1", True]], Dragon=True),
		Launch("2019-08-07", ["B1047"]),
		Launch("2019-11-11", ["B1048"], landings=[["OCISLY", True]], Starlink=True),
		Launch("2019-12-05", ["B1059"], landings=[["OCISLY", True]], Dragon=True),
		Launch("2019-12-17", ["B1056"], landings=[["OCISLY", True]]),

		Launch("2020-01-07", ["B1049"], landings=[["OCISLY", True]], Starlink=True),
		Launch("2020-01-19", ["B1046"], Dragon=True),
		Launch("2020-01-29", ["B1051"], landings=[["OCISLY", True]], Starlink=True),
		Launch("2020-02-17", ["B1056"], landings=[["OCISLY", False]], Starlink=True),
		Launch("2020-03-07", ["B1059"], landings=[["LZ-1", True]], Dragon=True),
		Launch("2020-03-18", ["B1048"], landings=[["OCISLY", False]], Starlink=True),
		Launch("2020-04-22", ["B1051"], landings=[["OCISLY", True]], Starlink=True),
		Launch("2020-05-30", ["B1058"], landings=[["OCISLY", True]], Dragon=True),
		Launch("2020-06-04", ["B1049"], landings=[["JRTI", True]], Starlink=True),
		Launch("2020-06-13", ["B1059"], landings=[["OCISLY", True]], Starlink=True),
		Launch("2020-06-30", ["B1060"], landings=[["JRTI", True]]),
		Launch("2020-07-20", ["B1058"], landings=[["JRTI", True]]),
		Launch("2020-08-07", ["B1051"], landings=[["OCISLY", True]], Starlink=True),
		Launch("2020-08-18", ["B1049"], landings=[["OCISLY", True]], Starlink=True),
		Launch("2020-08-30", ["B1059"], landings=[["LZ-1", True]]),
		#--------------------- Future launches ----------------------
		Launch("2020-09-03", ["B1060"], Starlink=True),
		Launch("2020-10-01", ["B1062"]),
		Launch("2020-10-23", ["B1061"], Dragon=True),
		Launch("2020-11-10", ["B1063"]),
	]