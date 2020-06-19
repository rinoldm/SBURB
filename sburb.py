import datetime
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.dates as mdates
import matplotlib.patches as patches
import matplotlib.transforms as transforms
from matplotlib.legend_handler import HandlerTuple

import data
import cores
import launches
	
def setAxes():
	axes = plt.gca()
	cores = data.cores
	
	axes.xaxis.grid(True)
	axes.xaxis.set_major_locator(mdates.YearLocator())
	axes.set_xlim(right = data.axisFurthestDate)
	
	axes.invert_yaxis()
	axes.set_yticks(range(0, len(cores)))
	axes.set_yticklabels(data.getCoreNumbers())
	axes.tick_params(length = 0)
	
	for core in cores:
		if (cores.index(core) % 2 == 0):
			plt.gca().add_patch(patches.Rectangle(
				(0, cores.index(core) - 0.5), 1, 1, linewidth = 0, color = '#fbfbfb', zorder = 1.3,
				transform = transforms.blended_transform_factory(axes.transAxes, axes.transData))
			)
	
	if data.mode in {'all', 'f1'}:
		axes.set_xlim(left = data.spaceXCreationDate - datetime.timedelta(365 / 4))
		axes.axvline(x = data.spaceXCreationDate, linestyle = '--', color = 'green')
	
	if data.mode in {'all', 'ft'}:
		axes.axvline(x = datetime.date.today(), linestyle = '--', color = 'blue')
				
	firstCores = data.getFirstCores()
	for core in firstCores:
		firstCoreIndex = cores.index(core)
		lastCoreIndex = cores.index(firstCores[firstCores.index(core) + 1]) if firstCores.index(core) != len(firstCores) - 1 else len(cores) - 1
		axes.axhline(y = firstCoreIndex - 0.5, linestyle = '-.', linewidth = 0.5, color = 'grey')
		axes.text(-0.05, (firstCoreIndex + lastCoreIndex) / 2, core.version, transform = transforms.blended_transform_factory(axes.transAxes, axes.transData), color = 'red', horizontalalignment='right', clip_on = False)

def setLegend():	
	legend = []
	for entry in data.legend:
		entrytuple = []
		for icon in entry['icons']:
			(iconColor, iconEdgeColor, iconStyle) = (icon[0], icon[1], icon[2])
			if iconStyle in {'o', 'x', '^', '*'}:
				entrytuple.append(mlines.Line2D([], [], color = iconColor, marker = iconStyle, linestyle = 'None', markersize = 10, markeredgewidth = 0.5, markeredgecolor = iconEdgeColor))
			else:
				entrytuple.append(patches.Patch(facecolor = iconColor, edgecolor = iconStyle))
		legend.append(tuple(entrytuple))

	plt.legend(legend, [entry['label'] for entry in data.legend], numpoints = 1, handler_map = {tuple: HandlerTuple(ndivide = None)}, loc = 'upper right')
	plt.title(data.chartName, fontsize = 16)
	plt.gcf().canvas.set_window_title(data.windowName)
	
def plotFalconHeavy(launch):
	heavyCoresIndexes = [data.getCoreNumbers().index(core) for core in launch.cores]
	plt.gca().add_patch(patches.Rectangle(
		(mdates.date2num(launch.date) - 9, min(heavyCoresIndexes) - 0.55),
		17, max(heavyCoresIndexes) - min(heavyCoresIndexes) + 1,
		linewidth = 1, facecolor = data.colors['HEAVY'], edgecolor = 'black', zorder = 1.5)
	)
	
def plotReuseRect(coreNumber, x, length):
	plt.gca().add_patch(patches.Rectangle(
		(x, data.getCoreNumbers().index(coreNumber) - 0.5),
		length, 1,
		linewidth = 0, color = data.colors['REUSE'], zorder = 1.4)
	)

def plotReuse():
	data.axisFurthestDate = max([launch.date for launch in data.launches]) + datetime.timedelta(365 / 4)
	for core in data.getCoreNumbers():
		coreLaunches = data.getLaunchesByCore(core)
		if len(coreLaunches) >= 1:
			for i in range(0, len(coreLaunches) - 1):
				x1 = mdates.date2num(coreLaunches[i])
				x2 = mdates.date2num(coreLaunches[i + 1])
				plotReuseRect(core,	x1,	x2 - x1)
				if data.mode == 'ft':
					plt.gca().text((x1 + x2) / 2, data.getCoreNumbers().index(core) - 0.3, int(x2 - x1), color = data.colors['DAYS'], horizontalalignment = 'center', verticalalignment = 'top', size = 9)

			if core in data.getActiveCoreNumbers():
				x1 = mdates.date2num(coreLaunches[len(coreLaunches) - 1])
				x2 = mdates.date2num(data.axisFurthestDate)
				plotReuseRect(core, x1, x2 - x1)

def plotLaunches():
	dataPoints = []

	for launch in data.launches:
		landings = launch.getLandings()
		for landing in landings:
			dataPoints.append({	'x': launch.date,
								'y': data.getCoreNumbers().index(landing['core']),
								'c': data.pickLaunchColor(launch, landings.index(landing)),
								'Dragon': launch.Dragon,
								'Starlink': launch.Starlink,
								'RUD': launch.RUD,
								'success': landing['success']})
		if len(launch.cores) > 1:
			plotFalconHeavy(launch)
			
	plt.scatter(x = [point['x'] for point in dataPoints if not point['Dragon'] and not point['Starlink']],
				y = [point['y'] for point in dataPoints if not point['Dragon'] and not point['Starlink']],
				c = [point['c'] for point in dataPoints if not point['Dragon'] and not point['Starlink']],
				edgecolors = ['black' if point['success'] else 'red' for point in dataPoints if not point['Dragon'] and not point['Starlink']],
				linewidth = [0.5 if point['success'] else 1 for point in dataPoints if not point['Dragon'] and not point['Starlink']],
				marker = 'o', s = 170, zorder = 3)
				
	plt.scatter(x = [point['x'] for point in dataPoints if point['Dragon'] and not point['Starlink']],
				y = [point['y'] for point in dataPoints if point['Dragon'] and not point['Starlink']],
				c = [point['c'] for point in dataPoints if point['Dragon'] and not point['Starlink']],
				edgecolors = ['black' if point['success'] else 'red' for point in dataPoints if point['Dragon'] and not point['Starlink']],
				linewidth = [0.5 if point['success'] else 1 for point in dataPoints if point['Dragon'] and not point['Starlink']],
				marker = '^', s = 170, zorder = 3)
				
	plt.scatter(x = [point['x'] for point in dataPoints if point['Starlink']],
				y = [point['y'] for point in dataPoints if point['Starlink']],
				c = [point['c'] for point in dataPoints if point['Starlink']],
				edgecolors = ['black' if point['success'] else 'red' for point in dataPoints if point['Starlink']],
				linewidth = [0.5 if point['success'] else 1 for point in dataPoints if point['Starlink']],
				marker = '*', s = 170, zorder = 3)

	plt.scatter(x = [point['x'] for point in dataPoints if point['RUD']],
				y = [point['y'] for point in dataPoints if point['RUD']],
				c = 'red',
				marker = 'x', s = 170, linewidth = 1, edgecolors = 'red', zorder = 3)
	
def main():
	plotLaunches(), plotReuse()
	setAxes(), setLegend()
	plt.show()

	return 0;
	
if __name__ == '__main__':
    main()