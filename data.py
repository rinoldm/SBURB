import sys
import datetime

windowName = "SpaceX Booster Use/Reuse Beholder"
chartName = "SpaceX Core History"
spaceXCreationDate = datetime.date(2002, 5, 6)

colors = {
	'EXPENDED':	'#bbbbbb',
	'HOP':		'#d9ff5e',
	'OCEAN':	'#053fff',
	'RTLS':		'#06b700',
	'ASDS':		'#56b9f7',
	'RUD':		'#ff0000',
	'REUSE':	'#b3e6ff',
	'DAYS':		'#3a84fc',
	'HEAVY':	'none',
}

legend = [
	{'icons': [[colors['EXPENDED'], 'black', 'o']], 'label': "No landing"},
	{'icons': [[colors['HOP'], 'black', 'o']], 'label': "Grasshopper hop"},
	{'icons': [[colors['OCEAN'], 'black', 'o']], 'label': "Ocean landing"},
	{'icons': [[colors['RTLS'], 'black', 'o']], 'label': "RTLS landing"},
	{'icons': [[colors['ASDS'],  'black', 'o']], 'label': "ASDS landing"},
	{'icons': [['none', 'red', 'o']],    'label': "Failed landing"},
	{'icons': [[colors['RUD'], 'red', 'x']],    'label': "RUD"},
	{'icons': [['none', 'black', '^']],    'label': "Dragon"},
	{'icons': [['none', 'black', '*']],    'label': "Starlink"},
	{'icons': [[colors['REUSE'], 'none', 'none']], 'label': "Reuse"},
	{'icons': [[colors['HEAVY'], 'none', 'black']], 'label': "Falcon Heavy"},
]

if len(sys.argv) != 2 or str.lower(sys.argv[1]) not in {'all', 'f1', 'f9', 'ft'}:
	print("Usage : py sburb.py [mode]       with mode = all, F1, F9 or FT (case-insensitive)")
	exit()
mode = str.lower(sys.argv[1])

def getCoreNumbers():
	return [core.number for core in cores]
		
def getActiveCoreNumbers():
	return [core.number for core in cores if core.active]
	
def getFirstCores():
	firstCores = []
	for core in cores:
		if core.version not in [firstCore.version for firstCore in firstCores]:
			firstCores.append(core)
	return firstCores
	
def getLaunchesByCore(core):
	return [launch.date for launch in launches if core in launch.cores]
		
def pickLaunchColor(launch, landingIndex):
	location = launch.landings[landingIndex][0]
	if (launch.hop == True):
		color = colors['HOP']
	elif (location in {"No attempt"}):
		color = colors['EXPENDED']
	elif (location in {"Ocean"}):
		color = colors['OCEAN']
	elif (location in {"Original JRTI", "JRTI", "OCISLY"}):
		color = colors['ASDS']
	elif (location in {"Land (parachutes)", "LZ-1", "LZ-2", "LZ-4"}):
		color = colors['RTLS']
	else:
		color = 'black'
	return color
