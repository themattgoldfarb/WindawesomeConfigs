from System.Drawing import Color, Font
from System.Linq import Enumerable
from Windawesome import ILayout, TileLayout, FullScreenLayout, FloatingLayout, IPlugin, Workspace
from Windawesome import Bar, LayoutWidget, WorkspacesWidget, ApplicationTabsWidget, SystemTrayWidget, CpuMonitorWidget, RamMonitorWidget, LaptopBatteryMonitorWidget, LanguageBarWidget, CurrentlyPlayingWidget, SeparatorWidget
from Windawesome import LoggerPlugin, ShortcutsManager, InputLanguageChangerPlugin
from Windawesome.NativeMethods import MOD
from System import Tuple
from System.Windows.Forms import Keys

def onLayoutLabelClick():
	if windawesome.CurrentWorkspace.Layout.LayoutName() == "Full Screen":
		windawesome.CurrentWorkspace.ChangeLayout(FloatingLayout())
	elif windawesome.CurrentWorkspace.Layout.LayoutName() == "Floating":
		windawesome.CurrentWorkspace.ChangeLayout(TileLayout())
	else:
		windawesome.CurrentWorkspace.ChangeLayout(FullScreenLayout())

config.WindowBorderWidth = 1
config.WindowPaddedBorderWidth = 0

config.CheckForUpdates = False

workspacesWidgetForegroundColors = [Color.Yellow for i in range(0, 10)]
workspacesWidgetForegroundColors[0] = Color.LightSeaGreen
workspacesWidgetBackgroundColors = [Color.Black for i in range(0, 10)]

config.Bars = Enumerable.ToArray[Bar]([
	Bar(windawesome.monitors[0],
		[
			WorkspacesWidget(
				normalForegroundColor = workspacesWidgetForegroundColors,
				normalBackgroundColor = workspacesWidgetBackgroundColors,
				highlightedForegroundColor = Color.DarkOrange,
				highlightedBackgroundColor = Color.Black,
				highlightedInactiveForegroundColor = Color.LightSeaGreen,
				highlightedInactiveBackgroundColor = Color.Black,
				flashingForegroundColor = Color.Black
			),
			LayoutWidget(
				foregroundColor = Color.Gold,
				backgroundColor = Color.Black,
				onClick = onLayoutLabelClick
			)
		],

		[
			SystemTrayWidget(),
			LanguageBarWidget(
				foregroundColor = Color.Gold,
				backgroundColor = Color.Black
			),
			SeparatorWidget(
				foregroundColor = Color.Gold,
				backgroundColor = Color.Black
			),
			DateTimeWidget("ddd, d-MMM", "", "", Color.Black, Color.Gold),
			SeparatorWidget(
				foregroundColor = Color.Gold,
				backgroundColor = Color.Black
			),
			DateTimeWidget("h:mm tt", "", "", Color.Black, Color.Gold),
		],

		[
			ApplicationTabsWidget(
				normalForegroundColor = Color.LightSeaGreen,
				normalBackgroundColor = Color.Black,
				highlightedForegroundColor = Color.DarkOrange,
				highlightedBackgroundColor = Color.Black,
			)
		],

		backgroundColor = Color.Black,
		font = Font("Consolas", 11)
	),
	Bar(windawesome.monitors[1],
		[
			WorkspacesWidget(
				normalForegroundColor = workspacesWidgetForegroundColors,
				normalBackgroundColor = workspacesWidgetBackgroundColors,
				highlightedForegroundColor = Color.DarkOrange,
				highlightedBackgroundColor = Color.Black,
				highlightedInactiveForegroundColor = Color.LightSeaGreen,
				highlightedInactiveBackgroundColor = Color.Black,
				flashingForegroundColor = Color.Black
			),
			LayoutWidget(
				foregroundColor = Color.Gold,
				backgroundColor = Color.Black,
				onClick = onLayoutLabelClick
			)
		],

		[
			SystemTrayWidget(True),
			LanguageBarWidget(
				foregroundColor = Color.Gold,
				backgroundColor = Color.Black
			),
			SeparatorWidget(
				foregroundColor = Color.Gold,
				backgroundColor = Color.Black
			),
			DateTimeWidget("ddd, d-MMM", "", "", Color.Black, Color.Gold),
			SeparatorWidget(
				foregroundColor = Color.Gold,
				backgroundColor = Color.Black
			),
			DateTimeWidget("h:mm tt", "", "", Color.Black, Color.Gold),
		],

		[
			ApplicationTabsWidget(
				normalForegroundColor = Color.LightSeaGreen,
				normalBackgroundColor = Color.Black,
				highlightedForegroundColor = Color.DarkOrange,
				highlightedBackgroundColor = Color.Black,
			)
		],

		backgroundColor = Color.Black,
		font = Font("Consolas", 11)
	),
		Bar(windawesome.monitors[2],
		[
			WorkspacesWidget(
				normalForegroundColor = workspacesWidgetForegroundColors,
				normalBackgroundColor = workspacesWidgetBackgroundColors,
				highlightedForegroundColor = Color.DarkOrange,
				highlightedBackgroundColor = Color.Black,
				highlightedInactiveForegroundColor = Color.LightSeaGreen,
				highlightedInactiveBackgroundColor = Color.Black,
				flashingForegroundColor = Color.Black
			),
			LayoutWidget(
				foregroundColor = Color.Gold,
				backgroundColor = Color.Black,
				onClick = onLayoutLabelClick
			)
		],

		[
			SystemTrayWidget(True),
			LanguageBarWidget(
				foregroundColor = Color.Gold,
				backgroundColor = Color.Black
			),
			SeparatorWidget(
				foregroundColor = Color.Gold,
				backgroundColor = Color.Black
			),
			DateTimeWidget("ddd, d-MMM", "", "", Color.Black, Color.Gold),
			SeparatorWidget(
				foregroundColor = Color.Gold,
				backgroundColor = Color.Black
			),
			DateTimeWidget("h:mm tt", "", "", Color.Black, Color.Gold),
		],

		[
			ApplicationTabsWidget(
				normalForegroundColor = Color.LightSeaGreen,
				normalBackgroundColor = Color.Black,
				highlightedForegroundColor = Color.DarkOrange,
				highlightedBackgroundColor = Color.Black,
			)
		],

		backgroundColor = Color.Black,
		font = Font("Consolas", 11)
	),
		Bar(windawesome.monitors[3],
		[
			WorkspacesWidget(
				normalForegroundColor = workspacesWidgetForegroundColors,
				normalBackgroundColor = workspacesWidgetBackgroundColors,
				highlightedForegroundColor = Color.DarkOrange,
				highlightedBackgroundColor = Color.Black,
				highlightedInactiveForegroundColor = Color.LightSeaGreen,
				highlightedInactiveBackgroundColor = Color.Black,
				flashingForegroundColor = Color.Black
			),
			LayoutWidget(
				foregroundColor = Color.Gold,
				backgroundColor = Color.Black,
				onClick = onLayoutLabelClick
			)
		],

		[
			SystemTrayWidget(True),
			LanguageBarWidget(
				foregroundColor = Color.Gold,
				backgroundColor = Color.Black
			),
			SeparatorWidget(
				foregroundColor = Color.Gold,
				backgroundColor = Color.Black
			),
			DateTimeWidget("ddd, d-MMM", "", "", Color.Black, Color.Gold),
			SeparatorWidget(
				foregroundColor = Color.Gold,
				backgroundColor = Color.Black
			),
			DateTimeWidget("h:mm tt", "", "", Color.Black, Color.Gold),
		],

		[
			ApplicationTabsWidget(
				normalForegroundColor = Color.LightSeaGreen,
				normalBackgroundColor = Color.Black,
				highlightedForegroundColor = Color.DarkOrange,
				highlightedBackgroundColor = Color.Black,
			)
		],

		backgroundColor = Color.Black,
		font = Font("Consolas", 11)
	),
	Bar(windawesome.monitors[0],
		[
			WorkspacesWidget(
				normalForegroundColor = workspacesWidgetForegroundColors,
				normalBackgroundColor = workspacesWidgetBackgroundColors,
				highlightedForegroundColor = Color.DarkOrange,
				highlightedBackgroundColor = Color.Black,
				highlightedInactiveForegroundColor = Color.LightSeaGreen,
				highlightedInactiveBackgroundColor = Color.Black,
				flashingForegroundColor = Color.Black
			),
			LayoutWidget(
				foregroundColor = Color.Gold,
				backgroundColor = Color.Black,
				onClick = onLayoutLabelClick
			)
		],

		[
			SystemTrayWidget(True),
			LanguageBarWidget(
				foregroundColor = Color.Gold,
				backgroundColor = Color.Black
			),
			SeparatorWidget(
				foregroundColor = Color.Gold,
				backgroundColor = Color.Black
			),
			DateTimeWidget("ddd, d-MMM", "", "", Color.Black, Color.Gold),
			SeparatorWidget(
				foregroundColor = Color.Gold,
				backgroundColor = Color.Black
			),
			DateTimeWidget("h:mm tt", "", "", Color.Black, Color.Gold),
		],

		[
			ApplicationTabsWidget(
				normalForegroundColor = Color.LightSeaGreen,
				normalBackgroundColor = Color.Black,
				highlightedForegroundColor = Color.DarkOrange,
				highlightedBackgroundColor = Color.Black,
			)
		],

		backgroundColor = Color.Black,
		font = Font("Consolas", 11)
	),
])

config.Workspaces = Enumerable.ToArray[Workspace]([
	Workspace(windawesome.monitors[3], TileLayout(masterAreaAxis = TileLayout.LayoutAxis.LeftToRight, masterAreaWindowsCount = 1, masterAreaFactor = 0.5), [config.Bars[3]], name = 'chat'),
	Workspace(windawesome.monitors[0], TileLayout(masterAreaAxis = TileLayout.LayoutAxis.LeftToRight, masterAreaWindowsCount = 1, masterAreaFactor = 0.5), [config.Bars[0]], name = 'explorer'),
	Workspace(windawesome.monitors[1], TileLayout(masterAreaAxis = TileLayout.LayoutAxis.LeftToRight, masterAreaWindowsCount = 1, masterAreaFactor = 0.5), [config.Bars[1]], name = 'browsers'),
	Workspace(windawesome.monitors[2], TileLayout(masterAreaAxis = TileLayout.LayoutAxis.LeftToRight, masterAreaWindowsCount = 1, masterAreaFactor = 0.5), [config.Bars[2]], name = 'dev'),
	Workspace(windawesome.monitors[2], TileLayout(masterAreaAxis = TileLayout.LayoutAxis.LeftToRight, masterAreaWindowsCount = 1, masterAreaFactor = 0.5), [config.Bars[2]], name = 'mail'),
	Workspace(windawesome.monitors[2], TileLayout(masterAreaAxis = TileLayout.LayoutAxis.LeftToRight, masterAreaWindowsCount = 1, masterAreaFactor = 0.5), [config.Bars[2]], name = 'music'),
	Workspace(windawesome.monitors[0], FullScreenLayout(), [config.Bars[0]]),
	Workspace(windawesome.monitors[0], FullScreenLayout(), [config.Bars[0]]),
	Workspace(windawesome.monitors[0], FullScreenLayout(), [], name = 'Remote')
])

config.StartingWorkspaces = [config.Workspaces[0],config.Workspaces[1],config.Workspaces[2],config.Workspaces[3]]

config.Plugins = [
	#LoggerPlugin(logWorkspaceSwitching = True, logWindowMinimization = True, logWindowRestoration = True,
	#	logActivation = True),
	ShortcutsManager(),
	InputLanguageChangerPlugin(["icoicq", "icoSKYPE", "icoGOOGLE", "icoChannel", "icoJabber"])
]
