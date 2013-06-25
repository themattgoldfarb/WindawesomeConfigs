from Windawesome import Windawesome, ProgramRule, State, OnWindowCreatedOrShownAction, OnWindowCreatedOnWorkspaceAction
from Windawesome.NativeMethods import WS, WS_EX

config.ProgramRules = [
	ProgramRule(
		className = "^CabinetWClass$", # Windows Explorer
		updateIcon = True,
		rules = [ProgramRule.Rule(workspace = 2,titlebar = State.HIDDEN, windowBorders=State.HIDDEN)]
	),
	ProgramRule(
		className = "^ExploreWClass$", # Windows Explorer
		updateIcon = True,
		rules = [ProgramRule.Rule(workspace = 2,titlebar = State.HIDDEN, windowBorders=State.HIDDEN)]
	),

	ProgramRule(
		className = "^{97E27FAA-C0B3-4b8e-A693-ED7881E99FC1}$", # foobar2000
		rules = [ProgramRule.Rule(workspace = 7)]
	),
	
	
	#music
	ProgramRule(
		displayName = ".*Grooveshark.*",
		rules = [ProgramRule.Rule(workspace = 6)]
	),
	ProgramRule(
		displayName = ".*Pandora Internet Radio.*",
		rules = [ProgramRule.Rule(workspace = 6)]
	),
	ProgramRule(
		className="^SpotifyMainWindow$",
		rules = [ProgramRule.Rule(workspace = 6)]
	),
	
	# browsers
	ProgramRule(
		className = "^Chrome_WidgetWin_1$", # Chrome
		rules = [ProgramRule.Rule(workspace = 3,titlebar = State.HIDDEN, windowBorders=State.HIDDEN)]
	),
	
	
	# mail
	ProgramRule(
		className = "^rctrl_renwnd32$", # Outlook
		rules = [ProgramRule.Rule(workspace = 5,titlebar = State.HIDDEN, windowBorders=State.HIDDEN)]
	),
	
	#chat
	ProgramRule(
		displayName = ".*HipChat.*",
		rules = [ProgramRule.Rule(workspace = 1,titlebar = State.HIDDEN, windowBorders=State.HIDDEN)]
	),	
	ProgramRule(
		displayName = ".*Buddy\sList.*",
		rules = [ProgramRule.Rule(workspace = 1,titlebar = State.HIDDEN, windowBorders=State.HIDDEN)]
	),	
	ProgramRule(
		className = "^gdkWindowToplevel$",
		rules = [ProgramRule.Rule(workspace = 1,titlebar = State.HIDDEN, windowBorders=State.HIDDEN)]
	),
	
	
	# terminals
	ProgramRule(
		className = "^Console_2_Main$",
		rules=[ProgramRule.Rule(workspace=2, titlebar = State.HIDDEN, windowBorders=State.HIDDEN)]
	),
	
	

	# editors
	ProgramRule(
		displayName = ".*Microsoft Visual Studio.*",
		onWindowCreatedAction = OnWindowCreatedOrShownAction.HideWindow,
		rules = [ProgramRule.Rule(workspace = 4, titlebar = State.HIDDEN, windowBorders = State.HIDDEN)]
	),
	ProgramRule(
		displayName = ".*Microsoft SQL Server Management Studio.*",
		onWindowCreatedAction = OnWindowCreatedOrShownAction.HideWindow,
		rules = [ProgramRule.Rule(workspace = 4, titlebar = State.HIDDEN, windowBorders = State.HIDDEN)]
	),
	ProgramRule(
		displayName = ".*Notepad\+\+.*",
		onWindowCreatedAction = OnWindowCreatedOrShownAction.HideWindow,
		rules = [ProgramRule.Rule(workspace = 4, titlebar = State.HIDDEN, windowBorders = State.HIDDEN)]
	),
	ProgramRule(
		displayName = ".*Sublime Text 2.*",
		onWindowCreatedAction = OnWindowCreatedOrShownAction.HideWindow,
		rules = [ProgramRule.Rule(workspace = 4, titlebar = State.HIDDEN, windowBorders = State.HIDDEN)]
	),

	#misc
	ProgramRule(
		className = "^TscShellContainerClass$",
		rules=[ProgramRule.Rule(workspace=9, titlebar=State.HIDDEN, windowBorders = State.HIDDEN)]
	),
	
	ProgramRule() # an all-catching rule in the end to manage all other windows
]
