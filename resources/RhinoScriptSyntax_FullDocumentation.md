# RhinoScriptSyntax - Complete API Documentation

Comprehensive reference with parameters, examples, and detailed descriptions.

**Statistics:** 898 total functions | 60 in use | 838 available

**Legend:** [IN USE] = Function currently used in code

---

## Table of Contents

- **[Application](#application)** (61 functions, 0 in use)
- **[Block](#block)** (25 functions, 0 in use)
- **[Curve](#curve)** (119 functions, 15 in use)
- **[Dimension](#dimension)** (39 functions, 0 in use)
- **[Document](#document)** (30 functions, 2 in use)
- **[Geometry](#geometry)** (35 functions, 2 in use)
- **[Grips](#grips)** (15 functions, 0 in use)
- **[Group](#group)** (17 functions, 0 in use)
- **[Hatch](#hatch)** (16 functions, 0 in use)
- **[Layer](#layer)** (33 functions, 8 in use)
- **[Light](#light)** (24 functions, 0 in use)
- **[Line](#line)** (10 functions, 0 in use)
- **[Linetype](#linetype)** (4 functions, 0 in use)
- **[Material](#material)** (16 functions, 0 in use)
- **[Mesh](#mesh)** (45 functions, 0 in use)
- **[Object](#object)** (60 functions, 12 in use)
- **[Plane](#plane)** (18 functions, 1 in use)
- **[Pointvector](#pointvector)** (33 functions, 0 in use)
- **[Selection](#selection)** (25 functions, 5 in use)
- **[Surface](#surface)** (100 functions, 14 in use)
- **[Toolbar](#toolbar)** (15 functions, 0 in use)
- **[Transformation](#transformation)** (25 functions, 0 in use)
- **[Userdata](#userdata)** (12 functions, 0 in use)
- **[Userinterface](#userinterface)** (38 functions, 0 in use)
- **[Utility](#utility)** (27 functions, 1 in use)
- **[View](#view)** (56 functions, 0 in use)

---

# Application

*61 functions | 0 in use*

---

## AddAlias

### Signature

```python
AddAlias(alias, macro)
```

### Description

Add new command alias to Rhino. Command aliases can be added manually by using Rhino's Options command and modifying the contents of the Aliases tab.

### Returns

bool: True or False indicating success or failure.

### Example

```python
import rhinoscriptsyntax as rs
rs.AddAlias("OriginLine", "!_Line 0,0,0")
```

### See Also

AliasCount, AliasMacro, AliasNames, DeleteAlias, IsAlias

---

## AddSearchPath

### Signature

```python
AddSearchPath(folder, index=-1)
```

### Description

Add new path to Rhino's search path list. Search paths can be added by using Rhino's Options command and modifying the contents of the files tab.

### Returns

number: The index where the item was inserted if success. -1 on failure.

### Example

```python
import rhinoscriptsyntax as rs
rs.AddSearchPath("C:\\My Python Scripts")
```

### See Also

DeleteSearchPath, SearchPathCount, SearchPathList

---

## AliasCount

### Signature

```python
AliasCount()
```

### Description

Returns number of command aliases in Rhino.

### Returns

number: the number of command aliases in Rhino.

### Example

```python
import rhinoscriptsyntax as rs
print("alias count = {}".format(rs.AliasCount()))
```

### See Also

AddAlias, AliasMacro, AliasNames, DeleteAlias, IsAlias

---

## AliasMacro

### Signature

```python
AliasMacro(alias, macro=None)
```

### Description

Returns or modifies the macro of a command alias.

### Returns

str: If a new macro is not specified, the existing macro if successful. str: If a new macro is specified, the previous macro if successful. null: None on error

### Example

```python
import rhinoscriptsyntax as rs
aliases = rs.AliasNames()
for alias in aliases:
 print("{} -> {}".format(alias, rs.AliasMacro(alias)))
```

### See Also

AddAlias, AliasCount, AliasNames, DeleteAlias, IsAlias

---

## AliasNames

### Signature

```python
AliasNames()
```

### Description

Returns a list of command alias names.

### Returns

str: a list of command alias names.

### Example

```python
import rhinoscriptsyntax as rs
aliases = rs.AliasNames()
for alias in aliases: print(alias)
```

### See Also

AddAlias, AliasCount, AliasMacro, DeleteAlias, IsAlias

---

## AppearanceColor

### Signature

```python
AppearanceColor(item, color=None)
```

### Description

Returns or modifies an application interface item's color.

### Returns

tuple (r255,g255,b255): if color is not specified, the current item color. tuple (r255,g255,b255): if color is specified, the previous item color.

### Example

```python
import rhinoscriptsyntax as rs
oldColor = rs.AppearanceColor(0)
newColor = rs.GetColor(oldColor)
if newColor is not None:
 rs.AppearanceColor(0, newColor)
 rs.Redraw()
```

### See Also

GetColor

---

## AutosaveFile

### Signature

```python
AutosaveFile(filename=None)
```

### Description

Returns or changes the file name used by Rhino's automatic file saving

### Returns

str: if filename is not specified, the name of the current autosave file str: if filename is specified, the name of the previous autosave file

### Example

```python
import rhinoscriptsyntax as rs
file = rs.AutosaveFile()
print("The current autosave file is {}".format(file))
```

### See Also

AutosaveInterval, EnableAutosave

---

## AutosaveInterval

### Signature

```python
AutosaveInterval(minutes=None)
```

### Description

Returns or changes how often the document will be saved when Rhino's automatic file saving mechanism is enabled

### Returns

number: if minutes is not specified, the current interval in minutes number: if minutes is specified, the previous interval in minutes

### Example

```python
import rhinoscriptsyntax as rs
minutes = rs.AutosaveInterval()
if minutes>20: rs.AutosaveInterval(20)
```

### See Also

AutosaveFile, EnableAutosave

---

## BuildDate

### Signature

```python
BuildDate()
```

### Description

Returns the build date of Rhino

### Returns

Datetime.date: the build date of Rhino. Will be converted to a string by most functions.

### Example

```python
import rhinoscriptsyntax as rs
build = rs.BuildDate()
print("Rhino Build:{}".format(build)
```

---

## ClearCommandHistory

### Signature

```python
ClearCommandHistory()
```

### Description

Clears contents of Rhino's command history window. You can view the command history window by using the CommandHistory command in Rhino.

### Returns

none

### Example

```python
import rhinoscriptsyntax as rs
rs.ClearCommandHistory()
```

### See Also

CommandHistory

---

## Command

### Signature

```python
Command(commandString, echo=True)
```

### Description

Runs a Rhino command script. All Rhino commands can be used in command scripts. The command can be a built-in Rhino command or one provided by a 3rd party plug-in.

### Returns

bool: True or False indicating success or failure Write command scripts just as you would type the command sequence at the command line. A space or a new line acts like pressing <Enter> at the command line. For more information, see "Scripting" in Rhino help. Note, this function is designed to run one command and one command only. Do not combine multiple Rhino commands into a single call to this method. WRONG: rs.Command("_Line _SelLast _Invert") CORRECT: rs.Command("_Line") rs.Command("_SelLast") rs.Command("_Invert") Also, the exclamation point and space character ( ! ) combination used by button macros and batch-driven scripts to cancel the previous command is not valid. WRONG: rs.Command("! _Line _Pause _Pause") CORRECT: rs.Command("_Line _Pause _Pause") After the command script has run, you can obtain the identifiers of most recently created or changed object by calling LastCreatedObjects.

### Example

```python
import rhinoscriptsyntax as rs
rs.Command("_Line 0,0,0 2,2,2")
rs.Command("_Line _Pause _Pause")
```

### See Also

IsCommand, LastCommandName, LastCommandResult, LastCreatedObjects, Prompt

---

## CommandHistory

### Signature

```python
CommandHistory()
```

### Description

Returns the contents of Rhino's command history window

### Returns

str: the contents of Rhino's command history window

### Example

```python
import rhinoscriptsyntax as rs
print(rs.CommandHistory())
```

### See Also

ClearCommandHistory

---

## DefaultRenderer

### Signature

```python
DefaultRenderer(renderer=None)
```

### Description

Returns or changes the default render plug-in

### Returns

guid: Unique identifier of default renderer

### Example

```python
import rhinoscriptsyntax as rs
rs.DefaultRenderer("MyRenderPlugIn")
```

### See Also

PlugIns

---

## DeleteAlias

### Signature

```python
DeleteAlias(alias)
```

### Description

Delete an existing alias from Rhino.

### Returns

bool: True or False indicating success

### Example

```python
import rhinoscriptsyntax as rs
print(rs.DeleteAlias("Hello"))
```

### See Also

AddAlias, AliasCount, AliasMacro, AliasNames, IsAlias

---

## DeleteSearchPath

### Signature

```python
DeleteSearchPath(folder)
```

### Description

Removes existing path from Rhino's search path list. Search path items can be removed manually by using Rhino's options command and modifying the contents of the files tab

### Returns

bool: True or False indicating success

### Example

```python
import rhinoscriptsyntax as rs
rs.DeleteSearchPath("C:\\My RhinoScripts")
```

### See Also

AddSearchPath, SearchPathCount, SearchPathList

---

## DisplayOleAlerts

### Signature

```python
DisplayOleAlerts(enable)
```

### Description

Enables/disables OLE Server Busy/Not Responding dialog boxes

### Returns

none

### Example

```python
import System
import rhinoscriptsyntax as rs
rs.DisplayOleAlerts( False )
t = System.Type.GetTypeFromProgID("Excel.Application")
objExcel = System.Activator.CreateObject(t)
...
```

---

## EdgeAnalysisColor

### Signature

```python
EdgeAnalysisColor(color=None)
```

### Description

Returns or modifies edge analysis color displayed by the ShowEdges command

### Returns

tuple (r255,g255,b255): if color is not specified, the current edge analysis color tuple (r255,g255,b255): if color is specified, the previous edge analysis color

### Example

```python
import rhinoscriptsyntax as rs
oldcolor = rs.EdgeAnalysisColor()
newcolor = rs.GetColor(oldcolor)
if newcolor is not None:
 rs.EdgeAnalysisColor(newcolor)
```

### See Also

EdgeAnalysisMode

---

## EdgeAnalysisMode

### Signature

```python
EdgeAnalysisMode(mode=None)
```

### Description

Returns or modifies edge analysis mode displayed by the ShowEdges command

### Returns

number: if mode is not specified, the current edge analysis mode number: if mode is specified, the previous edge analysis mode

### Example

```python
import rhinoscriptsyntax as rs
previous_mode = rs.EdgeAnalysisMode(1)
```

### See Also

EdgeAnalysisColor

---

## EnableAutosave

### Signature

```python
EnableAutosave(enable=True)
```

### Description

Enables or disables Rhino's automatic file saving mechanism

### Returns

bool: the previous autosave state

### Example

```python
import rhinoscriptsyntax as rs
prevstate = rs.EnableAutosave()
```

### See Also

AutosaveFile, AutosaveInterval

---

## EnablePlugIn

### Signature

```python
EnablePlugIn(plugin, enable=None)
```

### Description

Enables or disables a Rhino plug-in

### Returns

bool: True if set to load silently otherwise False

### Example

```python
import rhinoscriptsyntax as rs
print(rs.EnablePlugIn("RhinoCrasher", False))
```

### See Also

IsPlugIn, PlugInId, PlugIns

---

## ExeFolder

### Signature

```python
ExeFolder()
```

### Description

Returns the full path to Rhino's executable folder.

### Returns

str: the full path to Rhino's executable folder.

### Example

```python
import rhinoscriptsyntax as rs
folder = rs.ExeFolder()
print(folder)
```

### See Also

InstallFolder

---

## ExePlatform

### Signature

```python
ExePlatform()
```

### Description

Returns the platform of the Rhino executable

### Returns

str: the platform of the Rhino executable

### Example

```python
import rhinoscriptsyntax as rs
if rs.ExePlatform() == 1:
 print("You are using a 64-bit version of Rhino.")
else:
 print("You are using a 32-bit version of Rhino.")
```

### See Also

BuildDate, ExeVersion, SdkVersion

---

## ExeServiceRelease

### Signature

```python
ExeServiceRelease()
```

### Description

Returns the service release number of the Rhino executable

### Returns

str: the service release number of the Rhino executable

### Example

```python
import rhinoscriptsyntax as rs
print("Build date:{}".format(rs.BuildDate())
print("SDK Version:{}".format(rs.SdkVersion())
print("SDK Service Release:{}".format(rs.SdkServiceRelease())
print("Executable Version:{}".format(rs.ExeVersion())
print("Executable Service Release:{}".format(rs.ExeServiceRelease())
print("Serial Number:{}".format(rs.SerialNumber())
print("Node Type:{}".format(rs.NodeType())
print("Install Type:{}".format(rs.InstallType())
```

### See Also

BuildDate, ExeVersion, SdkVersion

---

## ExeVersion

### Signature

```python
ExeVersion()
```

### Description

Returns the major version number of the Rhino executable

### Returns

str: the major version number of the Rhino executable

### Example

```python
import rhinoscriptsyntax as rs
print("Build date:{}".format(rs.BuildDate()))
print("SDK Version:{}".format(rs.SdkVersion()))
print("SDK Service Release:{}".format(rs.SdkServiceRelease()))
print("Executable Version:{}".format(rs.ExeVersion()))
print("Executable Service Release:{}".format(rs.ExeServiceRelease()))
print("Serial Number:{}".format(rs.SerialNumber()))
print("Node Type:{}".format(rs.NodeType()))
print("Install Type:{}".format(rs.InstallType()))
```

### See Also

BuildDate, ExeServiceRelease, SdkVersion

---

## Exit

### Signature

```python
Exit()
```

### Description

Closes the rhino application

### Returns

none

### Example

```python
import rhinoscriptsyntax as rs
rs.Exit()
```

---

## FindFile

### Signature

```python
FindFile(filename)
```

### Description

Searches for a file using Rhino's search path. Rhino will look for a file in the following locations: 1. The current document's folder. 2. Folder's specified in Options dialog, File tab. 3. Rhino's System folders

### Returns

str: full path on success

### Example

```python
import rhinoscriptsyntax as rs
path = rs.FindFile("Rhino.exe")
print(path)
```

---

## GetPlugInObject

### Signature

```python
GetPlugInObject(plug_in)
```

### Description

Returns a scriptable object from a specified plug-in. Not all plug-ins contain scriptable objects. Check with the manufacturer of your plug-in to see if they support this capability.

### Returns

guid: scriptable object if successful null: None on error

### Example

```python
import rhinoscriptsyntax as rs
objPlugIn = rs.GetPlugInObject("SomePlugIn")
if objPlugIn is not None:
 print(objPlugIn.About())
```

---

## InCommand

### Signature

```python
InCommand(ignore_runners=True)
```

### Description

Determines if Rhino is currently running a command. Because Rhino allows for transparent commands (commands run from inside of other commands), this method returns the total number of active commands.

### Returns

number: the number of active commands

### Example

```python
import rhinoscriptsyntax as rs
commands = rs.InCommand()
if commands > 0:
 print("Rhino is running", commands, "command(s).")
else:
 print("Rhino is not running any command(s).")
```

### See Also

Command, IsCommand

---

## InstallFolder

### Signature

```python
InstallFolder()
```

### Description

The full path to Rhino's installation folder

### Returns

str: the full path to Rhino's installation folder

### Example

```python
import rhinoscriptsyntax as rs
print(rs.InstallFolder())
```

### See Also

ExeFolder

---

## IsAlias

### Signature

```python
IsAlias(alias)
```

### Description

Verifies that a command alias exists in Rhino

### Returns

bool: True if exists or False if the alias does not exist.

### Example

```python
import rhinoscriptsyntax as rs
print(rs.IsAlias("Hello"))
```

### See Also

AddAlias, AliasCount, AliasMacro, AliasNames, DeleteAlias

---

## IsCommand

### Signature

```python
IsCommand(command_name)
```

### Description

Verifies that a command exists in Rhino. Useful when scripting commands found in 3rd party plug-ins.

### Returns

bool: True if the string is a command or False if it is not a command.

### Example

```python
import rhinoscriptsyntax as rs
cmdname = rs.GetString("Command name to test")
if cmdname is not None:
 iscmd = rs.IsCommand(cmdname)
 if iscmd:
 print("The", cmdname, "command exists.")
 else:
 print("The", cmdname, "command does not exist.")
```

### See Also

Command, InCommand

---

## IsPlugIn

### Signature

```python
IsPlugIn(plugin)
```

### Description

Verifies that a plug-in is registered

### Returns

bool: True if the Guid is registered or False if it is not.

### Example

```python
import rhinoscriptsyntax as rs
plugin = rs.GetString("Plug-in name")
if rs.IsPlugIn(plugin): print("The plug-in is registered.")
else: print("The plug-in is not registered.")
```

### See Also

EnablePlugIn, PlugInId, PlugIns

---

## IsRunningOnWindows

### Signature

```python
IsRunningOnWindows()
```

### Description

Returns True if this script is being executed on a Windows platform

### Returns

bool: True if currently running on the Widows platform. False if it is not Windows.

### Example

```python
import rhinoscriptsyntax as rs
if rs.IsRunngingOnWindows():
 print("Running on Windows")
else:
 print("Running on Mac")
```

---

## LastCommandName

### Signature

```python
LastCommandName()
```

### Description

Returns the name of the last executed command

### Returns

str: the name of the last executed command

### Example

```python
import rhinoscriptsyntax as rs
rs.Command( "Line" )
print("The last command was the {} {}".format(rs.LastCommandName(), "command."))
```

### See Also

Command, IsCommand, LastCommandResult

---

## LastCommandResult

### Signature

```python
LastCommandResult()
```

### Description

Returns the result code for the last executed command

### Returns

number: the result code for the last executed command. 0 = success (command successfully completed) 1 = cancel (command was cancelled by the user) 2 = nothing (command did nothing, but was not cancelled) 3 = failure (command failed due to bad input, computational problem...) 4 = unknown command (the command was not found)

### Example

```python
import rhinoscriptsyntax as rs
rs.Command( "Line" )
result = rs.LastCommandResult()
if result==0:
 print("The command completed.")
else:
 print("The command did not complete.")
```

### See Also

Command, IsCommand, LastCommandName

---

## LocaleID

### Signature

```python
LocaleID()
```

### Description

Returns the current language used for the Rhino interface. The current language is returned as a locale ID, or LCID, value.

### Returns

number: the current language used for the Rhino interface as a locale ID, or LCID. 1029 Czech 1031 German-Germany 1033 English-United States 1034 Spanish-Spain 1036 French-France 1040 Italian-Italy 1041 Japanese 1042 Korean 1045 Polish

### Example

```python
import rhinoscriptsyntax as rs
lcid = rs.LocaleID()
if lcid==1029:
 print("message in Czech")
elif lcid==1031:
 print("message in German")
elif lcid==1033:
 print("message in English")
elif lcid==1034:
 print("message in Spanish")
elif lcid==1036:
 print("message in Italian")
elif lcid==1040:
 print("message in Japanese")
elif lcid==1042:
 print("message in Korean")
elif lcid==1045:
 print("message in Polish")
```

---

## Ortho

### Signature

```python
Ortho(enable=None)
```

### Description

Enables or disables Rhino's ortho modeling aid.

### Returns

bool: if enable is not specified, then the current ortho status bool: if enable is specified, then the previous ortho status

### Example

```python
import rhinoscriptsyntax as rs
if not rs.Ortho(): rs.Ortho(True)
```

### See Also

Osnap, Planar, Snap

---

## Osnap

### Signature

```python
Osnap(enable=None)
```

### Description

Enables or disables Rhino's object snap modeling aid. Object snaps are tools for specifying points on existing objects.

### Returns

bool: if enable is not specified, then the current osnap status bool: if enable is specified, then the previous osnap status

### Example

```python
import rhinoscriptsyntax as rs
if not rs.Osnap(): rs.Osnap(True)
```

### See Also

Ortho, OsnapMode, Planar, Snap

---

## OsnapDialog

### Signature

```python
OsnapDialog(visible=None)
```

### Description

Shows or hides Rhino's dockable object snap bar

### Returns

bool: if visible is not specified, then the current visible state bool: if visible is specified, then the previous visible state

### Example

```python
import rhinoscriptsyntax as rs
if not rs.OsnapDialog(): rs.OsnapDialog(True)
```

### See Also

Osnap, OsnapMode, ProjectOsnaps

---

## OsnapMode

### Signature

```python
OsnapMode(mode=None)
```

### Description

Returns or sets the object snap mode. Object snaps are tools for specifying points on existing objects

### Returns

number: if mode is not specified, then the current object snap mode(s) number: if mode is specified, then the previous object snap mode(s)

### Example

```python
import rhinoscriptsyntax as rs
rhOsnapModeEnd = 131072
#add 'End' mode while keeping the ones that are already set
mode = rs.OsnapMode()
rs.OsnapMode(mode + rhOsnapModeEnd)
#add 'End' mode while clearing the others
rs.OsnapMode(rhOsnapModeEnd)
```

### See Also

Osnap, OsnapDialog, ProjectOsnaps

---

## Planar

### Signature

```python
Planar(enable=None)
```

### Description

Enables or disables Rhino's planar modeling aid

### Returns

bool: if enable is not specified, then the current planar status bool: if enable is secified, then the previous planar status

### Example

```python
import rhinoscriptsyntax as rs
if not rs.Planar(): rs.Planar(True)
```

### See Also

Ortho, Osnap, Snap

---

## PlugInId

### Signature

```python
PlugInId(plugin)
```

### Description

Returns the identifier of a plug-in given the plug-in name

### Returns

guid: the id of the plug-in None: None if the plug-in isn't valid

### Example

```python
import rhinoscriptsyntax as rs
plugins = rs.PlugIns(0, 1)
if plugins:
 for plugin in plugins: print(rs.PlugInId(plugin))
```

### See Also

EnablePlugIn, IsPlugIn, PlugIns

---

## PlugIns

### Signature

```python
PlugIns(types=0, status=0)
```

### Description

Returns a list of registered Rhino plug-ins

### Returns

list of str: list of registered Rhino plug-ins

### Example

```python
import rhinoscriptsyntax as rs
plugins = rs.PlugIns(0, 1)
for plugin in plugins: print(plugin)
```

---

## ProjectOsnaps

### Signature

```python
ProjectOsnaps(enable=None)
```

### Description

Enables or disables object snap projection

### Returns

bool: the current object snap projection status

### Example

```python
import rhinoscriptsyntax as rs
if not rs.ProjectOsnaps(): rs.ProjectOsnaps(True)
```

### See Also

Osnap, OsnapDialog, OsnapMode

---

## Prompt

### Signature

```python
Prompt(message=None)
```

### Description

Change Rhino's command window prompt

### Returns

none

### Example

```python
import rhinoscriptsyntax as rs
rs.Prompt("Hello Rhino!")
```

### See Also

Command

---

## ScreenSize

### Signature

```python
ScreenSize()
```

### Description

Returns current width and height, of the screen of the primary monitor.

### Returns

tuple (width, height): containing two numbers identifying the width and height in pixels

### Example

```python
import rhinoscriptsyntax as rs
size = rs.ScreenSize()
print("Screen Width: {} pixels".format(size[0]))
print("Screen Height: {} pixels".format(size[1]))
```

---

## SdkVersion

### Signature

```python
SdkVersion()
```

### Description

Returns version of the Rhino SDK supported by the executing Rhino.

### Returns

str: the version of the Rhino SDK supported by the executing Rhino. Rhino SDK versions are 9 digit numbers in the form of YYYYMMDDn.

### Example

```python
import rhinoscriptsyntax as rs
print("Required SDK Version: {}".format(rs.SdkVersion()))
```

---

## SearchPathCount

### Signature

```python
SearchPathCount()
```

### Description

Returns the number of path items in Rhino's search path list. See "Options Files settings" in the Rhino help file for more details.

### Returns

number: the number of path items in Rhino's search path list

### Example

```python
import rhinoscriptsyntax as rs
count = rs.SearchPathCount()
if count>0:
 paths = rs.SearchPathList()
 for path in paths: print(path)
```

### See Also

AddSearchPath, DeleteSearchPath, SearchPathList

---

## SearchPathList

### Signature

```python
SearchPathList()
```

### Description

Returns all of the path items in Rhino's search path list. See "Options Files settings" in the Rhino help file for more details.

### Returns

list of str: list of search paths

### Example

```python
import rhinoscriptsyntax as rs
count = rs.SearchPathCount()
if count>0:
 paths = rs.SearchPathList()
 for path in paths: print(path)
```

### See Also

AddSearchPath, DeleteSearchPath, SearchPathCount

---

## SendKeystrokes

### Signature

```python
SendKeystrokes(keys=None, add_return=True)
```

### Description

Sends a string of printable characters to Rhino's command line

### Returns

none

### Example

```python
import rhinoscriptsyntax as rs
rs.SendKeystroke( "Hello Rhino!" )
rs.SendKeystrokes( 25/4 )
```

### See Also

Command

---

## Snap

### Signature

```python
Snap(enable=None)
```

### Description

Enables or disables Rhino's grid snap modeling aid

### Returns

bool: the current grid snap status

### Example

```python
import rhinoscriptsyntax as rs
if not rs.Snap(): rs.Snap(True)
```

### See Also

Ortho, Osnap, Planar

---

## StatusBarDistance

### Signature

```python
StatusBarDistance(distance=0)
```

### Description

Sets Rhino's status bar distance pane

### Returns

none

### Example

```python
import rhinoscriptsyntax as rs
rs.StatusBarDistance(3.14159)
```

### See Also

StatusBarMessage, StatusBarPoint

---

## StatusBarMessage

### Signature

```python
StatusBarMessage(message=None)
```

### Description

Sets Rhino's status bar message pane

### Returns

none

### Example

```python
import rhinoscriptsyntax as rs
rs.StatusBarMessage("Hello Rhino!")
```

### See Also

StatusBarDistance, StatusBarPoint

---

## StatusBarPoint

### Signature

```python
StatusBarPoint(point=None)
```

### Description

Sets Rhino's status bar point coordinate pane

### Returns

none

### Example

```python
import rhinoscriptsyntax as rs
pt = (1.1, 2.2, 3.3)
rs.StatusBarPoint(pt)
```

### See Also

StatusBarDistance, StatusBarMessage

---

## StatusBarProgressMeterHide

### Signature

```python
StatusBarProgressMeterHide()
```

### Description

Hide the progress meter

### Returns

none

---

## StatusBarProgressMeterShow

### Signature

```python
StatusBarProgressMeterShow(label, lower, upper, embed_label=True, show_percent=True)
```

### Description

Start the Rhino status bar progress meter

### Returns

bool: True or False indicating success or failure

---

## StatusBarProgressMeterUpdate

### Signature

```python
StatusBarProgressMeterUpdate(position, absolute=True)
```

### Description

Set the current position of the progress meter

### Returns

number: previous position setting.

---

## TemplateFile

### Signature

```python
TemplateFile(filename=None)
```

### Description

Returns or sets Rhino's default template file. This is the file used when Rhino starts.

### Returns

str: if filename is not specified, then the current default template file str: if filename is specified, then the previous default template file

### Example

```python
import rhinoscriptsyntax as rs
folder = rs.TemplateFolder()
filename = folder + "\\Millimeters.3dm"
rs.TemplateFile(filename)
```

### See Also

TemplateFolder

---

## TemplateFolder

### Signature

```python
TemplateFolder(folder=None)
```

### Description

Returns or sets the location of Rhino's template folder

### Returns

str: if folder is not specified, then the current template file folder str: if folder is specified, then the previous template file folder

### Example

```python
import rhinoscriptsyntax as rs
folder = rs.TemplateFolder()
filename = folder + "\\Millimeters.3dm"
rs.TemplateFile(filename)
```

### See Also

TemplateFile

---

## WindowHandle

### Signature

```python
WindowHandle()
```

### Description

Returns the windows handle of Rhino's main window

### Returns

IntPt: the Window's handle of Rhino's main window. IntPtr is a platform-specific type that is used to represent a pointer or a handle.

### Example

```python
import rhinoscriptsyntax as rs
handle = rs.WindowHandle()
print(handle)
```

---

## WorkingFolder

### Signature

```python
WorkingFolder(folder=None)
```

### Description

Returns or sets Rhino's working folder (directory). The working folder is the default folder for all file operations.

### Returns

str: if folder is not specified, then the current working folder str: if folder is specified, then the previous working folder

### Example

```python
import rhinoscriptsyntax as rs
folder = rs.WorkingFolder()
folder = rs.BrowseForFolder(folder, "Directory", "Select Directory")
if folder is not None:
 rs.WorkingFolder(folder)
```

### See Also

BrowseForFolder

---

# Block

*25 functions | 0 in use*

---

## AddBlock

### Signature

```python
AddBlock(object_ids, base_point, name=None, delete_input=False)
```

### Description

Adds a new block definition to the document

### Returns

str: name of new block definition on success

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.GetObjects("Select objects to define block")
if objs:
 point = rs.GetPoint("Block base point")
 if point:
 block = rs.AddBlock(objs, point, None, True)
 rs.InsertBlock(block, point)
```

### See Also

InsertBlock

---

## BlockContainerCount

### Signature

```python
BlockContainerCount(block_name)
```

### Description

Returns number of block definitions that contain a specified block definition

### Returns

number: the number of block definitions that contain a specified block definition

### Example

```python
import rhinoscriptscriptsyntax as rs
block = rs.GetString("Block name to query")
if rs.IsBlock(block):
 count = rs.BlockContainerCount(block)
 print("This block is nested in {} block(s).".format(count))
```

### See Also

BlockContainers, IsBlock

---

## BlockContainers

### Signature

```python
BlockContainers(block_name)
```

### Description

Returns names of the block definitions that contain a specified block definition.

### Returns

list(str, ...): A list of block definition names

### Example

```python
import rhinoscriptsyntax as rs
blockname = rs.GetString("Block name to query")
if rs.IsBlock(blockname):
 blocks = rs.BlockContainers(blockname)
 for block in blocks: print(block)
```

### See Also

BlockContainerCount, IsBlock

---

## BlockCount

### Signature

```python
BlockCount()
```

### Description

Returns the number of block definitions in the document

### Returns

number: the number of block definitions in the document

### Example

```python
import rhinoscriptsyntax as rs
count = rs.BlockCount()
print("There are {} blocks".format(count)
```

### See Also

BlockNames, IsBlock

---

## BlockDescription

### Signature

```python
BlockDescription(block_name, description=None)
```

### Description

Returns or sets the description of a block definition

### Returns

str: if description is not specified, the current description str: if description is specified, the previous description

### Example

```python
import rhinoscriptsyntax as rs
blockname = rs.GetString("Block name to list description")
if rs.IsBlock(blockname):
 desc = rs.BlockDescription(blockname)
 if desc is None: print("No description")
 else: print(desc)
```

### See Also

IsBlock

---

## BlockInstanceCount

### Signature

```python
BlockInstanceCount(block_name,where_to_look=0)
```

### Description

Counts number of instances of the block in the document. Nested instances are not included in the count.

### Returns

number: the number of instances of the block in the document

### Example

```python
import rhinoscriptsyntax as rs
blockname = rs.GetString("Block to count")
if rs.IsBlock(blockname):
 count = rs.BlockInstanceCount(blockname)
 print("{} block(s) found.".format(count))
```

### See Also

BlockInstanceInsertPoint, BlockInstances, BlockInstanceXform, IsBlockInstance

---

## BlockInstanceInsertPoint

### Signature

```python
BlockInstanceInsertPoint(object_id)
```

### Description

Returns the insertion point of a block instance.

### Returns

point: The insertion 3D point if successful

### Example

```python
import rhinoscriptsyntax as rs
strObject = rs.GetObject("Select block")
if rs.IsBlockInstance(strObject):
 rs.AddPoint( rs.BlockInstanceInsertPoint(strObject) )
```

### See Also

BlockInstanceCount, BlockInstances, BlockInstanceXform, IsBlockInstance

---

## BlockInstanceName

### Signature

```python
BlockInstanceName(object_id)
```

### Description

Returns the block name of a block instance

### Returns

str: the block name of a block instance

### Example

```python
import rhinoscriptsyntax as rs
strObject = rs.GetObject("Select block")
if rs.IsBlockInstance(strObject):
 print(rs.BlockInstanceName(strObject))
```

### See Also

BlockInstanceCount, BlockInstances, BlockInstanceXform, IsBlockInstance

---

## BlockInstanceXform

### Signature

```python
BlockInstanceXform(object_id)
```

### Description

Returns the location of a block instance relative to the world coordinate system origin (0,0,0). The position is returned as a 4x4 transformation matrix

### Returns

transform: the location, as a transform matrix, of a block instance relative to the world coordinate system origin

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select block to query")
if rs.IsBlockInstance(obj):
 arrMatrix = rs.BlockInstanceXform(obj)
 if arrMatrix is not None:
 pointId = rs.AddPoint([0,0,0])
 rs.TransformObject( pointId, arrMatrix)
```

### See Also

BlockInstanceCount, BlockInstanceInsertPoint, BlockInstances, IsBlockInstance

---

## BlockInstances

### Signature

```python
BlockInstances(block_name,where_to_look=0)
```

### Description

Returns the identifiers of the inserted instances of a block.

### Returns

list(guid, ...): Ids identifying the instances of a block in the model.

### Example

```python
import rhinoscriptsyntax as rs
strBlock = rs.GetString("Block to select")
if rs.IsBlock(strBlock):
 arrObjects = rs.BlockInstances(strBlock)
 if arrobjects:
 rs.SelectObjects(arrObjects)
```

### See Also

BlockInstanceCount, BlockInstanceInsertPoint, BlockInstanceXform, IsBlockInstance

---

## BlockNames

### Signature

```python
BlockNames( sort=False )
```

### Description

Returns the names of all block definitions in the document

### Returns

list(str, ...): the names of all block definitions in the document

### Example

```python
import rhinoscriptsyntax as rs
names = rs.BlockNames(True)
if names:
 for name in names: print(name)
```

### See Also

BlockCount, IsBlock

---

## BlockObjectCount

### Signature

```python
BlockObjectCount(block_name)
```

### Description

Returns number of objects that make up a block definition

### Returns

number: the number of objects that make up a block definition

### Example

```python
import rhinoscriptsyntax as rs
count = rs.BlockObjectCount()
print("There are {} blocks".format(count))
```

### See Also

BlockNames, BlockObjects, IsBlock

---

## BlockObjects

### Signature

```python
BlockObjects(block_name)
```

### Description

Returns identifiers of the objects that make up a block definition

### Returns

list(guid, ...): list of identifiers on success

### Example

```python
import rhinoscriptsyntax as rs
strBlock = rs.GetString("Block name to list identifiers")
if rs.IsBlock(strBlock):
 objects = rs.BlockObjects(strBlock)
 if objects:
 for item in objects: print(item)
```

### See Also

BlockNames, BlockObjectCount, IsBlock

---

## BlockPath

### Signature

```python
BlockPath(block_name)
```

### Description

Returns path to the source of a linked or embedded block definition. A linked or embedded block definition is a block definition that was inserted from an external file.

### Returns

str: path to the linked block on success

### Example

```python
import rhinoscriptsyntax as rs
strBlock = rs.GetString("Block name to list path")
if rs.IsBlockEmbedded(strBlock):
 print(rs.BlockPath(strBlock))
```

### See Also

IsBlock, IsBlockEmbedded

---

## BlockStatus

### Signature

```python
BlockStatus(block_name)
```

### Description

Returns the status of a linked block

### Returns

number: the status of a linked block Value Description -3 Not a linked block definition. -2 The linked block definition's file could not be opened or could not be read. -1 The linked block definition's file could not be found. 0 The linked block definition is up-to-date. 1 The linked block definition's file is newer than definition. 2 The linked block definition's file is older than definition. 3 The linked block definition's file is different than definition.

### Example

```python
import rhinoscriptsyntax as rs
block = rs.GetString("Block name to list description")
if rs.IsBlock(block):
 status = rs.BlockStatus(block)
 print("block status for {} is {}".format(block, status))
```

### See Also

IsBlock

---

## DeleteBlock

### Signature

```python
DeleteBlock(block_name)
```

### Description

Deletes a block definition and all of it's inserted instances.

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
strBlock = rs.GetString("Block name to delete")
if rs.IsBlock(strBlock):
 rs.DeleteBlock(strBlock)
```

### See Also

BlockNames, ExplodeBlockInstance, IsBlock

---

## ExplodeBlockInstance

### Signature

```python
ExplodeBlockInstance(object_id, explode_nested_instances=False)
```

### Description

Explodes a block instance into it's geometric components. The exploded objects are added to the document

### Returns

list(guid, ...): identifiers for the newly exploded objects on success

### Example

```python
import rhinoscriptsyntax as rs
strObject = rs.GetObject("Select block instance to explode")
if rs.IsBlockInstance(strObject):
 rs.ExplodeBlockInstance(strObject)
```

### See Also

DeleteBlock, IsBlockInstance

---

## InsertBlock

### Signature

```python
InsertBlock( block_name, insertion_point, scale=(1,1,1), angle_degrees=0, rotation_normal=(0,0,1) )
```

### Description

Inserts a block whose definition already exists in the document

### Returns

guid: id for the block that was added to the doc

---

## InsertBlock2

### Signature

```python
InsertBlock2(block_name, xform)
```

### Description

Inserts a block whose definition already exists in the document

### Returns

guid: id for the block that was added to the doc on success

---

## IsBlock

### Signature

```python
IsBlock(block_name)
```

### Description

Verifies the existence of a block definition in the document.

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
strBlock = rs.GetString("Block name")
if rs.IsBlock(strBlock):
 print("The block definition exists.")
else:
 print("The block definition does not exist.")
```

### See Also

IsBlockEmbedded, IsBlockInstance, IsBlockInUse, IsBlockReference

---

## IsBlockEmbedded

### Signature

```python
IsBlockEmbedded(block_name)
```

### Description

Verifies a block definition is embedded, or linked, from an external file.

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
strBlock = rs.GetString("Block name")
if rs.IsBlock(strBlock):
 if rs.IsBlockEmbedded(strBlock):
 print("The block definition is embedded.")
 else:
 print("The block definition is not embedded.")
else:
 print("The block definition does not exist.")
```

### See Also

IsBlock, IsBlockInstance, IsBlockInUse, IsBlockReference

---

## IsBlockInUse

### Signature

```python
IsBlockInUse(block_name, where_to_look=0)
```

### Description

Verifies that a block definition is being used by an inserted instance

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
strBlock = rs.GetString("Block name")
if rs.IsBlock(strBlock):
 if rs.IsBlockInUse(strBlock):
 print("The block definition is in use.")
 else:
 print("The block definition is not in use.")
else:
 print("The block definition does not exist.")
```

### See Also

IsBlock, IsBlockInstance, IsBlockEmbedded, IsBlockReference

---

## IsBlockInstance

### Signature

```python
IsBlockInstance(object_id)
```

### Description

Verifies an object is a block instance

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select block instance")
if rs.IsBlockInstance(obj):
 print("The object is a block instance.")
else:
 print("The object is not a block instance.")
```

### See Also

IsBlock, IsBlockEmbedded, IsBlockInUse, IsBlockReference

---

## IsBlockReference

### Signature

```python
IsBlockReference(block_name)
```

### Description

Verifies that a block definition is from a reference file.

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
strBlock = rs.GetString("Block name")
if rs.IsBlock(strBlock):
 if rs.IsBlockReference(strBlock):
 print("The block definition is a reference definition.")
 else:
 print("The block definition is not a reference definition.")
else:
 print("The block definition does not exist.")
```

### See Also

IsBlock, IsBlockEmbedded, IsBlockInUse, IsBlockInstance

---

## RenameBlock

### Signature

```python
RenameBlock( block_name, new_name )
```

### Description

Renames an existing block definition

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
strOldBlock = rs.GetString("Old block name")
if strOldBlock:
 strNewBlock = rs.GetString("New block name")
 if strNewBlock:
 rs.RenameBlock (strOldBlock, strNewBlock)
```

### See Also

BlockNames, IsBlock

---

# Curve

*119 functions | 15 in use*

---

## AddArc

### Signature

```python
AddArc(plane, radius, angle_degrees)
```

### Description

Adds an arc curve to the document

### Returns

guid: id of the new curve object

### Example

```python
import rhinoscriptsyntax as rs
plane = rs.WorldXYPlane()
plane = rs.RotatePlane(plane, 45.0, [0,0,1])
rs.AddArc( plane, 5.0, 45.0 )
```

### See Also

AddArc3Pt, ArcAngle, ArcCenterPoint, ArcMidPoint, ArcRadius, IsArc

---

## AddArc3Pt

** IN USE**

### Signature

```python
AddArc3Pt(start, end, point_on_arc)
```

### Description

Adds a 3-point arc curve to the document

### Returns

guid: id of the new curve object

### Example

```python
import rhinoscriptsyntax as rs
start = rs.GetPoint("Start of arc")
if start is not None:
 end = rs.GetPoint("End of arc")
 if end is not None:
 pton = rs.GetPoint("Point on arc")
 if pton is not None:
 rs.AddArc3Pt(start, end, pton)
```

### See Also

AddArc, ArcAngle, ArcCenterPoint, ArcMidPoint, ArcRadius, IsArc

---

## AddArcPtTanPt

### Signature

```python
AddArcPtTanPt(start, direction, end)
```

### Description

Adds an arc curve, created from a start point, a start direction, and an end point, to the document

### Returns

guid: id of the new curve object

### Example

```python
import rhinoscriptsyntax as rs
pick = rs.GetCurveObject("Select curve to extend")
point = rs.GetPoint("End of extension")
domain = rs.CurveDomain(pick[0])
if abs(pick[4]-domain[0]) < abs(pick[4]-domain[1]):
 origin = rs.CurveStartPoint(pick[0])
 tangent = rs.VectorReverse(rs.CurveTangent(pick[0], domain[0]))
else:
 origin = rs.CurveEndPoint(pick[0])
 tangent = rs.CurveTangent(pick[0], domain[1])
rs.AddArcPtTanPt(origin, tangent, point)
```

### See Also

AddArc, AddArc3Pt, IsArc

---

## AddBlendCurve

### Signature

```python
AddBlendCurve(curves, parameters, reverses, continuities)
```

### Description

Makes a curve blend between two curves

### Returns

guid: identifier of new curve on success

### Example

```python
import rhinoscriptsyntax as rs
curve0 = rs.AddLine((0,0,0), (0,9,0))
curve1 = rs.AddLine((1,10,0), (10,10,0))
curves = curve0, curve1
domain_crv0 = rs.CurveDomain(curve0)
domain_crv1 = rs.CurveDomain(curve1)
params = domain_crv0[1], domain_crv1[0]
revs = False, True
cont = 2,2
rs.AddBlendCurve( curves, params, revs, cont )
```

### See Also

AddFilletCurve

---

## AddCircle

** IN USE**

### Signature

```python
AddCircle(plane_or_center, radius)
```

### Description

Adds a circle curve to the document

### Returns

guid: id of the new curve object

### Example

```python
import rhinoscriptsyntax as rs
plane = rs.WorldXYPlane()
rs.AddCircle( plane, 5.0 )
```

### See Also

AddCircle3Pt, CircleCenterPoint, CircleCircumference, CircleRadius, IsCircle

---

## AddCircle3Pt

### Signature

```python
AddCircle3Pt(first, second, third)
```

### Description

Adds a 3-point circle curve to the document

### Returns

guid: id of the new curve object

### Example

```python
import rhinoscriptsyntax as rs
point1 = rs.GetPoint("First point on circle")
if point1:
 point2 = rs.GetPoint("Second point on circle")
 if point2:
 point3 = rs.GetPoint("Third point on circle")
 if point3:
 rs.AddCircle3Pt(point1, point2, point3)
```

### See Also

AddCircle, CircleCenterPoint, CircleCircumference, CircleRadius, IsCircle

---

## AddCurve

### Signature

```python
AddCurve(points, degree=3)
```

### Description

Adds a control points curve object to the document

### Returns

guid: id of the new curve object

### Example

```python
import rhinoscriptsyntax as rs
points = rs.GetPoints(True, message1="Pick curve point")
if points: rs.AddCurve(points)
```

### See Also

AddInterpCurve, IsCurve

---

## AddEllipse

** IN USE**

### Signature

```python
AddEllipse(plane, radiusX, radiusY)
```

### Description

Adds an elliptical curve to the document

### Returns

guid: id of the new curve object if successful

### Example

```python
import rhinoscriptsyntax as rs
plane = rs.WorldXYPlane()
rs.AddEllipse( plane, 5.0, 10.0 )
```

### See Also

AddEllipse3Pt, IsEllipse, EllipseCenterPoint, EllipseQuadPoints

---

## AddEllipse3Pt

### Signature

```python
AddEllipse3Pt(center, second, third)
```

### Description

Adds a 3-point elliptical curve to the document

### Returns

guid: id of the new curve object if successful

### Example

```python
import rhinoscriptsyntax as rs
center = (0,0,0)
second = (5,0,0)
third = (0,10,0)
rs.AddEllipse3Pt( center, second, third )
```

### See Also

AddEllipse, IsEllipse, EllipseCenterPoint, EllipseQuadPoints

---

## AddFilletCurve

### Signature

```python
AddFilletCurve(curve0id, curve1id, radius=1.0, base_point0=None, base_point1=None)
```

### Description

Adds a fillet curve between two curve objects

### Returns

guid: id of the new curve object if successful

### Example

```python
import rhinoscriptsyntax as rs
curve0 = rs.AddLine([0,0,0], [5,1,0])
curve1 = rs.AddLine([0,0,0], [1,5,0])
rs.AddFilletCurve( curve0, curve1 )
```

### See Also

CurveFilletPoints

---

## AddInterpCrvOnSrf

### Signature

```python
AddInterpCrvOnSrf(surface_id, points)
```

### Description

Adds an interpolated curve object that lies on a specified surface. Note, this function will not create periodic curves, but it will create closed curves.

### Returns

guid: id of the new curve object if successful

### Example

```python
import rhinoscriptsyntax as rs
surface_id = rs.GetObject("Select surface to draw curve on", rs.filter.surface)
if surface_id:
 point1 = rs.GetPointOnSurface( surface_id, "First point on surface")
 if point1:
 point2 = rs.GetPointOnSurface( surface_id, "Second point on surface")
 if point2:
 rs.AddInterpCrvOnSrf( surface_id, [point1, point2])
```

### See Also

AddCurve, AddInterpCurve, AddInterpCrvOnSrfUV

---

## AddInterpCrvOnSrfUV

### Signature

```python
AddInterpCrvOnSrfUV(surface_id, points)
```

### Description

Adds an interpolated curve object based on surface parameters, that lies on a specified surface. Note, this function will not create periodic curves, but it will create closed curves.

### Returns

guid: id of the new curve object if successful

### Example

```python
import rhinoscriptsyntax as rs
surface_id = rs.GetObject("Select surface to draw curve on", rs.filter.surface)
if surface_id:
 domainU = rs.SurfaceDomain( surface_id, 0)
 u0 = domainU[0]/2
 u1 = domainU[1]/2
 domainV = rs.SurfaceDomain( surface_id, 1)
 v0 = domainV[0]/2
 v1 = domainV[1]/2
 rs.AddInterpCrvOnSrfUV( surface_id, [[u0,v0],[u1,v1]])
```

### See Also

AddCurve, AddInterpCurve, AddInterpCrvOnSrf

---

## AddInterpCurve

** IN USE**

### Signature

```python
AddInterpCurve(points, degree=3, knotstyle=0, start_tangent=None, end_tangent=None)
```

### Description

Adds an interpolated curve object to the document. Options exist to make a periodic curve or to specify the tangent at the endpoints. The resulting curve is a non-rational NURBS curve of the specified degree.

### Returns

guid: id of the new curve object if successful

### Example

```python
import rhinoscriptsyntax as rs
points = (0,0,0), (1,1,0), (2,0,0), (3,1,0), (4,0,0), (5,1,0)
rs.AddInterpCurve(points)
```

### See Also

AddCurve, CurvePointCount, IsCurve

---

## AddLine

** IN USE**

### Signature

```python
AddLine(start, end)
```

### Description

Adds a line curve to the current model.

### Returns

guid: id of the new curve object

### Example

```python
import rhinoscriptsyntax as rs
start = rs.GetPoint("Start of line")
if start:
 end = rs.GetPoint("End of line")
 if end: rs.AddLine(start, end)
```

### See Also

CurveEndPoint, CurveStartPoint, IsLine

---

## AddNurbsCurve

### Signature

```python
AddNurbsCurve(points, knots, degree, weights=None)
```

### Description

Adds a NURBS curve object to the document

### Returns

guid: the identifier of the new object if successful, otherwise None

### Example

```python
import rhinoscriptsyntax as rs
curve_id = rs.GetObject("Pick a curve", rs.filter.curve)
if curve_id:
 points = rs.CurvePoints(curve_id)
 knots = rs.CurveKnots(curve_id)
 degree = rs.CurveDegree(curve_id)
 newcurve = rs.AddNurbsCurve( points, knots, degree)
 if newcurve: rs.SelectObject(newcurve)
```

### See Also

CurveDegree, CurveKnots, CurvePoints

---

## AddPolyline

** IN USE**

### Signature

```python
AddPolyline(points, replace_id=None)
```

### Description

Adds a polyline curve to the current model

### Returns

guid: id of the new curve object if successful

### Example

```python
import rhinoscriptsyntax as rs
points = rs.GetPoints(True)
if points: rs.AddPolyline(points)
```

### See Also

IsPolyline

---

## AddRectangle

### Signature

```python
AddRectangle(plane, width, height)
```

### Description

Add a rectangular curve to the document

### Returns

guid: id of new rectangle

### Example

```python
import rhinoscriptsyntax as rs
plane = rs.WorldXYPlane()
plane = rs.RotatePlane(plane, 45.0, [0,0,1])
rs.AddRectangle( plane, 5.0, 15.0 )
```

---

## AddSpiral

### Signature

```python
AddSpiral(point0, point1, pitch, turns, radius0, radius1=None)
```

### Description

Adds a spiral or helical curve to the document

### Returns

guid: id of new curve on success

### Example

```python
import rhinoscriptsyntax as rs
point0 = (0,0,0)
point1 = (0,0,10)
pitch = 1
turns = 10
radius0 = 5.0
radius1 = 8.0
rs.AddSpiral(point0, point1, pitch, turns, radius0, radius1)
```

---

## AddSubCrv

### Signature

```python
AddSubCrv(curve_id, param0, param1)
```

### Description

Add a curve object based on a portion, or interval of an existing curve object. Similar in operation to Rhino's SubCrv command

### Returns

guid: id of the new curve object if successful

### Example

```python
import rhinoscriptsyntax as rs
getresult = rs.GetCurveObject()
if getresult:
 curve_id = getresult[0]
 point0 = rs.GetPointOnCurve( curve_id )
 if point0:
 point1 = rs.GetPointOnCurve( curve_id )
 if point1:
 t0 = rs.CurveClosestPoint( curve_id, point0)
 t1 = rs.CurveClosestPoint( curve_id, point1)
 rs.AddSubCrv( curve_id, t0, t1 )
```

### See Also

CurveClosestPoint, GetCurveObject, GetPointOnCurve

---

## AddTweenCurves

### Signature

```python
AddTweenCurves(from_curve_id, to_curve_id, number_of_curves = 1, method = 0, sample_number = 10)
```

### Description

Creates curves between two open or closed input curves.

### Returns

list(guid, ...): The identifiers of the new tween objects if successful, None on error.

### Example

```python
import rhinoscriptsyntax as rs
curveA = rs.GetObject("Select first curve", rs.filter.curve)
curveB = rs.GetObject("Select second curve", rs.filter.curve)
arrResult = rs.AddTweenCurves(curveA, curveB, 6, 2, 30)
```

---

## ArcAngle

### Signature

```python
ArcAngle(curve_id, segment_index=-1)
```

### Description

Returns the angle of an arc curve object.

### Returns

number: The angle in degrees if successful.

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select arc")
if rs.IsArc(id):
 angle = rs.ArcAngle(id)
 print("Arc angle: {}".format(angle))
```

### See Also

AddArc3Pt, ArcCenterPoint, ArcMidPoint, ArcRadius, IsArc

---

## ArcCenterPoint

### Signature

```python
ArcCenterPoint(curve_id, segment_index=-1)
```

### Description

Returns the center point of an arc curve object

### Returns

point: The 3D center point of the arc if successful.

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select arc")
if rs.IsArc(id):
point = rs.ArcCenterPoint(id)
rs.AddPoint(point)
```

### See Also

AddArc3Pt, ArcAngle, ArcMidPoint, ArcRadius, IsArc

---

## ArcMidPoint

### Signature

```python
ArcMidPoint(curve_id, segment_index=-1)
```

### Description

Returns the mid point of an arc curve object

### Returns

point: The 3D mid point of the arc if successful.

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select arc")
if rs.IsArc(id):
 point = rs.ArcMidPoint(id)
 rs.AddPoint(point)
```

### See Also

AddArc3Pt, ArcAngle, ArcCenterPoint, ArcRadius, IsArc

---

## ArcRadius

### Signature

```python
ArcRadius(curve_id, segment_index=-1)
```

### Description

Returns the radius of an arc curve object

### Returns

number: The radius of the arc if successful.

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select arc")
if rs.IsArc(id):
 radius = rs.ArcRadius(id)
 print("Arc radius: {}".format(radius))
```

### See Also

AddArc3Pt, ArcAngle, ArcCenterPoint, ArcMidPoint, IsArc

---

## ChangeCurveDegree

### Signature

```python
ChangeCurveDegree(object_id, degree)
```

### Description

Changes the degree of a curve object. For more information see the Rhino help file for the ChangeDegree command.

### Returns

bool: True of False indicating success or failure. None: on failure

### See Also

IsCurve, CurveDegree

---

## CircleCenterPoint

### Signature

```python
CircleCenterPoint(curve_id, segment_index=-1, return_plane=False)
```

### Description

Returns the center point of a circle curve object

### Returns

point: The 3D center point of the circle if successful. plane: The plane of the circle if return_plane is True

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select circle")
if rs.IsCircle(id):
 point = rs.CircleCenterPoint(id)
 rs.AddPoint( point )
```

### See Also

AddCircle, AddCircle3Pt, CircleCircumference, CircleRadius, IsCircle

---

## CircleCircumference

### Signature

```python
CircleCircumference(curve_id, segment_index=-1)
```

### Description

Returns the circumference of a circle curve object

### Returns

number: The circumference of the circle if successful.

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select circle")
if rs.IsCircle(id):
 circumference = rs.CircleCircumference(id)
 print("Circle circumference: {}".format(circumference))
```

### See Also

AddCircle, AddCircle3Pt, CircleCenterPoint, CircleRadius, IsCircle

---

## CircleRadius

### Signature

```python
CircleRadius(curve_id, segment_index=-1)
```

### Description

Returns the radius of a circle curve object

### Returns

number: The radius of the circle if successful.

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select circle")
if rs.IsCircle(id):
 radius = rs.CircleRadius(id)
 print("Circle radius: {}".format(radius))
```

### See Also

AddCircle, AddCircle3Pt, CircleCenterPoint, CircleCircumference, IsCircle

---

## CloseCurve

### Signature

```python
CloseCurve(curve_id, tolerance=-1.0)
```

### Description

Closes an open curve object by making adjustments to the end points so they meet at a point

### Returns

guid: id of the new curve object if successful

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select curve", rs.filter.curve)
if not rs.IsCurveClosed(obj) and rs.IsCurveClosable(obj):
 rs.CloseCurve( obj )
```

### See Also

IsCurveClosable, IsCurveClosed

---

## ClosedCurveOrientation

### Signature

```python
ClosedCurveOrientation(curve_id, direction=(0,0,1))
```

### Description

Determine the orientation (counter-clockwise or clockwise) of a closed, planar curve

### Returns

number: 1 if the curve's orientation is clockwise -1 if the curve's orientation is counter-clockwise 0 if unable to compute the curve's orientation

---

## ConvertCurveToPolyline

### Signature

```python
ConvertCurveToPolyline(curve_id, angle_tolerance=5.0, tolerance=0.01, delete_input=False, min_edge_length=0, max_edge_length=0)
```

### Description

Convert curve to a polyline curve

### Returns

guid: The new curve if successful.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a curve")
if rs.IsCurve(obj):
 polyline = rs.ConvertCurveToPolyline(obj)
 if polyline: rs.SelectObject(polyline)
```

### See Also

IsCurve

---

## CurveArcLengthPoint

### Signature

```python
CurveArcLengthPoint(curve_id, length, from_start=True)
```

### Description

Returns the point on the curve that is a specified arc length from the start of the curve.

### Returns

point: on curve if successful

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a curve")
if rs.IsCurve(obj):
 length = rs.CurveLength(obj)
 point = rs.CurveArcLengthPoint(obj, length/3.0)
 rs.AddPoint( point )
```

### See Also

CurveEndPoint, CurveMidPoint, CurveStartPoint

---

## CurveArea

** IN USE**

### Signature

```python
CurveArea(curve_id)
```

### Description

Returns area of closed planar curves. The results are based on the current drawing units.

### Returns

list[number, number]: List of area information. The list will contain the following information: Element Description [0] The area. If more than one curve was specified, the value will be the cumulative area. [1] The absolute (+/-) error bound for the area.

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a curve", rs.filter.curve)
if id:
 props = rs.CurveArea(id)
 if props:
 print("The curve area is: {}".format(props[0]))
```

### See Also

IsCurve, IsCurveClosed, IsCurvePlanar

---

## CurveAreaCentroid

### Signature

```python
CurveAreaCentroid(curve_id)
```

### Description

Returns area centroid of closed, planar curves. The results are based on the current drawing units.

### Returns

tuple(point, vector): of area centroid information containing the following information: Element Description [0] The 3d centroid point. If more than one curve was specified, the value will be the cumulative area. [1] A 3d vector with the absolute (+/-) error bound for the area centroid.

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a curve", rs.filter.curve)
if id:
 props = rs.CurveAreaCentroid(id)
 if props:
 print("The curve area centroid is: {}".format(props[0]))
```

### See Also

IsCurve, IsCurveClosed, IsCurvePlanar

---

## CurveArrows

### Signature

```python
CurveArrows(curve_id, arrow_style=None)
```

### Description

Enables or disables a curve object's annotation arrows

### Returns

number: if arrow_style is not specified, the current annotation arrow style number: if arrow_style is specified, the previous arrow style

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a curve", rs.filter.curve)
if rs.CurveArrows(obj)!=3: rs.CurveArrows(obj, 3)
```

### See Also

IsCurve

---

## CurveBooleanDifference

### Signature

```python
CurveBooleanDifference(curve_id_0, curve_id_1, tolerance=None)
```

### Description

Calculates the difference between two closed, planar curves and adds the results to the document. Note, curves must be coplanar.

### Returns

list(guid, ...): The identifiers of the new objects if successful, None on error.

### Example

```python
import rhinoscriptsyntax as rs
curveA = rs.GetObject("Select first curve", rs.filter.curve)
curveB = rs.GetObject("Select second curve", rs.filter.curve)
arrResult = rs.CurveBooleanDifference(curveA, curveB)
if arrResult:
 rs.DeleteObject( curveA )
 rs.DeleteObject( curveB )
```

### See Also

CurveBooleanIntersection, CurveBooleanUnion

---

## CurveBooleanIntersection

### Signature

```python
CurveBooleanIntersection(curve_id_0, curve_id_1, tolerance=None)
```

### Description

Calculates the intersection of two closed, planar curves and adds the results to the document. Note, curves must be coplanar.

### Returns

list(guid, ...): The identifiers of the new objects.

### Example

```python
import rhinoscriptsyntax as rs
curveA = rs.GetObject("Select first curve", rs.filter.curve)
curveB = rs.GetObject("Select second curve", rs.filter.curve)
result = rs.CurveBooleanIntersection(curveA, curveB)
if result:
 rs.DeleteObject( curveA )
 rs.DeleteObject( curveB )
```

### See Also

CurveBooleanDifference, CurveBooleanUnion

---

## CurveBooleanUnion

### Signature

```python
CurveBooleanUnion(curve_id, tolerance=None)
```

### Description

Calculate the union of two or more closed, planar curves and add the results to the document. Note, curves must be coplanar.

### Returns

list(guid, ...): The identifiers of the new objects.

### Example

```python
import rhinoscriptsyntax as rs
curve_ids = rs.GetObjects("Select curves to union", rs.filter.curve)
if curve_ids and len(curve_ids)>1:
 result = rs.CurveBooleanUnion(curve_ids)
 if result: rs.DeleteObjects(curve_ids)
```

### See Also

CurveBooleanDifference, CurveBooleanIntersection

---

## CurveBrepIntersect

### Signature

```python
CurveBrepIntersect(curve_id, brep_id, tolerance=None)
```

### Description

Intersects a curve object with a brep object. Note, unlike the CurveSurfaceIntersection function, this function works on trimmed surfaces.

### Returns

list(guid, ...): identifiers for the newly created intersection objects if successful. None: on error.

### Example

```python
import rhinoscriptsyntax as rs
curve = rs.GetObject("Select a curve", rs.filter.curve)
if curve:
 brep = rs.GetObject("Select a brep", rs.filter.surface + rs.filter.polysurface)
 if brep: rs.CurveBrepIntersect( curve, brep )
```

### See Also

CurveSurfaceIntersection

---

## CurveClosestObject

### Signature

```python
CurveClosestObject(curve_id, object_ids)
```

### Description

Returns the 3D point locations on two objects where they are closest to each other. Note, this function provides similar functionality to that of Rhino's ClosestPt command.

### Returns

tuple[guid, point, point]: containing the results of the closest point calculation. The elements are as follows: [0] The identifier of the closest object. [1] The 3-D point that is closest to the closest object. [2] The 3-D point that is closest to the test curve.

### Example

```python
import rhinoscriptsyntax as rs
filter = rs.filter.curve | rs.filter.pointcloud | rs.filter.surface | rs.filter.polysurface
objects = rs.GetObjects("Select target objects for closest point", filter)
if objects:
 curve = rs.GetObject("Select curve")
 if curve:
 results = rs.CurveClosestObject(curve, objects)
 if results:
 print("Curve id: {}".format(results[0]))
 rs.AddPoint( results[1] )
 rs.AddPoint( results[2] )
```

### See Also

CurveClosestPoint, EvaluateCurve, IsCurve

---

## CurveClosestPoint

### Signature

```python
CurveClosestPoint(curve_id, test_point, segment_index=-1 )
```

### Description

Returns parameter of the point on a curve that is closest to a test point.

### Returns

number: The parameter of the closest point on the curve

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a curve")
if id:
 point = rs.GetPointOnCurve(id, "Pick a test point")
 if point:
 param = rs.CurveClosestPoint(id, point)
 print("Curve parameter: {}".format(param))
```

### See Also

EvaluateCurve, IsCurve

---

## CurveContourPoints

### Signature

```python
CurveContourPoints(curve_id, start_point, end_point, interval=None)
```

### Description

Returns the 3D point locations calculated by contouring a curve object.

### Returns

list(point, ....): A list of 3D points, one for each contour

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select curve", rs.filter.curve)
start_point = rs.GetPoint("Base point of center line")
end_point = rs.GetPoint("Endpoint of center line", start_point)
contour = rs.CurveContourPoints(obj, start_point, end_point)
if contour: rs.AddPoints(contour)
```

### See Also

AddSrfContourCrvs

---

## CurveCurvature

### Signature

```python
CurveCurvature(curve_id, parameter)
```

### Description

Returns the curvature of a curve at a parameter. See the Rhino help for details on curve curvature

### Returns

tuple[point, vector, point, number, vector]: of curvature information on success [0] = point at specified parameter [1] = tangent vector [2] = center of radius of curvature [3] = radius of curvature [4] = curvature vector None: on failure

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a curve")
if rs.IsCurve(obj):
 point = rs.GetPointOnCurve(obj, "Pick a test point")
 if point:
 param = rs.CurveClosestPoint(obj, point)
 if param:
 data = rs.CurveCurvature(obj, param)
 if data:
 print("Curve curvature evaluation at parameter {}".format(param, ":"))
 print(" 3-D Point: {}".format(data[0]))
 print(" 3-D Tangent: {}".format(data[1]))
 print(" Center of radius of curvature: {}".format(data[2]))
 print(" Radius of curvature: {}".format(data[3]))
 print(" 3-D Curvature: {}".format(data[4]))
```

### See Also

SurfaceCurvature

---

## CurveCurveIntersection

### Signature

```python
CurveCurveIntersection(curveA, curveB=None, tolerance=-1)
```

### Description

Calculates intersection of two curve objects.

### Returns

list of tuples: containing intersection information if successful. The list will contain one or more of the following elements: Element Type Description [n][0] Number The intersection event type, either Point (1) or Overlap (2). [n][1] Point3d If the event type is Point (1), then the intersection point on the first curve. If the event type is Overlap (2), then intersection start point on the first curve. [n][2] Point3d If the event type is Point (1), then the intersection point on the first curve. If the event type is Overlap (2), then intersection end point on the first curve. [n][3] Point3d If the event type is Point (1), then the intersection point on the second curve. If the event type is Overlap (2), then intersection start point on the second curve. [n][4] Point3d If the event type is Point (1), then the intersection point on the second curve. If the event type is Overlap (2), then intersection end point on the second curve. [n][5] Number If the event type is Point (1), then the first curve parameter. If the event type is Overlap (2), then the start value of the first curve parameter range. [n][6] Number If the event type is Point (1), then the first curve parameter. If the event type is Overlap (2), then the end value of the first curve parameter range. [n][7] Number If the event type is Point (1), then the second curve parameter. If the event type is Overlap (2), then the start value of the second curve parameter range. [n][8] Number If the event type is Point (1), then the second curve parameter. If the event type is Overlap (2), then the end value of the second curve parameter range.

### Example

```python
import rhinoscriptsyntax as rs
def ccx():
 curve1 = rs.GetObject("Select first curve", rs.filter.curve)
 if curve1 is None: return
 curve2 = rs.GetObject("Select second curve", rs.filter.curve)
 if curve2 is None: return
 intersection_list = rs.CurveCurveIntersection(curve1, curve2)
 if intersection_list is None:
 print("Selected curves do not intersect.")
 return
 for intersection in intersection_list:
 if intersection[0] == 1:
 print("Point")
 print("Intersection point on first curve: {}".format(intersection[1]))
 print("Intersection point on second curve: {}".format(intersection[3]))
 print("First curve parameter: {}".format(intersection[5]))
 print("Second curve parameter: {}".format(intersection[7]))
 else:
 print("Overlap")
 print("Intersection start point on first curve: {}".format(intersection[1]))
 print("Intersection end point on first curve: {}".format(intersection[2]))
 print("Intersection start point on second curve: {}".format(intersection[3]))
 print("Intersection end point on second curve: {}".format(intersection[4]))
 print("First curve parameter range: {} to {}".format(intersection[5], intersection[6]))
 print("Second curve parameter range: {} to {}".format(intersection[7], intersection[8]))
ccx()
```

### See Also

CurveSurfaceIntersection

---

## CurveDegree

### Signature

```python
CurveDegree(curve_id, segment_index=-1)
```

### Description

Returns the degree of a curve object.

### Returns

number: The degree of the curve if successful. None: on error.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a curve")
if rs.IsCurve(obj):
 degree = rs.CurveDegree(obj)
 print("Curve degree:{}".format(degree))
```

### See Also

CurveDomain, IsCurve

---

## CurveDeviation

### Signature

```python
CurveDeviation(curve_a, curve_b)
```

### Description

Returns the minimum and maximum deviation between two curve objects

### Returns

tuple[number, number, number, number, number, number]: of deviation information on success [0] = curve_a parameter at maximum overlap distance point [1] = curve_b parameter at maximum overlap distance point [2] = maximum overlap distance [3] = curve_a parameter at minimum overlap distance point [4] = curve_b parameter at minimum overlap distance point [5] = minimum distance between curves None on error

### Example

```python
import rhinoscriptsyntax as rs
curveA = rs.GetObject("Select first curve to test", rs.filter.curve)
curveB = rs.GetObject("Select second curve to test", rs.filter.curve)
deviation = rs.CurveDeviation(curveA, curveB)
if deviation:
 print("Minimum deviation = {}".format(deviation[5]))
 print("Maximum deviation = {}".format(deviation[2]))
```

### See Also

CurveArea, CurveAreaCentroid

---

## CurveDim

### Signature

```python
CurveDim(curve_id, segment_index=-1)
```

### Description

Returns the dimension of a curve object

### Returns

number: The dimension of the curve if successful. None on error.

### Example

```python
import rhinoscriptsyntax as rs
curve = rs.GetObject("Select a curve")
if rs.IsCurve(curve):
 print("Curve dimension = {}".format(rs.CurveDim(curve)))
```

### See Also

CurveDegree, CurveDomain

---

## CurveDirectionsMatch

### Signature

```python
CurveDirectionsMatch(curve_id_0, curve_id_1)
```

### Description

Tests if two curve objects are generally in the same direction or if they would be more in the same direction if one of them were flipped. When testing curve directions, both curves must be either open or closed - you cannot test one open curve and one closed curve.

### Returns

bool: True if the curve directions match, otherwise False.

### Example

```python
import rhinoscriptsyntax as rs
curve1 = rs.GetObject("Select first curve to compare", rs.filter.curve)
curve2 = rs.GetObject("Select second curve to compare", rs.filter.curve)
if rs.CurveDirectionsMatch(curve1, curve2):
 print("Curves are in the same direction")
else:
 print("Curve are not in the same direction")
```

### See Also

ReverseCurve

---

## CurveDiscontinuity

### Signature

```python
CurveDiscontinuity(curve_id, style)
```

### Description

Search for a derivatitive, tangent, or curvature discontinuity in a curve object.

### Returns

list(point, ...): 3D points where the curve is discontinuous

### Example

```python
import rhinoscriptsyntax as rs
curve = rs.GetObject("Select a curve", rs.filter.curve)
if rs.IsCurve(curve):
 points = rs.CurveDiscontinuity(curve, 2)
 if points: rs.AddPoints( points )
```

### See Also

IsCurve

---

## CurveDomain

### Signature

```python
CurveDomain(curve_id, segment_index=-1)
```

### Description

Returns the domain of a curve object as an indexable object with two elements.

### Returns

list(number, number): the domain of the curve if successful. [0] Domain minimum [1] Domain maximum None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a curve")
if rs.IsCurve(obj):
 domain = rs.CurveDomain(obj)
 print("Curve domain: {} to {}".format(domain[0], domain[1]))
```

### See Also

CurveDegree, IsCurve

---

## CurveEditPoints

### Signature

```python
CurveEditPoints(curve_id, return_parameters=False, segment_index=-1)
```

### Description

Returns the edit, or Greville, points of a curve object. For each curve control point, there is a corresponding edit point.

### Returns

list(point, ....): curve edit points on success None on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a curve")
if rs.IsCurve(obj):
 points = rs.CurveEditPoints(obj)
 if points: rs.AddPointCloud( points )
```

### See Also

IsCurve, CurvePointCount, CurvePoints

---

## CurveEndPoint

### Signature

```python
CurveEndPoint(curve_id, segment_index=-1)
```

### Description

Returns the end point of a curve object

### Returns

point: The 3d endpoint of the curve if successful. None: on error

### Example

```python
import rhinoscriptsyntax as rs
object = rs.GetObject("Select a curve")
if rs.IsCurve(object):
 point = rs.CurveEndPoint(object)
 rs.AddPoint(point)
```

### See Also

CurveMidPoint, CurveStartPoint, IsCurve

---

## CurveFilletPoints

### Signature

```python
CurveFilletPoints(curve_id_0, curve_id_1, radius=1.0, base_point_0=None, base_point_1=None, return_points=True)
```

### Description

Find points at which to cut a pair of curves so that a fillet of a specified radius fits. A fillet point is a pair of points (point0, point1) such that there is a circle of radius tangent to curve curve0 at point0 and tangent to curve curve1 at point1. Of all possible fillet points, this function returns the one which is the closest to the base point base_point_0, base_point_1. Distance from the base point is measured by the sum of arc lengths along the two curves.

### Returns

list(point, point, point, vector, vector, vector): If return_points is True, then a list of point and vector values if successful. The list elements are as follows: [0] A point on the first curve at which to cut (point). [1] A point on the second curve at which to cut (point). [2] The fillet plane's origin (point). This point is also the center point of the fillet [3] The fillet plane's X axis (vector). [4] The fillet plane's Y axis (vector). [5] The fillet plane's Z axis (vector). guid: If return_points is False, then the identifier of the fillet curve if successful. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
curve0 = rs.AddLine([0,0,0], [5,1,0])
curve1 = rs.AddLine([0,0,0], [1,5,0])
fillet = rs.CurveFilletPoints(curve0, curve1)
if fillet:
 rs.AddPoint( fillet[0] )
 rs.AddPoint( fillet[1] )
 rs.AddPoint( fillet[2] )
```

### See Also

AddFilletCurve

---

## CurveFrame

### Signature

```python
CurveFrame(curve_id, parameter, segment_index=-1)
```

### Description

Returns the plane at a parameter of a curve. The plane is based on the tangent and curvature vectors at a parameter.

### Returns

plane: The plane at the specified parameter if successful. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
curve = rs.GetCurveObject("Select a curve")
if curve:
 plane = rs.CurveFrame(curve[0], curve[4])
 rs.AddPlaneSurface(plane, 5.0, 3.0)
```

### See Also

CurvePerpFrame

---

## CurveKnotCount

### Signature

```python
CurveKnotCount(curve_id, segment_index=-1)
```

### Description

Returns the knot count of a curve object.

### Returns

number: The number of knots if successful. None: if not successful or on error.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a curve")
if rs.IsCurve(obj):
 count = rs.CurveKnotCount(obj)
 print("Curve knot count:{}".format(count))
```

### See Also

DivideCurve, IsCurve

---

## CurveKnots

### Signature

```python
CurveKnots(curve_id, segment_index=-1)
```

### Description

Returns the knots, or knot vector, of a curve object

### Returns

list(number, ....): knot values if successful. None: if not successful or on error.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a curve")
if rs.IsCurve(obj):
 knots = rs.CurveKnots(obj)
 if knots:
 for knot in knots: print("Curve knot value:{}".format(knot))
```

### See Also

CurveKnotCount, IsCurve

---

## CurveLength

** IN USE**

### Signature

```python
CurveLength(curve_id, segment_index=-1, sub_domain=None)
```

### Description

Returns the length of a curve object.

### Returns

number: The length of the curve if successful. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
object = rs.GetObject("Select a curve")
if rs.IsCurve(object):
 length = rs.CurveLength(object)
 print("Curve length:{}".format(length))
```

### See Also

CurveDomain, IsCurve

---

## CurveMidPoint

### Signature

```python
CurveMidPoint(curve_id, segment_index=-1)
```

### Description

Returns the mid point of a curve object.

### Returns

point: The 3D midpoint of the curve if successful. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
object = rs.GetObject("Select a curve")
if rs.IsCurve(object):
 point = rs.CurveMidPoint(pbject)
 rs.AddPoint( point )
```

### See Also

CurveEndPoint, CurveStartPoint, IsCurve

---

## CurveNormal

### Signature

```python
CurveNormal(curve_id, segment_index=-1)
```

### Description

Returns the normal direction of the plane in which a planar curve object lies.

### Returns

vector: The 3D normal vector if successful. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
object = rs.GetObject("Select a planar curve")
if rs.IsCurve(object) and rs.IsCurvePlanar(object):
 normal = rs.CurveNormal(object)
 if normal: print("Curve Normal:{}".format(normal))
```

### See Also

IsCurve, IsCurvePlanar

---

## CurveNormalizedParameter

### Signature

```python
CurveNormalizedParameter(curve_id, parameter)
```

### Description

Converts a curve parameter to a normalized curve parameter; one that ranges between 0-1

### Returns

number: normalized curve parameter

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select curve")
if rs.IsCurve(obj):
 domain = rs.CurveDomain(obj)
 parameter = (domain[0]+domain[1])/2.0
 print("Curve parameter:{}".format(parameter))
 normalized = rs.CurveNormalizedParameter(obj, parameter)
 print("Normalized parameter:{}".format(normalized))
```

### See Also

CurveDomain, CurveParameter

---

## CurveParameter

### Signature

```python
CurveParameter(curve_id, parameter)
```

### Description

Converts a normalized curve parameter to a curve parameter; one within the curve's domain

### Returns

number: curve parameter

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select curve")
if rs.IsCurve(obj):
 normalized = 0.5
 print("Normalized parameter:{}".format(normalized))
 parameter = rs.CurveParameter(obj, normalized)
 print("Curve parameter:{}".format(parameter))
```

### See Also

CurveDomain, CurveNormalizedParameter

---

## CurvePerpFrame

### Signature

```python
CurvePerpFrame(curve_id, parameter)
```

### Description

Returns the perpendicular plane at a parameter of a curve. The result is relatively parallel (zero-twisting) plane

### Returns

plane: Plane on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
crv = rs.GetCurveObject("Select a curve")
if crv:
 plane = rs.CurvePerpFrame(crv[0], crv[4])
 rs.AddPlaneSurface( plane, 1, 1 )
```

### See Also

CurveFrame

---

## CurvePlane

### Signature

```python
CurvePlane(curve_id, segment_index=-1)
```

### Description

Returns the plane in which a planar curve lies. Note, this function works only on planar curves.

### Returns

plane: The plane in which the curve lies if successful. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
curve = rs.GetObject("Select a curve", rs.filter.curve)
if rs.IsCurvePlanar(curve):
 plane = rs.CurvePlane(curve)
 rs.ViewCPlane(None, plane)
```

### See Also

IsCurve, IsCurvePlanar

---

## CurvePointCount

### Signature

```python
CurvePointCount(curve_id, segment_index=-1)
```

### Description

Returns the control points count of a curve object.

### Returns

number: Number of control points if successful. None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a curve")
if rs.IsCurve(obj):
 count = rs.CurvePointCount(obj)
 print("Curve point count:{}".format(count))
```

### See Also

DivideCurve, IsCurve

---

## CurvePoints

### Signature

```python
CurvePoints(curve_id, segment_index=-1)
```

### Description

Returns the control points, or control vertices, of a curve object. If the curve is a rational NURBS curve, the euclidean control vertices are returned.

### Returns

list(point, ...): the control points, or control vertices, of a curve object

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a curve")
if rs.IsCurve(obj):
 points = rs.CurvePoints(obj)
 if points: [rs.AddPoint(pt) for pt in points]
```

### See Also

CurvePointCount, IsCurve

---

## CurveRadius

### Signature

```python
CurveRadius(curve_id, test_point, segment_index=-1)
```

### Description

Returns the radius of curvature at a point on a curve.

### Returns

number: The radius of curvature at the point on the curve if successful. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a curve")
if rs.IsCurve(obj):
 point = rs.GetPointOnCurve(obj, "Pick a test point")
 if point:
 radius = rs.CurveRadius(obj, point)
 print("Radius of curvature:{}".format(radius))
```

### See Also

IsCurve

---

## CurveSeam

### Signature

```python
CurveSeam(curve_id, parameter)
```

### Description

Adjusts the seam, or start/end, point of a closed curve.

### Returns

bool: True or False indicating success or failure.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select closed curve", rs.filter.curve)
if rs.IsCurveClosed(obj):
 domain = rs.CurveDomain(obj)
 parameter = (domain[0] + domain[1])/2.0
 rs.CurveSeam( obj, parameter )
```

### See Also

IsCurve, IsCurveClosed

---

## CurveStartPoint

### Signature

```python
CurveStartPoint(curve_id, segment_index=-1, point=None)
```

### Description

Returns the start point of a curve object

### Returns

point: The 3D starting point of the curve if successful.

### Example

```python
import rhinoscriptsyntax as rs
object = rs.GetObject("Select a curve")
if rs.IsCurve(object):
 point = rs.CurveStartPoint(object)
 rs.AddPoint(point)
```

### See Also

CurveEndPoint, CurveMidPoint, IsCurve

---

## CurveSurfaceIntersection

### Signature

```python
CurveSurfaceIntersection(curve_id, surface_id, tolerance=-1, angle_tolerance=-1)
```

### Description

Calculates intersection of a curve object with a surface object. Note, this function works on the untrimmed portion of the surface.

### Returns

list(list(point, point, point, point, number, number, number, number, number, number), ...): of intersection information if successful. The list will contain one or more of the following elements: Element Type Description [n][0] Number The intersection event type, either Point(1) or Overlap(2). [n][1] Point3d If the event type is Point(1), then the intersection point on the first curve. If the event type is Overlap(2), then intersection start point on the first curve. [n][2] Point3d If the event type is Point(1), then the intersection point on the first curve. If the event type is Overlap(2), then intersection end point on the first curve. [n][3] Point3d If the event type is Point(1), then the intersection point on the second curve. If the event type is Overlap(2), then intersection start point on the surface. [n][4] Point3d If the event type is Point(1), then the intersection point on the second curve. If the event type is Overlap(2), then intersection end point on the surface. [n][5] Number If the event type is Point(1), then the first curve parameter. If the event type is Overlap(2), then the start value of the first curve parameter range. [n][6] Number If the event type is Point(1), then the first curve parameter. If the event type is Overlap(2), then the end value of the curve parameter range. [n][7] Number If the event type is Point(1), then the U surface parameter. If the event type is Overlap(2), then the U surface parameter for curve at (n, 5). [n][8] Number If the event type is Point(1), then the V surface parameter. If the event type is Overlap(2), then the V surface parameter for curve at (n, 5). [n][9] Number If the event type is Point(1), then the U surface parameter. If the event type is Overlap(2), then the U surface parameter for curve at (n, 6). [n][10] Number If the event type is Point(1), then the V surface parameter. If the event type is Overlap(2), then the V surface parameter for curve at (n, 6).

### Example

```python
import rhinoscriptsyntax as rs
def csx():
 curve = rs.GetObject("Select curve", rs.filter.curve)
 if curve is None: return
 surface = rs.GetObject("Select surface", rs.filter.surface)
 if surface is None: return
 intersection_list = rs.CurveSurfaceIntersection(curve, surface)
 if intersection_list is None:
 print("Curve and surface do not intersect.")
 return
 for intersection in intersection_list:
 if intersection[0]==1:
 print("Point")
 print("Intersection point on curve:{}".format(intersection[1]))
 print("Intersection point on surface:{}".format(intersection[3]))
 print("Curve parameter:{}".format(intersection[5]))
 print("Surface parameter: {}, {}".format(intersection[7], intersection[8]))
 else:
 print("Overlap")
 print("Intersection start point on curve:{}".format(intersection[1]))
 print("Intersection end point on curve:{}".format(intersection[2]))
 print("Intersection start point on surface:{}".format(intersection[3]))
 print("Intersection end point on surface:{}".format(intersection[4]))
 print("Curve parameter range: {} to {}".format(intersection[5], intersection[6]))
 print("Surface parameter range: {}, {} to {}, {}".format(intersection[7] intersection[8], intersection[9], intersection[10]))
csx()
```

### See Also

CurveCurveIntersection, CurveBrepIntersect

---

## CurveTangent

### Signature

```python
CurveTangent(curve_id, parameter, segment_index=-1)
```

### Description

Returns a 3D vector that is the tangent to a curve at a parameter.

### Returns

vector: A 3D vector if successful. None: on error.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a curve", rs.filter.curve)
if obj:
 point = rs.GetPointOnCurve(obj)
 if point:
 param = rs.CurveClosestPoint(obj, point)
 normal = rs.CurveTangent(obj, param)
 print(normal)
```

### See Also

CurveClosestPoint, CurveDomain

---

## CurveWeights

### Signature

```python
CurveWeights(curve_id, segment_index=-1)
```

### Description

Returns list of weights that are assigned to the control points of a curve

### Returns

number: The weight values of the curve if successful. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a curve")
if rs.IsCurve(obj):
 weights = rs.CurveWeights(obj)
 if weights:
 for weight in weights:
 print("Curve control point weight value:{}".format(weight))
```

### See Also

CurveKnots, IsCurve

---

## DivideCurve

### Signature

```python
DivideCurve(curve_id, segments, create_points=False, return_points=True)
```

### Description

Divides a curve object into a specified number of segments.

### Returns

list(point|number, ...): If `return_points` is not specified or True, then a list containing 3D division points. list(point|number, ...): If `return_points` is False, then an array containing division curve parameters. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a curve")
if obj:
 points = rs.DivideCurve(obj, 4)
 for point in points: rs.AddPoint(point)
```

### See Also

DivideCurveEquidistant, DivideCurveLength

---

## DivideCurveEquidistant

### Signature

```python
DivideCurveEquidistant(curve_id, distance, create_points=False, return_points=True)
```

### Description

Divides a curve such that the linear distance between the points is equal.

### Returns

list(point|number, ...): points or curve parameters based on the value of return_points none on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a curve", rs.filter.curve)
if obj:
 points = rs.DivideCurveEquidistant(obj, 4, True)
```

### See Also

DivideCurve, DivideCurveLength

---

## DivideCurveLength

### Signature

```python
DivideCurveLength(curve_id, length, create_points=False, return_points=True)
```

### Description

Divides a curve object into segments of a specified length.

### Returns

list(point, ...): If return_points is not specified or True, then a list containing division points. list(number, ...): If return_points is False, then an array containing division curve parameters. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a curve")
if rs.IsCurve(obj):
 length = rs.CurveLength(obj) / 4
 points = rs.DivideCurveLength(obj, length)
 for point in points: rs.AddPoint(point)
```

### See Also

DivideCurve, DivideCurveEquidistant

---

## EllipseCenterPoint

### Signature

```python
EllipseCenterPoint(curve_id)
```

### Description

Returns the center point of an elliptical-shaped curve object.

### Returns

point: The 3D center point of the ellipse if successful.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select ellipse")
if rs.IsEllipse(obj):
 point = rs.EllipseCenterPoint(obj)
 rs.AddPoint( point )
```

### See Also

IsEllipse, EllipseQuadPoints

---

## EllipseQuadPoints

### Signature

```python
EllipseQuadPoints(curve_id)
```

### Description

Returns the quadrant points of an elliptical-shaped curve object.

### Returns

list(point, point, point, point): Four points identifying the quadrants of the ellipse

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select ellipse")
if rs.IsEllipse(obj):
 rs.AddPoints( rs.EllipseQuadPoints(obj) )
```

### See Also

IsEllipse, EllipseCenterPoint

---

## EvaluateCurve

### Signature

```python
EvaluateCurve(curve_id, t, segment_index=-1)
```

### Description

Evaluates a curve at a parameter and returns a 3D point

### Returns

point: a 3-D point if successful None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a curve")
if rs.IsCurve(obj):
 domain = rs.CurveDomain(obj)
 t = domain[1]/2.0
 point = rs.EvaluateCurve(obj, t)
 rs.AddPoint( point )
```

### See Also

CurveClosestPoint, IsCurve

---

## ExplodeCurves

** IN USE**

### Signature

```python
ExplodeCurves(curve_ids, delete_input=False)
```

### Description

Explodes, or un-joins, one curves. Polycurves will be exploded into curve segments. Polylines will be exploded into line segments. ExplodeCurves will return the curves in topological order.

### Returns

list(guid, ...): identifying the newly created curve objects

### Example

```python
import rhinoscriptsyntax as rs
crv = rs.GetObject("Select curve to explode", rs.filter.curve)
if rs.IsCurve(crv): rs.ExplodeCurves(crv)
```

### See Also

IsCurve, IsPolyCurve, IsPolyline, JoinCurves

---

## ExtendCurve

### Signature

```python
ExtendCurve(curve_id, extension_type, side, boundary_object_ids)
```

### Description

Extends a non-closed curve object by a line, arc, or smooth extension until it intersects a collection of objects.

### Returns

guid: The identifier of the new object if successful. None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
filter = rs.filter.curve | rs.filter.surface | rs.filter.polysurface
objects = rs.GetObjects("Select boundary objects", filter)
if objects:
 curve = rs.GetObject("Select curve to extend", rs.filter.curve)
 if curve: rs.ExtendCurve( curve, 2, 1, objects )
```

### See Also

ExtendCurveLength, ExtendCurvePoint

---

## ExtendCurveLength

** IN USE**

### Signature

```python
ExtendCurveLength(curve_id, extension_type, side, length)
```

### Description

Extends a non-closed curve by a line, arc, or smooth extension for a specified distance

### Returns

guid: The identifier of the new object None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
curve = rs.GetObject("Select curve to extend", rs.filter.curve)
if curve:
 length = rs.GetReal("Length to extend", 3.0)
 if length: rs.ExtendCurveLength( curve, 2, 2, length )
```

### See Also

ExtendCurve, ExtendCurvePoint

---

## ExtendCurvePoint

### Signature

```python
ExtendCurvePoint(curve_id, side, point, extension_type=2)
```

### Description

Extends a non-closed curve by smooth extension to a point

### Returns

guid: The identifier of the new object if successful. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
curve = rs.GetObject("Select curve to extend", rs.filter.curve)
if curve:
 point = rs.GetPoint("Point to extend to")
 if point: rs.ExtendCurvePoint(curve, 1, point)
```

### See Also

ExtendCurve, ExtendCurveLength

---

## FairCurve

### Signature

```python
FairCurve(curve_id, tolerance=1.0)
```

### Description

Fairs a curve. Fair works best on degree 3 (cubic) curves. Fair attempts to remove large curvature variations while limiting the geometry changes to be no more than the specified tolerance. Sometimes several applications of this method are necessary to remove nasty curvature problems.

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
curves = rs.GetObjects("Select curves to fair", rs.filter.curve)
if curves:
 [rs.FairCurve(curve) for curve in curves]
```

---

## FitCurve

### Signature

```python
FitCurve(curve_id, degree=3, distance_tolerance=-1, angle_tolerance=-1)
```

### Description

Reduces number of curve control points while maintaining the curve's same general shape. Use this function for replacing curves with many control points. For more information, see the Rhino help for the FitCrv command.

### Returns

guid: The identifier of the new object None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
oldCurve = rs.GetObject("Select curve to fit", rs.filter.curve)
if oldCurve:
 newCurve = rs.FitCurve(oldCurve)
 if newCurve: rs.DeleteObject(oldCurve)
```

---

## InsertCurveKnot

### Signature

```python
InsertCurveKnot(curve_id, parameter, symmetrical=False )
```

### Description

Inserts a knot into a curve object

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select curve for knot insertion", rs.filter.curve)
if obj:
 point = rs.GetPointOnCurve(obj, "Point on curve to add knot")
 if point:
 parameter = rs.CurveClosestPoint(obj, point)
 rs.InsertCurveKnot( obj, parameter )
```

### See Also

CurveKnotCount, CurveKnots

---

## IsArc

### Signature

```python
IsArc(curve_id, segment_index=-1)
```

### Description

Verifies an object is an open arc curve

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select an arc")
if rs.IsArc(obj):
 print("The object is an arc.")
else:
 print("The object is not an arc.")
```

### See Also

AddArc3Pt, ArcAngle, ArcCenterPoint, ArcMidPoint, ArcRadius

---

## IsCircle

### Signature

```python
IsCircle(curve_id, tolerance=None)
```

### Description

Verifies an object is a circle curve

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a circle")
if rs.IsCircle(obj):
 print("The object is a circle.")
else:
 print("The object is not a circle.")
```

### See Also

AddCircle, AddCircle3Pt, CircleCenterPoint, CircleCircumference, CircleRadius

---

## IsCurve

** IN USE**

### Signature

```python
IsCurve(object_id)
```

### Description

Verifies an object is a curve

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
object = rs.GetObject("Select a curve")
if rs.IsCurve(object):
 print("The object is a curve.")
else:
 print("The object is not a curve.")
```

### See Also

IsCurveClosed, IsCurveLinear, IsCurvePeriodic, IsCurvePlanar

---

## IsCurveClosable

### Signature

```python
IsCurveClosable(curve_id, tolerance=None)
```

### Description

Decide if it makes sense to close off the curve by moving the end point to the start point based on start-end gap size and length of curve as approximated by chord defined by 6 points

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
crv = rs.GetObject("Select curve", rs.filter.curve)
if not rs.IsCurveClosed(crv) and rs.IsCurveClosable(crv):
 rs.CloseCurve( crv, 0.1 )
```

### See Also

CloseCurve, IsCurveClosed

---

## IsCurveClosed

** IN USE**

### Signature

```python
IsCurveClosed(object_id)
```

### Description

Verifies an object is a closed curve object

### Returns

bool: True if successful otherwise False. None on error

### Example

```python
import rhinoscriptsyntax as rs
object = rs.GetObject("Select a curve")
if rs.IsCurve(object):
 if rs.IsCurveClosed(oObject):
 print("The object is a closed curve.")
 else:
 print("The object is not a closed curve.")
else:
 print("The object is not a curve.")
```

### See Also

IsCurve, IsCurveLinear, IsCurvePeriodic, IsCurvePlanar

---

## IsCurveInPlane

### Signature

```python
IsCurveInPlane(object_id, plane=None)
```

### Description

Test a curve to see if it lies in a specific plane

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a curve")
if rs.IsCurve(obj) and rs.IsCurvePlanar(obj):
 if rs.IsCurveInPlane(obj):
 print("The curve lies in the current cplane.")
 else:
 print("The curve does not lie in the current cplane.")
else:
 print("The object is not a planar curve.")
```

### See Also

IsCurve, IsCurvePlanar

---

## IsCurveLinear

### Signature

```python
IsCurveLinear(object_id, segment_index=-1)
```

### Description

Verifies an object is a linear curve

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a curve")
if rs.IsCurve(id):
 if rs.IsCurveLinear(id):
 print("The object is a linear curve.")
 else:
 print("The object is not a linear curve.")
else:
 print("The object is not a curve.")
```

### See Also

IsCurve, IsCurveClosed, IsCurvePeriodic, IsCurvePlanar

---

## IsCurvePeriodic

### Signature

```python
IsCurvePeriodic(curve_id, segment_index=-1)
```

### Description

Verifies an object is a periodic curve object

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a curve")
if rs.IsCurve(obj):
 if rs.IsCurvePeriodic(obj):
 print("The object is a periodic curve.")
 else:
 print("The object is not a periodic curve.")
else:
 print("The object is not a curve.")
```

### See Also

IsCurve, IsCurveClosed, IsCurveLinear, IsCurvePlanar

---

## IsCurvePlanar

** IN USE**

### Signature

```python
IsCurvePlanar(curve_id, segment_index=-1)
```

### Description

Verifies an object is a planar curve

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a curve")
if rs.IsCurve(obj):
 if rs.IsCurvePlanar(obj):
 print("The object is a planar curve.")
 else:
 print("The object is not a planar curve.")
else:
 print("The object is not a curve.")
```

### See Also

IsCurve, IsCurveClosed, IsCurveLinear, IsCurvePeriodic

---

## IsCurveRational

### Signature

```python
IsCurveRational(curve_id, segment_index=-1)
```

### Description

Verifies an object is a rational NURBS curve

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a curve")
if rs.IsCurve(obj):
 if rs.IsCurveRational(obj):
 print("The object is a rational NURBS curve.")
 else:
 print("The object is not a rational NURBS curve.")
else:
 print("The object is not a curve.")
```

### See Also

IsCurve, IsCurveClosed, IsCurveLinear, IsCurvePeriodic

---

## IsEllipse

### Signature

```python
IsEllipse(object_id, segment_index=-1)
```

### Description

Verifies an object is an elliptical-shaped curve

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select an ellipse")
if rs.IsEllipse(obj):
 print("The object is an ellipse.")
else:
 print("The object is not an ellipse.")
```

### See Also

EllipseCenterPoint, EllipseQuadPoints

---

## IsLine

### Signature

```python
IsLine(object_id, segment_index=-1)
```

### Description

Verifies an object is a line curve

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a line")
if rs.IsLine(obj):
 print("The object is a line.")
else:
 print("The object is not a line.")
```

### See Also

AddLine

---

## IsPointOnCurve

### Signature

```python
IsPointOnCurve(object_id, point, segment_index=-1)
```

### Description

Verifies that a point is on a curve

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a curve")
if rs.IsCurve(obj):
 point = rs.GetPoint("Pick a test point")
 if point:
 if rs.IsPointOnCurve(obj, point):
 print("The point is on the curve")
 else:
 print("The point is not on the curve")
```

### See Also

IsCurve

---

## IsPolyCurve

### Signature

```python
IsPolyCurve(object_id, segment_index=-1)
```

### Description

Verifies an object is a PolyCurve curve

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a polycurve")
if rs.IsPolyCurve(obj):
 print("The object is a polycurve.")
else:
 print("The object is not a polycurve.")
```

### See Also

PolyCurveCount

---

## IsPolyline

### Signature

```python
IsPolyline( object_id, segment_index=-1 )
```

### Description

Verifies an object is a Polyline curve object

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a polyline")
if rs.IsPolyline(obj):
 print("The object is a polyline.")
else:
 print("The object is not a polyline.")
```

### See Also

IsPolyline, PolylineVertices

---

## JoinCurves

** IN USE**

### Signature

```python
JoinCurves(object_ids, delete_input=False, tolerance=None)
```

### Description

Joins multiple curves together to form one or more curves or polycurves

### Returns

list(guid, ...): Object id representing the new curves

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.GetObjects("Select curves to join", rs.filter.curve)
if objs: rs.JoinCurves(objs)
```

### See Also

ExplodeCurves, IsCurve, IsCurveClosed

---

## LineFitFromPoints

### Signature

```python
LineFitFromPoints(points)
```

### Description

Returns a line that was fit through an array of 3D points

### Returns

line: line on success

### Example

```python
import rhinoscriptsyntax as rs
points = rs.GetPoints()
if points and len(points)>1:
 line=rs.LineFitFromPoints(points)
 if line: rs.AddLine(line.From, line.To)
```

### See Also

AddLine, CurveEndPoint, CurveStartPoint

---

## MakeCurveNonPeriodic

### Signature

```python
MakeCurveNonPeriodic(curve_id, delete_input=False)
```

### Description

Makes a periodic curve non-periodic. Non-periodic curves can develop kinks when deformed

### Returns

guid: id of the new or modified curve if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
curve = rs.GetObject("Select a curve", rs.filter.curve)
if rs.IsCurvePeriodic(curve): rs.MakeCurveNonPeriodic( curve )
```

### See Also

IsCurvePeriodic

---

## MeanCurve

### Signature

```python
MeanCurve(curve0, curve1, tolerance=None)
```

### Description

Creates an average curve from two curves

### Returns

guid: id of the new or modified curve if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
curve0 = rs.GetObject("Select the first curve", rs.filter.curve)
curve1 = rs.GetObject("Select the second curve", rs.filter.curve)
rs.MeanCurve( curve0, curve1 )
```

### See Also

UnitAngleTolerance

---

## MeshPolyline

### Signature

```python
MeshPolyline(polyline_id)
```

### Description

Creates a polygon mesh object based on a closed polyline curve object. The created mesh object is added to the document

### Returns

guid: identifier of the new mesh object None: on error

### Example

```python
import rhinoscriptsyntax as rs
polyline = rs.GetObject("Select a polyline", rs.filter.curve)
if polyline:
 if rs.IsPolyline(polyline) and rs.IsCurveClosed(polyline):
 rs.MeshPolyline( polyline )
```

### See Also

IsCurveClosed, IsPolyline

---

## OffsetCurve

** IN USE**

### Signature

```python
OffsetCurve(object_id, direction, distance, normal=None, style=1)
```

### Description

Offsets a curve by a distance. The offset curve will be added to Rhino

### Returns

list(guid, ...): list of ids for the new curves on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a curve", rs.filter.curve)
if rs.IsCurve(obj):
 rs.OffsetCurve( obj, [0,0,0], 1.0 )
```

### See Also

OffsetCurveOnSurface, OffsetSurface

---

## OffsetCurveOnSurface

### Signature

```python
OffsetCurveOnSurface(curve_id, surface_id, distance_or_parameter)
```

### Description

Offset a curve on a surface. The source curve must lie on the surface. The offset curve or curves will be added to Rhino

### Returns

list(guid, ...): identifiers of the new curves if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
def TestOffset():
 curve = rs.GetObject("Select curve on a surface", rs.filter.curve)
 if curve is None: return False
 surface = rs.GetObject("Select base surface", rs.filter.surface)
 if surface is None: return False
 point = rs.GetPointOnSurface( surface, "Through point" )
 if point is None: return False
 parameter = rs.SurfaceClosestPoint(surface, point)
 rc = rs.OffsetCurveOnSurface( curve, surface, parameter )
 return rc is not None

TestOffset()
```

### See Also

OffsetCurve, OffsetSurface

---

## PlanarClosedCurveContainment

### Signature

```python
PlanarClosedCurveContainment(curve_a, curve_b, plane=None, tolerance=None)
```

### Description

Determines the relationship between the regions bounded by two coplanar simple closed curves

### Returns

number: a number identifying the relationship if successful 0 = the regions bounded by the curves are disjoint 1 = the two curves intersect 2 = the region bounded by curve_a is inside of curve_b 3 = the region bounded by curve_b is inside of curve_a None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
curve1 = rs.GetObject("Select first curve", rs.filter.curve )
curve2 = rs.GetObject("Select second curve", rs.filter.curve )
if rs.IsCurvePlanar(curve1) and rs.IsCurvePlanar(curve2):
 if rs.IsCurveClosed(curve1) and rs.IsCurveClosed(curve2):
 if rs.IsCurveInPlane(curve1) and rs.IsCurveInPlane(curve2):
 result = rs.PlanarClosedCurveContainment(curve1, curve2)
 if result==0: print("The regions bounded by the curves are disjoint.")
 elif result==1: print("The two curves intersect..")
 elif result==2: print("The region bounded by Curve1 is inside of Curve2.")
 else: print("The region bounded by Curve2 is inside of Curve1.")
```

### See Also

PlanarCurveCollision, PointInPlanarClosedCurve

---

## PlanarCurveCollision

### Signature

```python
PlanarCurveCollision(curve_a, curve_b, plane=None, tolerance=None)
```

### Description

Determines if two coplanar curves intersect

### Returns

bool: True if the curves intersect; otherwise False

### Example

```python
import rhinoscriptsyntax as rs
curve1 = rs.GetObject("Select first curve")
curve2 = rs.GetObject("Select second curve")
if( rs.IsCurvePlanar(curve1) and rs.IsCurvePlanar(curve2) and rs.IsCurveInPlane(curve1) and rs.IsCurveInPlane(curve2) ):
 if rs.PlanarCurveCollision(curve1, curve2):
 print("The coplanar curves intersect.")
 else:
 print("The coplanar curves do not intersect.")
```

### See Also

CurveCurveIntersection, PlanarClosedCurveContainment, PointInPlanarClosedCurve

---

## PointInPlanarClosedCurve

### Signature

```python
PointInPlanarClosedCurve(point, curve, plane=None, tolerance=None)
```

### Description

Determines if a point is inside of a closed curve, on a closed curve, or outside of a closed curve

### Returns

number: number identifying the result if successful 0 = point is outside of the curve 1 = point is inside of the curve 2 = point in on the curve

### Example

```python
import rhinoscriptsyntax as rs
curve = rs.GetObject("Select a planar, closed curve", rs.filter.curve)
if rs.IsCurveClosed(curve) and rs.IsCurvePlanar(curve):
 point = rs.GetPoint("Pick a point")
 if point:
 result = rs.PointInPlanarClosedCurve(point, curve)
 if result==0: print("The point is outside of the closed curve.")
 elif result==1: print("The point is inside of the closed curve.")
 else: print("The point is on the closed curve.")
```

### See Also

PlanarClosedCurveContainment, PlanarCurveCollision

---

## PolyCurveCount

### Signature

```python
PolyCurveCount(curve_id, segment_index=-1)
```

### Description

Returns the number of curve segments that make up a polycurve

### Returns

number: the number of curve segments in a polycurve if successful None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a polycurve")
if rs.IsPolyCurve(obj):
 count = rs.PolyCurveCount(obj)
 if count: print("The polycurve contains {} curves".format(count))
```

### See Also

IsPolyCurve

---

## PolylineVertices

### Signature

```python
PolylineVertices(curve_id, segment_index=-1)
```

### Description

Returns the vertices of a polyline curve on success

### Returns

list(point, ...): an list of Point3d vertex points if successful None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a polyline")
if rs.IsPolyline(obj):
 points = rs.PolylineVertices(obj)
 if points:
 for point in points: rs.AddPoint(point)
```

### See Also

AddPolyline, IsPolyline

---

## ProjectCurveToMesh

### Signature

```python
ProjectCurveToMesh(curve_ids, mesh_ids, direction)
```

### Description

Projects one or more curves onto one or more surfaces or meshes

### Returns

list(guid, ...): list of identifiers for the resulting curves.

### Example

```python
import rhinoscriptsyntax as rs
mesh = rs.GetObject("Select mesh to project onto", rs.filter.mesh)
curve= rs.GetObject("Select curve to project", rs.filter.curve)
#Project down...
results = rs.ProjectCurveToMesh(curve, mesh, (0,0,-1))
```

### See Also

ProjectCurveToSurface, ProjectPointToMesh, ProjectPointToSurface

---

## ProjectCurveToSurface

### Signature

```python
ProjectCurveToSurface(curve_ids, surface_ids, direction)
```

### Description

Projects one or more curves onto one or more surfaces or polysurfaces

### Returns

list(guid, ...): list of identifiers

### Example

```python
import rhinoscriptsyntax as rs
surface = rs.GetObject("Select surface to project onto", rs.filter.surface)
curve = rs.GetObject("Select curve to project", rs.filter.curve)
# Project down...
results = rs.ProjectCurveToSurface(curve, surface, (0,0,-1))
```

### See Also

ProjectCurveToMesh, ProjectPointToMesh, ProjectPointToSurface

---

## RebuildCurve

### Signature

```python
RebuildCurve(curve_id, degree=3, point_count=10)
```

### Description

Rebuilds a curve to a given degree and control point count. For more information, see the Rhino help for the Rebuild command.

### Returns

bool: True of False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
curve = rs.GetObject("Select curve to rebuild", rs.filter.curve)
if curve: rs.RebuildCurve(curve, 3, 10)
```

### See Also

RebuildSurface

---

## RemoveCurveKnot

### Signature

```python
RemoveCurveKnot(curve, parameter)
```

### Description

Deletes a knot from a curve object.

### Returns

bool: True of False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs

crv_info = rs.GetCurveObject("Select curve near knot to be removed")
if crv_info:
 crv_id = crv_info[0]
 crv_param = crv_info[4]
 rs.RemoveCurveKnot(crv_id, crv_param)
```

### See Also

RemoveSurfaceKnot

---

## ReverseCurve

### Signature

```python
ReverseCurve(curve_id)
```

### Description

Reverses the direction of a curve object. Same as Rhino's Dir command

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
curve = rs.GetObject("Select a curve to reverse")
if rs.IsCurve(curve): rs.ReverseCurve(curve)
```

### See Also

CurveDirectionsMatch

---

## SimplifyCurve

### Signature

```python
SimplifyCurve(curve_id, flags=0)
```

### Description

Replace a curve with a geometrically equivalent polycurve. The polycurve will have the following properties: - All the polycurve segments are lines, polylines, arcs, or NURBS curves. - The NURBS curves segments do not have fully multiple interior knots. - Rational NURBS curves do not have constant weights. - Any segment for which IsCurveLinear or IsArc is True is a line, polyline segment, or an arc. - Adjacent co-linear or co-circular segments are combined. - Segments that meet with G1-continuity have there ends tuned up so that they meet with G1-continuity to within machine precision. - If the polycurve is a polyline, a polyline will be created

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
curve = rs.GetObject("Select a curve to simplify", rs.filter.curve)
if curve: rs.SimplifyCurve(curve)
```

### See Also

IsArc, IsCurveLinear

---

## SplitCurve

### Signature

```python
SplitCurve(curve_id, parameter, delete_input=True)
```

### Description

Splits, or divides, a curve at a specified parameter. The parameter must be in the interior of the curve's domain

### Returns

list(guid, ....): list of new curves on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
curve = rs.GetObject("Select a curve to split", rs.filter.curve)
if rs.IsCurve(curve):
 domain = rs.CurveDomain(curve)
 parameter = domain[1] / 2.0
 rs.SplitCurve( curve, parameter )
```

### See Also

TrimCurve

---

## TrimCurve

### Signature

```python
TrimCurve(curve_id, interval, delete_input=True)
```

### Description

Trims a curve by removing portions of the curve outside a specified interval

### Returns

list(guid, ...): identifier of the new curve on success None: on failure

### Example

```python
import rhinoscriptsyntax as rs
curve = rs.GetObject("Select a curve to trim", rs.filter.curve)
if rs.IsCurve(curve):
 domain = rs.CurveDomain(curve)
 domain[1] /= 2.0
 rs.TrimCurve( curve, domain )
```

### See Also

SplitCurve

---

# Dimension

*39 functions | 0 in use*

---

## AddAlignedDimension

### Signature

```python
AddAlignedDimension(start_point, end_point, point_on_dimension_line, style=None)
```

### Description

Adds an aligned dimension object to the document. An aligned dimension is a linear dimension lined up with two points

### Returns

guid: identifier of new dimension on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
origin = 1, 1, 0
offset = 11, 5, 0
point = 1, 3, 0
rs.AddAlignedDimension( origin, offset, point )
```

### See Also

IsAlignedDimension

---

## AddDimStyle

### Signature

```python
AddDimStyle(dimstyle_name=None)
```

### Description

Adds a new dimension style to the document. The new dimension style will be initialized with the current default dimension style properties.

### Returns

str: name of the new dimension style on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
print("New dimension style: {}".format(rs.AddDimStyle()))
print("New dimension style: {}".format(rs.AddDimStyle("MyDimStyle")))
```

### See Also

CurrentDimStyle, DeleteDimStyle, IsDimStyle, RenameDimStyle

---

## AddLeader

### Signature

```python
AddLeader(points, view_or_plane=None, text=None)
```

### Description

Adds a leader to the document. Leader objects are planar. The 3D points passed to this function should be co-planar

### Returns

guid: identifier of the new leader on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
points = rs.GetPoints(True, False, "Select leader points")
if points: rs.AddLeader( points )
```

### See Also

IsLeader, LeaderText

---

## AddLinearDimension

### Signature

```python
AddLinearDimension(plane, start_point, end_point, point_on_dimension_line)
```

### Description

Adds a linear dimension to the document

### Returns

guid: identifier of the new object on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
points = rs.GetPoints(True, False, "Select 3 dimension points")
if points and len(points)>2:
 rs.AddLinearDimension(rs.WorldXYPlane(), points[0], points[1], points[2] )
```

### See Also

IsLeader, LeaderText

---

## CurrentDimStyle

### Signature

```python
CurrentDimStyle(dimstyle_name=None)
```

### Description

Returns or changes the current default dimension style

### Returns

str: if dimstyle_name is not specified, name of the current dimension style str: if dimstyle_name is specified, name of the previous dimension style None: on error

### Example

```python
import rhinoscriptsyntax as rs
rs.AddDimStyle("MyDimStyle")
rs.CurrentDimStyle("MyDimStyle")
```

### See Also

AddDimStyle, DeleteDimStyle, IsDimStyle, RenameDimStyle

---

## DeleteDimStyle

### Signature

```python
DeleteDimStyle(dimstyle_name)
```

### Description

Removes an existing dimension style from the document. The dimension style to be removed cannot be referenced by any dimension objects.

### Returns

str: The name of the deleted dimension style if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
dimstyle = rs.GetString("Dimension style to remove")
if dimstyle: rs.DeleteDimStyle(dimstyle)
```

### See Also

AddDimStyle, CurrentDimStyle, IsDimStyle, RenameDimStyle

---

## DimStyleAnglePrecision

### Signature

```python
DimStyleAnglePrecision(dimstyle, precision=None)
```

### Description

Returns or changes the angle display precision of a dimension style

### Returns

number: If a precision is not specified, the current angle precision number: If a precision is specified, the previous angle precision

### Example

```python
import rhinoscriptsyntax as rs
dimstyle = rs.CurrentDimStyle()
precision = rs.DimStyleAnglePrecision(dimstyle)
if precision>2:
 rs.DimStyleAnglePrecision( dimstyle, 2 )
```

### See Also

DimStyleArrowSize, DimStyleExtension, DimStyleFont, DimStyleLinearPrecision, DimStyleNumberFormat, DimStyleOffset, DimStyleTextAlignment, DimStyleTextHeight

---

## DimStyleArrowSize

### Signature

```python
DimStyleArrowSize(dimstyle, size=None)
```

### Description

Returns or changes the arrow size of a dimension style

### Returns

number: If size is not specified, the current arrow size number: If size is specified, the previous arrow size None: on error

### Example

```python
import rhinoscriptsyntax as rs
dimstyle = rs.CurrentDimStyle()
size = rs.DimStyleArrowSize(dimstyle)
if size>1.0: rs.DimStyleArrowSize( dimstyle, 1.0 )
```

### See Also

DimStyleAnglePrecision, DimStyleExtension, DimStyleFont, DimStyleLinearPrecision, DimStyleNumberFormat, DimStyleOffset, DimStyleTextAlignment, DimStyleTextHeight

---

## DimStyleCount

### Signature

```python
DimStyleCount()
```

### Description

Returns the number of dimension styles in the document

### Returns

number: the number of dimension styles in the document

### Example

```python
import rhinoscriptsyntax as rs
count = rs.DimStyleCount()
print("There are", count, "dimension styles.")
```

### See Also

DimStyleNames, IsDimStyle

---

## DimStyleExtension

### Signature

```python
DimStyleExtension(dimstyle, extension=None)
```

### Description

Returns or changes the extension line extension of a dimension style

### Returns

number: if extension is not specified, the current extension line extension number: if extension is specified, the previous extension line extension None: on error

### Example

```python
import rhinoscriptsyntax as rs
dimstyle = rs.CurrentDimStyle()
extension = rs.DimStyleExtension(dimstyle)
if extension>0.5: rs.DimStyleExtension( dimstyle, 0.5 )
```

### See Also

DimStyleAnglePrecision, DimStyleArrowSize, DimStyleFont, DimStyleLinearPrecision, DimStyleNumberFormat, DimStyleOffset, DimStyleTextAlignment, DimStyleTextHeight

---

## DimStyleFont

### Signature

```python
DimStyleFont(dimstyle, font=None)
```

### Description

Returns or changes the font used by a dimension style

### Returns

str: if font is not specified, the current font if successful str: if font is specified, the previous font if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
dimstyle = rs.CurrentDimStyle()
font = rs.DimStyleFont(dimstyle)
if font!="Arial": rs.DimStyleFont( dimstyle, "Arial" )
```

### See Also

DimStyleAnglePrecision, DimStyleArrowSize, DimStyleExtension, DimStyleLinearPrecision, DimStyleNumberFormat, DimStyleOffset, DimStyleTextAlignment, DimStyleTextHeight

---

## DimStyleLeaderArrowSize

### Signature

```python
DimStyleLeaderArrowSize(dimstyle, size=None)
```

### Description

Returns or changes the leader arrow size of a dimension style

### Returns

number: if size is not specified, the current leader arrow size number: if size is specified, the previous leader arrow size None: on error

### Example

```python
import rhinoscriptsyntax as rs
dimstyle = rs.CurrentDimStyle()
size = rs.DimStyleLeaderArrowSize(dimstyle)
if size>1.0: rs.DimStyleLeaderArrowSize( dimstyle, 1.0 )
```

### See Also

DimStyleAnglePrecision, DimStyleArrowSize, DimStyleExtension, DimStyleFont, DimStyleLinearPrecision, DimStyleNumberFormat, DimStyleOffset, DimStyleTextAlignment, DimStyleTextHeight

---

## DimStyleLengthFactor

### Signature

```python
DimStyleLengthFactor(dimstyle, factor=None)
```

### Description

Returns or changes the length factor of a dimension style. Length factor is the conversion between Rhino units and dimension units

### Returns

number: if factor is not defined, the current length factor number: if factor is defined, the previous length factor None: on error

### Example

```python
import rhinoscriptsyntax as rs
dimstyle = rs.CurrentDimStyle()
factor = rs.DimStyleLengthFactor(dimstyle)
if factor>1.0: rs.DimStyleLengthFactor( dimstyle, 1.0 )
```

### See Also

DimStylePrefix, DimStyleSuffix

---

## DimStyleLinearPrecision

### Signature

```python
DimStyleLinearPrecision(dimstyle, precision=None)
```

### Description

Returns or changes the linear display precision of a dimension style

### Returns

number: if precision is not specified, the current linear precision value number: if precision is specified, the previous linear precision value None: on error

### Example

```python
import rhinoscriptsyntax as rs
dimstyle = rs.CurrentDimStyle()
precision = rs.DimStyleLinearPrecision(dimstyle)
if precision>2: rs.DimStyleLinearPrecision( dimstyle, 2 )
```

### See Also

DimStyleAnglePrecision, DimStyleArrowSize, DimStyleExtension, DimStyleFont, DimStyleNumberFormat, DimStyleOffset, DimStyleTextAlignment, DimStyleTextHeight

---

## DimStyleNames

### Signature

```python
DimStyleNames(sort=False)
```

### Description

Returns the names of all dimension styles in the document

### Returns

list(str, ...): the names of all dimension styles in the document

### Example

```python
import rhinoscriptsyntax as rs
dimstyles = rs.DimStyleNames()
if dimstyles:
 for dimstyle in dimstyles: print(dimstyle)
```

### See Also

DimStyleCount, IsDimStyle

---

## DimStyleNumberFormat

### Signature

```python
DimStyleNumberFormat(dimstyle, format=None)
```

### Description

Returns or changes the number display format of a dimension style

### Returns

number: if format is not specified, the current display format number: if format is specified, the previous display format None: on error

### Example

```python
import rhinoscriptsyntax as rs
dimstyle = rs.CurrentDimStyle()
format = rs.DimStyleNumberFormat(dimstyle)
if format>0: rs.DimStyleNumberFormat( dimstyle, 0 )
```

### See Also

DimStyleAnglePrecision, DimStyleArrowSize, DimStyleExtension, DimStyleFont, DimStyleLinearPrecision, DimStyleOffset, DimStyleTextAlignment, DimStyleTextHeight

---

## DimStyleOffset

### Signature

```python
DimStyleOffset(dimstyle, offset=None)
```

### Description

Returns or changes the extension line offset of a dimension style

### Returns

number: if offset is not specified, the current extension line offset number: if offset is specified, the previous extension line offset None: on error

### Example

```python
import rhinoscriptsyntax as rs
dimstyle = rs.CurrentDimStyle()
offset = rs.DimStyleOffset(dimstyle)
if offset>0.5: rs.DimStyleOffset( dimstyle, 0.5 )
```

### See Also

DimStyleAnglePrecision, DimStyleArrowSize, DimStyleExtension, DimStyleFont, DimStyleLinearPrecision, DimStyleNumberFormat, DimStyleTextAlignment, DimStyleTextHeight

---

## DimStylePrefix

### Signature

```python
DimStylePrefix(dimstyle, prefix=None)
```

### Description

Returns or changes the prefix of a dimension style - the text to prefix to the dimension text.

### Returns

str: if prefix is not specified, the current prefix str: if prefix is specified, the previous prefix None: on error

### Example

```python
import rhinoscriptsyntax as rs
dimstyle = rs.CurrentDimStyle()
rs.DimStylePrefix( dimstyle, "[" )
```

### See Also

DimStyleLengthFactor, DimStyleSuffix

---

## DimStyleScale

### Signature

```python
DimStyleScale(dimstyle, scale=None)
```

### Description

Returns or modifies the scale of a dimension style.

### Returns

number: if scale is not specified, the current scale number: if scale is specified, the previous scale None: on error

### Example

```python
import rhinoscriptsyntax as rs
from scriptcontext import doc
dimstyle = doc.DimStyles.Current
scale = rs.DimStyleScale(dimstyle)
rs.DimStyleScale(dimstyle, scale*2.0)
```

### See Also

DimStyleTextHeight, DimStyleOffset

---

## DimStyleSuffix

### Signature

```python
DimStyleSuffix(dimstyle, suffix=None)
```

### Description

Returns or changes the suffix of a dimension style - the text to append to the dimension text.

### Returns

str: if suffix is not specified, the current suffix str: if suffix is specified, the previous suffix None: on error

### Example

```python
import rhinoscriptsyntax as rs
dimstyle = rs.CurrentDimStyle()
rs.DimStyleSuffix( dimstyle, "}" )
```

### See Also

DimStyleLengthFactor, DimStylePrefix

---

## DimStyleTextAlignment

### Signature

```python
DimStyleTextAlignment(dimstyle, alignment=None)
```

### Description

Returns or changes the text alignment mode of a dimension style

### Returns

number: if alignment is not specified, the current text alignment number: if alignment is specified, the previous text alignment None: on error

### Example

```python
import rhinoscriptsyntax as rs
dimstyle = rs.CurrentDimStyle()
alignment = rs.DimStyleTextAlignment(dimstyle)
if alignment!=2: rs.DimStyleTextAlignment( dimstyle, 2 )
```

### See Also

DimStyleAnglePrecision, DimStyleArrowSize, DimStyleExtension, DimStyleFont, DimStyleLinearPrecision, DimStyleNumberFormat, DimStyleOffset, DimStyleTextHeight

---

## DimStyleTextGap

### Signature

```python
DimStyleTextGap(dimstyle, gap=None)
```

### Description

Returns or changes the text gap used by a dimension style

### Returns

number: if gap is not specified, the current text gap number: if gap is specified, the previous text gap None: on error

### Example

```python
import rhinoscriptsyntax as rs
dimstyle = rs.CurrentDimStyle()
gap = rs.DimStyleTextGap(dimstyle)
if gap>0.25: rs.DimStyleTextGap( dimstyle, 0.25 )
```

### See Also

DimStyleAnglePrecision, DimStyleArrowSize, DimStyleExtension, DimStyleFont, DimStyleLinearPrecision, DimStyleNumberFormat, DimStyleOffset, DimStyleTextAlignment, DimStyleTextHeight

---

## DimStyleTextHeight

### Signature

```python
DimStyleTextHeight(dimstyle, height=None)
```

### Description

Returns or changes the text height used by a dimension style

### Returns

number: if height is not specified, the current text height number: if height is specified, the previous text height None: on error

### Example

```python
import rhinoscriptsyntax as rs
dimstyle = rs.CurrentDimStyle()
height = rs.DimStyleTextHeight(dimstyle)
if offset>1.0: rs.DimStyleTextHeight( dimstyle, 1.0 )
```

### See Also

DimStyleAnglePrecision, DimStyleArrowSize, DimStyleExtension, DimStyleFont, DimStyleLinearPrecision, DimStyleNumberFormat, DimStyleOffset, DimStyleTextAlignment

---

## DimensionStyle

### Signature

```python
DimensionStyle(object_id, dimstyle_name=None)
```

### Description

Returns or modifies the dimension style of a dimension object

### Returns

str: if dimstyle_name is not specified, the object's current dimension style name str: if dimstyle_name is specified, the object's previous dimension style name None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a dimension")
if rs.IsDimension(obj): rs.DimensionStyle(obj, "Default")
```

### See Also

DimStyleNames, IsDimStyle

---

## DimensionText

### Signature

```python
DimensionText(object_id)
```

### Description

Returns the text displayed by a dimension object

### Returns

str: the text displayed by a dimension object

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a dimension")
if rs.IsDimension(obj):
 print(rs.DimensionText(obj))
```

### See Also

DimensionUserText, DimensionValue, IsDimension

---

## DimensionUserText

### Signature

```python
DimensionUserText(object_id, usertext=None)
```

### Description

Returns of modifies the user text string of a dimension object. The user text is the string that gets printed when the dimension is defined

### Returns

str: if usertext is not specified, the current usertext string str: if usertext is specified, the previous usertext string

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a dimension")
if rs.IsDimension(obj):
 usertext = "!= " + chr(177) + str(rs.UnitAbsoluteTolerance())
 rs.DimensionUserText( obj, usertext )
```

### See Also

DimensionText, DimensionValue, IsDimension

---

## DimensionValue

### Signature

```python
DimensionValue(object_id)
```

### Description

Returns the value of a dimension object

### Returns

number: numeric value of the dimension if successful

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a dimension")
if rs.IsDimension(obj):
 print(rs.DimensionValue(obj))
```

### See Also

DimensionText, DimensionUserText, IsDimension

---

## IsAlignedDimension

### Signature

```python
IsAlignedDimension(object_id)
```

### Description

Verifies an object is an aligned dimension object

### Returns

bool: True or False. None on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a dimension")
if rs.IsAlignedDimension(obj):
 print("The object is an aligned dimension.")
else:
 print("The object is not an aligned dimension.")
```

### See Also

IsAngularDimension, IsDiameterDimension, IsDimension, IsLinearDimension, IsOrdinateDimension, IsRadialDimension

---

## IsAngularDimension

### Signature

```python
IsAngularDimension(object_id)
```

### Description

Verifies an object is an angular dimension object

### Returns

bool: True or False. None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a dimension")
if rs.IsAngularDimension(obj):
 print("The object is an angular dimension.")
else:
 print("The object is not an angular dimension.")
```

### See Also

IsAlignedDimension, IsDiameterDimension, IsDimension, IsLinearDimension, IsOrdinateDimension, IsRadialDimension

---

## IsDiameterDimension

### Signature

```python
IsDiameterDimension(object_id)
```

### Description

Verifies an object is a diameter dimension object

### Returns

bool: True or False. None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a dimension")
if rs.IsDiameterDimension(obj):
 print("The object is a diameter dimension.")
else:
 print("The object is not a diameter dimension.")
```

### See Also

IsAlignedDimension, IsAngularDimension, IsDimension, IsLinearDimension, IsOrdinateDimension, IsRadialDimension

---

## IsDimStyle

### Signature

```python
IsDimStyle(dimstyle)
```

### Description

Verifies the existance of a dimension style in the document

### Returns

bool: True or False. None: on error

### Example

```python
import rhinoscriptsyntax as rs
dimstyle = rs.GetString("Dimension style to test")
if rs.IsDimStyle(dimstyle):
 if rs.IsDimStyleReference(dimstyle):
 print("The dimension style is from a reference file.")
 else:
 print("The dimension style is not from a reference file.")
else:
 print("The dimension style does not exist.")
```

### See Also

IsDimStyleReference

---

## IsDimStyleReference

### Signature

```python
IsDimStyleReference(dimstyle)
```

### Description

Verifies that an existing dimension style is from a reference file

### Returns

bool: True or False. None: on error

### Example

```python
import rhinoscriptsyntax as rs
dimstyle = rs.GetString("Dimension style to test")
if rs.IsDimStyle(dimstyle):
 if rs.IsDimStyleReference(dimstyle):
 print("The dimension style is from a reference file.")
 else:
 print("The dimension style is not from a reference file.")
else:
 print("The dimension style does not exist.")
```

### See Also

IsDimStyle

---

## IsDimension

### Signature

```python
IsDimension(object_id)
```

### Description

Verifies an object is a dimension object

### Returns

bool: True or False. None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a dimension")
if rs.IsDimension(obj):
 print("The object is a dimension.")
else:
 print("The object is not a dimension.")
```

### See Also

IsAlignedDimension, IsAngularDimension, IsDiameterDimension, IsLinearDimension, IsOrdinateDimension, IsRadialDimension

---

## IsLeader

### Signature

```python
IsLeader(object_id)
```

### Description

Verifies an object is a dimension leader object

### Returns

bool: True or False. None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a leader")
if rs.IsLeader(obj):
 print("The object is a leader.")
else:
 print("The object is not a leader.")
```

### See Also

AddLeader, LeaderText

---

## IsLinearDimension

### Signature

```python
IsLinearDimension(object_id)
```

### Description

Verifies an object is a linear dimension object

### Returns

bool: True or False. None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a dimension")
if rs.IsLinearDimension(obj):
 print("The object is a linear dimension.")
else:
 print("The object is not a linear dimension.")
```

### See Also

IsAlignedDimension, IsAngularDimension, IsDiameterDimension, IsDimension, IsOrdinateDimension, IsRadialDimension

---

## IsOrdinateDimension

### Signature

```python
IsOrdinateDimension(object_id)
```

### Description

Verifies an object is an ordinate dimension object

### Returns

bool: True or False. None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a dimension")
if rs.IsOrdinateDimension(obj):
 print("The object is an ordinate dimension.")
else:
 print("The object is not an ordinate dimension.")
```

### See Also

IsAlignedDimension, IsAngularDimension, IsDiameterDimension, IsDimension, IsLinearDimension, IsRadialDimension

---

## IsRadialDimension

### Signature

```python
IsRadialDimension(object_id)
```

### Description

Verifies an object is a radial dimension object

### Returns

bool: True or False. None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a dimension")
if rs.IsRadialDimension(obj):
 print("The object is a radial dimension.")
else:
 print("The object is not a radial dimension.")
```

### See Also

IsAlignedDimension, IsAngularDimension, IsDiameterDimension, IsDimension, IsLinearDimension, IsOrdinateDimension

---

## LeaderText

### Signature

```python
LeaderText(object_id, text=None)
```

### Description

Returns or modifies the text string of a dimension leader object

### Returns

str: if text is not specified, the current text string str: if text is specified, the previous text string None on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a leader")
if rs.IsLeader(obj): print(rs.LeaderText(obj))
```

### See Also

AddLeader, IsLeader

---

## RenameDimStyle

### Signature

```python
RenameDimStyle(oldstyle, newstyle)
```

### Description

Renames an existing dimension style

### Returns

str: the new dimension style name if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
oldstyle = rs.GetString("Old dimension style name")
if oldstyle:
 newstyle = rs.GetString("New dimension style name")
 if newstyle: rs.RenameDimStyle( oldstyle, newstyle )
```

### See Also

AddDimStyle, CurrentDimStyle, DeleteDimStyle, IsDimStyle

---

# Document

*30 functions | 2 in use*

---

## CreatePreviewImage

### Signature

```python
CreatePreviewImage(filename, view=None, size=None, flags=0, wireframe=False)
```

### Description

Create a bitmap preview image of the current model

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
result = rs.CreatePreviewImage("test.jpg")
if result:
 print( "test.jpg created successfully.")
else:
 print( "Unable to create preview image.")
```

### See Also

ExtractPreviewImage

---

## DocumentModified

### Signature

```python
DocumentModified(modified=None)
```

### Description

Returns or sets the document's modified flag. This flag indicates whether or not any changes to the current document have been made. NOTE: setting the document modified flag to False will prevent the "Do you want to save this file..." from displaying when you close Rhino.

### Returns

bool: if no modified state is specified, the current modified state bool: if a modified state is specified, the previous modified state

### Example

```python
import rhinoscriptsyntax as rs
modified = rs.IsDocumentModified()
if not modified: rs.DocumentModified(True)
```

### See Also

IsDocumentModified

---

## DocumentName

### Signature

```python
DocumentName()
```

### Description

Returns the name of the currently loaded Rhino document (3DM file)

### Returns

str: the name of the currently loaded Rhino document (3DM file)

### Example

```python
import rhinoscriptsyntax as rs
name = rs.DocumentName()
print(name)
```

### See Also

DocumentPath

---

## DocumentPath

### Signature

```python
DocumentPath()
```

### Description

Returns path of the currently loaded Rhino document (3DM file)

### Returns

str: the path of the currently loaded Rhino document (3DM file)

### Example

```python
import rhinoscriptsyntax as rs
path = rs.DocumentPath()
print(path)
```

### See Also

DocumentName

---

## EnableRedraw

### Signature

```python
EnableRedraw(enable=True)
```

### Description

Enables or disables screen redrawing

### Returns

bool: previous screen redrawing state

### Example

```python
import rhinoscriptsyntax as rs
redraw = rs.EnableRedraw(True)
```

### See Also

Redraw

---

## ExtractPreviewImage

### Signature

```python
ExtractPreviewImage(filename, modelname=None)
```

### Description

Extracts the bitmap preview image from the specified model (.3dm)

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
result = rs.ExtractPreviewImage("test.jpg")
if result:
 print("Test.jpg created successfully.")
else:
 print("Unable to extract preview image.")
```

### See Also

CreatePreviewImage

---

## IsDocumentModified

### Signature

```python
IsDocumentModified()
```

### Description

Verifies that the current document has been modified in some way

### Returns

bool: True or False. None on error

### Example

```python
import rhinoscriptsyntax as rs
modified = rs.IsDocumentModified()
if not modified: rs.DocumentModified(True)
```

### See Also

DocumentModified

---

## Notes

### Signature

```python
Notes(newnotes=None)
```

### Description

Returns or sets the document's notes. Notes are generally created using Rhino's Notes command

### Returns

str: if `newnotes` is omitted, the current notes if successful str: if `newnotes` is specified, the previous notes if successful

### Example

```python
import rhinoscriptsyntax as rs
notes = rs.Notes()
if notes: rs.MessageBox(notes)
```

---

## ReadFileVersion

### Signature

```python
ReadFileVersion()
```

### Description

Returns the file version of the current document. Use this function to determine which version of Rhino last saved the document. Note, this function will not return values from referenced or merged files.

### Returns

str: the file version of the current document

### Example

```python
import rhinoscriptsyntax as rs
print("ReadFileVersion = {}".format(rs.ReadFileVersion()))
```

### See Also

DocumentName, DocumentPath

---

## Redraw

** IN USE**

### Signature

```python
Redraw()
```

### Description

Redraws all views

### Returns

None

### Example

```python
import rhinoscriptsyntax as rs
rs.Redraw()
```

### See Also

EnableRedraw

---

## RenderAntialias

### Signature

```python
RenderAntialias(style=None)
```

### Description

Returns or sets render antialiasing style

### Returns

number: if style is not specified, the current antialiasing style number: if style is specified, the previous antialiasing style

### Example

```python
import rhinoscriptsyntax as rs
rs.RenderAntialias(1)
```

### See Also

RenderColor, RenderResolution, RenderSettings

---

## RenderColor

### Signature

```python
RenderColor(item, color=None)
```

### Description

Returns or sets the render ambient light or background color

### Returns

color: if color is not specified, the current item color color: if color is specified, the previous item color

### Example

```python
import rhinoscriptsyntax as rs
render_background_color = 1
rs.RenderColor( render_background_color, (0,0,255) )
```

### See Also

RenderAntialias, RenderResolution, RenderSettings

---

## RenderMeshDensity

### Signature

```python
RenderMeshDensity(density=None)
```

### Description

Returns or sets the render mesh density property of the active document. For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

### Returns

number: if density is not specified, the current render mesh density if successful. number: if density is specified, the previous render mesh density if successful.

### Example

```python
import rhinoscriptsyntax as rs
print("Quality: %s" % rs.RenderMeshQuality())
print("Mesh density: %s" % rs.RenderMeshDensity())
print("Maximum angle: %s" % rs.RenderMeshMaxAngle())
print("Maximum aspect ratio: %s" % rs.RenderMeshMaxAspectRatio())
print("Minimun edge length: %s" % rs.RenderMeshMinEdgeLength())
print("Maximum edge length: %s" % rs.RenderMeshMaxEdgeLength())
print("Maximum distance, edge to surface: %s" % rs.RenderMeshMaxDistEdgeToSrf())
print("Minumum initial grid quads: %s" % rs.RenderMeshMinInitialGridQuads())
print("Other settings: %s" % rs.RenderMeshSettings())
```

### See Also

RenderMeshDensity, RenderMeshMaxAngle, RenderMeshMaxAspectRatio, RenderMeshMaxDistEdgeToSrf, RenderMeshMaxEdgeLength, RenderMeshMinEdgeLength, RenderMeshMinInitialGridQuads, RenderMeshQuality, RenderMeshSettings

---

## RenderMeshMaxAngle

### Signature

```python
RenderMeshMaxAngle(angle_degrees=None)
```

### Description

Returns or sets the render mesh maximum angle property of the active document. For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

### Returns

number: if angle_degrees is not specified, the current maximum angle if successful. number: if angle_degrees is specified, the previous maximum angle if successful. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
print("Quality: %s" % rs.RenderMeshQuality())
print("Mesh density: %s" % rs.RenderMeshDensity())
print("Maximum angle: %s" % rs.RenderMeshMaxAngle())
print("Maximum aspect ratio: %s" % rs.RenderMeshMaxAspectRatio())
print("Minimun edge length: %s" % rs.RenderMeshMinEdgeLength())
print("Maximum edge length: %s" % rs.RenderMeshMaxEdgeLength())
print("Maximum distance, edge to surface: %s" % rs.RenderMeshMaxDistEdgeToSrf())
print("Minumum initial grid quads: %s" % rs.RenderMeshMinInitialGridQuads())
print("Other settings: %s" % rs.RenderMeshSettings())
```

### See Also

RenderMeshDensity, RenderMeshMaxAngle, RenderMeshMaxAspectRatio, RenderMeshMaxDistEdgeToSrf, RenderMeshMaxEdgeLength, RenderMeshMinEdgeLength, RenderMeshMinInitialGridQuads, RenderMeshQuality, RenderMeshSettings

---

## RenderMeshMaxAspectRatio

### Signature

```python
RenderMeshMaxAspectRatio(ratio=None)
```

### Description

Returns or sets the render mesh maximum aspect ratio property of the active document. For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

### Returns

number: if ratio is not specified, the current render mesh maximum aspect ratio if successful. number: if ratio is specified, the previous render mesh maximum aspect ratio if successful. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
print("Quality: %s" % rs.RenderMeshQuality())
print("Mesh density: %s" % rs.RenderMeshDensity())
print("Maximum angle: %s" % rs.RenderMeshMaxAngle())
print("Maximum aspect ratio: %s" % rs.RenderMeshMaxAspectRatio())
print("Minimun edge length: %s" % rs.RenderMeshMinEdgeLength())
print("Maximum edge length: %s" % rs.RenderMeshMaxEdgeLength())
print("Maximum distance, edge to surface: %s" % rs.RenderMeshMaxDistEdgeToSrf())
print("Minumum initial grid quads: %s" % rs.RenderMeshMinInitialGridQuads())
print("Other settings: %s" % rs.RenderMeshSettings())
```

### See Also

RenderMeshDensity, RenderMeshMaxAngle, RenderMeshMaxAspectRatio, RenderMeshMaxDistEdgeToSrf, RenderMeshMaxEdgeLength, RenderMeshMinEdgeLength, RenderMeshMinInitialGridQuads, RenderMeshQuality, RenderMeshSettings

---

## RenderMeshMaxDistEdgeToSrf

### Signature

```python
RenderMeshMaxDistEdgeToSrf(distance=None)
```

### Description

Returns or sets the render mesh maximum distance, edge to surface parameter of the active document. For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

### Returns

number: if distance is not specified, the current render mesh maximum distance, edge to surface if successful. number: if distance is specified, the previous render mesh maximum distance, edge to surface if successful. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
print("Quality: %s" % rs.RenderMeshQuality())
print("Mesh density: %s" % rs.RenderMeshDensity())
print("Maximum angle: %s" % rs.RenderMeshMaxAngle())
print("Maximum aspect ratio: %s" % rs.RenderMeshMaxAspectRatio())
print("Minimun edge length: %s" % rs.RenderMeshMinEdgeLength())
print("Maximum edge length: %s" % rs.RenderMeshMaxEdgeLength())
print("Maximum distance, edge to surface: %s" % rs.RenderMeshMaxDistEdgeToSrf())
print("Minumum initial grid quads: %s" % rs.RenderMeshMinInitialGridQuads())
print("Other settings: %s" % rs.RenderMeshSettings())
```

### See Also

RenderMeshDensity, RenderMeshMaxAngle, RenderMeshMaxAspectRatio, RenderMeshMaxDistEdgeToSrf, RenderMeshMaxEdgeLength, RenderMeshMinEdgeLength, RenderMeshMinInitialGridQuads, RenderMeshQuality, RenderMeshSettings

---

## RenderMeshMaxEdgeLength

### Signature

```python
RenderMeshMaxEdgeLength(distance=None)
```

### Description

Returns or sets the render mesh maximum edge length parameter of the active document. For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

### Returns

number: if distance is not specified, the current render mesh maximum edge length if successful. number: if distance is specified, the previous render mesh maximum edge length if successful. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
print("Quality: %s" % rs.RenderMeshQuality())
print("Mesh density: %s" % rs.RenderMeshDensity())
print("Maximum angle: %s" % rs.RenderMeshMaxAngle())
print("Maximum aspect ratio: %s" % rs.RenderMeshMaxAspectRatio())
print("Minimun edge length: %s" % rs.RenderMeshMinEdgeLength())
print("Maximum edge length: %s" % rs.RenderMeshMaxEdgeLength())
print("Maximum distance, edge to surface: %s" % rs.RenderMeshMaxDistEdgeToSrf())
print("Minumum initial grid quads: %s" % rs.RenderMeshMinInitialGridQuads())
print("Other settings: %s" % rs.RenderMeshSettings())
```

### See Also

RenderMeshDensity, RenderMeshMaxAngle, RenderMeshMaxAspectRatio, RenderMeshMaxDistEdgeToSrf, RenderMeshMaxEdgeLength, RenderMeshMinEdgeLength, RenderMeshMinInitialGridQuads, RenderMeshQuality, RenderMeshSettings

---

## RenderMeshMinEdgeLength

### Signature

```python
RenderMeshMinEdgeLength(distance=None)
```

### Description

Returns or sets the render mesh minimum edge length parameter of the active document. For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

### Returns

number: if distance is not specified, the current render mesh minimum edge length if successful. number: if distance is specified, the previous render mesh minimum edge length if successful. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
print("Quality: %s" % rs.RenderMeshQuality())
print("Mesh density: %s" % rs.RenderMeshDensity())
print("Maximum angle: %s" % rs.RenderMeshMaxAngle())
print("Maximum aspect ratio: %s" % rs.RenderMeshMaxAspectRatio())
print("Minimun edge length: %s" % rs.RenderMeshMinEdgeLength())
print("Maximum edge length: %s" % rs.RenderMeshMaxEdgeLength())
print("Maximum distance, edge to surface: %s" % rs.RenderMeshMaxDistEdgeToSrf())
print("Minumum initial grid quads: %s" % rs.RenderMeshMinInitialGridQuads())
print("Other settings: %s" % rs.RenderMeshSettings())
```

### See Also

RenderMeshDensity, RenderMeshMaxAngle, RenderMeshMaxAspectRatio, RenderMeshMaxDistEdgeToSrf, RenderMeshMaxEdgeLength, RenderMeshMinEdgeLength, RenderMeshMinInitialGridQuads, RenderMeshQuality, RenderMeshSettings

---

## RenderMeshMinInitialGridQuads

### Signature

```python
RenderMeshMinInitialGridQuads(quads=None)
```

### Description

Returns or sets the render mesh minimum initial grid quads parameter of the active document. For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

### Returns

number: if quads is not specified, the current render mesh minimum initial grid quads if successful. number: if quads is specified, the previous render mesh minimum initial grid quads if successful. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
print("Quality: %s" % rs.RenderMeshQuality())
print("Mesh density: %s" % rs.RenderMeshDensity())
print("Maximum angle: %s" % rs.RenderMeshMaxAngle())
print("Maximum aspect ratio: %s" % rs.RenderMeshMaxAspectRatio())
print("Minimun edge length: %s" % rs.RenderMeshMinEdgeLength())
print("Maximum edge length: %s" % rs.RenderMeshMaxEdgeLength())
print("Maximum distance, edge to surface: %s" % rs.RenderMeshMaxDistEdgeToSrf())
print("Minumum initial grid quads: %s" % rs.RenderMeshMinInitialGridQuads())
print("Other settings: %s" % rs.RenderMeshSettings())
```

### See Also

RenderMeshDensity, RenderMeshMaxAngle, RenderMeshMaxAspectRatio, RenderMeshMaxDistEdgeToSrf, RenderMeshMaxEdgeLength, RenderMeshMinEdgeLength, RenderMeshMinInitialGridQuads, RenderMeshQuality, RenderMeshSettings

---

## RenderMeshQuality

### Signature

```python
RenderMeshQuality(quality=None)
```

### Description

Returns or sets the render mesh quality of the active document. For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

### Returns

number: if quality is not specified, the current render mesh quality if successful. number: if quality is specified, the previous render mesh quality if successful. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
print("Quality: %s" % rs.RenderMeshQuality())
print("Mesh density: %s" % rs.RenderMeshDensity())
print("Maximum angle: %s" % rs.RenderMeshMaxAngle())
print("Maximum aspect ratio: %s" % rs.RenderMeshMaxAspectRatio())
print("Minimun edge length: %s" % rs.RenderMeshMinEdgeLength())
print("Maximum edge length: %s" % rs.RenderMeshMaxEdgeLength())
print("Maximum distance, edge to surface: %s" % rs.RenderMeshMaxDistEdgeToSrf())
print("Minumum initial grid quads: %s" % rs.RenderMeshMinInitialGridQuads())
print("Other settings: %s" % rs.RenderMeshSettings())
```

### See Also

RenderMeshDensity, RenderMeshMaxAngle, RenderMeshMaxAspectRatio, RenderMeshMaxDistEdgeToSrf, RenderMeshMaxEdgeLength, RenderMeshMinEdgeLength, RenderMeshMinInitialGridQuads, RenderMeshQuality, RenderMeshSettings

---

## RenderMeshSettings

### Signature

```python
RenderMeshSettings(settings=None)
```

### Description

Returns or sets the render mesh settings of the active document. For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

### Returns

number: if settings is not specified, the current render mesh settings if successful. number: if settings is specified, the previous render mesh settings if successful. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
print("Quality: %s" % rs.RenderMeshQuality())
print("Mesh density: %s" % rs.RenderMeshDensity())
print("Maximum angle: %s" % rs.RenderMeshMaxAngle())
print("Maximum aspect ratio: %s" % rs.RenderMeshMaxAspectRatio())
print("Minimun edge length: %s" % rs.RenderMeshMinEdgeLength())
print("Maximum edge length: %s" % rs.RenderMeshMaxEdgeLength())
print("Maximum distance, edge to surface: %s" % rs.RenderMeshMaxDistEdgeToSrf())
print("Minumum initial grid quads: %s" % rs.RenderMeshMinInitialGridQuads())
print("Other settings: %s" % rs.RenderMeshSettings())
```

### See Also

RenderMeshDensity, RenderMeshMaxAngle, RenderMeshMaxAspectRatio, RenderMeshMaxDistEdgeToSrf, RenderMeshMaxEdgeLength, RenderMeshMinEdgeLength, RenderMeshMinInitialGridQuads, RenderMeshQuality, RenderMeshSettings

---

## RenderResolution

### Signature

```python
RenderResolution(resolution=None)
```

### Description

Returns or sets the render resolution

### Returns

tuple(number, number): if resolution is not specified, the current resolution width,height tuple(number, number): if resolution is specified, the previous resolution width, height

### Example

```python
import rhinoscriptsyntax as rs
sizex, sizey = rs.Viewsize()
resolution = sizex/2 , sizey/2
rs.RenderResolution( resolution )
```

### See Also

RenderAntialias, RenderColor, RenderSettings

---

## RenderSettings

### Signature

```python
RenderSettings(settings=None)
```

### Description

Returns or sets render settings

### Returns

number: if settings are not specified, the current render settings in bit-coded flags number: if settings are specified, the previous render settings in bit-coded flags

### Example

```python
import rhinoscriptsyntax as rs
render_annotations = 8
settings = rs.RenderSettings()
if settings & render_annotations:
 settings = settings - render_annotations
 rs.RenderSettings( settings )
```

### See Also

RenderAntialias, RenderColor, RenderResolution

---

## UnitAbsoluteTolerance

### Signature

```python
UnitAbsoluteTolerance(tolerance=None, in_model_units=True)
```

### Description

Resturns or sets the document's absolute tolerance. Absolute tolerance is measured in drawing units. See Rhino's document properties command (Units and Page Units Window) for details

### Returns

number: if tolerance is not specified, the current absolute tolerance number: if tolerance is specified, the previous absolute tolerance

### Example

```python
import rhinoscriptsyntax as rs
tol = rs.UnitAbsoluteTolerance()
if tol<0.01:
 rs.UnitAbsoluteTolerance( 0.01 )
```

### See Also

UnitAngleTolerance, UnitDistanceDisplayPrecision, UnitRelativeTolerance, UnitSystem

---

## UnitAngleTolerance

### Signature

```python
UnitAngleTolerance(angle_tolerance_degrees=None, in_model_units=True)
```

### Description

Return or set the document's angle tolerance. Angle tolerance is measured in degrees. See Rhino's DocumentProperties command (Units and Page Units Window) for details

### Returns

number: if angle_tolerance_degrees is not specified, the current angle tolerance number: if angle_tolerance_degrees is specified, the previous angle tolerance

### Example

```python
import rhinoscriptsyntax as rs
tol = rs.UnitAngleTolerance()
if tol<3.0:
 rs.UnitAngleTolerance(3.0)
```

### See Also

UnitAbsoluteTolerance, UnitDistanceDisplayPrecision, UnitRelativeTolerance, UnitSystem

---

## UnitDistanceDisplayPrecision

### Signature

```python
UnitDistanceDisplayPrecision(precision=None, model_units=True)
```

### Description

Return or set the document's distance display precision

### Returns

number: If precision is not specified, the current distance display precision if successful. If precision is specified, the previous distance display precision if successful. If not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
precision = 3
rs.UnitDistanceDisplayPrecision( precision )
```

### See Also

UnitAbsoluteTolerance, UnitAngleTolerance, UnitRelativeTolerance, UnitSystem

---

## UnitRelativeTolerance

### Signature

```python
UnitRelativeTolerance(relative_tolerance=None, in_model_units=True)
```

### Description

Return or set the document's relative tolerance. Relative tolerance is measured in percent. See Rhino's DocumentProperties command (Units and Page Units Window) for details

### Returns

number: if relative_tolerance is not specified, the current tolerance in percent number: if relative_tolerance is specified, the previous tolerance in percent

### Example

```python
import rhinoscriptsyntax as rs
tol = rs.UnitRelativeTolerance()
if tol<1.0:
 rs.UnitRelativeTolerance(1.0)
```

### See Also

UnitAbsoluteTolerance, UnitAngleTolerance, UnitDistanceDisplayPrecision, UnitSystem

---

## UnitScale

### Signature

```python
UnitScale(to_system, from_system=None)
```

### Description

Return the scale factor for changing between unit systems.

### Returns

number: scale factor for changing between unit systems

### Example

```python
import rhinoscriptsyntax as rs
print(rs.UnitScale(3, 4)) # 100.0
print(rs.UnitScale(3, 8)) # 2.54
print(rs.UnitScale(8, 9)) # 12.0
```

### See Also

UnitSystem, UnitSystemName

---

## UnitSystem

### Signature

```python
UnitSystem(unit_system=None, scale=False, in_model_units=True)
```

### Description

Return or set the document's unit system. See Rhino's DocumentProperties command (Units and Page Units Window) for details

### Returns

number: if unit_system is not specified, the current unit system number: if unit_system is specified, the previous unit system None: on error

### Example

```python
import rhinoscriptsyntax as rs
rhUnitMillimeters = 2
rhUnitInches = 8
current_system = rs.UnitSystem()
if current_system==rhUnitMillimeters:
 rs.UnitSystem(rhUnitInches, True)
```

### See Also

UnitAbsoluteTolerance, UnitAngleTolerance, UnitDistanceDisplayPrecision, UnitRelativeTolerance

---

## UnitSystemName

** IN USE**

### Signature

```python
UnitSystemName(capitalize=False, singular=True, abbreviate=False, model_units=True)
```

### Description

Returns the name of the current unit system

### Returns

str: The name of the current units system if successful.

### Example

```python
import rhinoscriptsyntax as rs
system = rs.UnitSystemName(False, False, False)
print("The units system is set to{}".format(system))
```

### See Also

UnitSystem

---

# Geometry

*35 functions | 2 in use*

---

## AddClippingPlane

### Signature

```python
AddClippingPlane(plane, u_magnitude, v_magnitude, views=None)
```

### Description

Create a clipping plane for visibly clipping away geometry in a specific view. Note, clipping planes are infinite

### Returns

guid: object identifier on success None: on failure

### Example

```python
import rhinoscriptsyntax as rs
rs.AddClippingPlane( rs.WorldXYPlane(), 5.0, 3.0 )
```

### See Also

IsClippingPlane

---

## AddPictureFrame

### Signature

```python
AddPictureFrame(plane, filename, width=0.0, height=0.0, self_illumination=True, embed=False, use_alpha=False, make_mesh=False)
```

### Description

Creates a picture frame and adds it to the document.

### Returns

guid: object identifier on success None: on failure

---

## AddPoint

** IN USE**

### Signature

```python
AddPoint(point, y=None, z=None)
```

### Description

Adds point object to the document.

### Returns

guid: identifier for the object that was added to the doc

### Example

```python
import rhinoscriptsyntax as rs
rs.AddPoint( (1,2,3) )
```

### See Also

IsPoint, PointCoordinates

---

## AddPointCloud

### Signature

```python
AddPointCloud(points, colors=None)
```

### Description

Adds point cloud object to the document

### Returns

guid: identifier of point cloud on success

### Example

```python
import rhinoscriptsyntax as rs
points = (0,0,0), (1,1,1), (2,2,2), (3,3,3)
rs.AddPointCloud(points)
```

### See Also

IsPointCloud, PointCloudCount, PointCloudPoints

---

## AddPoints

### Signature

```python
AddPoints(points)
```

### Description

Adds one or more point objects to the document

### Returns

list(guid, ...): identifiers of the new objects on success

### Example

```python
import rhinoscriptsyntax as rs
points = rs.GetPoints(True, True, "Select points")
if points: rs.AddPoints(points)
```

### See Also

AddPoint, AddPointCloud

---

## AddText

### Signature

```python
AddText(text, point_or_plane, height=1.0, font=None, font_style=0, justification=None)
```

### Description

Adds a text string to the document

### Returns

guid: identifier for the object that was added to the doc on success None: on failure

### Example

```python
import rhinoscriptsyntax as rs
point = rs.GetPoint("Pick point")
if point: rs.AddText("Hello Rhino!", point)
```

### See Also

IsText

---

## AddTextDot

### Signature

```python
AddTextDot(text, point)
```

### Description

Add a text dot to the document.

### Returns

guid: The identifier of the new object if successful

### Example

```python
import rhinoscriptsyntax as rs
rs.AddTextDot("howdy",(1,2,3))
```

### See Also

IsTextDot

---

## Area

### Signature

```python
Area(object_id)
```

### Description

Compute the area of a closed curve, hatch, surface, polysurface, or mesh

### Returns

number: area if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
a = rs.Area('a9e34aa8-226c-4e17-9e11-b74bf2cf581b')
```

### See Also

IsPoint, PointCoordinates

---

## BoundingBox

** IN USE**

### Signature

```python
BoundingBox(objects, view_or_plane=None, in_world_coords=True)
```

### Description

Returns either world axis-aligned or a construction plane axis-aligned bounding box of an object or of several objects

### Returns

list(point, point, point, point, point, point, point, point): Eight 3D points that define the bounding box. Points returned in counter-clockwise order starting with the bottom rectangle of the box. None: on error

### Example

```python
import rhinoscriptsyntax as rs
object = rs.GetObject("Select object")
if object:
 box = rs.BoundingBox(object)
 if box:
 for i, point in enumerate(box):
 rs.AddTextDot( i, point )
```

---

## CompareGeometry

### Signature

```python
CompareGeometry(first, second)
```

### Description

Compares two objects to determine if they are geometrically identical.

### Returns

True if the objects are geometrically identical, otherwise False.

### Example

```python
import rhinoscriptsyntax as rs
object1 = rs.GetObject("Select first object")
object2 = rs.GetObject("Select second object")
if object:
print("Objects are identical" if rs.CompareGeometry(object1, object2) else "Objects differ")
```

---

## ExplodeText

### Signature

```python
ExplodeText(text_id, delete=False)
```

### Description

Creates outline curves for a given text entity

### Returns

list(guid): of outline curves

### Example

```python
import rhinoscriptsyntax as rs
text = rs.AddText("abcd", rs.WorldXYPlane())
rs.ExplodeText(text, True)
```

### See Also

IsHatch, HatchPattern, HatchRotation, HatchScale

---

## IsClippingPlane

### Signature

```python
IsClippingPlane(object_id)
```

### Description

Verifies that an object is a clipping plane object

### Returns

bool: True if the object with a given id is a clipping plane

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a clipping plane")
if rs.IsClippingPlane(id):
 print("The object is a clipping plane.")
else:
 print("The object is not a clipping plane.")
```

### See Also

AddClippingPlane

---

## IsPoint

### Signature

```python
IsPoint(object_id)
```

### Description

Verifies an object is a point object.

### Returns

bool: True if the object with a given id is a point

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a point")
if rs.IsPoint(id):
 print("The object is a point.")
else:
 print("The object is not a point.")
```

### See Also

AddPoint, PointCoordinates

---

## IsPointCloud

### Signature

```python
IsPointCloud(object_id)
```

### Description

Verifies an object is a point cloud object.

### Returns

bool: True if the object with a given id is a point cloud

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a point cloud")
if rs.IsPointCloud(id):
 print("The object is a point cloud.")
else:
 print("The object is not a point cloud.")
```

### See Also

AddPointCloud, PointCloudCount, PointCloudPoints

---

## IsText

### Signature

```python
IsText(object_id)
```

### Description

Verifies an object is a text object.

### Returns

bool: True if the object with a given id is a text object

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a text object")
if rs.IsText(id):
 print("The object is a text object.")
else:
 print("The object is not a text object.")
```

### See Also

AddText

---

## IsTextDot

### Signature

```python
IsTextDot(object_id)
```

### Description

Verifies an object is a text dot object.

### Returns

bool: True if the object with a given id is a text dot object

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a text dot object")
if rs.IsTextDot(id):
 print("The object is a text dot object.")
else:
 print("The object is not a text dot object.")
```

### See Also

AddTextDot

---

## PointCloudClosestPoints

### Signature

```python
PointCloudClosestPoints(pt_cloud, needle_points, distance)
```

### Description

Returns a list of lists of point indices in a point cloud that are closest to needle_points. Each inner list references all points within or on the surface of a sphere of distance radius.

### Returns

[[int, ...], ...]: a list of lists with the indices of the found points.

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select point cloud", rs.filter.pointcloud)
if id:
 result = rs.PointCloudClosestPoints(id, [[0,0,0]], 1.0)
 if result and result[0]:
 print("The first point next to origin within a 1.0 unit radius is: %s." % result[0][0])
 else:
 print("There is no point in the point cloud within a 1.0 unit radius sphere from origin.")
```

### See Also

AddPointCloud, IsPointCloud, PointCloudPoints

---

## PointCloudCount

### Signature

```python
PointCloudCount(object_id)
```

### Description

Returns the point count of a point cloud object

### Returns

number: number of points if successful

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select point cloud", rs.filter.pointcloud)
print("Point count:{}".format(rs.PointCloudCount(id)))
```

### See Also

AddPointCloud, IsPointCloud, PointCloudPoints

---

## PointCloudHasHiddenPoints

### Signature

```python
PointCloudHasHiddenPoints(object_id)
```

### Description

Verifies that a point cloud has hidden points

### Returns

bool: True if cloud has hidden points, otherwise False

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a point cloud", rs.filter.pointcloud)
if rs.PointCloudHasHiddenPoints(obj):
 print("The point cloud has hidden points.")
else:
 print("The point cloud has no hidden points.")
```

### See Also

PointCloudHasPointColors, PointCloudHidePoints, PointCloudPointColors

---

## PointCloudHasPointColors

### Signature

```python
PointCloudHasPointColors(object_id)
```

### Description

Verifies that a point cloud has point colors

### Returns

bool: True if cloud has point colors, otherwise False

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a point cloud", rs.filter.pointcloud)
if rs.PointCloudHasPointColors(obj):
 print("The point cloud has point colors.")
else:
 print("The point cloud has no point colors.")
```

### See Also

PointCloudHasPointColors, PointCloudHidePoints, PointCloudPointColors

---

## PointCloudHidePoints

### Signature

```python
PointCloudHidePoints(object_id, hidden=[])
```

### Description

Returns or modifies the hidden points of a point cloud object

### Returns

list(bool, ....): List of point cloud hidden states

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select point cloud", rs.filter.pointcloud)
if obj:
 hidden = [True] * rs.PointCloudCount(obj)
 for i in range(len(hidden)):
 hidden[i] = (i%2==0)
 rs.PointCloudHidePoints(obj, hidden)
```

### See Also

PointCloudHasPointColors, PointCloudPointColors

---

## PointCloudKNeighbors

### Signature

```python
PointCloudKNeighbors(pt_cloud, needle_points, amount=1)
```

### Description

Returns amount indices of points in a point cloud that are near needle_points.

### Returns

[int, int,...]: a list of indices of the found points, if amount equals 1. [[int, ...], ...]: nested lists with amount items within a list, with the indices of the found points.

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select point cloud", rs.filter.pointcloud)
if id:
 result = rs.PointCloudKNeighbors(id, [(0,0,0)])
 if result:
 print("The closest point to origin has index : %s." % result[0])
```

### See Also

AddPointCloud, IsPointCloud, PointCloudPoints

---

## PointCloudPointColors

### Signature

```python
PointCloudPointColors(object_id, colors=[])
```

### Description

Returns or modifies the point colors of a point cloud object

### Returns

list(color, ...): List of point cloud colors

### Example

```python
import rhinoscriptsyntax as rs
import random

def RandomColor():
 red = random.randint(0,255)
 green = random.randint(0,255)
 blue = random.randint(0,255)
 return rs.coercecolor((red,green,blue))

obj = rs.GetObject("Select point cloud", rs.filter.pointcloud)
if obj:
 colors = [RandomColor() for i in range(rs.PointCloudCount(obj))]
 rs.PointCloudColors(obj, colors)
```

### See Also

PointCloudHasHiddenPoints, PointCloudHasPointColors, PointCloudHidePoints

---

## PointCloudPoints

### Signature

```python
PointCloudPoints(object_id)
```

### Description

Returns the points of a point cloud object

### Returns

list(guid, ...): list of points if successful

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select point cloud", rs.filter.pointcloud)
points = rs.PointCloudPoints(id)
if points: for point in points: print(point)
```

### See Also

AddPointCloud, IsPointCloud, PointCloudCount

---

## PointCoordinates

### Signature

```python
PointCoordinates(object_id, point=None)
```

### Description

Returns or modifies the X, Y, and Z coordinates of a point object

### Returns

point: If point is not specified, the current 3-D point location point: If point is specified, the previous 3-D point location

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select point", rs.filter.point)
point = rs.PointCoordinates(id)
if point: print(point)
```

### See Also

AddPoint, IsPoint

---

## TextDotFont

### Signature

```python
TextDotFont(object_id, fontface=None)
```

### Description

Returns or modified the font of a text dot

### Returns

str: If font is not specified, the current text dot font str: If font is specified, the previous text dot font None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select text dot")
if rs.IsTextDot(obj): rs.TextDotFont( obj, "Arial" )
```

### See Also

AddTextDot, IsTextDot, TextDotHeight, TextDotPoint, TextDotText

---

## TextDotHeight

### Signature

```python
TextDotHeight(object_id, height=None)
```

### Description

Returns or modified the font height of a text dot

### Returns

number: If height is not specified, the current text dot height number: If height is specified, the previous text dot height None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select text dot")
if rs.IsTextDot(obj): rs.TextDotHeight(obj, 10.0)
```

### See Also

AddTextDot, IsTextDot, TextDotFont, TextDotPoint, TextDotText

---

## TextDotPoint

### Signature

```python
TextDotPoint(object_id, point=None)
```

### Description

Returns or modifies the location, or insertion point, on a text dot object

### Returns

point: If point is not specified, the current 3-D text dot location point: If point is specified, the previous 3-D text dot location None: if not successful, or on error

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select text dot")
if rs.IsTextDot(id):
 point = rs.TestDotPoint(id)
 rs.AddPoint( point )
 rs.TextDotPoint(id, [0,0,0])
```

### See Also

AddTextDot, IsTextDot, TextDotText

---

## TextDotText

### Signature

```python
TextDotText(object_id, text=None)
```

### Description

Returns or modifies the text on a text dot object

### Returns

str: If text is not specified, the current text dot text str: If text is specified, the previous text dot text None: if not successful, or on error

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select text dot")
if rs.IsTextDot(id):
 rs.TextDotText( id, "Rhino")
```

### See Also

AddTextDot, IsTextDot, TextDotPoint

---

## TextObjectFont

### Signature

```python
TextObjectFont(object_id, font=None)
```

### Description

Returns of modifies the font used by a text object

### Returns

str: if a font is not specified, the current font face name str: if a font is specified, the previous font face name None: if not successful, or on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select text")
if rs.IsText(obj): rs.TextObjectFont(obj, "Arial")
```

### See Also

AddText, IsText, TextObjectHeight, TextObjectPlane, TextObjectPoint, TextObjectStyle, TextObjectText

---

## TextObjectHeight

### Signature

```python
TextObjectHeight(object_id, height=None)
```

### Description

Returns or modifies the height of a text object

### Returns

number: if height is not specified, the current text height number: if height is specified, the previous text height None: if not successful, or on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select text")
if rs.IsText(obj):
 rs.TextObjectHeight( obj, 1.0 )
```

### See Also

AddText, IsText, TextObjectFont, TextObjectPlane, TextObjectPoint, TextObjectStyle, TextObjectText

---

## TextObjectPlane

### Signature

```python
TextObjectPlane(object_id, plane=None)
```

### Description

Returns or modifies the plane used by a text object

### Returns

plane: if a plane is not specified, the current plane if successful plane: if a plane is specified, the previous plane if successful None: if not successful, or on Error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select text")
if rs.IsText(obj):
 plane = rs.ViewCPlane("Top")
 rs.TextObjectPlane( obj, plane )
```

### See Also

AddText, IsText, TextObjectFont, TextObjectHeight, TextObjectPoint, TextObjectStyle, TextObjectText

---

## TextObjectPoint

### Signature

```python
TextObjectPoint(object_id, point=None)
```

### Description

Returns or modifies the location of a text object

### Returns

point: if point is not specified, the 3D point identifying the current location point: if point is specified, the 3D point identifying the previous location None: if not successful, or on Error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select text")
if rs.IsText(obj):
 rs.TextObjectPoint( obj, [0,0,0] )
```

### See Also

AddText, IsText, TextObjectFont, TextObjectHeight, TextObjectPlane, TextObjectStyle, TextObjectText

---

## TextObjectStyle

### Signature

```python
TextObjectStyle(object_id, style=None)
```

### Description

Returns or modifies the font style of a text object

### Returns

number: if style is not specified, the current font style number: if style is specified, the previous font style None: if not successful, or on Error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select text")
if rs.IsText(obj):
 rs.TextObjectStyle( obj, 3 )
```

### See Also

AddText, IsText, TextObjectFont, TextObjectHeight, TextObjectPlane, TextObjectPoint, TextObjectText

---

## TextObjectText

### Signature

```python
TextObjectText(object_id, text=None)
```

### Description

Returns or modifies the text string of a text object.

### Returns

str: if text is not specified, the current string value if successful str: if text is specified, the previous string value if successful None: if not successful, or on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select text")
if rs.IsText(obj): rs.TextObjectText(obj, "Rhino")
```

### See Also

AddText, IsText, TextObjectFont, TextObjectHeight, TextObjectPlane, TextObjectPoint, TextObjectStyle

---

# Grips

*15 functions | 0 in use*

---

## EnableObjectGrips

### Signature

```python
EnableObjectGrips(object_id, enable=True)
```

### Description

Enables or disables an object's grips. For curves and surfaces, these are also called control points.

### Returns

bool: True on success, False on failure

### Example

```python
import rhinoscriptsyntax as rs
objects = rs.GetObjects("Select objects")
if objects: [rs.EnableObjectGrips(obj) for obj in objs]
```

### See Also

ObjectGripCount, ObjectGripsOn, ObjectGripsSelected, SelectObjectGrips, UnselectObjectGrips

---

## GetObjectGrip

### Signature

```python
GetObjectGrip(message=None, preselect=False, select=False)
```

### Description

Prompts the user to pick a single object grip

### Returns

tuple(guid, number, point): defining a grip record. [0] = identifier of the object that owns the grip [1] = index value of the grip [2] = location of the grip None: on error

### Example

```python
import rhinoscriptsyntax as rs
curve = rs.GetObject("Select a curve", rs.filter.curve)
if curve:
 rs.EnableObjectGrips( curve )
 grip = rs.GetObjectGrip("Select a curve grip")
 if grip: print(grip[2])
```

### See Also

GetObjectGrips

---

## GetObjectGrips

### Signature

```python
GetObjectGrips(message=None, preselect=False, select=False)
```

### Description

Prompts user to pick one or more object grips from one or more objects.

### Returns

list((guid, number, point), ...): containing one or more grip records. Each grip record is a tuple [n][0] = identifier of the object that owns the grip [n][1] = index value of the grip [n][2] = location of the grip None: on error

### Example

```python
import rhinoscriptsyntax as rs
curves = rs.GetObjects("Select curves", rs.filter.curves)
if curves:
 for curve in curves: rs.EnableObjectGrips(curve)
 grips = rs.GetObjectGrips("Select curve grips")
 if grips: for grip in grips: print(grip[0])
```

### See Also

GetObjectGrip

---

## NextObjectGrip

### Signature

```python
NextObjectGrip(object_id, index, direction=0, enable=True)
```

### Description

Returns the next grip index from a specified grip index of an object

### Returns

number: index of the next grip on success None: on failure

### Example

```python
import rhinoscriptsyntax as rs
object_id = rs.GetObject("Select curve", rs.filter.curve)
if object_id:
 rs.EnableObjectGrips( object_id )
 count = rs.ObjectGripCount( object_id )
 for i in range(0,count,2):
 rs.NextObjectGrip(object_id, i, 0, True)
```

### See Also

EnableObjectGrips, PrevObjectGrip

---

## ObjectGripCount

### Signature

```python
ObjectGripCount(object_id)
```

### Description

Returns number of grips owned by an object

### Returns

number: number of grips if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if rs.ObjectGripsOn(obj):
 print("Grip count ={}".format(rs.ObjectGripCount(obj)))
```

### See Also

EnableObjectGrips, ObjectGripsOn, ObjectGripsSelected, SelectObjectGrips, UnselectObjectGrips

---

## ObjectGripLocation

### Signature

```python
ObjectGripLocation(object_id, index, point=None)
```

### Description

Returns or modifies the location of an object's grip

### Returns

point: if point is not specified, the current location of the grip referenced by index point: if point is specified, the previous location of the grip referenced by index None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select curve", rs.filter.curve)
if obj:
 rs.EnableObjectGrips(obj)
 point = rs.ObjectGripLocation(obj, 0)
 point[0] = point[0] + 1.0
 point[1] = point[1] + 1.0
 point[2] = point[2] + 1.0
 rs.ObjectGripLocation(obj, 0, point)
 rs.EnableObjectGrips(obj, False)
```

### See Also

EnableObjectGrips, ObjectGripLocations

---

## ObjectGripLocations

### Signature

```python
ObjectGripLocations(object_id, points=None)
```

### Description

Returns or modifies the location of all grips owned by an object. The locations of the grips are returned in a list of Point3d with each position in the list corresponding to that grip's index. To modify the locations of the grips, you must provide a list of points that contain the same number of points at grips

### Returns

list(point, ...): if points is not specified, the current location of all grips list(point, ...): if points is specified, the previous location of all grips None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select curve", rs.filter.curve)
if obj:
 rs.EnableObjectGrips( obj )
 points = rs.ObjectGripLocations(obj)
 for point in points: print(point)
```

### See Also

EnableObjectGrips, ObjectGripCount, ObjectGripLocation

---

## ObjectGripsOn

### Signature

```python
ObjectGripsOn(object_id)
```

### Description

Verifies that an object's grips are turned on

### Returns

bool: True or False indicating Grips state None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if rs.ObjectGripsOn(obj):
 print("Grip count = {}".format(rs.ObjectGripCount(obj)))
```

### See Also

EnableObjectGrips, ObjectGripCount, ObjectGripsSelected, SelectObjectGrips, UnselectObjectGrips

---

## ObjectGripsSelected

### Signature

```python
ObjectGripsSelected(object_id)
```

### Description

Verifies that an object's grips are turned on and at least one grip is selected

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if rs.ObjectGripsSelected(obj):
 rs.UnselectObjectGrips( obj )
```

### See Also

EnableObjectGrips, ObjectGripCount, ObjectGripsOn, SelectObjectGrips, UnselectObjectGrips

---

## PrevObjectGrip

### Signature

```python
PrevObjectGrip(object_id, index, direction=0, enable=True)
```

### Description

Returns the previous grip index from a specified grip index of an object

### Returns

number: index of the next grip on success None: on failure

### Example

```python
import rhinoscriptsyntax as rs
object_id = rs.GetObject("Select curve", rs.filter.curve)
if object_id:
 rs.EnableObjectGrips(object_id)
 count = rs.ObjectGripCount(object_id)
 for i in range(count-1, 0, -2):
 rs.PrevObjectGrip(object_id, i, 0, True)
```

### See Also

EnableObjectGrips, NextObjectGrip

---

## SelectObjectGrip

### Signature

```python
SelectObjectGrip(object_id, index)
```

### Description

Selects a single grip owned by an object. If the object's grips are not turned on, the grips will not be selected

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select curve", rs.filter.curve)
if obj:
 rs.EnableObjectGrips( obj )
 count = rs.ObjectGripCount( obj )
 for i in range(0,count,2): rs.SelectObjectGrip(obj,i)
```

### See Also

EnableObjectGrips, ObjectGripCount, SelectObjectGrips

---

## SelectObjectGrips

### Signature

```python
SelectObjectGrips(object_id)
```

### Description

Selects an object's grips. If the object's grips are not turned on, they will not be selected

### Returns

number: Number of grips selected on success None: on failure

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if rs.ObjectGripsSelected(obj)==False:
 rs.SelectObjectGrips( obj )
```

### See Also

EnableObjectGrips, ObjectGripCount, SelectObjectGrip

---

## SelectedObjectGrips

### Signature

```python
SelectedObjectGrips(object_id)
```

### Description

Returns a list of grip indices indentifying an object's selected grips

### Returns

list(number): list of indices on success None: on failure or if no grips are selected

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select curve", rs.filter.curve)
if obj:
 rs.EnableObjectGrips( obj )
 count = rs.ObjectGripCount( obj )
 for i in range(0,count,2):
 rs.SelectObjectGrip( obj, i )
 grips = rs.SelectedObjectGrips(obj)
 if grips: print(len(grips{}).format("grips selected"))
```

### See Also

EnableObjectGrips, SelectObjectGrip, SelectObjectGrips

---

## UnselectObjectGrip

### Signature

```python
UnselectObjectGrip(object_id, index)
```

### Description

Unselects a single grip owned by an object. If the object's grips are not turned on, the grips will not be unselected

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select curve", rs.filter.curve)
if obj:
 rs.EnableObjectGrips( obj )
 count = rs.ObjectGripCount(obj)
 for i in range(0,count,2):
 rs.UnselectObjectGrip( obj, i )
```

### See Also

EnableObjectGrips, ObjectGripCount, UnselectObjectGrips

---

## UnselectObjectGrips

### Signature

```python
UnselectObjectGrips(object_id)
```

### Description

Unselects an object's grips. Note, the grips will not be turned off.

### Returns

number: Number of grips unselected on success None: on failure

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if rs.ObjectGripsSelected(obj): rs.UnselectObjectGrips(obj)
```

### See Also

EnableObjectGrips, ObjectGripCount, UnselectObjectGrip

---

# Group

*17 functions | 0 in use*

---

## AddGroup

### Signature

```python
AddGroup(group_name=None)
```

### Description

Adds a new empty group to the document

### Returns

str: name of the new group if successful None: is not successful or on error

### Example

```python
import rhinoscriptsyntax as rs
name = rs.AddGroup("NewGroup")
```

### See Also

DeleteGroup, GroupCount, GroupNames, IsGroup, RenameGroup

---

## AddObjectToGroup

### Signature

```python
AddObjectToGroup(object_id, group_name)
```

### Description

Adds a single object to an existing group.

### Returns

True or False representing success or failure

### Example

```python
import rhinoscriptsyntax as rs
name = "NewGroup"
id = rs.GetObject("Select object to add to group")
if id: rs.AddObjectToGroup(id,name)
```

### See Also

AddObjectsToGroup, IsGroupEmpty, ObjectGroups, ObjectsByGroup

---

## AddObjectsToGroup

### Signature

```python
AddObjectsToGroup(object_ids, group_name)
```

### Description

Adds one or more objects to an existing group.

### Returns

number: number of objects added to the group

### Example

```python
import rhinoscriptsyntax as rs
name = "NewGroup"
object_ids = rs.GetObjects("Select objects to add to group")
if object_ids: rs.AddObjectsToGroup(object_ids, name)
```

### See Also

AddObjectToGroup, IsGroupEmpty, ObjectGroups, ObjectsByGroup

---

## DeleteGroup

### Signature

```python
DeleteGroup(group_name)
```

### Description

Removes an existing group from the document. Reference groups cannot be removed. Deleting a group does not delete the member objects

### Returns

bool: True or False representing success or failure

### Example

```python
import rhinoscriptsyntax as rs
groups = rs.GroupNames()
if groups:
 for group in groups: rs.DeleteGroup(group)
```

### See Also

AddGroup, GroupCount, GroupNames, IsGroup, RenameGroup

---

## GroupCount

### Signature

```python
GroupCount()
```

### Description

Returns the number of groups in the document

### Returns

number: the number of groups in the document

### Example

```python
import rhinoscriptsyntax as rs
numgroups = rs.GroupCount()
print("Group count:{}".format(numgroups))
```

### See Also

AddGroup, DeleteGroup, GroupNames, IsGroup, RenameGroup

---

## GroupNames

### Signature

```python
GroupNames()
```

### Description

Returns the names of all the groups in the document None if no names exist in the document

### Returns

list(str, ...): the names of all the groups in the document. None if no names exist in the document

### Example

```python
import rhinoscriptsyntax as rs
groups = rs.GroupNames()
if groups:
 for group in groups: print(group)
```

### See Also

AddGroup, DeleteGroup, GroupCount, IsGroup, RenameGroup

---

## HideGroup

### Signature

```python
HideGroup(group_name)
```

### Description

Hides a group of objects. Hidden objects are not visible, cannot be snapped to, and cannot be selected

### Returns

number: The number of objects that were hidden

### Example

```python
import rhinoscriptsyntax as rs
groups = rs.GroupNames()
if groups:
 for group in groups: rs.HideGroup(group)
```

### See Also

LockGroup, ShowGroup, UnlockGroup

---

## IsGroup

### Signature

```python
IsGroup(group_name)
```

### Description

Verifies the existance of a group

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
group = rs.GetString("Group name to verify")
if rs.IsGroup(group):
 print("The group exists.")
else:
 print("The group does not exist.")
```

### See Also

AddGroup, DeleteGroup, GroupCount, GroupNames, RenameGroup

---

## IsGroupEmpty

### Signature

```python
IsGroupEmpty(group_name)
```

### Description

Verifies that an existing group is empty, or contains no object members

### Returns

bool: True or False if group_name exists None: if group_name does not exist

### Example

```python
import rhinoscriptsyntax as rs
names = rs.GroupNames()
if names:
 for name in names:
 if rs.IsGroupEmpty(name): rs.DeleteGroup(name)
```

### See Also

AddObjectsToGroup, AddObjectToGroup, RemoveObjectFromAllGroups, RemoveObjectFromGroup, RemoveObjectsFromGroup

---

## LockGroup

### Signature

```python
LockGroup(group_name)
```

### Description

Locks a group of objects. Locked objects are visible and they can be snapped to. But, they cannot be selected

### Returns

number: Number of objects that were locked if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
names = rs.GroupNames()
if names:
 for name in names: rs.LockGroup(name)
```

### See Also

HideGroup, ShowGroup, UnlockGroup

---

## ObjectTopGroup

### Signature

```python
ObjectTopGroup(object_id)
```

### Description

Returns the top most group name that an object is assigned. This function primarily applies to objects that are members of nested groups

### Returns

str: the top group's name if successful None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select object to add to group")
groupName = rs.ObjectTopGroup(id)
```

### See Also

ObjectGroups

---

## RemoveObjectFromAllGroups

### Signature

```python
RemoveObjectFromAllGroups(object_id)
```

### Description

Removes a single object from any and all groups that it is a member. Neither the object nor the group can be reference objects

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
object = rs.GetObject("Select object")
if object: rs.RemoveObjectFromAllGroups(object)
```

### See Also

IsGroupEmpty, ObjectGroups, ObjectsByGroup, RemoveObjectFromGroup, RemoveObjectsFromGroup

---

## RemoveObjectFromGroup

### Signature

```python
RemoveObjectFromGroup(object_id, group_name)
```

### Description

Remove a single object from an existing group

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
name = "NewGroup"
id = rs.GetObject("Select object")
if name: rs.RemoveObjectFromGroup(id,name)
```

### See Also

IsGroupEmpty, ObjectGroups, ObjectsByGroup, RemoveObjectFromAllGroups, RemoveObjectsFromGroup

---

## RemoveObjectsFromGroup

### Signature

```python
RemoveObjectsFromGroup(object_ids, group_name)
```

### Description

Removes one or more objects from an existing group

### Returns

number: The number of objects removed from the group is successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
group = "NewGroup"
ids = rs.GetObjects("Select objects")
if ids: rs.RemoveObjectsFromGroup(ids,group)
```

### See Also

IsGroupEmpty, ObjectGroups, ObjectsByGroup, RemoveObjectFromAllGroups, RemoveObjectFromGroup

---

## RenameGroup

### Signature

```python
RenameGroup(old_name, new_name)
```

### Description

Renames an existing group

### Returns

str: the new group name if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
strOldGroup = rs.GetString("Old group name")
if strOldGroup:
 strNewGroup = rs.GetString("New group name")
 if strNewName: rs.RenameGroup(strOldGroup, strNewGroup)
```

### See Also

AddGroup, DeleteGroup, GroupCount, GroupNames, IsGroup

---

## ShowGroup

### Signature

```python
ShowGroup(group_name)
```

### Description

Shows a group of previously hidden objects. Hidden objects are not visible, cannot be snapped to, and cannot be selected

### Returns

number: The number of objects that were shown if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
groups = rs.GroupNames()
if groups:
 for group in groups: rs.ShowGroup(group)
```

### See Also

HideGroup, LockGroup, UnlockGroup

---

## UnlockGroup

### Signature

```python
UnlockGroup(group_name)
```

### Description

Unlocks a group of previously locked objects. Lockes objects are visible, can be snapped to, but cannot be selected

### Returns

number: The number of objects that were unlocked if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
groups = rs.GroupNames()
if groups:
 for group in groups: rs.UnlockGroup(group)
```

### See Also

HideGroup, LockGroup, ShowGroup

---

# Hatch

*16 functions | 0 in use*

---

## AddHatch

### Signature

```python
AddHatch(curve_id, hatch_pattern=None, scale=1.0, rotation=0.0)
```

### Description

Creates a new hatch object from a closed planar curve object

### Returns

guid:identifier of the newly created hatch on success None on error

### Example

```python
import rhinoscriptsyntax as rs
circle = rs.AddCircle(rs.WorldXYPlane(), 10.0)
if rs.IsHatchPattern("Grid"):
 rs.AddHatch( circle, "Grid" )
else:
 rs.AddHatch( circle, rs.CurrentHatchPattern() )
```

### See Also

AddHatches, CurrentHatchPattern, HatchPatternNames

---

## AddHatchPatterns

### Signature

```python
AddHatchPatterns(filename, replace=False)
```

### Description

Adds hatch patterns to the document by importing hatch pattern definitions from a pattern file.

### Returns

list(str, ...): Names of the newly added hatch patterns if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
filename = rs.OpenFileName("Import", "Pattern Files (*.pat)|*.pat||")
if filename:
 patterns = rs.AddHatchPatterns(filename)
 if patterns:
 for pattern in patterns: print(pattern)
```

### See Also

HatchPatternCount, HatchPatternNames

---

## AddHatches

### Signature

```python
AddHatches(curve_ids, hatch_pattern=None, scale=1.0, rotation=0.0, tolerance=None)
```

### Description

Creates one or more new hatch objects a list of closed planar curves

### Returns

list(guid, ...): identifiers of the newly created hatch on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
curves = rs.GetObjects("Select closed planar curves", rs.filter.curve)
if curves:
 if rs.IsHatchPattern("Grid"):
 rs.AddHatches( curves, "Grid" )
 else:
 rs.AddHatches( curves, rs.CurrentHatchPattern() )
```

### See Also

AddHatch, CurrentHatchPattern, HatchPatternNames

---

## CurrentHatchPattern

### Signature

```python
CurrentHatchPattern(hatch_pattern=None)
```

### Description

Returns or sets the current hatch pattern file

### Returns

str: if hatch_pattern is not specified, the current hatch pattern str: if hatch_pattern is specified, the previous hatch pattern None: on error

### Example

```python
import rhinoscriptsyntax as rs
if rs.IsHatchPattern("Hatch2"): rs.CurrentHatchPattern("Hatch2")
```

### See Also

HatchPatternCount, HatchPatternNames

---

## ExplodeHatch

### Signature

```python
ExplodeHatch(hatch_id, delete=False)
```

### Description

Explodes a hatch object into its component objects. The exploded objects will be added to the document. If the hatch object uses a solid pattern, then planar face Brep objects will be created. Otherwise, line curve objects will be created

### Returns

list(guid, ...): list of identifiers for the newly created objects None: on error

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select object")
if rs.IsHatch(id): rs.ExplodeHatch(id, True)
```

### See Also

IsHatch, HatchPattern, HatchRotation, HatchScale

---

## HatchPattern

### Signature

```python
HatchPattern(hatch_id, hatch_pattern=None)
```

### Description

Returns or changes a hatch object's hatch pattern

### Returns

str: if hatch_pattern is not specified, the current hatch pattern str: if hatch_pattern is specified, the previous hatch pattern None: on error

### Example

```python
import rhinoscriptsyntax as rs
objects = rs.AllObjects()
if objects is not None:
 for obj in objects:
 if rs.IsHatch(obj) and rs.HatchPattern(obj)=="Solid":
 rs.SelectObject(obj)
```

### See Also

AddHatch, AddHatches, HatchRotation, HatchScale, IsHatch

---

## HatchPatternCount

### Signature

```python
HatchPatternCount()
```

### Description

Returns the number of hatch patterns in the document

### Returns

number: the number of hatch patterns in the document

### Example

```python
import rhinoscriptsyntax as rs
print("There are {} hatch patterns.".format(rs.HatchPatternCount()))
```

### See Also

HatchPatternNames

---

## HatchPatternDescription

### Signature

```python
HatchPatternDescription(hatch_pattern)
```

### Description

Returns the description of a hatch pattern. Note, not all hatch patterns have descriptions

### Returns

str: description of the hatch pattern on success otherwise None

### Example

```python
import rhinoscriptsyntax as rs
patterns = rs.HatchPatternNames()
for pattern in patterns:
 description = rs.HatchPatternDescription(pattern)
 if description: print("{} - {}".format(pattern, description))
 else: print(pattern)
```

### See Also

HatchPatternCount, HatchPatternNames

---

## HatchPatternFillType

### Signature

```python
HatchPatternFillType(hatch_pattern)
```

### Description

Returns the fill type of a hatch pattern.

### Returns

number: hatch pattern's fill type if successful 0 = solid, uses object color 1 = lines, uses pattern file definition 2 = gradient, uses fill color definition None: if unsuccessful

### Example

```python
import rhinoscriptsyntax as rs
patterns = rs.HatchPatternNames()
for pattern in patterns:
 fill = rs.HatchPatternFillType(pattern)
 print("{} - {}".format(pattern, fill))
```

### See Also

HatchPatternCount, HatchPatternNames

---

## HatchPatternNames

### Signature

```python
HatchPatternNames()
```

### Description

Returns the names of all of the hatch patterns in the document

### Returns

list(str, ...): the names of all of the hatch patterns in the document

### Example

```python
import rhinoscriptsyntax as rs
patterns = rs.HatchPatternNames()
for pattern in patterns:
 description = rs.HatchPatternDescription(pattern)
 if description: print("{} - {}".format(pattern, description))
 else: print(pattern)
```

### See Also

HatchPatternCount

---

## HatchRotation

### Signature

```python
HatchRotation(hatch_id, rotation=None)
```

### Description

Returns or modifies the rotation applied to the hatch pattern when it is mapped to the hatch's plane

### Returns

number: if rotation is not defined, the current rotation angle number: if rotation is specified, the previous rotation angle None: on error

### Example

```python
import rhinoscriptsyntax as rs
objects = rs.AllObjects()
if objects:
 for obj in objects:
 if rs.IsHatch(obj) and rs.HatchRotation(obj)>0:
 rs.HatchRotation(obj,0)
```

### See Also

AddHatch, AddHatches, HatchPattern, HatchScale, IsHatch

---

## HatchScale

### Signature

```python
HatchScale(hatch_id, scale=None)
```

### Description

Returns or modifies the scale applied to the hatch pattern when it is mapped to the hatch's plane

### Returns

number: if scale is not defined, the current scale factor number: if scale is defined, the previous scale factor None: on error

### Example

```python
import rhinoscriptsyntax as rs
objects = rs.NormalObjects()
if objects:
 for obj in objects:
 if rs.IsHatch(obj) and rs.HatchScale(obj)>1.0:
 rs.HatchScale(obj, 1.0)
```

### See Also

HatchPattern, HatchRotation, IsHatch

---

## IsHatch

### Signature

```python
IsHatch(object_id)
```

### Description

Verifies the existence of a hatch object in the document

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if rs.IsHatch(obj): print("Object is a hatch")
else: print("Object is not a hatch")
```

### See Also

HatchPattern, HatchRotation, HatchScale

---

## IsHatchPattern

### Signature

```python
IsHatchPattern(name)
```

### Description

Verifies the existence of a hatch pattern in the document

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
hatch = rs.GetString("Hatch pattern name")
if rs.IsHatchPattern(hatch): print("The hatch pattern exists.")
else: print("The hatch pattern does not exist.")
```

### See Also

IsHatchPatternCurrent, IsHatchPatternReference

---

## IsHatchPatternCurrent

### Signature

```python
IsHatchPatternCurrent(hatch_pattern)
```

### Description

Verifies that a hatch pattern is the current hatch pattern

### Returns

bool: True or False None: on error

### Example

```python
import rhinoscriptsyntax as rs
hatch = rs.GetString("Hatch pattern name")
if rs.IsHatchPattern(hatch):
 if rs.IsHatchPatternCurrent(hatch):
 print("The hatch pattern is current.")
 else:
 print("The hatch pattern is not current.")
else: print("The hatch pattern does not exist.")
```

### See Also

IsHatchPattern, IsHatchPatternReference

---

## IsHatchPatternReference

### Signature

```python
IsHatchPatternReference(hatch_pattern)
```

### Description

Verifies that a hatch pattern is from a reference file

### Returns

bool: True or False None: on error

### Example

```python
import rhinoscriptsyntax as rs
hatch = rs.GetString("Hatch pattern name")
if rs.IsHatchPattern(hatch):
 if rs.IsHatchPatternReference(hatch):
 print("The hatch pattern is reference.")
 else:
 print("The hatch pattern is not reference.")
else:
 print("The hatch pattern does not exist.")
```

### See Also

IsHatchPattern, IsHatchPatternCurrent

---

# Layer

*33 functions | 8 in use*

---

## AddLayer

** IN USE**

### Signature

```python
AddLayer(name=None, color=None, visible=True, locked=False, parent=None)
```

### Description

Add a new layer to the document

### Returns

str: The full name of the new layer if successful.

### Example

```python
import rhinoscriptsyntax as rs
from System.Drawing import Color
print("New layer:{}".format(rs.AddLayer()))
print("New layer:{}".format(rs.AddLayer("MyLayer1")))
print("New layer:{}".format(rs.AddLayer("MyLayer2", Color.DarkSeaGreen)))
print("New layer:{}".format(rs.AddLayer("MyLayer3", Color.Cornsilk)))
print("New layer:{}".format(rs.AddLayer("MyLayer4",parent="MyLayer3")))
```

### See Also

CurrentLayer, DeleteLayer, RenameLayer

---

## CurrentLayer

** IN USE**

### Signature

```python
CurrentLayer(layer=None)
```

### Description

Returns or changes the current layer

### Returns

str: If a layer name is not specified, the full name of the current layer str: If a layer name is specified, the full name of the previous current layer

### Example

```python
import rhinoscriptsyntax as rs
rs.AddLayer("MyLayer")
rs.CurrentLayer("MyLayer")
```

### See Also

AddLayer, DeleteLayer, RenameLayer

---

## DeleteLayer

** IN USE**

### Signature

```python
DeleteLayer(layer)
```

### Description

Removes an existing layer from the document. The layer to be removed cannot be the current layer. Unlike the PurgeLayer method, the layer must be empty, or contain no objects, before it can be removed. Any layers that are children of the specified layer will also be removed if they are also empty.

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
layer = rs.GetString("Layer to remove")
if layer: rs.DeleteLayer(layer)
```

### See Also

AddLayer, CurrentLayer, PurgeLayer, RenameLayer

---

## ExpandLayer

### Signature

```python
ExpandLayer( layer, expand )
```

### Description

Expands a layer. Expanded layers can be viewed in Rhino's layer dialog

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
if rs.IsLayerExpanded("Default"):
 rs.ExpandLayer( "Default", False )
```

### See Also

IsLayerExpanded

---

## IsLayer

** IN USE**

### Signature

```python
IsLayer(layer)
```

### Description

Verifies the existance of a layer in the document

### Returns

bool: True on success otherwise False

### Example

```python
import rhinoscriptsyntax as rs
layer = rs.GetString("Layer name")
if rs.IsLayer(layer):
 print("The layer exists.")
else:
 print("The layer does not exist.")
```

### See Also

IsLayerChangeable, IsLayerEmpty, IsLayerLocked, IsLayerOn, IsLayerReference, IsLayerSelectable, IsLayerVisible

---

## IsLayerChangeable

### Signature

```python
IsLayerChangeable(layer)
```

### Description

Verifies that the objects on a layer can be changed (normal)

### Returns

bool: True on success otherwise False

### Example

```python
import rhinoscriptsyntax as rs
layer = rs.GetString("Layer name")
if rs.IsLayer(layer):
 if rs.IsLayerChangeable(layer): print("The layer is changeable.")
 else: print("The layer is not changeable.")
else:
 print("The layer does not exist.")
```

### See Also

IsLayer, IsLayerEmpty, IsLayerLocked, IsLayerOn, IsLayerReference, IsLayerSelectable, IsLayerVisible

---

## IsLayerChildOf

### Signature

```python
IsLayerChildOf(layer, test)
```

### Description

Verifies that a layer is a child of another layer

### Returns

bool: True on success otherwise False

### Example

```python
import rhinoscriptsyntax as rs
rs.AddLayer("MyLayer1")
rs.AddLayer("MyLayer2", parent="MyLayer1")
rs.AddLayer("MyLayer3", parent="MyLayer2")
rs.MessageBox( rs.IsLayerChildOf("MyLayer1", "MyLayer3") )
```

### See Also

IsLayerParentOf

---

## IsLayerCurrent

### Signature

```python
IsLayerCurrent(layer)
```

### Description

Verifies that a layer is the current layer

### Returns

bool: True on success otherwise False

### Example

```python
import rhinoscriptsyntax as rs
layer = rs.GetString("Layer name")
if rs.IsLayer(layer):
 if rs.IsLayerCurrent(layer): print("The layer is current.")
 else: print("The layer is not current.")
else:
 print("The layer does not exist.")
```

### See Also

IsLayer, IsLayerEmpty, IsLayerLocked, IsLayerOn, IsLayerReference, IsLayerSelectable, IsLayerVisible

---

## IsLayerEmpty

### Signature

```python
IsLayerEmpty(layer)
```

### Description

Verifies that an existing layer is empty, or contains no objects

### Returns

bool: True on success otherwise False

### Example

```python
import rhinoscriptsyntax as rs
layer = rs.GetString("Layer name")
if rs.IsLayer(layer):
 if rs.IsLayerEmpty(layer): print("The layer is empty.")
 else: print("The layer is not empty.")
else:
 print("The layer does not exist.")
```

### See Also

IsLayerChangeable, IsLayerLocked, IsLayerOn, IsLayerReference, IsLayerSelectable, IsLayerVisible

---

## IsLayerExpanded

### Signature

```python
IsLayerExpanded(layer)
```

### Description

Verifies that a layer is expanded. Expanded layers can be viewed in Rhino's layer dialog

### Returns

bool: True on success otherwise False

### Example

```python
import rhinoscriptsyntax as rs
if rs.IsLayerExpanded("Default"):
 rs.ExpandLayer( "Default", False )
```

### See Also

ExpandLayer

---

## IsLayerOn

### Signature

```python
IsLayerOn(layer)
```

### Description

Verifies that a layer is on.

### Returns

bool: True on success otherwise False

### Example

```python
import rhinoscriptsyntax as rs
layer = rs.GetString("Layer name")
if rs.IsLayer(layer):
 if rs.IsLayerOn(layer): print("The layer is on.")
 else: print("The layer is not on.")
else:
 print("The layer does not exist.")
```

### See Also

IsLayer, IsLayerChangeable, IsLayerEmpty, IsLayerLocked, IsLayerReference, IsLayerSelectable, IsLayerVisible

---

## IsLayerParentOf

### Signature

```python
IsLayerParentOf(layer, test)
```

### Description

Verifies that a layer is a parent of another layer

### Returns

bool: True on success otherwise False

### Example

```python
import rhinoscriptsyntax as rs
rs.AddLayer("MyLayer1")
rs.AddLayer("MyLayer2", parent="MyLayer1")
rs.AddLayer("MyLayer3", parent="MyLayer2")
rs.MessageBox( rs.IsLayerParentOf("MyLayer3", "MyLayer1") )
```

### See Also

IsLayerChildOf

---

## IsLayerReference

### Signature

```python
IsLayerReference(layer)
```

### Description

Verifies that a layer is from a reference file.

### Returns

bool: True on success otherwise False

### Example

```python
import rhinoscriptsyntax as rs
layer = rs.GetString("Layer name")
if rs.IsLayer(layer):
 if rs.IsLayerReference(layer): print("The layer is a reference layer.")
 else: print("The layer is not a reference layer.")
else:
 print("The layer does not exist.")
```

### See Also

IsLayer, IsLayerChangeable, IsLayerEmpty, IsLayerLocked, IsLayerOn, IsLayerSelectable, IsLayerVisible

---

## IsLayerSelectable

### Signature

```python
IsLayerSelectable(layer)
```

### Description

Verifies that an existing layer is selectable (normal and reference)

### Returns

bool: True on success otherwise False

### Example

```python
import rhinoscriptsyntax as rs
layer = rs.GetString("Layer name")
if rs.IsLayer(layer):
 if rs.IsLayerSelectable(layer): print("The layer is selectable.")
 else: print("The layer is not selectable.")
else:
 print("The layer does not exist.")
```

### See Also

IsLayer, IsLayerChangeable, IsLayerEmpty, IsLayerLocked, IsLayerOn, IsLayerReference, IsLayerVisible

---

## IsLayerVisible

### Signature

```python
IsLayerVisible(layer)
```

### Description

Verifies that a layer is visible (normal, locked, and reference)

### Returns

bool: True on success otherwise False

### Example

```python
import rhinoscriptsyntax as rs
layer = rs.GetString("Layer name")
if rs.IsLayer(layer):
 if rs.IsLayerVisible(layer): print("The layer is visible")
 else: print("The layer is not visible")
else:
 print("The layer does not exist.")
```

### See Also

IsLayer, IsLayerChangeable, IsLayerEmpty, IsLayerLocked, IsLayerOn, IsLayerReference, IsLayerSelectable

---

## LayerChildCount

### Signature

```python
LayerChildCount(layer)
```

### Description

Returns the number of immediate child layers of a layer

### Returns

number: the number of immediate child layers if successful

### Example

```python
import rhinoscriptsyntax as rs
children = rs.LayerChildCount("Default")
if children: rs.ExpandLayer("Default", True)
```

### See Also

LayerChildren

---

## LayerChildren

### Signature

```python
LayerChildren(layer)
```

### Description

Returns the immediate child layers of a layer

### Returns

list(str, ...): List of children layer names

### Example

```python
import rhinoscriptsyntax as rs
children = rs.LayerChildren("Default")
if children:
 for child in children: print(child)
```

### See Also

LayerChildCount, ParentLayer

---

## LayerColor

** IN USE**

### Signature

```python
LayerColor(layer, color=None)
```

### Description

Returns or changes the color of a layer.

### Returns

color: If a color value is not specified, the current color value on success color: If a color value is specified, the previous color value on success

### Example

```python
import rhinoscriptsyntax as rs
import random
from System.Drawing import Color

def randomcolor():
 red = int(255*random.random())
 green = int(255*random.random())
 blue = int(255*random.random())
 return Color.FromArgb(red,green,blue)

layerNames = rs.LayerNames()
if layerNames:
 for name in layerNames: rs.LayerColor(name, randomcolor())
```

---

## LayerCount

### Signature

```python
LayerCount()
```

### Description

Returns the number of layers in the document

### Returns

number: the number of layers in the document

### Example

```python
import rhinoscriptsyntax as rs
count = rs.LayerCount()
print("There are {} layers".format(count))
```

### See Also

LayerNames

---

## LayerId

### Signature

```python
LayerId(layer)
```

### Description

Returns the identifier of a layer given the layer's name.

### Returns

guid (str): The layer's identifier if successful. None: If not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
id = rs.LayerId('Layer 01')
```

### See Also

LayerName

---

## LayerIds

### Signature

```python
LayerIds()
```

### Description

Return identifiers of all layers in the document

### Returns

list(guid, ...): the identifiers of all layers in the document

### Example

```python
import rhinoscriptsyntax as rs
layers = rs.LayerIds()
for layer in layers: print(layer)
```

### See Also

LayerCount, LayerNames

---

## LayerLinetype

### Signature

```python
LayerLinetype(layer, linetype=None)
```

### Description

Returns or changes the linetype of a layer

### Returns

str: If linetype is not specified, name of the current linetype str: If linetype is specified, name of the previous linetype

### Example

```python
import rhinoscriptsyntax as rs
layers = rs.LayerNames()
if layers:
 for layer in layers:
 if rs.LayerLinetype(layer)!="Continuous":
 rs.LayerLinetype(layer,"Continuous")
```

### See Also

LayerPrintColor, LayerPrintWidth

---

## LayerLocked

** IN USE**

### Signature

```python
LayerLocked(layer, locked=None)
```

### Description

Returns or changes the locked mode of a layer

### Returns

bool: If locked is not specified, the current layer locked mode bool: If locked is specified, the previous layer locked mode

### Example

```python
import rhinoscriptsyntax as rs
layers = rs.LayerNames()
if layers:
 for layer in layers:
 if rs.LayerLocked(layer): rs.LayerLocked(layer, False)
```

### See Also

LayerVisible

---

## LayerMaterialIndex

### Signature

```python
LayerMaterialIndex(layer,index=None)
```

### Description

Returns or changes the material index of a layer. A material index of -1 indicates that no material has been assigned to the layer. Thus, the layer will use Rhino's default layer material

### Returns

number: a zero-based material index if successful

### Example

```python
import rhinoscriptsyntax as rs
index = rs.LayerMaterialIndex("Default")
if index is not None:
 if index==-1:
 print("The default layer does not have a material assigned.")
 else:
 print("The default layer has a material assigned.")
```

---

## LayerName

### Signature

```python
LayerName(layer_id, fullpath=True)
```

### Description

Return the name of a layer given it's identifier

### Returns

str: the layer's name if successful None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
layers = rs.LayerIds()
if layers:
 for layer in layers: print(rs.LayerName(layer))
```

### See Also

LayerId

---

## LayerNames

** IN USE**

### Signature

```python
LayerNames(sort=False)
```

### Description

Returns the names of all layers in the document.

### Returns

list(str, ...): list of layer names

### Example

```python
import rhinoscriptsyntax as rs
layers = rs.LayerNames()
if layers:
 for layer in layers: print(layer)
```

### See Also

LayerCount

---

## LayerOrder

### Signature

```python
LayerOrder(layer)
```

### Description

Returns the current display order index of a layer as displayed in Rhino's layer dialog box. A display order index of -1 indicates that the current layer dialog filter does not allow the layer to appear in the layer list

### Returns

number: 0 based index of layer

### Example

```python
import rhinoscriptsyntax as rs
index = rs.LayerOrder("Default")
if index is not None:
 if index==-1: print("The layer does not display in the Layer dialog.")
 else: print("The layer does display in the Layer dialog.")
```

---

## LayerPrintColor

### Signature

```python
LayerPrintColor(layer, color=None)
```

### Description

Returns or changes the print color of a layer. Layer print colors are represented as RGB colors.

### Returns

color: if color is not specified, the current layer print color color: if color is specified, the previous layer print color None: on error

### Example

```python
import rhinoscriptsyntax as rs
layers = rs.LayerNames()
if layers:
 for layer in layers:
 black = rs.CreateColor((0,0,0))
 if rs.LayerPrintColor(layer)!=black:
 rs.LayerPrintColor(layer, black)
```

### See Also

LayerLinetype, LayerPrintWidth

---

## LayerPrintWidth

### Signature

```python
LayerPrintWidth(layer, width=None)
```

### Description

Returns or changes the print width of a layer. Print width is specified in millimeters. A print width of 0.0 denotes the "default" print width.

### Returns

number: if width is not specified, the current layer print width number: if width is specified, the previous layer print width

### Example

```python
import rhinoscriptsyntax as rs
layers = rs.LayerNames()
if layers:
 for layer in layers:
 if rs.LayerPrintWidth(layer)!=0:
 rs.LayerPrintWidth(layer, 0)
```

### See Also

LayerLinetype, LayerPrintColor

---

## LayerVisible

** IN USE**

### Signature

```python
LayerVisible(layer, visible=None, forcevisible_or_donotpersist=False)
```

### Description

Returns or changes the visible property of a layer.

### Returns

bool: if visible is not specified, the current layer visibility bool: if visible is specified, the previous layer visibility

### Example

```python
import rhinoscriptsyntax as rs
layers = rs.LayerNames()
if layers:
 for layer in layers:
 if rs.LayerVisible(layer)==False:
 rs.LayerVisible(layer,True)
```

### See Also

LayerLocked

---

## ParentLayer

### Signature

```python
ParentLayer(layer, parent=None)
```

### Description

Return or modify the parent layer of a layer

### Returns

str: If parent is not specified, the name of the current parent layer str: If parent is specified, the name of the previous parent layer None: if the layer does not have a parent

### Example

```python
import rhinoscriptsyntax as rs
layers = rs.LayerNames()
for layer in layers:
 parent = rs.ParentLayer(layer)
 print("Layer: {}, Parent: {}".format(layer, parent))
```

### See Also

LayerChildren

---

## PurgeLayer

### Signature

```python
PurgeLayer(layer)
```

### Description

Removes an existing layer from the document. The layer will be removed even if it contains geometry objects. The layer to be removed cannot be the current layer empty.

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
layer = rs.GetString("Layer to purge")
if layer: rs.PurgeLayer(layer)
```

### See Also

AddLayer, CurrentLayer, DeleteLayer, RenameLayer

---

## RenameLayer

### Signature

```python
RenameLayer(oldname, newname)
```

### Description

Renames an existing layer

### Returns

str: The new layer name if successful otherwise None

### Example

```python
import rhinoscriptsyntax as rs
oldname = rs.GetString("Old layer name")
if oldname:
 newname = rs.GetString("New layer name")
 if newname: rs.RenameLayer(oldname, newname)
```

### See Also

AddLayer, CurrentLayer, DeleteLayer

---

# Light

*24 functions | 0 in use*

---

## AddDirectionalLight

### Signature

```python
AddDirectionalLight(start_point, end_point)
```

### Description

Adds a new directional light object to the document

### Returns

(guid): identifier of the new object if successful

### Example

```python
import rhinoscriptsyntax as rs
end = rs.GetPoint("End of light vector direction")
if end:
 start = rs.GetPoint("Start of light vector direction", end)
 if start: rs.AddDirectionalLight( start, end )
```

### See Also

IsDirectionalLight

---

## AddLinearLight

### Signature

```python
AddLinearLight(start_point, end_point, width=None)
```

### Description

Adds a new linear light object to the document

### Returns

guid: identifier of the new object if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
start = rs.GetPoint("Light origin")
if start:
 end = rs.GetPoint("Light length and direction", start)
 if end: rs.AddLinearLight(start, end)
```

### See Also

IsLinearLight

---

## AddPointLight

### Signature

```python
AddPointLight(point)
```

### Description

Adds a new point light object to the document

### Returns

guid: identifier of the new object if successful

### Example

```python
import rhinoscriptsyntax as rs
point = rs.GetPoint("Point light location")
if point: rs.AddPointLight(point)
```

### See Also

IsPointLight

---

## AddRectangularLight

### Signature

```python
AddRectangularLight(origin, width_point, height_point)
```

### Description

Adds a new rectangular light object to the document

### Returns

guid: identifier of the new object if successful

### Example

```python
import rhinoscriptsyntax as rs
rect = rs.GetRectangle(2)
if rect: rs.AddRectangularLight( rect[0], rect[1], rect[3] )
```

### See Also

IsRectangularLight

---

## AddSpotLight

### Signature

```python
AddSpotLight(origin, radius, apex_point)
```

### Description

Adds a new spot light object to the document

### Returns

guid: identifier of the new object

### Example

```python
import rhinoscriptsyntax as rs
radius = 5.0
origin = rs.GetPoint("Base of cone")
if origin:
 apex = rs.GetPoint("End of cone", origin)
 if apex: rs.AddSpotLight(origin, radius, apex)
```

### See Also

IsSpotLight, SpotLightHardness, SpotLightShadowIntensity

---

## EnableLight

### Signature

```python
EnableLight(object_id, enable=None)
```

### Description

Enables or disables a light object

### Returns

bool: if enable is not specified, the current enabled status bool: if enable is specified, the previous enabled status None: on error

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select light", rs.filter.light)
if id: rs.EnableLight( id, False )
```

### See Also

IsLight, IsLightEnabled, LightColor, LightCount, LightName, LightObjects

---

## IsDirectionalLight

### Signature

```python
IsDirectionalLight(object_id)
```

### Description

Verifies a light object is a directional light

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a light", rs.filter.light)
if rs.IsDirectionalLight(id):
 print("The object is a directional light.")
else:
 print("The object is not a directional light.")
```

### See Also

AddDirectionalLight

---

## IsLight

### Signature

```python
IsLight(object_id)
```

### Description

Verifies an object is a light object

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a light")
if rs.IsLight(id):
 print("The object is a light.")
else:
 print("The object is not a light.")
```

### See Also

EnableLight, IsLightEnabled, LightColor, LightCount, LightName, LightObjects

---

## IsLightEnabled

### Signature

```python
IsLightEnabled(object_id)
```

### Description

Verifies a light object is enabled

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a light", rs.filter.light)
if rs.IsLightEnabled(id):
 print("The light is enabled (on).")
else:
 print("The light is disabled (off).")
```

### See Also

EnableLight, IsLight, LightColor, LightCount, LightName, LightObjects

---

## IsLightReference

### Signature

```python
IsLightReference(object_id)
```

### Description

Verifies a light object is referenced from another file

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a light", rs.filter.light)
if rs.IsLightReference(id):
 print("The light is a reference object.")
else:
 print("The light is not a reference object.")
```

### See Also

IsObjectReference

---

## IsLinearLight

### Signature

```python
IsLinearLight(object_id)
```

### Description

Verifies a light object is a linear light

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a light", rs.filter.light)
if rs.IsLinearLight(id):
 print("The object is a linear light.")
else:
 print("The object is not a linear light.")
```

### See Also

AddLinearLight

---

## IsPointLight

### Signature

```python
IsPointLight(object_id)
```

### Description

Verifies a light object is a point light

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a light", rs.filter.light)
if rs.IsPointLight(id):
 print("The object is a point light.")
else:
 print("The object is not a point light.")
```

### See Also

AddPointLight

---

## IsRectangularLight

### Signature

```python
IsRectangularLight(object_id)
```

### Description

Verifies a light object is a rectangular light

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a light", rs.filter.light)
if rs.IsRectangularLight(id):
 print("The object is a rectangular light.")
else:
 print("The object is not a rectangular light.")
```

### See Also

AddRectangularLight

---

## IsSpotLight

### Signature

```python
IsSpotLight(object_id)
```

### Description

Verifies a light object is a spot light

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a light", rs.filter.light)
if rs.IsSpotLight(id):
 print("The object is a spot light.")
else:
 print("The object is not a spot light.")
```

### See Also

AddSpotLight, SpotLightHardness, SpotLightShadowIntensity

---

## LightColor

### Signature

```python
LightColor(object_id, color=None)
```

### Description

Returns or changes the color of a light

### Returns

color: if color is not specified, the current color color: if color is specified, the previous color

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a light", rs.filter.light)
if id: rs.LightColor( id, (0,255,255) )
```

### See Also

EnableLight, IsLight, IsLightEnabled, LightCount, LightName, LightObjects

---

## LightCount

### Signature

```python
LightCount()
```

### Description

Returns the number of light objects in the document

### Returns

number: the number of light objects in the document

### Example

```python
import rhinoscriptsyntax as rs
print("There are {} lights".format(rs.LightCount()))
```

### See Also

EnableLight, IsLight, IsLightEnabled, LightColor, LightName, LightObjects

---

## LightDirection

### Signature

```python
LightDirection(object_id, direction=None)
```

### Description

Returns or changes the direction of a light object

### Returns

vector: if direction is not specified, the current direction vector: if direction is specified, the previous direction

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a light", rs.filter.light)
if id: print( rs.LightDirection(id) )
```

### See Also

IsLight, LightLocation

---

## LightLocation

### Signature

```python
LightLocation(object_id, location=None)
```

### Description

Returns or changes the location of a light object

### Returns

point: if location is not specified, the current location point: if location is specified, the previous location

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a light", rs.filter.light)
if id: rs.AddPoint( rs.LightLocation(id) )
```

### See Also

IsLight, LightDirection

---

## LightName

### Signature

```python
LightName(object_id, name=None)
```

### Description

Returns or changes the name of a light object

### Returns

str: if name is not specified, the current name str: if name is specified, the previous name

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a light", rs.filter.light)
if id:
 name = rs.GetString("New light name")
 if name: rs.LightName(id, name)
```

### See Also

EnableLight, IsLight, IsLightEnabled, LightColor, LightCount, LightObjects

---

## LightObjects

### Signature

```python
LightObjects()
```

### Description

Returns list of identifiers of light objects in the document

### Returns

list(guid, ...): the list of identifiers of light objects in the document

### Example

```python
import rhinoscriptsyntax as rs
lights = rs.LightObjects()
if lights:
 rs.AddLayer( "Lights" )
 for light in lights: rs.ObjectLayer( light, "Lights" )
```

### See Also

EnableLight, IsLight, IsLightEnabled, LightColor, LightCount, LightName

---

## RectangularLightPlane

### Signature

```python
RectangularLightPlane(object_id)
```

### Description

Returns the plane of a rectangular light object

### Returns

plane: the plane if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a rectangular light", rs.filter.light)
if id:
 rc = rs.RectangularLightPlane(id)
 if rc:
 plane, extents = rc
 rs.AddPlaneSurface( plane, extents[0], extents[1] )
```

### See Also

IsRectangularLight

---

## SpotLightHardness

### Signature

```python
SpotLightHardness(object_id, hardness=None)
```

### Description

Returns or changes the hardness of a spot light. Spotlight hardness controls the fully illuminated region.

### Returns

number: if hardness is not specified, the current hardness number: if hardness is specified, the previous hardness

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a light", rs.filter.light)
if id: rs.SpotLightHardness(id, 0.75)
```

### See Also

AddSpotLight, IsSpotLight, SpotLightRadius, SpotLightShadowIntensity

---

## SpotLightRadius

### Signature

```python
SpotLightRadius(object_id, radius=None)
```

### Description

Returns or changes the radius of a spot light.

### Returns

number: if radius is not specified, the current radius number: if radius is specified, the previous radius

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a light", rs.filter.light)
if id: rs.SpotLightRadius(id, 5.0)
```

### See Also

AddSpotLight, IsSpotLight, SpotLightHardness, SpotLightShadowIntensity

---

## SpotLightShadowIntensity

### Signature

```python
SpotLightShadowIntensity(object_id, intensity=None)
```

### Description

Returns or changes the shadow intensity of a spot light.

### Returns

number: if intensity is not specified, the current intensity number: if intensity is specified, the previous intensity

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select a light", rs.filter.light)
if id: rs.SpotLightShadowIntensity(id, 0.75)
```

### See Also

AddSpotLight, IsSpotLight, SpotLightHardness, SpotLightRadius

---

# Line

*10 functions | 0 in use*

---

## LineClosestPoint

### Signature

```python
LineClosestPoint(line, testpoint)
```

### Description

Finds the point on an infinite line that is closest to a test point

### Returns

point: the point on the line that is closest to the test point if successful, otherwise None

### Example

```python
import rhinoscriptsyntax as rs
line = (0,0,0), (5,5,0)
point = (15, 10, 0)
result = rs.LineClosestPoint( line, point)
if result: rs.AddPoint(result)
```

### See Also

LineIsFartherThan, LineMaxDistanceTo, LineMinDistanceTo, LinePlane, LineTransform

---

## LineCylinderIntersection

### Signature

```python
LineCylinderIntersection(line, cylinder_plane, cylinder_height, cylinder_radius)
```

### Description

Calculates the intersection of a line and a cylinder

### Returns

list(point, ...): list of intersection points (0, 1, or 2 points)

### Example

```python
import rhinoscriptsyntax as rs
plane = rs.WorldXYPlane()
line = (-10,0,0), (10,0,10)
points = rs.LineCylinderIntersection(line, plane, cylinder_height=10, cylinder_radius=5)
if points:
 for point in points: rs.AddPoint(point)
```

### See Also

LineLineIntersection, LinePlaneIntersection, LineSphereIntersection

---

## LineIsFartherThan

### Signature

```python
LineIsFartherThan(line, distance, point_or_line)
```

### Description

Determines if the shortest distance from a line to a point or another line is greater than a specified distance

### Returns

bool: True if the shortest distance from the line to the other project is greater than distance, False otherwise None: on error

### Example

```python
import rhinoscriptsyntax as rs
line = (0,0,0), (10,10,0)
testPoint = (10,5,0)
print(rs.LineIsFartherThan(line, 3, testPoint))
```

### See Also

LineClosestPoint, LineMaxDistanceTo, LineMinDistanceTo, LinePlane, LineTransform

---

## LineLineIntersection

### Signature

```python
LineLineIntersection(lineA, lineB)
```

### Description

Calculates the intersection of two non-parallel lines. Note, the two lines do not have to intersect for an intersection to be found. (see help)

### Returns

tuple(point, point): containing a point on the first line and a point on the second line if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
lineA = (1,1,0), (5,0,0)
lineB = (1,3,0), (5,5,0)
point = rs.LineLineIntersection(lineA, lineB)
if point:
 rs.AddPoint(point[0])
 rs.AddPoint(point[1])
```

### See Also

IntersectPlanes, LinePlaneIntersection, PlanePlaneIntersection

---

## LineMaxDistanceTo

### Signature

```python
LineMaxDistanceTo(line, point_or_line)
```

### Description

Finds the longest distance between a line as a finite chord, and a point or another line

### Returns

number: A distance (D) such that if Q is any point on the line and P is any point on the other object, then D >= Rhino.Distance(Q, P). None: on error

### Example

```python
import rhinoscriptsyntax as rs
line = (0,0,0), (10,10,0)
print(rs.LineMaxDistanceTo( line, (10,5,0) ))
```

### See Also

LineClosestPoint, LineIsFartherThan, LineMinDistanceTo, LinePlane, LineTransform

---

## LineMinDistanceTo

### Signature

```python
LineMinDistanceTo(line, point_or_line)
```

### Description

Finds the shortest distance between a line as a finite chord, and a point or another line

### Returns

number: A distance (D) such that if Q is any point on the line and P is any point on the other object, then D <= Rhino.Distance(Q, P). None: on error

### Example

```python
import rhinoscriptsyntax as rs
line = (0,0,0), (10,10,0)
print(rs.LineMinDistanceTo(line, (10,5,0)))
```

### See Also

LineClosestPoint, LineIsFartherThan, LineMaxDistanceTo, LinePlane, LineTransform

---

## LinePlane

### Signature

```python
LinePlane(line)
```

### Description

Returns a plane that contains the line. The origin of the plane is at the start of the line. If possible, a plane parallel to the world XY, YZ, or ZX plane is returned

### Returns

plane: the plane if successful None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
lineFrom = (0,0,0)
lineTo = (10,10,0)
distance = rs.Distance(lineFrom, lineTo)
plane = rs.LinePlane([lineFrom, lineTo])
rs.AddPlaneSurface( plane, distance, distance )
```

### See Also

LineClosestPoint, LineIsFartherThan, LineMaxDistanceTo, LineMinDistanceTo, LineTransform

---

## LinePlaneIntersection

### Signature

```python
LinePlaneIntersection(line, plane)
```

### Description

Calculates the intersection of a line and a plane.

### Returns

point: The 3D point of intersection is successful. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
plane = rs.WorldXYPlane()
line = (2, 11, 13), (20, 4, -10)
point = rs.LinePlaneIntersection(line, plane)
if( point!=None ): rs.AddPoint(point)
```

### See Also

LineLineIntersection, PlanePlaneIntersection

---

## LineSphereIntersection

### Signature

```python
LineSphereIntersection(line, sphere_center, sphere_radius)
```

### Description

Calculates the intersection of a line and a sphere

### Returns

list(point, ...): list of intersection points if successful, otherwise None

### Example

```python
import rhinoscriptsyntax as rs
radius = 10
line = (-10,0,0), (10,0,10)
points = rs.LineSphereIntersection(line, (0,0,0), radius)
if points:
 for point in points: rs.AddPoint(point)
```

### See Also

LineCylinderIntersection, LineLineIntersection, LinePlaneIntersection

---

## LineTransform

### Signature

```python
LineTransform(line, xform)
```

### Description

Transforms a line

### Returns

guid: transformed line

### Example

```python
import rhinoscriptsyntax as rs
line = (0,0,0), (10,10,0)
rs.AddLine( line[0], line[1] )
plane = rs.WorldXYPlane()
xform = rs.XformRotation(30, plane.Zaxis, plane.Origin)
line = rs.LineTransform(line, xform)
rs.AddLine( line.From, line.To )
```

### See Also

LineClosestPoint, LineIsFartherThan, LineMaxDistanceTo, LineMinDistanceTo, LinePlane

---

# Linetype

*4 functions | 0 in use*

---

## IsLinetype

### Signature

```python
IsLinetype(name_or_id)
```

### Description

Verifies the existance of a linetype in the document

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
name = rs.GetString("Linetype name")
if rs.IsLinetype(name): print("The linetype exists.")
else: print("The linetype does not exist")
```

### See Also

IsLinetypeReference

---

## IsLinetypeReference

### Signature

```python
IsLinetypeReference(name_or_id)
```

### Description

Verifies that an existing linetype is from a reference file

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
name = rs.GetString("Linetype name")
if rs.IsLinetype(name):
 if rs.IsLinetypeReference(name):
 print("The linetype is a reference linetype.")
 else:
 print("The linetype is not a reference linetype.")
else:
 print("The linetype does not exist.")
```

### See Also

IsLinetype

---

## LinetypeCount

### Signature

```python
LinetypeCount()
```

### Description

Returns number of linetypes in the document

### Returns

number: the number of linetypes in the document

### Example

```python
import rhinoscriptsyntax as rs
count = rs.LinetypeCount()
print("There are {} linetypes".format(count))
```

### See Also

LinetypeNames

---

## LinetypeNames

### Signature

```python
LinetypeNames(sort=False)
```

### Description

Returns names of all linetypes in the document

### Returns

list(str, ...): list of linetype names if successful

### Example

```python
import rhinoscriptsyntax as rs
names = rs.LinetypeNames()
if names:
 for name in names: print(name)
```

### See Also

LinetypeCount

---

# Material

*16 functions | 0 in use*

---

## AddMaterialToLayer

### Signature

```python
AddMaterialToLayer(layer)
```

### Description

Add material to a layer and returns the new material's index. If the layer already has a material, then the layer's current material index is returned

### Returns

number: Material index of the layer if successful None: if not successful or on error

### Example

```python
import rhinoscriptsyntax as rs
layer = rs.CurrentLayer()
index = rs.LayerMaterialIndex(layer)
if index==-1: index = rs.AddMaterialToLayer(layer)
```

### See Also

LayerMaterialIndex, IsMaterialDefault

---

## AddMaterialToObject

### Signature

```python
AddMaterialToObject(object_id)
```

### Description

Adds material to an object and returns the new material's index. If the object already has a material, the the object's current material index is returned.

### Returns

number: material index of the object

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject()
if obj:
 index = rs.ObjectMaterialIndex(obj)
 if index==-1: index = rs.AddMaterialToObject(obj)
```

### See Also

IsMaterialDefault, ObjectMaterialIndex, ObjectMaterialSource

---

## CopyMaterial

### Signature

```python
CopyMaterial(source_index, destination_index)
```

### Description

Copies definition of a source material to a destination material

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
src = rs.LayerMaterialIndex("Default")
dest = rs.LayerMaterialIndex(rs.CurrentLayer())
if src>=0 and dest>=0 and src!=dest:
 rs.CopyMaterial( src, dest )
```

### See Also

LayerMaterialIndex, ObjectMaterialIndex

---

## IsMaterialDefault

### Signature

```python
IsMaterialDefault(material_index)
```

### Description

Verifies a material is a copy of Rhino's built-in "default" material. The default material is used by objects and layers that have not been assigned a material.

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject()
if obj:
 index = rs.ObjectMaterialIndex(obj)
 if rs.IsMaterialDefault(index):
 print("Object is assigned default material.")
 else:
 print("Object is not assigned default material.")
```

### See Also

LayerMaterialIndex, ObjectMaterialIndex

---

## IsMaterialReference

### Signature

```python
IsMaterialReference(material_index)
```

### Description

Verifies a material is referenced from another file

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject()
if obj:
 index = rs.ObjectMaterialIndex(obj)
 if rs.IsMaterialReference(index):
 print("The material is referenced from another file.")
 else:
 print("The material is not referenced from another file.")
```

### See Also

IsLayerReference, IsLightReference, IsObjectReference

---

## MatchMaterial

### Signature

```python
MatchMaterial(source, destination)
```

### Description

Copies the material definition from one material to one or more objects

### Returns

number: number of objects that were modified if successful None: if not successful or on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select source object")
if obj and rs.ObjectMaterialIndex(obj)>-1:
 objects = rs.GetObjects("Select destination objects")
 if objects: rs.MatchMaterial( obj, objects )
```

### See Also

CopyMaterial, LayerMaterialIndex, ObjectMaterialIndex

---

## MaterialBump

### Signature

```python
MaterialBump(material_index, filename=None)
```

### Description

Returns or modifies a material's bump bitmap filename

### Returns

str: if filename is not specified, the current bump bitmap filename str: if filename is specified, the previous bump bitmap filename None: if not successful or on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if obj:
 index = rs.ObjectMaterialIndex(obj)
 if index>-1:
 rs.MaterialBump( index, "C:\\Users\\Steve\\Desktop\\bumpimage.png" )
```

### See Also

MaterialColor, MaterialName, MaterialReflectiveColor, MaterialShine, MaterialTexture, MaterialTransparency

---

## MaterialColor

### Signature

```python
MaterialColor(material_index, color=None)
```

### Description

Returns or modifies a material's diffuse color.

### Returns

color: if color is not specified, the current material color color: if color is specified, the previous material color None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if obj:
 index = rs.ObjectMaterialIndex(obj)
 if index>-1:
 rs.MaterialColor( index, (127, 255, 191) )
```

### See Also

MaterialBump, MaterialName, MaterialReflectiveColor, MaterialShine, MaterialTexture, MaterialTransparency

---

## MaterialEnvironmentMap

### Signature

```python
MaterialEnvironmentMap(material_index, filename=None)
```

### Description

Returns or modifies a material's environment bitmap filename.

### Returns

str: if filename is not specified, the current environment bitmap filename str: if filename is specified, the previous environment bitmap filename None: if not successful or on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if obj:
 index = rs.ObjectMaterialIndex(obj)
 if index>-1:
 rs.MaterialEnvironmentMap( index, "C:\\Users\\Steve\\Desktop\\emapimage.png" )
```

### See Also

MaterialBump, MaterialTexture, MaterialTransparencyMap

---

## MaterialName

### Signature

```python
MaterialName(material_index, name=None)
```

### Description

Returns or modifies a material's user defined name

### Returns

str: if name is not specified, the current material name str: if name is specified, the previous material name None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if obj:
 index = rs.ObjectMaterialIndex(obj)
 if index>-1:
 rs.MaterialName( index, "Fancy_Material" )
```

### See Also

MaterialBump, MaterialColor, MaterialReflectiveColor, MaterialShine, MaterialTexture, MaterialTransparency

---

## MaterialReflectiveColor

### Signature

```python
MaterialReflectiveColor(material_index, color=None)
```

### Description

Returns or modifies a material's reflective color.

### Returns

color: if color is not specified, the current material reflective color color: if color is specified, the previous material reflective color None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if obj:
 index = rs.ObjectMaterialIndex(obj)
 if index>-1:
 rs.MaterialReflectiveColor( index, (191, 191, 255) )
```

### See Also

MaterialBump, MaterialColor, MaterialName, MaterialShine, MaterialTexture, MaterialTransparency

---

## MaterialShine

### Signature

```python
MaterialShine(material_index, shine=None)
```

### Description

Returns or modifies a material's shine value

### Returns

number: if shine is not specified, the current material shine value number: if shine is specified, the previous material shine value None: on error

### Example

```python
import rhinoscriptsyntax as rs
MAX_SHINE = 255.0
obj = rs.GetObject("Select object")
if obj:
 index = rs.ObjectMaterialIndex(obj)
 if index>-1:
 rs.MaterialShine( index, MAX_SHINE/2 )
```

### See Also

MaterialBump, MaterialColor, MaterialName, MaterialReflectiveColor, MaterialTexture, MaterialTransparency

---

## MaterialTexture

### Signature

```python
MaterialTexture(material_index, filename=None)
```

### Description

Returns or modifies a material's texture bitmap filename

### Returns

str: if filename is not specified, the current texture bitmap filename str: if filename is specified, the previous texture bitmap filename None: if not successful or on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if obj:
 index = rs.ObjectMaterialIndex(obj)
 if index>-1:
 rs.MaterialTexture( index, "C:\\Users\\Steve\\Desktop\\textureimage.png" )
```

### See Also

MaterialBump, MaterialColor, MaterialName, MaterialReflectiveColor, MaterialShine, MaterialTransparency

---

## MaterialTransparency

### Signature

```python
MaterialTransparency(material_index, transparency=None)
```

### Description

Returns or modifies a material's transparency value

### Returns

number: if transparency is not specified, the current material transparency value number: if transparency is specified, the previous material transparency value None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if obj:
 index = rs.ObjectMaterialIndex(obj)
 if index>-1:
 rs.MaterialTransparency( index, 0.50 )
```

### See Also

MaterialBump, MaterialColor, MaterialName, MaterialReflectiveColor, MaterialShine, MaterialTexture

---

## MaterialTransparencyMap

### Signature

```python
MaterialTransparencyMap(material_index, filename=None)
```

### Description

Returns or modifies a material's transparency bitmap filename

### Returns

str: if filename is not specified, the current transparency bitmap filename str: if filename is specified, the previous transparency bitmap filename None: if not successful or on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if obj:
 index = rs.ObjectMaterialIndex(obj)
 if index>-1:
 rs.MaterialTransparencyMap( index, "C:\\Users\\Steve\\Desktop\\texture.png" )
```

### See Also

MaterialBump, MaterialEnvironmentMap, MaterialTexture

---

## ResetMaterial

### Signature

```python
ResetMaterial(material_index)
```

### Description

Resets a material to Rhino's default material

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if obj:
 index = rs.ObjectMaterialIndex(obj)
 if index>-1: rs.ResetMaterial(index)
```

### See Also

LayerMaterialIndex, ObjectMaterialIndex

---

# Mesh

*45 functions | 0 in use*

---

## AddMesh

### Signature

```python
AddMesh(vertices, face_vertices, vertex_normals=None, texture_coordinates=None, vertex_colors=None)
```

### Description

Add a mesh object to the document

### Returns

guid: Identifier of the new object if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
vertices = []
vertices.append((0.0,0.0,0.0))
vertices.append((5.0, 0.0, 0.0))
vertices.append((10.0, 0.0, 0.0))
vertices.append((0.0, 5.0, 0.0))
vertices.append((5.0, 5.0, 0.0))
vertices.append((10.0, 5.0, 0.0))
vertices.append((0.0, 10.0, 0.0))
vertices.append((5.0, 10.0, 0.0))
vertices.append((10.0, 10.0, 0.0))
faceVertices = []
faceVertices.append((0,1,4,4))
faceVertices.append((2,4,1,1))
faceVertices.append((0,4,3,3))
faceVertices.append((2,5,4,4))
faceVertices.append((3,4,6,6))
faceVertices.append((5,8,4,4))
faceVertices.append((6,4,7,7))
faceVertices.append((8,7,4,4))
rs.AddMesh( vertices, faceVertices )
```

### See Also

MeshFaces, MeshFaceVertices, MeshVertexNormals, MeshVertices

---

## AddPlanarMesh

### Signature

```python
AddPlanarMesh(object_id, delete_input=False)
```

### Description

Creates a planar mesh from a closed, planar curve

### Returns

guid: id of the new mesh on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select planar curves to build mesh", rs.filter.curve)
if obj: rs.AddPlanarMesh(obj)
```

### See Also

IsCurveClosed, IsCurvePlanar

---

## CurveMeshIntersection

### Signature

```python
CurveMeshIntersection(curve_id, mesh_id, return_faces=False)
```

### Description

Calculates the intersection of a curve object and a mesh object

### Returns

list(point, ...): if return_false is omitted or False, then a list of intersection points list([point, number], ...): if return_false is True, the a one-dimensional list containing information about each intersection. Each element contains the following two elements [0] = point of intersection [1] = mesh face index where intersection lies None: on error

### Example

```python
import rhinoscriptsyntax as rs
curve = rs.GetObject("Select curve to intersect", rs.filter.curve)
if curve:
 mesh = rs.GetObject("Select mesh to intersect", rs.filter.mesh)
 if mesh:
 cmx = rs.CurveMeshIntersection(curve, mesh, True)
 if cmx:
 for element in cmx:
 print("{}, Face index = {}".format(element[0], element[1]))
 rs.AddPoint(element[0])
```

### See Also

MeshClosestPoint, MeshMeshIntersection

---

## DisjointMeshCount

### Signature

```python
DisjointMeshCount(object_id)
```

### Description

Returns number of meshes that could be created by calling SplitDisjointMesh

### Returns

number: The number of meshes that could be created

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select mesh", rs.filter.mesh)
if rs.DisjointMeshCount(obj)>1: rs.SplitDisjointMesh(obj)
```

### See Also

IsMesh, SplitDisjointMesh

---

## DuplicateMeshBorder

### Signature

```python
DuplicateMeshBorder(mesh_id)
```

### Description

Creates curves that duplicates a mesh border

### Returns

list(guid, ...): list of curve ids on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select mesh", rs.filter.mesh)
if obj: rs.DuplicateMeshBorder(obj)
```

### See Also

DuplicateEdgeCurves, DuplicateSurfaceBorder

---

## ExplodeMeshes

### Signature

```python
ExplodeMeshes(mesh_ids, delete=False)
```

### Description

Explodes a mesh object, or mesh objects int submeshes. A submesh is a collection of mesh faces that are contained within a closed loop of unwelded mesh edges. Unwelded mesh edges are where the mesh faces that share the edge have unique mesh vertices (not mesh topology vertices) at both ends of the edge

### Returns

list(guid, ...): List of resulting objects after explode.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select mesh to explode", rs.filter.mesh)
if rs.IsMesh(obj): rs.ExplodeMeshes(obj)
```

### See Also

IsMesh

---

## IsMesh

### Signature

```python
IsMesh(object_id)
```

### Description

Verifies if an object is a mesh

### Returns

bool: True if successful, otherwise False

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a mesh")
if rs.IsMesh(obj):
 print("The object is a mesh.")
else:
 print("The object is not a mesh.")
```

### See Also

IsMeshClosed, MeshFaceCount, MeshFaces, MeshVertexCount, MeshVertices

---

## IsMeshClosed

### Signature

```python
IsMeshClosed(object_id)
```

### Description

Verifies a mesh object is closed

### Returns

bool: True if successful, otherwise False.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a mesh", rs.filter.mesh)
if rs.IsMeshClosed(obj):
 print("The mesh is closed.")
else:
 print("The mesh is not closed.")
```

### See Also

IsMesh

---

## IsMeshManifold

### Signature

```python
IsMeshManifold(object_id)
```

### Description

Verifies a mesh object is manifold. A mesh for which every edge is shared by at most two faces is called manifold. If a mesh has at least one edge that is shared by more than two faces, then that mesh is called non-manifold

### Returns

bool: True if successful, otherwise False.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a mesh", rs.filter.mesh)
if rs.IsMeshClosed(obj):
 print("The mesh is manifold.")
else:
 print("The mesh is non-manifold.")
```

### See Also

IsMesh, IsMeshClosed

---

## IsPointOnMesh

### Signature

```python
IsPointOnMesh(object_id, point)
```

### Description

Verifies a point is on a mesh

### Returns

bool: True if successful, otherwise False. None: on error.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a mesh")
if rs.IsMesh(obj):
 point = rs.GetPointOnMesh(strObject, "Pick a test point")
 if point:
 if rs.IsPointOnMesh(obj, point):
 print("The point is on the mesh")
 else:
 print("The point is not on the mesh")
```

### See Also

IsMesh, MeshClosestPoint

---

## JoinMeshes

### Signature

```python
JoinMeshes(object_ids, delete_input=False)
```

### Description

Joins two or or more mesh objects together

### Returns

guid: identifier of newly created mesh on success

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.GetObjects("Select meshes to join", rs.filter.mesh)
if objs and len(objs)>1: rs.JoinMeshes(objs, True)
```

### See Also

JoinCurves, JoinSurfaces

---

## MeshArea

### Signature

```python
MeshArea(object_ids)
```

### Description

Returns approximate area of one or more mesh objects

### Returns

list(number, number, number): if successful where [0] = number of meshes used in calculation [1] = total area of all meshes [2] = the error estimate None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select mesh", rs.filter.mesh )
if obj:
 area_rc = rs.MeshArea(obj)
 if area_rc: print("Mesh area:{}".format(area_rc[1]))
```

### See Also

MeshVolume

---

## MeshAreaCentroid

### Signature

```python
MeshAreaCentroid(object_id)
```

### Description

Calculates the area centroid of a mesh object

### Returns

point: representing the area centroid if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select mesh", rs.filter.mesh )
rs.AddPoint( rs.MeshAreaCentroid(obj) )
```

### See Also

IsMesh, MeshArea, MeshVolume, MeshVolumeCentroid

---

## MeshBooleanDifference

### Signature

```python
MeshBooleanDifference(input0, input1, delete_input=True, tolerance=None)
```

### Description

Performs boolean difference operation on two sets of input meshes

### Returns

list(guid, ...): identifiers of newly created meshes

### Example

```python
import rhinoscriptsyntax as rs
input0 = rs.GetObjects("Select first set of meshes", rs.filter.mesh)
if input0:
 input1 = rs.GetObjects("Select second set of meshes", rs.filter.mesh)
 if input1: rs.MeshBooleanDifference(input0, input1)
```

### See Also

MeshBooleanIntersection, MeshBooleanSplit, MeshBooleanUnion

---

## MeshBooleanIntersection

### Signature

```python
MeshBooleanIntersection(input0, input1, delete_input=True)
```

### Description

Performs boolean intersection operation on two sets of input meshes

### Returns

list(guid, ...): identifiers of new meshes on success

### Example

```python
import rhinoscriptsyntax as rs
input0 = rs.GetObjects("Select first set of meshes", rs.filter.mesh)
if input0:
 input1 = rs.GetObjects("Select second set of meshes", rs.filter.mesh)
 if input1: rs.MeshBooleanIntersection(input0, input1)
```

### See Also

MeshBooleanDifference, MeshBooleanSplit, MeshBooleanUnion

---

## MeshBooleanSplit

### Signature

```python
MeshBooleanSplit(input0, input1, delete_input=True)
```

### Description

Performs boolean split operation on two sets of input meshes

### Returns

list(guid, ...): identifiers of new meshes on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
input0 = rs.GetObjects("Select first set of meshes", rs.filter.mesh)
if input0:
 input1 = rs.GetObjects("Select second set of meshes", rs.filter.mesh)
 if input1: rs.MeshBooleanSplit(input0, input1)
```

### See Also

MeshBooleanDifference, MeshBooleanIntersection, MeshBooleanUnion

---

## MeshBooleanUnion

### Signature

```python
MeshBooleanUnion(mesh_ids, delete_input=True)
```

### Description

Performs boolean union operation on a set of input meshes

### Returns

list(guid, ...): identifiers of new meshes

### Example

```python
import rhinoscriptsyntax as rs
input = rs.GetObjects("Select meshes to union", rs.filter.mesh)
if input: rs.MeshBooleanUnion(input)
```

### See Also

MeshBooleanDifference, MeshBooleanIntersection, MeshBooleanSplit

---

## MeshClosestPoint

### Signature

```python
MeshClosestPoint(object_id, point, maximum_distance=None)
```

### Description

Returns the point on a mesh that is closest to a test point

### Returns

tuple(point, number): containing the results of the calculation where [0] = the 3-D point on the mesh [1] = the index of the mesh face on which the 3-D point lies None: on error

### Example

```python
import rhinocriptsyntax as rs
obj = rs.GetObject("Select mesh", rs.filter.mesh)
point = rs.GetPoint("Pick test point")
intersect = rs.MeshClosestPoint(obj, point)
if intersect: rs.AddPoint(intersect)
```

### See Also

MeshFaceCount, MeshFaces

---

## MeshFaceCenters

### Signature

```python
MeshFaceCenters(mesh_id)
```

### Description

Returns the center of each face of the mesh object

### Returns

list(point, ...): points defining the center of each face

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select mesh", rs.filter.mesh)
centers = rs.MeshFaceCenters(obj)
if centers:
 for point in centers: rs.AddPoint(point)
```

### See Also

IsMesh, MeshFaceCount, MeshFaces

---

## MeshFaceCount

### Signature

```python
MeshFaceCount(object_id)
```

### Description

Returns total face count of a mesh object

### Returns

number: the number of mesh faces if successful

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select mesh", rs.filter.mesh )
print("Quad faces:{}".format(rs.MeshQuadCount(obj)))
print("Triangle faces:{}".format(rs.MeshTriangleCount(obj)))
print("Total faces:{}".format(rs.MeshFaceCount(obj)))
```

### See Also

IsMesh, MeshFaces, MeshVertexCount, MeshVertices

---

## MeshFaceNormals

### Signature

```python
MeshFaceNormals(mesh_id)
```

### Description

Returns the face unit normal for each face of a mesh object

### Returns

list(vector, ...): 3D vectors that define the face unit normals of the mesh None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select mesh", rs.filter.mesh)
normals = rs.MeshFaceNormals(obj)
if normals:
 for vector in normals: print(vector)
```

### See Also

MeshHasFaceNormals, MeshFaceCount, MeshFaces

---

## MeshFaceVertices

### Signature

```python
MeshFaceVertices(object_id)
```

### Description

Returns the vertex indices of all faces of a mesh object

### Returns

list((number, number, number, number), ...): containing tuples of 4 numbers that define the vertex indices for each face of the mesh. Both quad and triangle faces are returned. If the third and fourth vertex indices are identical, the face is a triangle.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select mesh", rs.filter.mesh)
faceVerts = rs.MeshFaceVertices( obj )
if faceVerts:
 for count, face in enumerate(faceVerts):
 print("face({}) = ({}, {}, {}, {})".format(count, face[0], face[1], face[2], face[3]))
```

### See Also

IsMesh, MeshFaceCount, MeshFaces

---

## MeshFaces

### Signature

```python
MeshFaces(object_id, face_type=True)
```

### Description

Returns face vertices of a mesh

### Returns

list([point, point, point, point], ...): 3D points that define the face vertices of the mesh. If face_type is True, then faces are returned as both quads and triangles (4 3D points). For triangles, the third and fourth vertex will be identical. If face_type is False, then faces are returned as only triangles(3 3D points). Quads will be converted to triangles.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select mesh", rs.filter.mesh)
faces = rs.MeshFaces(obj, False)
if faces:
 rs.EnableRedraw(False)
 i = 0
 while( i<=len(faces) ):
 face = faces[i], faces[i+1], faces[i+2], faces[i]
 rs.AddPolyline( face )
 i += 3
rs.EnableRedraw(True)
```

### See Also

IsMesh, MeshFaceCount, MeshVertexCount, MeshVertices

---

## MeshHasFaceNormals

### Signature

```python
MeshHasFaceNormals(object_id)
```

### Description

Verifies a mesh object has face normals

### Returns

bool: True if successful, otherwise False.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a mesh", rs.filter.mesh)
if rs.MeshHasFaceNormals(obj):
 print("The mesh has face normal.")
else:
 print("The mesh does not have face normals.")
```

### See Also

MeshFaceNormals

---

## MeshHasTextureCoordinates

### Signature

```python
MeshHasTextureCoordinates(object_id)
```

### Description

Verifies a mesh object has texture coordinates

### Returns

bool: True if successful, otherwise False.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a mesh", rs.filter.mesh)
if rs.MeshHasTextureCoordinates(obj):
 print("The mesh has texture coordinates.")
else:
 print("The mesh does not have texture coordinates.")
```

---

## MeshHasVertexColors

### Signature

```python
MeshHasVertexColors(object_id)
```

### Description

Verifies a mesh object has vertex colors

### Returns

bool: True if successful, otherwise False.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a mesh", rs.filter.mesh)
if rs.mesh.MeshHasVertexColors(obj):
 print("The mesh has vertex colors.")
else:
 print("The mesh does not have vertex colors.")
```

### See Also

MeshVertexColors

---

## MeshHasVertexNormals

### Signature

```python
MeshHasVertexNormals(object_id)
```

### Description

Verifies a mesh object has vertex normals

### Returns

bool: True if successful, otherwise False.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a mesh", rs.filter.mesh)
if rs.MeshHasVertexNormals(obj):
 print("The mesh has vertex normals.")
else:
 print("The mesh does not have vertex normals.")
```

### See Also

MeshVertexNormals

---

## MeshMeshIntersection

### Signature

```python
MeshMeshIntersection(mesh1, mesh2, tolerance=None)
```

### Description

Calculates the intersections of a mesh object with another mesh object

### Returns

list(point, ...): of points that define the vertices of the intersection curves

### Example

```python
import rhinoscriptsyntax as rs
mesh1 = rs.GetObject("Select first mesh to intersect", rs.filter.mesh)
mesh2 = rs.GetObject("Select second mesh to intersect", rs.filter.mesh)
results = rs.MeshMeshIntersection(mesh1, mesh2)
if results:
 for points in results: rs.AddPolyline(points)
```

### See Also

CurveMeshIntersection, MeshClosestPoint

---

## MeshNakedEdgePoints

### Signature

```python
MeshNakedEdgePoints(object_id)
```

### Description

Identifies the naked edge points of a mesh object. This function shows where mesh vertices are not completely surrounded by faces. Joined meshes, such as are made by MeshBox, have naked mesh edge points where the sub-meshes are joined

### Returns

list(bool, ...): of boolean values that represent whether or not a mesh vertex is naked or not. The number of elements in the list will be equal to the value returned by MeshVertexCount. In which case, the list will identify the naked status for each vertex returned by MeshVertices None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select mesh", rs.filter.mesh)
vertices = rs.MeshVertices( obj )
naked = rs.MeshNakedEdgePoints( obj )
for i, vertex in enumerate(vertices):
 if naked[i]: rs.AddPoint(vertex)
```

### See Also

IsMesh, MeshVertexCount, MeshVertices

---

## MeshOffset

### Signature

```python
MeshOffset(mesh_id, distance)
```

### Description

Makes a new mesh with vertices offset at a distance in the opposite direction of the existing vertex normals

### Returns

guid: identifier of the new mesh object if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
mesh = rs.GetObject("Select mesh to offset", rs.filter.mesh)
rs.MeshOffset( mesh, 10.0 )
```

### See Also

IsMesh

---

## MeshOutline

### Signature

```python
MeshOutline(object_ids, view=None)
```

### Description

Creates polyline curve outlines of mesh objects

### Returns

list(guid, ...): polyline curve identifiers on success

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.GetObjects("Select mesh objects to outline", rs.filter.mesh)
if objs: rs.MeshOutline(objs)
```

### See Also

IsMesh

---

## MeshQuadCount

### Signature

```python
MeshQuadCount(object_id)
```

### Description

Returns the number of quad faces of a mesh object

### Returns

number: the number of quad mesh faces if successful

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select mesh", rs.filter.mesh )
print("Quad faces:{}".format(rs.MeshQuadCount(obj)))
print("Triangle faces:{}".format(rs.MeshTriangleCount(obj)))
print("Total faces:{}".format(rs.MeshFaceCount(obj)))
```

### See Also

MeshQuadCount

---

## MeshQuadsToTriangles

### Signature

```python
MeshQuadsToTriangles(object_id)
```

### Description

Converts a mesh object's quad faces to triangles

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select mesh", rs.filter.mesh )
if rs.MeshQuadCount(obj)>0:
 rs.MeshQuadsToTriangles(obj)
```

---

## MeshToNurb

### Signature

```python
MeshToNurb(object_id, trimmed_triangles=True, delete_input=False)
```

### Description

Duplicates each polygon in a mesh with a NURBS surface. The resulting surfaces are then joined into a polysurface and added to the document

### Returns

list(guid, ...): identifiers for the new breps on success

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select mesh", rs.filter.mesh)
if obj: rs.MeshToNurb(obj)
```

### See Also

IsMesh, MeshFaces, MeshVertices

---

## MeshTriangleCount

### Signature

```python
MeshTriangleCount(object_id)
```

### Description

Returns number of triangular faces of a mesh

### Returns

number: The number of triangular mesh faces if successful

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select mesh", rs.filter.mesh )
print("Quad faces:{}".format(rs.MeshQuadCount(obj)))
print("Triangle faces:{}".format(rs.MeshTriangleCount(obj)))
print("Total faces:{}".format(rs.MeshFaceCount(obj)))
```

### See Also

IsMesh

---

## MeshVertexColors

### Signature

```python
MeshVertexColors(mesh_id, colors=0)
```

### Description

Returns of modifies vertex colors of a mesh

### Returns

color: if colors is not specified, the current vertex colors color: if colors is specified, the previous vertex colors

### Example

```python
import rhinoscriptsyntax as rs
import random

def randomcolor():
 r = random.randint(0,255)
 g = random.randint(0,255)
 b = random.randint(0,255)
 return r,g,b

obj = rs.GetObject("Select mesh", rs.filter.mesh)
if obj:
 colors = []
 for i in range(rs.MeshVertexCount(obj)): colors.append( randomcolor() )
 rs.MeshVertexColors( obj, colors )
```

### See Also

MeshHasVertexColors, MeshVertexCount, MeshVertices

---

## MeshVertexCount

### Signature

```python
MeshVertexCount(object_id)
```

### Description

Returns the vertex count of a mesh

### Returns

number: The number of mesh vertices if successful.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select mesh", rs.filter.mesh )
print("Vertex count: {}".format(rs.MeshVertexCount(obj)))
```

### See Also

IsMesh, MeshFaceCount, MeshFaces, MeshVertices

---

## MeshVertexFaces

### Signature

```python
MeshVertexFaces(mesh_id, vertex_index)
```

### Description

Returns the mesh faces that share a specified mesh vertex

### Returns

list(number, ...): face indices on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
import random
def TestMeshVertexFaces():
 mesh = rs.GetObject("Select mesh", rs.filter.mesh)
 vertices = rs.MeshVertices(mesh)
 meshfaces = rs.MeshFaceVertices(mesh)
 vertex = random.randint(0, len(vertices)-1) #some random vertex
 vertex_faces = rs.MeshVertexFaces(mesh, vertex )
 if vertex_faces:
 rs.AddPoint( vertices[vertex] )
 for face_index in vertex_faces:
 face = meshfaces[face_index]
 polyline = []
 polyline.append( vertices[face[0]] )
 polyline.append( vertices[face[1]] )
 polyline.append( vertices[face[2]] )
 if face[2]!=face[3]:
 polyline.append( vertices[face[3]] )
 polyline.append( polyline[0] )
 rs.AddPolyline(polyline)

TestMeshVertexFaces()
```

### See Also

MeshFaces, MeshFaceVertices, MeshVertices

---

## MeshVertexNormals

### Signature

```python
MeshVertexNormals(mesh_id)
```

### Description

Returns the vertex unit normal for each vertex of a mesh

### Returns

list(vector, ...): of vertex normals, (empty list if no normals exist)

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select mesh", rs.filter.mesh)
normals = rs.MeshVertexNormals(obj)
if normals:
 for normal in normals: print(normal)
```

### See Also

MeshHasVertexNormals, MeshVertexCount, MeshVertices

---

## MeshVertices

### Signature

```python
MeshVertices(object_id)
```

### Description

Returns the vertices of a mesh

### Returns

list(point, ...): vertex points in the mesh

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select mesh", rs.filter.mesh)
vertices = rs.MeshVertices(obj)
if vertices: rs.AddPointCloud(vertices)
```

### See Also

IsMesh, MeshFaceCount, MeshFaces, MeshVertexCount

---

## MeshVolume

### Signature

```python
MeshVolume(object_ids)
```

### Description

Returns the approximate volume of one or more closed meshes

### Returns

tuple(number, number, number): containing 3 velues if successful where [0] = number of meshes used in volume calculation [1] = total volume of all meshes [2] = the error estimate None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select mesh", rs.filter.mesh )
if obj and rs.IsMeshClosed(obj):
 volume = rs.MeshVolume(obj)
 if volume: print("Mesh volume:{}".format(volume[1]))
```

### See Also

IsMeshClosed, MeshArea

---

## MeshVolumeCentroid

### Signature

```python
MeshVolumeCentroid(object_id)
```

### Description

Calculates the volume centroid of a mesh

### Returns

point: Point3d representing the volume centroid None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select mesh", rs.filter.mesh )
centroid = rs.MeshVolumeCentroid(obj)
rs.AddPoint( centroid )
```

### See Also

IsMesh, MeshArea, MeshAreaCentroid, MeshVolume

---

## PullCurveToMesh

### Signature

```python
PullCurveToMesh(mesh_id, curve_id)
```

### Description

Pulls a curve to a mesh. The function makes a polyline approximation of the input curve and gets the closest point on the mesh for each point on the polyline. Then it "connects the points" to create a polyline on the mesh

### Returns

guid: identifier new curve on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
mesh = rs.GetObject("Select mesh that pulls", rs.filter.mesh)
curve = rs.GetObject("Select curve to pull", rs.filter.curve)
rs.PullCurveToMesh( mesh, curve )
```

### See Also

IsMesh

---

## SplitDisjointMesh

### Signature

```python
SplitDisjointMesh(object_id, delete_input=False)
```

### Description

Splits up a mesh into its unconnected pieces

### Returns

list(guid, ...): identifiers for the new meshes

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select mesh", rs.filter.mesh)
if rs.DisjointMeshCount(obj)>0: rs.SplitDisjointMesh(obj)
```

### See Also

IsMesh, DisjointMeshCount

---

## UnifyMeshNormals

### Signature

```python
UnifyMeshNormals(object_id)
```

### Description

Fixes inconsistencies in the directions of faces of a mesh

### Returns

number: the number of faces that were modified

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select mesh", rs.filter.mesh)
if rs.IsMesh(obj): rs.UnifyMeshNormals(obj)
```

### See Also

IsMesh

---

# Object

*60 functions | 12 in use*

---

## CopyObject

** IN USE**

### Signature

```python
CopyObject(object_id, translation=None)
```

### Description

Copies object from one location to another, or in-place.

### Returns

guid: id for the copy if successful None: if not able to copy

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select object to copy")
if id:
 start = rs.GetPoint("Point to copy from")
 if start:
 end = rs.GetPoint("Point to copy to", start)
 if end:
 translation = end-start
 rs.CopyObject( id, translation )
```

### See Also

CopyObjects

---

## CopyObjects

### Signature

```python
CopyObjects(object_ids, translation=None)
```

### Description

Copies one or more objects from one location to another, or in-place.

### Returns

list(guid, ...): identifiers for the copies if successful

### Example

```python
import rhinoscriptsyntax as rs
objectIds = rs.GetObjects("Select objects to copy")
if objectIds:
 start = rs.GetPoint("Point to copy from")
 if start:
 end = rs.GetPoint("Point to copy to", start)
 if end:
 translation = end-start
 rs.CopyObjects( objectIds, translation )
```

### See Also

CopyObject

---

## DeleteObject

** IN USE**

### Signature

```python
DeleteObject(object_id)
```

### Description

Deletes a single object from the document

### Returns

bool: True of False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select object to delete")
if id: rs.DeleteObject(id)
```

### See Also

DeleteObjects

---

## DeleteObjects

** IN USE**

### Signature

```python
DeleteObjects(object_ids)
```

### Description

Deletes one or more objects from the document

### Returns

number: Number of objects deleted

### Example

```python
import rhinoscriptsyntax as rs
object_ids = rs.GetObjects("Select objects to delete")
if object_ids: rs.DeleteObjects(object_ids)
```

### See Also

DeleteObject

---

## FlashObject

### Signature

```python
FlashObject(object_ids, style=True)
```

### Description

Causes the selection state of one or more objects to change momentarily so the object appears to flash on the screen

### Returns

None

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.ObjectsByLayer("Default")
if objs: rs.FlashObject(objs)
```

### See Also

HideObjects, SelectObjects, ShowObjects, UnselectObjects

---

## HideObject

### Signature

```python
HideObject(object_id)
```

### Description

Hides a single object

### Returns

bool: True of False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select object to hide")
if id: rs.HideObject(id)
```

### See Also

HideObjects, IsObjectHidden, ShowObject, ShowObjects

---

## HideObjects

### Signature

```python
HideObjects(object_ids)
```

### Description

Hides one or more objects

### Returns

number: Number of objects hidden

### Example

```python
import rhinoscriptsyntax as rs
ids = rs.GetObjects("Select objects to hide")
if ids: rs.HideObjects(ids)
```

### See Also

HideObjects, IsObjectHidden, ShowObject, ShowObjects

---

## IsLayoutObject

### Signature

```python
IsLayoutObject(object_id)
```

### Description

Verifies that an object is in either page layout space or model space

### Returns

bool: True if the object is in page layout space bool: False if the object is in model space

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select object")
if id:
 if rs.IsLayoutObject(id):
 print("The object is in page layout space.")
 else:
 print("The object is in model space.")
```

### See Also

IsObject, IsObjectReference

---

## IsObject

### Signature

```python
IsObject(object_id)
```

### Description

Verifies the existence of an object

### Returns

bool: True if the object exists bool: False if the object does not exist

### Example

```python
import rhinoscriptsyntax as rs
#Do something here...
if rs.IsObject(id):
 print("The object exists.")
else:
 print("The object does not exist.")
```

### See Also

IsObjectHidden, IsObjectInGroup, IsObjectLocked, IsObjectNormal, IsObjectReference, IsObjectSelectable, IsObjectSelected, IsObjectSolid

---

## IsObjectHidden

### Signature

```python
IsObjectHidden(object_id)
```

### Description

Verifies that an object is hidden. Hidden objects are not visible, cannot be snapped to, and cannot be selected

### Returns

bool: True if the object is hidden bool: False if the object is not hidden

### Example

```python
import rhinoscriptsyntax as rs
# Do something here...
if rs.IsObjectHidden(id):
 print("The object is hidden.")
else:
 print("The object is not hidden.")
```

### See Also

IsObject, IsObjectInGroup, IsObjectLocked, IsObjectNormal, IsObjectReference, IsObjectSelectable, IsObjectSelected, IsObjectSolid

---

## IsObjectInBox

### Signature

```python
IsObjectInBox(object_id, box, test_mode=True)
```

### Description

Verifies an object's bounding box is inside of another bounding box

### Returns

bool: True if object is inside box bool: False is object is not inside box

### Example

```python
import rhinoscriptsyntax as rs
box = rs.GetBox()
if box:
 rs.EnableRedraw(False)
 object_list = rs.AllObjects()
 for obj in object_list:
 if rs.IsObjectInBox(obj, box, False):
 rs.SelectObject( obj )
 rs.EnableRedraw( True )
```

### See Also

BoundingBox, GetBox

---

## IsObjectInGroup

### Signature

```python
IsObjectInGroup(object_id, group_name=None)
```

### Description

Verifies that an object is a member of a group

### Returns

bool: True if the object is a member of the specified group. If a group_name was not specified, the object is a member of some group. bool: False if the object is not a member of the specified group. If a group_name was not specified, the object is not a member of any group

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select object")
if id:
 name = rs.GetString("Group name")
 if name:
 result = rs.IsObjectInGroup(id, name)
 if result:
 print("The object belongs to the group.")
 else:
 print("The object does not belong to the group.")
```

### See Also

IsObject, IsObjectHidden, IsObjectLocked, IsObjectNormal, IsObjectReference, IsObjectSelectable, IsObjectSelected, IsObjectSolid

---

## IsObjectLocked

### Signature

```python
IsObjectLocked(object_id)
```

### Description

Verifies that an object is locked. Locked objects are visible, and can be snapped to, but cannot be selected

### Returns

bool: True if the object is locked bool: False if the object is not locked

### Example

```python
import rhinoscriptsyntax as rs
# Do something here...
if rs.IsObjectLocked(object):
 print("The object is locked.")
else:
 print("The object is not locked.")
```

### See Also

IsObject, IsObjectHidden, IsObjectInGroup, IsObjectNormal, IsObjectReference, IsObjectSelectable, IsObjectSelected, IsObjectSolid

---

## IsObjectNormal

### Signature

```python
IsObjectNormal(object_id)
```

### Description

Verifies that an object is normal. Normal objects are visible, can be snapped to, and can be selected

### Returns

bool: True if the object is normal bool: False if the object is not normal

### Example

```python
import rhinoscriptsyntax as rs
#Do something here...
if rs.IsObjectNormal(object):
 print("The object is normal.")
else:
 print("The object is not normal.")
```

### See Also

IsObject, IsObjectHidden, IsObjectInGroup, IsObjectLocked, IsObjectReference, IsObjectSelectable, IsObjectSelected, IsObjectSolid

---

## IsObjectReference

### Signature

```python
IsObjectReference(object_id)
```

### Description

Verifies that an object is a reference object. Reference objects are objects that are not part of the current document

### Returns

bool: True if the object is a reference object bool: False if the object is not a reference object

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select object")
if rs.IsObjectReference(id):
 print("The object is a reference object.")
else:
 print("The object is not a reference object.")
```

### See Also

IsObject, IsObjectHidden, IsObjectInGroup, IsObjectLocked, IsObjectNormal, IsObjectSelectable, IsObjectSelected, IsObjectSolid

---

## IsObjectSelectable

### Signature

```python
IsObjectSelectable(object_id)
```

### Description

Verifies that an object can be selected

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
# Do something here...
if rs.IsObjectSelectable(object):
rs.SelectObject( object )
```

### See Also

IsObject, IsObjectHidden, IsObjectInGroup, IsObjectLocked, IsObjectNormal, IsObjectReference, IsObjectSelected, IsObjectSolid

---

## IsObjectSelected

### Signature

```python
IsObjectSelected(object_id)
```

### Description

Verifies that an object is currently selected.

### Returns

int: 0, the object is not selected int: 1, the object is selected int: 2, the object is entirely persistently selected int: 3, one or more proper sub-objects are selected

### Example

```python
import rhinoscriptsyntax as rs
object = rs.GetObject()
if rs.IsObjectSelected(object):
 print("The object is selected.")
else:
 print("The object is not selected.")
```

### See Also

IsObject, IsObjectHidden, IsObjectInGroup, IsObjectLocked, IsObjectNormal, IsObjectReference, IsObjectSelectable, IsObjectSolid

---

## IsObjectSolid

### Signature

```python
IsObjectSolid(object_id)
```

### Description

Determines if an object is closed, solid

### Returns

bool: True if the object is solid, or a mesh is closed. bool: False otherwise.

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select object")
if rs.IsObjectSolid(id):
 print("The object is solid.")
else:
 print("The object is not solid.")
```

### See Also

IsObject, IsObjectHidden, IsObjectInGroup, IsObjectLocked, IsObjectNormal, IsObjectReference, IsObjectSelectable, IsObjectSelected

---

## IsObjectValid

### Signature

```python
IsObjectValid(object_id)
```

### Description

Verifies an object's geometry is valid and without error

### Returns

bool: True if the object is valid

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select object")
if rs.IsObjectValid(id):
 print("The object is valid.")
else:
 print("The object is not valid.")
```

### See Also

IsObject

---

## IsVisibleInView

### Signature

```python
IsVisibleInView(object_id, view=None)
```

### Description

Verifies an object is visible in a view

### Returns

bool: True if the object is visible in the specified view, otherwise False. None on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if rs.IsObject(obj):
 view = rs.CurrentView()
 if rs.IsVisibleInView(obj, view):
 print("The object is visible in {}.".format(view))
 else:
 print("The object is not visible in {}.".format(view))
```

### See Also

IsObject, IsView

---

## LockObject

### Signature

```python
LockObject(object_id)
```

### Description

Locks a single object. Locked objects are visible, and they can be snapped to. But, they cannot be selected.

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select object to lock")
if id: rs.LockObject(id)
```

### See Also

IsObjectLocked, LockObjects, UnlockObject, UnlockObjects

---

## LockObjects

### Signature

```python
LockObjects(object_ids)
```

### Description

Locks one or more objects. Locked objects are visible, and they can be snapped to. But, they cannot be selected.

### Returns

number: number of objects locked

### Example

```python
import rhinoscriptsyntax as rs
ids = rs.GetObjects("Select objects to lock")
if ids: rs.LockObjects(ids)
```

### See Also

IsObjectLocked, LockObject, UnlockObject, UnlockObjects

---

## MatchObjectAttributes

### Signature

```python
MatchObjectAttributes(target_ids, source_id=None)
```

### Description

Matches, or copies the attributes of a source object to a target object

### Returns

number: number of objects modified

### Example

```python
import rhinoscriptsyntax as rs
targets = rs.GetObjects("Select objects")
if targets:
 source = rs.GetObject("Select object to match")
 if source: rs.MatchObjectAttributes( targets, source )
```

### See Also

GetObject, GetObjects

---

## MirrorObject

** IN USE**

### Signature

```python
MirrorObject(object_id, start_point, end_point, copy=False)
```

### Description

Mirrors a single object

### Returns

guid: Identifier of the mirrored object if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object to mirror")
if obj:
 start = rs.GetPoint("Start of mirror plane")
 end = rs.GetPoint("End of mirror plane")
 if start and end:
 rs.MirrorObject( obj, start, end, True )
```

### See Also

MirrorObjects

---

## MirrorObjects

### Signature

```python
MirrorObjects(object_ids, start_point, end_point, copy=False)
```

### Description

Mirrors a list of objects

### Returns

list(guid, ...): List of identifiers of the mirrored objects if successful

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.GetObjects("Select objects to mirror")
if objs:
 start = rs.GetPoint("Start of mirror plane")
 end = rs.GetPoint("End of mirror plane")
 if start and end:
 rs.MirrorObjects( objs, start, end, True )
```

### See Also

MirrorObject

---

## MoveObject

** IN USE**

### Signature

```python
MoveObject(object_id, translation)
```

### Description

Moves a single object

### Returns

guid: Identifier of the moved object if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select object to move")
if id:
 start = rs.GetPoint("Point to move from")
 if start:
 end = rs.GetPoint("Point to move to")
 if end:
 translation = end-start
 rs.MoveObject(id, translation)
```

### See Also

MoveObjects

---

## MoveObjects

### Signature

```python
MoveObjects(object_ids, translation)
```

### Description

Moves one or more objects

### Returns

list(guid, ...): identifiers of the moved objects if successful

### Example

```python
import rhinoscriptsyntax as rs
ids = rs.GetObjects("Select objects to move")
if ids:
 start = rs.GetPoint("Point to move from")
 if start:
 end = rs.GetPoint("Point to move to")
 if end:
 translation = end-start
 rs.MoveObjects( ids, translation )
```

### See Also

MoveObject

---

## ObjectColor

** IN USE**

### Signature

```python
ObjectColor(object_ids, color=None)
```

### Description

Returns of modifies the color of an object. Object colors are represented as RGB colors. An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed

### Returns

color: If color value is not specified, the current color value color: If color value is specified, the previous color value number: If object_ids is a list, then the number of objects modified

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.GetObjects("Select objects to change color")
if objs:
 color = rs.GetColor(0)
 if color:
 for obj in objs: rs.ObjectColor( obj, color )
```

### See Also

ObjectColorSource, ObjectsByColor

---

## ObjectColorSource

### Signature

```python
ObjectColorSource(object_ids, source=None)
```

### Description

Returns of modifies the color source of an object.

### Returns

if color source is not specified, the current color source is color source is specified, the previous color source if color_ids is a list, then the number of objects modifief

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.GetObjects("Select objects to reset color source")
if objs:
 for obj In objs: rs.ObjectColorSource(obj, 0)
```

### See Also

ObjectColor

---

## ObjectDescription

### Signature

```python
ObjectDescription(object_id)
```

### Description

Returns a short text description of an object

### Returns

A short text description of the object if successful.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if obj:
 description = rs.ObjectDescription(obj)
 print("Object description:"{} .format(description))
```

### See Also

ObjectType

---

## ObjectGroups

### Signature

```python
ObjectGroups(object_id)
```

### Description

Returns all of the group names that an object is assigned to

### Returns

list(str, ...): list of group names on success

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if obj:
 groups = rs.ObjectGroups(obj)
 if groups:
 for group in groups: print("Object group: {}".format(group))
 else:
 print("No groups.")
```

### See Also

ObjectsByGroup

---

## ObjectLayer

** IN USE**

### Signature

```python
ObjectLayer(object_id, layer=None)
```

### Description

Returns or modifies the layer of an object

### Returns

str: If a layer is not specified, the object's current layer str: If a layer is specified, the object's previous layer number: If object_id is a list or tuple, the number of objects modified

### Example

```python
import rhinoscriptsyntax as rs
id = rs.GetObject("Select object")
if id: rs.ObjectLayer(id, "Default")
```

### See Also

ObjectsByLayer

---

## ObjectLayout

### Signature

```python
ObjectLayout(object_id, layout=None, return_name=True)
```

### Description

Returns or changes the layout or model space of an object

### Returns

str: if layout is not specified, the object's current page layout view str: if layout is specified, the object's previous page layout view None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if obj: rs.ObjectLayout(obj, "Page 1")
```

### See Also

IsLayoutObject, IsLayout, ViewNames

---

## ObjectLinetype

### Signature

```python
ObjectLinetype(object_ids, linetype=None)
```

### Description

Returns of modifies the linetype of an object

### Returns

str: If a linetype is not specified, the object's current linetype str: If linetype is specified, the object's previous linetype number: If object_ids is a list, the number of objects modified

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if obj: rs.ObjectLinetype(obj, "Continuous")
```

### See Also

ObjectLinetypeSource

---

## ObjectLinetypeSource

### Signature

```python
ObjectLinetypeSource(object_ids, source=None)
```

### Description

Returns of modifies the linetype source of an object

### Returns

number: If a source is not specified, the object's current linetype source number: If source is specified, the object's previous linetype source number: If object_ids is a list, the number of objects modified

### Example

```python
import rhinoscriptsyntax as rs
objects = rs.GetObjects("Select objects to reset linetype source")
if objects:
 for obj in objects: rs.ObjectLinetypeSource( obj, 0 )
```

### See Also

ObjectLinetype

---

## ObjectMaterialIndex

### Signature

```python
ObjectMaterialIndex(object_id, material_index=None)
```

### Description

Returns or changes the material index of an object. Rendering materials are stored in Rhino's rendering material table. The table is conceptually an array. Render materials associated with objects and layers are specified by zero based indices into this array.

### Returns

number: If the return value of ObjectMaterialSource is "material by object", then the return value of this function is the index of the object's rendering material. A material index of -1 indicates no material has been assigned, and that Rhino's internal default material has been assigned to the object. None: on failure

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if obj:
 source = rs.ObjectMaterialSource(obj)
 if source==0:
 print("The material source is by layer")
 else:
 print("The material source is by object")
 index = rs.ObjectMaterialIndex(obj)
 if index==-1: print("The material is default.")
 else: print("The material is custom.")
```

### See Also

ObjectMaterialSource

---

## ObjectMaterialSource

### Signature

```python
ObjectMaterialSource(object_ids, source=None)
```

### Description

Returns or modifies the rendering material source of an object.

### Returns

number: If source is not specified, the current rendering material source number: If source is specified, the previous rendering material source number: If object_ids refers to multiple objects, the number of objects modified

### Example

```python
import rhinoscriptsyntax as rs
objects = rs.GetObjects("Select objects to reset rendering material source")
if objects:
 [rs.ObjectMaterialSource(obj, 0) for obj in objects]
```

### See Also

ObjectMaterialIndex

---

## ObjectName

** IN USE**

### Signature

```python
ObjectName(object_id, name=None)
```

### Description

Returns or modifies the name of an object

### Returns

str: If name is not specified, the current object name str: If name is specified, the previous object name number: If object_id is a list, the number of objects changed

### Example

```python
import rhinoscriptsyntax as rs
points = rs.GetPoints(message1="Pick some points")
if points:
 count = 0
 for point in points:
 obj = rs.AddPoint(point)
 if obj:
 rs.ObjectName( obj, "Point"+str(count) )
 count += 1
```

### See Also

ObjectsByName

---

## ObjectPrintColor

### Signature

```python
ObjectPrintColor(object_ids, color=None)
```

### Description

Returns or modifies the print color of an object

### Returns

color: If color is not specified, the object's current print color color: If color is specified, the object's previous print color number: If object_ids is a list or tuple, the number of objects modified

### Example

```python
import rhinoscriptsyntax as rs
objects = rs.GetObjects("Select objects to change print color")
if objects:
 color = rs.GetColor()
 if color:
 for object in objects: rs.ObjectPrintColor(object, color)
```

### See Also

ObjectPrintColorSource

---

## ObjectPrintColorSource

### Signature

```python
ObjectPrintColorSource(object_ids, source=None)
```

### Description

Returns or modifies the print color source of an object

### Returns

number: If source is not specified, the object's current print color source number: If source is specified, the object's previous print color source number: If object_ids is a list or tuple, the number of objects modified

### Example

```python
import rhinoscriptsyntax as rs
objects = rs.GetObjects("Select objects to reset print color source")
if objects:
 for object in objects: rs.ObjectPrintColorSource(object, 0)
```

### See Also

ObjectPrintColor

---

## ObjectPrintWidth

### Signature

```python
ObjectPrintWidth(object_ids, width=None)
```

### Description

Returns or modifies the print width of an object

### Returns

number: If width is not specified, the object's current print width number: If width is specified, the object's previous print width number: If object_ids is a list or tuple, the number of objects modified

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.GetObjects("Select objects to change print width")
if objs:
 for obj in objs: rs.ObjectPrintWidth(obj,0.5)
```

### See Also

ObjectPrintWidthSource

---

## ObjectPrintWidthSource

### Signature

```python
ObjectPrintWidthSource(object_ids, source=None)
```

### Description

Returns or modifies the print width source of an object

### Returns

number: If source is not specified, the object's current print width source number: If source is specified, the object's previous print width source number: If object_ids is a list or tuple, the number of objects modified

### Example

```python
import rhinoscriptsyntax as rs
objects = rs.GetObjects("Select objects to reset print width source")
if objects:
 for obj in objects: rs.ObjectPrintWidthSource(obj,0)
```

### See Also

ObjectPrintColor

---

## ObjectType

** IN USE**

### Signature

```python
ObjectType(object_id)
```

### Description

Returns the object type

### Returns

number: The object type if successful. The valid object types are as follows: Value Description 0 Unknown object 1 Point 2 Point cloud 4 Curve 8 Surface or single-face brep 16 Polysurface or multiple-face 32 Mesh 256 Light 512 Annotation 4096 Instance or block reference 8192 Text dot object 16384 Grip object 32768 Detail 65536 Hatch 131072 Morph control 134217728 Cage 268435456 Phantom 536870912 Clipping plane 1073741824 Extrusion

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if obj:
 objtype = rs.ObjectType(obj)
 print("Object type:{}".format(objtype))
```

### See Also

ObjectsByType

---

## OrientObject

### Signature

```python
OrientObject(object_id, reference, target, flags=0)
```

### Description

Orients a single object based on input points. If two 3-D points are specified, then this method will function similar to Rhino's Orient command. If more than two 3-D points are specified, then the function will orient similar to Rhino's Orient3Pt command. The orient flags values can be added together to specify multiple options. Value Description 1 Copy object. The default is not to copy the object. 2 Scale object. The default is not to scale the object. Note, the scale option only applies if both reference and target contain only two 3-D points.

### Returns

guid: The identifier of the oriented object if successful.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object to orient")
if obj:
 reference = rs.GetPoints(message1="First reference point")
 if reference and len(reference)>0:
 target = rs.GetPoints(message1="First target point")
 if target and len(target)>0:
 rs.OrientObject( obj, reference, target )
```

---

## RotateObject

### Signature

```python
RotateObject(object_id, center_point, rotation_angle, axis=None, copy=False)
```

### Description

Rotates a single object

### Returns

guid: Identifier of the rotated object if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object to rotate")
if obj:
 point = rs.GetPoint("Center point of rotation")
 if point: rs.RotateObject(obj, point, 45.0, None, copy=True)
```

### See Also

RotateObjects

---

## RotateObjects

** IN USE**

### Signature

```python
RotateObjects( object_ids, center_point, rotation_angle, axis=None, copy=False)
```

### Description

Rotates multiple objects

### Returns

list(guid, ...): identifiers of the rotated objects if successful

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.GetObjects("Select objects to rotate")
if objs:
 point = rs.GetPoint("Center point of rotation")
 if point:
 rs.RotateObjects( objs, point, 45.0, None, True )
```

### See Also

RotateObject

---

## ScaleObject

** IN USE**

### Signature

```python
ScaleObject(object_id, origin, scale, copy=False)
```

### Description

Scales a single object. Can be used to perform a uniform or non-uniform scale transformation. Scaling is based on the active construction plane.

### Returns

guid: Identifier of the scaled object if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object to scale")
if obj:
 origin = rs.GetPoint("Origin point")
 if origin:
 rs.ScaleObject( obj, origin, (1,2,3), True )
```

### See Also

ScaleObjects

---

## ScaleObjects

### Signature

```python
ScaleObjects(object_ids, origin, scale, copy=False)
```

### Description

Scales one or more objects. Can be used to perform a uniform or non- uniform scale transformation. Scaling is based on the active construction plane.

### Returns

list(guid, ...): identifiers of the scaled objects if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.GetObjects("Select objects to scale")
if objs:
 origin = rs.GetPoint("Origin point")
 if origin:
 rs.ScaleObjects( objs, origin, (2,2,2), True )
```

### See Also

ScaleObject

---

## SelectObject

### Signature

```python
SelectObject(object_id, redraw=True)
```

### Description

Selects a single object

### Returns

bool: True on success

### Example

```python
import rhinoscriptsyntax as rs
rs.Command( "Line 0,0,0 5,5,0" )
id = rs.FirstObject()
if id: rs.SelectObject(id)
# Do something here...
rs.UnselectObject(id)
```

### See Also

IsObjectSelectable, IsObjectSelected, SelectObjects, UnselectObject, UnselectObjects

---

## SelectObjects

** IN USE**

### Signature

```python
SelectObjects( object_ids)
```

### Description

Selects one or more objects

### Returns

number: number of selected objects

### Example

```python
import rhinoscriptsyntax as rs
ids = rs.GetObjects("Select object to copy in-place")
if ids:
 rs.UnselectObjects(ids)
 copies = rs.CopyObjects(ids)
 if copies: rs.SelectObjects(copies)
```

### See Also

IsObjectSelectable, IsObjectSelected, SelectObject, UnselectObject, UnselectObjects

---

## ShearObject

### Signature

```python
ShearObject(object_id, origin, reference_point, angle_degrees, copy=False)
```

### Description

Perform a shear transformation on a single object

### Returns

guid: Identifier of the sheared object if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object to shear")
if obj:
 origin = rs.GetPoint("Origin point")
 refpt = rs.GetPoint("Reference point")
 if origin and refpt:
 rs.ShearObject(obj, origin, refpt, 45.0, True)
```

### See Also

ShearObjects

---

## ShearObjects

### Signature

```python
ShearObjects(object_ids, origin, reference_point, angle_degrees, copy=False)
```

### Description

Shears one or more objects

### Returns

list(guid, ...]): identifiers of the sheared objects if successful

### Example

```python
import rhinoscriptsyntax as rs
object_ids = rs.GetObjects("Select objects to shear")
if object_ids:
 origin = rs.GetPoint("Origin point")
 refpt = rs.GetPoint("Reference point")
 if origin and refpt:
 rs.ShearObjects( object_ids, origin, refpt, 45.0, True )
```

### See Also

ShearObject

---

## ShowObject

### Signature

```python
ShowObject(object_id)
```

### Description

Shows a previously hidden object. Hidden objects are not visible, cannot be snapped to and cannot be selected

### Returns

bool: True of False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object to hide")
if obj: rs.HideObject(obj)
# Do something here...
rs.ShowObject( obj )
```

### See Also

HideObject, HideObjects, IsObjectHidden, ShowObjects

---

## ShowObjects

### Signature

```python
ShowObjects(object_ids)
```

### Description

Shows one or more objects. Hidden objects are not visible, cannot be snapped to and cannot be selected

### Returns

number: Number of objects shown

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.GetObjects("Select objects to hide")
if objs: rs.HideObjects(objs)
#Do something here...
rs.ShowObjects( objs )
```

### See Also

HideObject, HideObjects, IsObjectHidden, ShowObject

---

## TransformObject

### Signature

```python
TransformObject(object_id, matrix, copy=False)
```

### Description

Moves, scales, or rotates an object given a 4x4 transformation matrix. The matrix acts on the left.

### Returns

(guid): The identifier of the transformed object None: if not successful, or on error

### Example

```python
# Rotate an object by theta degrees about the world Z axis
import math
import rhinoscriptsyntax as rs
degrees = 90.0 # Some angle
radians = math.radians(degrees)
c = math.cos(radians)
s = math.sin(radians)
matrix = []
matrix.append( [c,-s, 0, 0] )
matrix.append( [s, c, 0, 0] )
matrix.append( [0, 0, 1, 0] )
matrix.append( [0, 0, 0, 1] )
obj = rs.GetObject("Select object to rotate")
if obj: rs.TransformObject( obj, matrix )
```

### See Also

TransformObjects

---

## TransformObjects

### Signature

```python
TransformObjects(object_ids, matrix, copy=False)
```

### Description

Moves, scales, or rotates a list of objects given a 4x4 transformation matrix. The matrix acts on the left.

### Returns

list(guid, ...): ids identifying the newly transformed objects

### Example

```python
import rhinoscriptsyntax as rs
# Translate (move) objects by (10,10,0)
xform = rs.XformTranslation([10,10,0])
objs = rs.GetObjects("Select objects to translate")
if objs: rs.TransformObjects(objs, xform)
```

### See Also

TransformObject

---

## UnlockObject

### Signature

```python
UnlockObject(object_id)
```

### Description

Unlocks an object. Locked objects are visible, and can be snapped to, but they cannot be selected.

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object to lock")
if obj: rs.LockObject(obj)
#Do something here...
rs.UnlockObject( obj )
```

### See Also

IsObjectLocked, LockObject, LockObjects, UnlockObjects

---

## UnlockObjects

### Signature

```python
UnlockObjects(object_ids)
```

### Description

Unlocks one or more objects. Locked objects are visible, and can be snapped to, but they cannot be selected.

### Returns

number: number of objects unlocked

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.GetObjects("Select objects to lock")
if objs: rs.LockObjects(objs)
#Do something here...
rs.UnlockObjects( objs )
```

### See Also

IsObjectLocked, LockObject, LockObjects, UnlockObject

---

## UnselectObject

### Signature

```python
UnselectObject(object_id)
```

### Description

Unselects a single selected object

### Returns

bool: True of False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
rs.Command("Line 0,0,0 5,5,0")
obj = rs.FirstObject()
if obj: rs.SelectObject(obj)
#Do something here...
rs.UnselectObject( obj )
```

### See Also

IsObjectSelected, SelectObject, SelectObjects, UnselectObjects

---

## UnselectObjects

### Signature

```python
UnselectObjects(object_ids)
```

### Description

Unselects one or more selected objects.

### Returns

number: The number of objects unselected

### Example

```python
import rhinoscriptsyntax as rs
objects = rs.GetObjects("Select object to copy in-place")
if objects:
 rs.UnselectObjects(objects)
 copies= rs.CopyObjects(objects)
 if copies: rs.SelectObjects(copies)
```

### See Also

IsObjectSelected, SelectObject, SelectObjects, UnselectObject

---

# Plane

*18 functions | 1 in use*

---

## DistanceToPlane

### Signature

```python
DistanceToPlane(plane, point)
```

### Description

Returns the distance from a 3D point to a plane

### Returns

number: The distance if successful, otherwise None

### Example

```python
import rhinoscriptsyntax as rs
point = rs.GetPoint("Point to test")
if point:
 plane = rs.ViewCPlane()
 if plane:
 distance = rs.DistanceToPlane(plane, point)
 if distance is not None:
 print("Distance to plane: {}".format(distance))
```

### See Also

Distance, PlaneClosestPoint

---

## EvaluatePlane

### Signature

```python
EvaluatePlane(plane, parameter)
```

### Description

Evaluates a plane at a U,V parameter

### Returns

point: Point3d on success

### Example

```python
import rhinoscriptsyntax as rs
view = rs.CurrentView()
plane = rs.ViewCPlane(view)
point = rs.EvaluatePlane(plane, (5,5))
rs.AddPoint( point )
```

### See Also

PlaneClosestPoint

---

## IntersectPlanes

### Signature

```python
IntersectPlanes(plane1, plane2, plane3)
```

### Description

Calculates the intersection of three planes

### Returns

point: the intersection point between the 3 planes on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
plane1 = rs.WorldXYPlane()
plane2 = rs.WorldYZPlane()
plane3 = rs.WorldZXPlane()
point = rs.IntersectPlanes(plane1, plane2, plane3)
if point: rs.AddPoint(point)
```

### See Also

LineLineIntersection, LinePlaneIntersection, PlanePlaneIntersection

---

## MovePlane

### Signature

```python
MovePlane(plane, origin)
```

### Description

Moves the origin of a plane

### Returns

plane: moved plane

### Example

```python
import rhinoscriptsyntax as rs
origin = rs.GetPoint("CPlane origin")
if origin:
 plane = rs.ViewCPlane()
 plane = rs.MovePlane(plane,origin)
 rs.ViewCplane(plane)
```

### See Also

PlaneFromFrame, PlaneFromNormal, RotatePlane

---

## PlaneClosestPoint

### Signature

```python
PlaneClosestPoint(plane, point, return_point=True)
```

### Description

Returns the point on a plane that is closest to a test point.

### Returns

point: If return_point is omitted or True, then the 3-D point point: If return_point is False, then an array containing the U,V parameters of the point None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
point = rs.GetPoint("Point to test")
if point:
 plane = rs.ViewCPlane()
 if plane:
 print(rs.PlaneClosestPoint(plane, point))
```

### See Also

DistanceToPlane, EvaluatePlane

---

## PlaneCurveIntersection

### Signature

```python
PlaneCurveIntersection(plane, curve, tolerance=None)
```

### Description

Intersect an infinite plane and a curve object

### Returns

A list of intersection information tuple if successful. The list will contain one or more of the following tuple: Element Type Description [0] Number The intersection event type, either Point (1) or Overlap (2). [1] Point3d If the event type is Point (1), then the intersection point on the curve. If the event type is Overlap (2), then intersection start point on the curve. [2] Point3d If the event type is Point (1), then the intersection point on the curve. If the event type is Overlap (2), then intersection end point on the curve. [3] Point3d If the event type is Point (1), then the intersection point on the plane. If the event type is Overlap (2), then intersection start point on the plane. [4] Point3d If the event type is Point (1), then the intersection point on the plane. If the event type is Overlap (2), then intersection end point on the plane. [5] Number If the event type is Point (1), then the curve parameter. If the event type is Overlap (2), then the start value of the curve parameter range. [6] Number If the event type is Point (1), then the curve parameter. If the event type is Overlap (2), then the end value of the curve parameter range. [7] Number If the event type is Point (1), then the U plane parameter. If the event type is Overlap (2), then the U plane parameter for curve at (n, 5). [8] Number If the event type is Point (1), then the V plane parameter. If the event type is Overlap (2), then the V plane parameter for curve at (n, 5). [9] Number If the event type is Point (1), then the U plane parameter. If the event type is Overlap (2), then the U plane parameter for curve at (n, 6). [10] Number If the event type is Point (1), then the V plane parameter. If the event type is Overlap (2), then the V plane parameter for curve at (n, 6). None: on error

### Example

```python
import rhinoscriptsyntax as rs
curve = rs.GetObject("Select curve", rs.filter.curve)
if curve:
 plane = rs.WorldXYPlane()
 intersections = rs.PlaneCurveIntersection(plane, curve)
 if intersections:
 for intersection in intersections:
 rs.AddPoint(intersection[1])
```

### See Also

IntersectPlanes, PlanePlaneIntersection, PlaneSphereIntersection

---

## PlaneEquation

### Signature

```python
PlaneEquation(plane)
```

### Description

Returns the equation of a plane as a tuple of four numbers. The standard equation of a plane with a non-zero vector is Ax+By+Cz+D=0

### Returns

tuple(number, number, number, number): containing four numbers that represent the coefficients of the equation (A, B, C, D) if successful None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
plane = rs.ViewCPlane()
equation = rs.PlaneEquation(plane)
print("A = {}".format(equation[0]))
print("B = {}".format(equation[1]))
print("C = {}".format(equation[2]))
print("D = {}".format(equation[3]))
```

### See Also

PlaneFromFrame, PlaneFromNormal, PlaneFromPoints

---

## PlaneFitFromPoints

### Signature

```python
PlaneFitFromPoints(points)
```

### Description

Returns a plane that was fit through an array of 3D points.

### Returns

plane: The plane if successful None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
points = rs.GetPoints()
if points:
 plane = rs.PlaneFitFromPoints(points)
 if plane:
 magX = plane.XAxis.Length
 magY = plane.YAxis.Length
 rs.AddPlaneSurface( plane, magX, magY )
```

### See Also

PlaneFromFrame, PlaneFromNormal, PlaneFromPoints

---

## PlaneFromFrame

### Signature

```python
PlaneFromFrame(origin, x_axis, y_axis)
```

### Description

Construct a plane from a point, and two vectors in the plane.

### Returns

plane: The plane if successful.

### Example

```python
import rhinoscriptsyntax as rs
origin = rs.GetPoint("CPlane origin")
if origin:
 xaxis = (1,0,0)
 yaxis = (0,0,1)
 plane = rs.PlaneFromFrame( origin, xaxis, yaxis )
 rs.ViewCPlane(None, plane)
```

### See Also

MovePlane, PlaneFromNormal, PlaneFromPoints, RotatePlane

---

## PlaneFromNormal

** IN USE**

### Signature

```python
PlaneFromNormal(origin, normal, xaxis=None)
```

### Description

Creates a plane from an origin point and a normal direction vector.

### Returns

plane: The plane if successful.

### Example

```python
import rhinoscriptsyntax as rs
origin = rs.GetPoint("CPlane origin")
if origin:
 direction = rs.GetPoint("CPlane direction")
 if direction:
 normal = direction - origin
 normal = rs.VectorUnitize(normal)
 rs.ViewCPlane( None, rs.PlaneFromNormal(origin, normal) )
```

### See Also

MovePlane, PlaneFromFrame, PlaneFromPoints, RotatePlane

---

## PlaneFromPoints

### Signature

```python
PlaneFromPoints(origin, x, y)
```

### Description

Creates a plane from three non-colinear points

### Returns

plane: The plane if successful, otherwise None

### Example

```python
import rhinoscriptsyntax as rs
corners = rs.GetRectangle()
if corners:
 rs.ViewCPlane( rs.PlaneFromPoints(corners[0], corners[1], corners[3]))
```

### See Also

PlaneFromFrame, PlaneFromNormal

---

## PlanePlaneIntersection

### Signature

```python
PlanePlaneIntersection(plane1, plane2)
```

### Description

Calculates the intersection of two planes

### Returns

line: a line with two 3d points identifying the starting/ending points of the intersection None: on error

### Example

```python
import rhinoscriptsyntax as rs
plane1 = rs.WorldXYPlane()
plane2 = rs.WorldYZPlane()
line = rs.PlanePlaneIntersection(plane1, plane2)
if line: rs.AddLine(line[0], line[1])
```

### See Also

IntersectPlanes, LineLineIntersection, LinePlaneIntersection

---

## PlaneSphereIntersection

### Signature

```python
PlaneSphereIntersection(plane, sphere_plane, sphere_radius)
```

### Description

Calculates the intersection of a plane and a sphere

### Returns

list(number, point|plane, number): of intersection results Element Type Description [0] number The type of intersection, where 0 = point and 1 = circle. [1] point or plane If a point intersection, the a Point3d identifying the 3-D intersection location. If a circle intersection, then the circle's plane. The origin of the plane will be the center point of the circle [2] number If a circle intersection, then the radius of the circle. None: on error

### Example

```python
import rhinoscriptsyntax as rs
plane = rs.WorldXYPlane()
radius = 10
results = rs.PlaneSphereIntersection(plane, plane, radius)
if results:
 if results[0]==0:
 rs.AddPoint(results[1])
 else:
 rs.AddCircle(results[1], results[2])
```

### See Also

IntersectPlanes, LinePlaneIntersection, PlanePlaneIntersection

---

## PlaneTransform

### Signature

```python
PlaneTransform(plane, xform)
```

### Description

Transforms a plane

### Returns

plane:the resulting plane if successful None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
plane = rs.ViewCPlane()
xform = rs.XformRotation(45.0, plane.Zaxis, plane.Origin)
plane = rs.PlaneTransform(plane, xform)
rs.ViewCPlane(None, plane)
```

### See Also

PlaneFromFrame, PlaneFromNormal, PlaneFromPoints

---

## RotatePlane

### Signature

```python
RotatePlane(plane, angle_degrees, axis)
```

### Description

Rotates a plane

### Returns

plane: rotated plane on success

### Example

```python
import rhinoscriptsyntax as rs
plane = rs.ViewCPlane()
rotated = rs.RotatePlane(plane, 45.0, plane.XAxis)
rs.ViewCPlane( None, rotated )
```

### See Also

MovePlane, PlaneFromFrame, PlaneFromNormal

---

## WorldXYPlane

### Signature

```python
WorldXYPlane()
```

### Description

Returns Rhino's world XY plane

### Returns

plane: Rhino's world XY plane

### Example

```python
import rhinoscriptsyntax as rs
view = rs.CurrentView()
rs.ViewCPlane( view, rs.WorldXYPlane() )
```

### See Also

WorldYZPlane, WorldZXPlane

---

## WorldYZPlane

### Signature

```python
WorldYZPlane()
```

### Description

Returns Rhino's world YZ plane

### Returns

plane: Rhino's world YZ plane

### Example

```python
import rhinoscriptsyntax as rs
view = rs.CurrentView()
rs.ViewCPlane( view, rs.WorldYZPlane() )
```

### See Also

WorldXYPlane, WorldZXPlane

---

## WorldZXPlane

### Signature

```python
WorldZXPlane()
```

### Description

Returns Rhino's world ZX plane

### Returns

plane: Rhino's world ZX plane

### Example

```python
import rhinoscriptsyntax as rs
view = rs.CurrentView()
rs.ViewCPlane( view, rs.WorldZXPlane() )
```

### See Also

WorldXYPlane, WorldYZPlane

---

# Pointvector

*33 functions | 0 in use*

---

## IsVectorParallelTo

### Signature

```python
IsVectorParallelTo(vector1, vector2)
```

### Description

Compares two vectors to see if they are parallel

### Returns

number: the value represents -1 = the vectors are anti-parallel 0 = the vectors are not parallel 1 = the vectors are parallel

### Example

```python
import rhinoscriptsyntax as rs
vector1 = (1,0,0)
vector2 = (0,1,0)
print(rs.IsVectorParallelTo( vector1, vector2 ))
```

### See Also

IsVectorPerpendicularTo, IsVectorTiny, IsVectorZero

---

## IsVectorPerpendicularTo

### Signature

```python
IsVectorPerpendicularTo(vector1, vector2)
```

### Description

Compares two vectors to see if they are perpendicular

### Returns

bool: True if vectors are perpendicular, otherwise False

### Example

```python
import rhinoscriptsyntax as rs
vector1 = (1,0,0)
vector2 = (0,1,0)
print(rs.IsVectorPerpendicularTo( vector1, vector2 ))
```

### See Also

IsVectorParallelTo, IsVectorTiny, IsVectorZero

---

## IsVectorTiny

### Signature

```python
IsVectorTiny(vector)
```

### Description

Verifies that a vector is very short. The X,Y,Z elements are <= 1.0e-12

### Returns

bool: True if the vector is tiny, otherwise False

### Example

```python
import rhinoscriptsyntax as rs
pt1 = rs.GetPoint("First point")
pt2 = rs.GetPoint("Next point")
vector = pt2 - pt1
if rs.IsVectorTiny(vector):
 print("The vector is tiny.")
else:
 print("The vector is not tiny.")
```

### See Also

IsVectorZero, VectorCreate

---

## IsVectorZero

### Signature

```python
IsVectorZero(vector)
```

### Description

Verifies that a vector is zero, or tiny. The X,Y,Z elements are equal to 0.0

### Returns

bool: True if the vector is zero, otherwise False

### Example

```python
import rhinoscriptsyntax as rs
pt1 = rs.GetPoint("First point")
pt2 = rs.GetPoint("Next point")
vector = pt2 - pt1
if rs.IsVectorZero(vector):
 print("The vector is zero.")
else:
 print("The vector is not zero.")
```

### See Also

IsVectorTiny, VectorCreate

---

## PointAdd

### Signature

```python
PointAdd(point1, point2)
```

### Description

Adds a 3D point or a 3D vector to a 3D point

### Returns

point: the resulting 3D point if successful

### Example

```python
import rhinoscriptsyntax as rs
point1 = (1,1,1)
point2 = (2,2,2)
point = rs.PointAdd(point1, point2)
print(point)
```

### See Also

PointCompare, PointDivide, PointScale, PointSubtract, PointTransform

---

## PointArrayBoundingBox

### Signature

```python
PointArrayBoundingBox(points, view_or_plane=None, in_world_coords=True)
```

### Description

Returns either a world axis-aligned or a construction plane axis-aligned bounding box of an array of 3-D point locations.

### Returns

list(point, ....): Eight points that define the bounding box. Points returned in counter- clockwise order starting with the bottom rectangle of the box. None: on error

### See Also

BoundingBox

---

## PointArrayClosestPoint

### Signature

```python
PointArrayClosestPoint(points, test_point)
```

### Description

Finds the point in a list of 3D points that is closest to a test point

### Returns

number: index of the element in the point list that is closest to the test point

### Example

```python
import rhinoscriptsyntax as rs
cloud = rs.GetObject("Select point cloud")
if cloud:
 point = rs.GetPoint("Point to test")
 if point:
 cloud = rs.PointCloudPoints(cloud)
 index = rs.PointArrayClosestPoint(cloud, point)
 if index is not None:
 point_id = rs.AddPoint(cloud[index])
 rs.SelectObject( point_id )
```

### See Also

CurveClosestPoint, SurfaceClosestPoint

---

## PointArrayTransform

### Signature

```python
PointArrayTransform(points, xform)
```

### Description

Transforms a list of 3D points

### Returns

list(point, ...): transformed points on success

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
points = rs.BoundingBox(obj)
xform = rs.XformRotation2(45.0, (0,0,1), (0,0,0))
points = rs.PointArrayTransform(points, xform)
rs.AddPoints(points)
```

### See Also

PointArrayClosestPoint

---

## PointClosestObject

### Signature

```python
PointClosestObject(point, object_ids)
```

### Description

Finds the object that is closest to a test point

### Returns

list(guid, point): closest [0] object_id and [1] point on object on success None: on failure

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.GetObjects("Select target objects for closest point", 63)
if objs:
 point = rs.GetPoint("Test point")
 if point:
 results = rs.PointClosestObject(point, objs)
 if results:
 print("Object id:{}".format(results[0]))
 rs.AddPoint( results[1] )
```

### See Also

CurveClosestObject

---

## PointCompare

### Signature

```python
PointCompare(point1, point2, tolerance=None)
```

### Description

Compares two 3D points

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
point1 = (1,1,1)
point2 = (2,2,2)
print(rs.PointCompare(point1, point2))
```

### See Also

PointAdd, PointDivide, PointScale, PointSubtract, PointTransform

---

## PointDivide

### Signature

```python
PointDivide(point, divide)
```

### Description

Divides a 3D point by a value

### Returns

point: resulting point

### Example

```python
import rhinoscriptsyntax as rs
point = rs.PointDivide([5,5,0], 5)
print(point)
```

### See Also

PointAdd, PointCompare, PointScale, PointSubtract, PointTransform

---

## PointScale

### Signature

```python
PointScale(point, scale)
```

### Description

Scales a 3D point by a value

### Returns

point: resulting point on success

### Example

```python
import rhinoscriptsyntax as rs
point = rs.PointScale([1,0,0], 5)
print(point)
```

### See Also

PointAdd, PointCompare, PointDivide, PointSubtract, PointTransform

---

## PointSubtract

### Signature

```python
PointSubtract(point1, point2)
```

### Description

Subtracts a 3D point or a 3D vector from a 3D point

### Returns

point: the resulting 3D point if successful

### Example

```python
import rhinoscriptsyntax as rs
point1 = (1,1,1)
point2 = (2,2,2)
point = rs.PointSubtract(point1, point2)
print(point)
```

### See Also

PointAdd, PointCompare, PointDivide, PointScale, PointTransform

---

## PointTransform

### Signature

```python
PointTransform(point, xform)
```

### Description

Transforms a 3D point

### Returns

vector: transformed vector on success

### Example

```python
# Translate (move) objects by (10,10,0)
import rhinoscriptsyntax as rs
point = 5,5,0
matrix = rs.XformTranslation((10,10,0))
result = rs.PointTransform(point, matrix)
print(result)
```

### See Also

PointAdd, PointCompare, PointDivide, PointScale, PointSubtract

---

## PointsAreCoplanar

### Signature

```python
PointsAreCoplanar(points, tolerance=1.0e-12)
```

### Description

Verifies that a list of 3D points are coplanar

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
def SurfacesAreCoplanar(srf1, srf2):
 if( not rs.IsSurface(srf1) or not rs.IsSurface(srf2) ): return False
 if( not rs.IsSurfacePlanar(srf1) or not rs.IsSurfacePlanar(srf2) ): return False
 pts1 = rs.SurfacePoints(srf1)
 pts2 = rs.SurfacePoints(srf2)
 if( pts1==None or pts2==None ): return False
 pts1.extend(pts2)
 return rs.PointsAreCoplanar(pts1)

x = rs.GetObject( "First surface to test", rs.filter.surface)
y = rs.GetObject( "Second surface to test", rs.filter.surface)
print(SurfacesAreCoplanar(x, y))
```

### See Also

IsPoint, IsPointCloud, PointCoordinates

---

## ProjectPointToMesh

### Signature

```python
ProjectPointToMesh(points, mesh_ids, direction)
```

### Description

Projects one or more points onto one or more meshes

### Returns

list(point, ...): projected points on success

### Example

```python
import rhinoscriptsyntax as rs
mesh = rs.GetObject("Select mesh to project onto", rs.filter.mesh)
objects = rs.GetObjects("Select points to project", rs.filter.point)
points = [rs.PointCoordinates(obj) for obj in objects]
# project down...
results = rs.ProjectPointToMesh(points, mesh, (0,0,-1))
rs.AddPoints( results )
```

### See Also

ProjectCurveToMesh, ProjectCurveToSurface, ProjectPointToSurface

---

## ProjectPointToSurface

### Signature

```python
ProjectPointToSurface(points, surface_ids, direction)
```

### Description

Projects one or more points onto one or more surfaces or polysurfaces

### Returns

list(point, ...): projected points on success

### Example

```python
import rhinoscriptsyntax as rs
surface = rs.GetObject("Select surface to project onto", rs.filter.surface)
objects = rs.GetObjects("Select points to project", rs.filter.point)
points = [rs.PointCoordinates(obj) for obj in objects]
# Project down...
results = rs.ProjectPointToSurface(points, surface, (0,0,-1))
rs.AddPoints(results)
```

### See Also

ProjectCurveToMesh, ProjectCurveToSurface, ProjectPointToMesh

---

## PullPoints

### Signature

```python
PullPoints(object_id, points)
```

### Description

Pulls an array of points to a surface or mesh object. For more information, see the Rhino help file Pull command

### Returns

list(point, ...): 3D points pulled onto surface or mesh

### Example

```python
import rhinoscriptsyntax as rs
surface = rs.GetObject("Select surface that pulls", rs.filter.surface)
objects = rs.GetObjects("Select points to pull", rs.filter.point)
points = [rs.PointCoordinates(obj) for obj in objects]
results = rs.PullPoints( surface, points )
rs.AddPoints( results )
```

### See Also

PullCurve

---

## VectorAdd

### Signature

```python
VectorAdd(vector1, vector2)
```

### Description

Adds two 3D vectors

### Returns

vector: the resulting 3D vector if successful

### Example

```python
import rhinoscriptsyntax as rs
vector1 = (1,0,0)
vector2 = (0,1,0)
vector = rs.VectorAdd(vector1, vector2)
print(vector)
```

### See Also

VectorCreate, VectorScale, VectorSubtract

---

## VectorAngle

### Signature

```python
VectorAngle(vector1, vector2)
```

### Description

Returns the angle, in degrees, between two 3-D vectors

### Returns

number: The angle in degrees if successful None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
s0 = rs.GetObject("Surface 0", rs.filter.surface)
s1 = rs.GetObject("Surface 1", rs.filter.surface)
du0 = rs.SurfaceDomain(s0, 0)
dv0 = rs.SurfaceDomain(s0, 1)
du1 = rs.SurfaceDomain(s1, 0)
dv1 = rs.SurfaceDomain(s1, 1)
n0 = rs.SurfaceNormal(s0, (du0[0], dv0[0]))
n1 = rs.SurfaceNormal(s1, (du1[0], dv1[0]))
print(rs.VectorAngle(n0, n1))
print(rs.VectorAngle(n0, rs.VectorReverse(n1)))
```

### See Also

Angle, Angle2

---

## VectorCompare

### Signature

```python
VectorCompare(vector1, vector2)
```

### Description

Compares two 3D vectors

### Returns

number: result of comparing the vectors. -1 if vector1 is less than vector2 0 if vector1 is equal to vector2 1 if vector1 is greater than vector2

### Example

```python
import rhinoscriptsyntax as rs
vector1 = (1,0,0)
vector2 = (0,1,0)
rc = rs.VectorCompare(vector1 , vector2)
print(rc)
```

### See Also

IsVectorTiny, IsVectorZero, VectorCreate

---

## VectorCreate

### Signature

```python
VectorCreate(to_point, from_point)
```

### Description

Creates a vector from two 3D points

### Returns

vector: the resulting vector if successful

### Example

```python
import rhinoscriptsyntax as rs
point1 = rs.GetPoint("First point")
point2 = rs.GetPoint("Next point")
vector = rs.VectorCreate(point2, point1)
print(vector)
```

### See Also

IsVectorTiny, IsVectorZero, VectorCompare, VectorUnitize

---

## VectorCrossProduct

### Signature

```python
VectorCrossProduct(vector1, vector2)
```

### Description

Calculates the cross product of two 3D vectors

### Returns

vector: the resulting cross product direction if successful

### Example

```python
import rhinoscriptsyntax as rs
vector1 = (1,0,0)
vector2 = (0,1,0)
vector = rs.VectorCrossProduct(vector1, vector2)
print(vector)
```

### See Also

VectorDotProduct, VectorUnitize

---

## VectorDivide

### Signature

```python
VectorDivide(vector, divide)
```

### Description

Divides a 3D vector by a value

### Returns

vector: resulting vector on success

### Example

```python
import rhinoscriptsyntax as rs
vector = rs.VectorDivide((5,5,0), 5)
print(vector)
```

### See Also

VectorAdd, VectorCreate, VectorSubtract

---

## VectorDotProduct

### Signature

```python
VectorDotProduct(vector1, vector2)
```

### Description

Calculates the dot product of two 3D vectors

### Returns

vector: the resulting dot product if successful

### Example

```python
import rhinoscriptsyntax as rs
vector1 = [1,0,0]
vector2 = [0,1,0]
dblDotProduct = rs.VectorDotProduct(vector1, vector2)
print(dblDotProduct)
```

### See Also

VectorCrossProduct, VectorUnitize

---

## VectorLength

### Signature

```python
VectorLength(vector)
```

### Description

Returns the length of a 3D vector

### Returns

number: The length of the vector if successful, otherwise None

### Example

```python
import rhinoscriptsyntax as rs
point1 = rs.GetPoint("First point")
point2 = rs.GetPoint("Next point")
vector = rs.VectorCreate(point1, point2)
print(rs.VectorLength(vector))
```

### See Also

VectorAdd, VectorCreate, VectorSubtract, VectorUnitize

---

## VectorMultiply

### Signature

```python
VectorMultiply(vector1, vector2)
```

### Description

Multiplies two 3D vectors

### Returns

vector: the resulting inner (dot) product if successful

### Example

```python
import rhinoscriptsyntax as rs
product = rs.VectorMultiply( [2,2,2], [3,3,3] )
print(product)
```

### See Also

VectorAdd, VectorCreate, VectorSubtract

---

## VectorReverse

### Signature

```python
VectorReverse(vector)
```

### Description

Reverses the direction of a 3D vector

### Returns

vector: reversed vector on success

### Example

```python
import rhinoscriptsyntax as rs
vector = rs.VectorReverse([1,0,0])
print(vector)
```

### See Also

VectorCreate, VectorUnitize

---

## VectorRotate

### Signature

```python
VectorRotate(vector, angle_degrees, axis)
```

### Description

Rotates a 3D vector

### Returns

vector: rotated vector on success

### Example

```python
import rhinoscriptsyntax as rs
vector = rs.VectorRotate([1,0,0], 90.0, [0,0,1])
print(vector)
```

### See Also

VectorCreate, VectorScale

---

## VectorScale

### Signature

```python
VectorScale(vector, scale)
```

### Description

Scales a 3-D vector

### Returns

vector: resulting vector on success

### Example

```python
import rhinoscriptsyntax as rs
vector = rs.VectorScale([1,0,0], 5)
print(vector)
```

### See Also

VectorAdd, VectorCreate, VectorSubtract

---

## VectorSubtract

### Signature

```python
VectorSubtract(vector1, vector2)
```

### Description

Subtracts two 3D vectors

### Returns

vector: the resulting 3D vector

### Example

```python
import rhinoscriptsyntax as rs
vector1 = [1,0,0]
vector2 = [0,1,0]
vector = rs.VectorSubtract(vector1, vector2)
print(vector)
```

### See Also

VectorAdd, VectorCreate, VectorScale

---

## VectorTransform

### Signature

```python
VectorTransform(vector, xform)
```

### Description

Transforms a 3D vector

### Returns

vector: transformed vector on success

### Example

```python
import rhinoscriptsyntax as rs
vector = (1,0,0) #world x-axis
xform = rs.XformRotation2(90.0, (0,0,1), (0,0,0))
vector = rs.VectorTransform(vector, xform)
print(vector)
```

### See Also

IsVectorZero, VectorCreate, VectorUnitize

---

## VectorUnitize

### Signature

```python
VectorUnitize(vector)
```

### Description

Unitizes, or normalizes a 3D vector. Note, zero vectors cannot be unitized

### Returns

vector: unitized vector on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
vector = rs.VectorUnitize( [1.5,-4.1,3.6] )
print(vector)
```

### See Also

IsVectorZero, VectorCreate

---

# Selection

*25 functions | 5 in use*

---

## AllObjects

** IN USE**

### Signature

```python
AllObjects(select=False, include_lights=False, include_grips=False, include_references=False)
```

### Description

Returns identifiers of all objects in the document.

### Returns

list(guid, ...): identifiers for all the objects in the document

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.AllObjects()
for obj in objs: print("Object identifier: {}".format(obj))
```

### See Also

HiddenObjects, LockedObjects, NormalObjects

---

## FirstObject

### Signature

```python
FirstObject(select=False, include_lights=False, include_grips=False)
```

### Description

Returns identifier of the first object in the document. The first object is the last object created by the user.

### Returns

guid: The identifier of the object if successful.

### Example

```python
import rhinoscriptsyntax as rs
rs.AddLine( (0,0,0), (5,5,0) )
rs.AddLine( (0,0,0), (5,0,0) )
rs.AddLine( (0,0,0), (0,5,0) )
objectId = rs.FirstObject()
print("Object identifier: {}".format(objectId))
rs.SelectObject(objectId)
```

### See Also

LastObject, NextObject

---

## GetCurveObject

### Signature

```python
GetCurveObject(message=None, preselect=False, select=False)
```

### Description

Prompts user to pick or select a single curve object

### Returns

Tuple containing the following information [0] guid identifier of the curve object [1] bool True if the curve was preselected, otherwise False [2] number selection method 0 = selected by non-mouse method (SelAll, etc.). 1 = selected by mouse click on the object. 2 = selected by being inside of a mouse window. 3 = selected by intersecting a mouse crossing window. [3] point selection point [4] number the curve parameter of the selection point [5] str name of the view selection was made None: if no object picked

### Example

```python
import rhinoscriptsyntax as rs
select_result = rs.GetCurveObject("Select curve")
if select_result:
 print("Curve identifier: {}".format(select_result[0]))
```

### See Also

GetObject, GetObjects, GetSurfaceObject

---

## GetObject

### Signature

```python
GetObject(message=None, filter=0, preselect=False, select=False, custom_filter=None, subobjects=False)
```

### Description

Prompts user to pick, or select, a single object.

### Returns

guid: Identifier of the picked object None: if user did not pick an object

### Example

```python
import rhinoscriptsyntax as rs
objectId = rs.GetObject("Pick any object")
if objectId:
 print("Object identifier: {}".format(objectId))
objectId = rs.GetObject("Pick a curve or surface", rs.filter.curve | rs.filter.surface)
if objectId:
 print("Object identifier: {}".format(objectId))
```

### See Also

GetCurveObject, GetObjectEx, GetObjects, GetSurfaceObject

---

## GetObjectEx

### Signature

```python
GetObjectEx(message=None, filter=0, preselect=False, select=False, objects=None)
```

### Description

Prompts user to pick, or select a single object

### Returns

tuple(guid, bool, number, point, str): containing the following information [0] identifier of the object [1] True if the object was preselected, otherwise False [2] selection method (see help) [3] selection point [4] name of the view selection was made None: if no object selected

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObjectEx("Select object", 0, True)
if obj:
 print("Object id = {}".format(obj[0]))
 print("Object was preselected = {}".format(obj[1]))
 if obj[2]==0:
 print("Selection method = 0 (non-mouse)")
 elif obj[2]==1:
 print("Selection method = 1 (mouse)")
 print("Pick point = {}".format(obj[3]))
 elif obj[2]==2:
 print("Selection method = 2 (window)")
 elif obj[2]==3:
 print("Selection method = 3 (crossing)")
 print("Active view = {}".format(obj[4]))
```

### See Also

GetCurveObject, GetObject, GetObjects, GetObjectsEx, GetSurfaceObject

---

## GetObjects

### Signature

```python
GetObjects(message=None, filter=0, group=True, preselect=False, select=False, objects=None, minimum_count=1, maximum_count=0, custom_filter=None)
```

### Description

Prompts user to pick or select one or more objects.

### Returns

list(guid, ...): identifiers of the picked objects

### Example

```python
import rhinoscriptsyntax as rs
objectIds = rs.GetObjects("Pick some curves", rs.filter.curve)
for id in objectIds: print("Object identifier:{}".format(id))
```

### See Also

GetCurveObject, GetObject, GetSurfaceObject

---

## GetObjectsEx

### Signature

```python
GetObjectsEx(message=None, filter=0, group=True, preselect=False, select=False, objects=None)
```

### Description

Prompts user to pick, or select one or more objects

### Returns

list(tuple(guid, bool, number, point, str), ...): containing the following information [n][0] identifier of the object [n][1] True if the object was preselected, otherwise False [n][2] selection method (see help) [n][3] selection point [n][4] name of the view selection was made

### Example

```python
import rhinoscriptsyntax as rs
objects = rs.GetObjectsEx("Select objects", 0, True)
for obj in objects:
 print("Object id = {}".format(obj[0]))
 print("Object was preselected = {}".format(obj[1]))
 if obj[2]==0:
 print("Selection method = 0 (non-mouse)")
 elif obj[2]==1:
 print("Selection method = 1 (mouse)")
 print("Pick point = {}".format(obj[3]))
 elif obj[2]==2:
 print("Selection method = 2 (window)")
 elif obj[2]==3:
 print("Selection method = 3 (crossing)")
 print("Active view = {}".format(obj[4]))
```

### See Also

GetCurveObject, GetObject, GetObjectEx, GetObjects, GetSurfaceObject

---

## GetPointCoordinates

### Signature

```python
GetPointCoordinates(message="Select points", preselect=False)
```

### Description

Prompts the user to select one or more point objects.

### Returns

list(point, ...): 3d coordinates of point objects on success

### Example

```python
import rhinoscriptsyntax as rs
points = rs.GetPointCoordinates()
for point in points: print(point)
```

### See Also

GetObject, GetObjects, GetPoint, GetPoints, PointCoordinates

---

## GetSurfaceObject

### Signature

```python
GetSurfaceObject(message="Select surface", preselect=False, select=False)
```

### Description

Prompts the user to select a single surface

### Returns

tuple(guid, bool, number, point, (number, number), str): of information on success [0] identifier of the surface [1] True if the surface was preselected, otherwise False [2] selection method ( see help ) [3] selection point [4] u,v surface parameter of the selection point [5] name of the view in which the selection was made None: on error

### Example

```python
import rhinoscriptsyntax as rs
select = rs.GetSurfaceObject("Select surface")
if select:
 print("Surface identifier: {}".format(select[0]))
```

### See Also

GetCurveObject, GetObject, GetObjects

---

## HiddenObjects

### Signature

```python
HiddenObjects(include_lights=False, include_grips=False, include_references=False)
```

### Description

Returns identifiers of all hidden objects in the document. Hidden objects are not visible, cannot be snapped to, and cannot be selected

### Returns

list(guid, ...): identifiers of the hidden objects if successful.

### Example

```python
import rhinoscriptsyntax as rs
hidden = rs.HiddenObjects()
for obj in hidden: print("Object identifier{}".format(obj))
```

### See Also

AllObjects, LockedObjects, NormalObjects

---

## InvertSelectedObjects

### Signature

```python
InvertSelectedObjects(include_lights=False, include_grips=False, include_references=False)
```

### Description

Inverts the current object selection. The identifiers of the newly selected objects are returned

### Returns

list(guid, ...): identifiers of the newly selected objects if successful.

### Example

```python
import rhinoscriptsyntax as rs
rs.GetObjects("Select some objects", select=True)
objs = rs.InvertSelectedObjects()
for id in objs: print("Object identifier:{}".format(id))
```

### See Also

SelectedObjects, UnselectAllObjects

---

## LastCreatedObjects

### Signature

```python
LastCreatedObjects(select=False)
```

### Description

Returns identifiers of the objects that were most recently created or changed by scripting a Rhino command using the Command function. It is important to call this function immediately after calling the Command function as only the most recently created or changed object identifiers will be returned

### Returns

list(guid, ...): identifiers of the most recently created or changed objects if successful.

### Example

```python
import rhinoscriptsyntax as rs
rs.Command( "_-Circle 0,0,0 10" )
rs.Command( "_-Circle 10,0,0 10" )
rs.Command( "_-Circle 20,0,0 10" )
objs = rs.LastCreatedObjects()
if objs:
 # Only the last circle will be selected
 rs.SelectObjects( objs )
```

### See Also

Command

---

## LastObject

### Signature

```python
LastObject(select=False, include_lights=False, include_grips=False)
```

### Description

Returns the identifier of the last object in the document. The last object in the document is the first object created by the user

### Returns

guid: identifier of the object on success

### Example

```python
import rhinoscriptsyntax as rs
rs.AddLine((0,0,0), (5,5,0))
rs.AddCircle((0,0,0), 5)
print("Object identifier: {}".format(rs.LastObject()))
```

### See Also

FirstObject, NextObject

---

## LockedObjects

### Signature

```python
LockedObjects(include_lights=False, include_grips=False, include_references=False)
```

### Description

Returns identifiers of all locked objects in the document. Locked objects cannot be snapped to, and cannot be selected

### Returns

list(guid, ...): identifiers the locked objects if successful.

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.LockedObjects()
for obj in objs: print("Object identifier:{}".format(obj))
```

### See Also

AllObjects, HiddenObjects, NormalObjects

---

## NextObject

### Signature

```python
NextObject(object_id, select=False, include_lights=False, include_grips=False)
```

### Description

Returns the identifier of the next object in the document

### Returns

guid: identifier of the object on success

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.FirstObject()
while obj:
 print("Object identifier:{}".format(obj))
 obj = rs.NextObject(obj)
```

### See Also

FirstObject, LastObject

---

## NormalObjects

### Signature

```python
NormalObjects(include_lights=False, include_grips=False)
```

### Description

Returns identifiers of all normal objects in the document. Normal objects are visible, can be snapped to, and are independent of selection state

### Returns

list(guid, ...): identifier of normal objects if successful.

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.NormalObjects()
for obj in objs: print("Object identifier:{}".format(obj))
```

### See Also

AllObjects, HiddenObjects, LockedObjects

---

## ObjectsByColor

### Signature

```python
ObjectsByColor(color, select=False, include_lights=False)
```

### Description

Returns identifiers of all objects based on color

### Returns

list(guid, ...): identifiers of objects of the selected color.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Pick any object")
if obj:
 color = rs.ObjectColor(obj)
 rs.ObjectsByColor(color, True)
```

---

## ObjectsByGroup

### Signature

```python
ObjectsByGroup(group_name, select=False)
```

### Description

Returns identifiers of all objects based on the objects' group name

### Returns

list(guid, ...):identifiers for objects in the group on success

### Example

```python
import rhinoscriptsyntax as rs
group = rs.GetString("Group to select")
if group: rs.ObjectsByGroup( group, True )
```

---

## ObjectsByLayer

** IN USE**

### Signature

```python
ObjectsByLayer(layer_name, select=False)
```

### Description

Returns identifiers of all objects based on the objects' layer name

### Returns

list(guid, ...): identifiers for objects in the specified layer

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Pick any object")
if obj:
 layer = rs.ObjectLayer(obj)
 rs.ObjectsByLayer(layer, True)
```

---

## ObjectsByName

### Signature

```python
ObjectsByName(name, select=False, include_lights=False, include_references=False)
```

### Description

Returns identifiers of all objects based on user-assigned name

### Returns

list(guid, ...): identifiers for objects with the specified name.

### Example

```python
import rhinoscriptsyntax as rs
name = rs.GetString("Name to select")
if name: rs.ObjectsByName(name,True)
```

---

## ObjectsByType

** IN USE**

### Signature

```python
ObjectsByType(geometry_type, select=False, state=0)
```

### Description

Returns identifiers of all objects based on the objects' geometry type.

### Returns

list(guid, ...): identifiers of object that fit the specified type(s).

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.ObjectsByType(4 | 8, True)
```

---

## SelectedObjects

** IN USE**

### Signature

```python
SelectedObjects(include_lights=False, include_grips=False)
```

### Description

Returns the identifiers of all objects that are currently selected

### Returns

list(guid, ...) identifiers of selected objects

### Example

```python
import rhinoscriptsyntax as rs
objects = rs.SelectedObjects()
for obj in objects: print("Object identifier: {}".format(obj))
```

### See Also

InvertSelectedObjects, UnselectAllObjects

---

## UnselectAllObjects

** IN USE**

### Signature

```python
UnselectAllObjects()
```

### Description

Unselects all objects in the document

### Returns

number: the number of objects that were unselected

### Example

```python
import rhinoscriptsyntax as rs
count = rs.UnselectAllObjects()
print("{} objects were unselected".format(count))
```

### See Also

InvertSelectedObjects, SelectedObjects

---

## VisibleObjects

### Signature

```python
VisibleObjects(view=None, select=False, include_lights=False, include_grips=False)
```

### Description

Return identifiers of all objects that are visible in a specified view

### Returns

list(guid, ...): identifiers of the visible objects

### Example

```python
import rhinoscriptsyntax as rs
object_ids = rs.VisibleObjects("Top")
if object_ids:
 for id in object_ids: print("Object identifier:{}".format(id))
```

### See Also

IsView, IsVisibleInView

---

## WindowPick

### Signature

```python
WindowPick(corner1, corner2, view=None, select=False, in_window=True)
```

### Description

Picks objects using either a window or crossing selection

### Returns

list(guid, ...): identifiers of selected objects on success

### Example

```python
import rhinoscriptsyntax as rs
rs.WindowPick((0,0,0), (0,0,0), None, True)
```

---

# Surface

*100 functions | 14 in use*

---

## AddBox

** IN USE**

### Signature

```python
AddBox(corners)
```

### Description

Adds a box shaped polysurface to the document

### Returns

guid: identifier of the new object on success

### Example

```python
import rhinoscriptsyntax as rs
box = rs.GetBox()
if box: rs.AddBox(box)
```

### See Also

AddCone, AddCylinder, AddSphere, AddTorus

---

## AddCone

** IN USE**

### Signature

```python
AddCone(base, height, radius, cap=True)
```

### Description

Adds a cone shaped polysurface to the document

### Returns

guid: identifier of the new object on success

### Example

```python
import rhinoscriptsyntax as rs
radius = 5.0
base = rs.GetPoint("Base of cone")
if base:
 height = rs.GetPoint("Height of cone", base)
 if height: rs.AddCone(base, height, radius)
```

### See Also

AddBox, AddCylinder, AddSphere, AddTorus

---

## AddCutPlane

### Signature

```python
AddCutPlane(object_ids, start_point, end_point, normal=None)
```

### Description

Adds a planar surface through objects at a designated location. For more information, see the Rhino help file for the CutPlane command

### Returns

guid: identifier of new object on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.GetObjects("Select objects for cut plane")
if objs:
 point0 = rs.GetPoint("Start of cut plane")
 if point0:
 point1 = rs.GetPoint("End of cut plane", point0)
 if point1: rs.AddCutPlane( objs, point0, point1 )
```

### See Also

AddPlaneSurface

---

## AddCylinder

### Signature

```python
AddCylinder(base, height, radius, cap=True)
```

### Description

Adds a cylinder-shaped polysurface to the document

### Returns

guid: identifier of new object if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
radius = 5.0
base = rs.GetPoint("Base of cylinder")
if base:
 height = rs.GetPoint("Height of cylinder", base)
 if height: rs.AddCylinder( base, height, radius )
```

### See Also

AddBox, AddCone, AddSphere, AddTorus

---

## AddEdgeSrf

### Signature

```python
AddEdgeSrf(curve_ids)
```

### Description

Creates a surface from 2, 3, or 4 edge curves

### Returns

guid: identifier of new object if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
curves = rs.GetObjects("Select 2, 3, or 4 curves", rs.filter.curve)
if curves and len(curves)>1 ): rs.AddEdgeSrf(curves)
```

### See Also

AddPlanarSrf, AddSrfControlPtGrid, AddSrfPt, AddSrfPtGrid

---

## AddLoftSrf

** IN USE**

### Signature

```python
AddLoftSrf(object_ids, start=None, end=None, loft_type=0, simplify_method=0, value=0, closed=False)
```

### Description

Adds a surface created by lofting curves to the document. - no curve sorting performed. pass in curves in the order you want them sorted - directions of open curves not adjusted. Use CurveDirectionsMatch and ReverseCurve to adjust the directions of open curves - seams of closed curves are not adjusted. Use CurveSeam to adjust the seam of closed curves

### Returns

list(guid, ...):Array containing the identifiers of the new surface objects if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.GetObjects("Pick curves to loft", rs.filter.curve)
if objs: rs.AddLoftSrf(objs)
```

### See Also

CurveDirectionsMatch, CurveSeam, ReverseCurve

---

## AddNetworkSrf

### Signature

```python
AddNetworkSrf(curves, continuity=1, edge_tolerance=0, interior_tolerance=0, angle_tolerance=0)
```

### Description

Creates a surface from a network of crossing curves

### Returns

guid: identifier of new object if successful

### Example

```python
import rhinoscriptsyntax as rs
curve_ids = rs.GetObjects("Select curves in network", 4, True, True)
if len(curve_ids) > 0:
 rs.AddNetworkSrf(curve_ids)
```

---

## AddNurbsSurface

### Signature

```python
AddNurbsSurface(point_count, points, knots_u, knots_v, degree, weights=None)
```

### Description

Adds a NURBS surface object to the document

### Returns

guid: identifier of new object if successful None on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Pick a surface", rs.filter.surface)
if obj:
 point_count = rs.SurfacePointCount(obj)
 points = rs.SurfacePoints(obj)
 knots = rs.SurfaceKnots(obj)
 degree = rs.SurfaceDegree(obj)
 if rs.IsSurfaceRational(obj):
 weights = rs.SurfaceWeights(obj)
 obj = rs.AddNurbsSurface(point_count, points, knots[0], knots[1], degree, weights)
 else:
 obj = rs.AddNurbsSurface(point_count, points, knots[0], knots[1], degree)
 if obj: rs.SelectObject(obj)
```

### See Also

IsSurfaceRational, SurfaceDegree, SurfaceKnotCount, SurfaceKnots, SurfacePointCount, SurfacePoints, SurfaceWeights

---

## AddPatch

### Signature

```python
AddPatch(object_ids, uv_spans_tuple_OR_surface_object_id, tolerance=None, trim=True, point_spacing=0.1, flexibility=1.0, surface_pull=1.0, fix_edges=False)
```

### Description

Fits a surface through curve, point, point cloud, and mesh objects.

### Returns

guid: Identifier of the new surface object if successful. None: on error.

---

## AddPipe

### Signature

```python
AddPipe(curve_id, parameters, radii, blend_type=0, cap=0, fit=False)
```

### Description

Creates a single walled surface with a circular profile around a curve

### Returns

list(guid, ...): identifiers of new objects created

### Example

```python
import rhinoscriptsyntax as rs
curve = rs.GetObject("Select curve to create pipe around", rs.filter.curve, True)
if curve:
 domain = rs.CurveDomain(curve)
 rs.AddPipe(curve, 0, 4)
```

---

## AddPlanarSrf

### Signature

```python
AddPlanarSrf(object_ids)
```

### Description

Creates one or more surfaces from planar curves

### Returns

list(guid, ...): identifiers of surfaces created on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.GetObjects("Select planar curves to build surface", rs.filter.curve)
if objs: rs.AddPlanarSrf(objs)
```

### See Also

AddEdgeSrf, AddSrfControlPtGrid, AddSrfPt, AddSrfPtGrid

---

## AddPlaneSurface

### Signature

```python
AddPlaneSurface(plane, u_dir, v_dir)
```

### Description

Create a plane surface and add it to the document.

### Returns

guid: The identifier of the new object if successful. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
rs.AddPlaneSurface( rs.WorldXYPlane(), 5.0, 3.0 )
```

### See Also

AddCutPlane, AddEdgeSrf, AddSrfControlPtGrid, AddSrfPt, AddSrfPtGrid, IsPlaneSurface

---

## AddRailRevSrf

### Signature

```python
AddRailRevSrf(profile, rail, axis, scale_height=False)
```

### Description

Adds a surface created through profile curves that define the surface shape and two curves that defines a surface edge.

### Returns

guid: identifier of the new object if successful None: if not successful, or on error

### Example

```python
import rhinoscriptsyntax as rs
profile = rs.GetObject("Select a profile", rs.filter.curve)
if profile:
 rail = rs.GetObject("Select a rail", rs.filter.curve)
 if rail:
 rs.AddRailRevSrf(profile, rail, ((0,0,0),(0,0,1)))
```

### See Also

AddSweep1, CurveDirectionsMatch, ReverseCurve

---

## AddRevSrf

** IN USE**

### Signature

```python
AddRevSrf(curve_id, axis, start_angle=0.0, end_angle=360.0)
```

### Description

Create a surface by revolving a curve around an axis

### Returns

guid: identifier of new object if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
curve = rs.AddLine((5,0,0), (10,0,10))
rs.AddRevSrf( curve, ((0,0,0), (0,0,1)) )
```

---

## AddSphere

** IN USE**

### Signature

```python
AddSphere(center_or_plane, radius)
```

### Description

Add a spherical surface to the document

### Returns

guid: identifier of the new object on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
radius = 2
center = rs.GetPoint("Center of sphere")
if center: rs.AddSphere(center, radius)
```

### See Also

AddBox, AddCone, AddCylinder, AddTorus

---

## AddSrfContourCrvs

### Signature

```python
AddSrfContourCrvs(object_id, points_or_plane, interval=None)
```

### Description

Adds a spaced series of planar curves resulting from the intersection of defined cutting planes through a surface or polysurface. For more information, see Rhino help for details on the Contour command

### Returns

guid: ids of new contour curves on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object", rs.filter.surface + rs.filter.polysurface)
startpoint = rs.GetPoint("Base point of center line")
endpoint = rs.GetPoint("Endpoint of center line", startpoint)
rs.AddSrfContourCrvs( obj, (startpoint, endpoint) )
```

### See Also

CurveContourPoints

---

## AddSrfControlPtGrid

### Signature

```python
AddSrfControlPtGrid(count, points, degree=(3,3))
```

### Description

Creates a surface from a grid of points

### Returns

guid: The identifier of the new object if successful. None: if not successful, or on error.

---

## AddSrfPt

### Signature

```python
AddSrfPt(points)
```

### Description

Creates a new surface from either 3 or 4 corner points.

### Returns

guid: The identifier of the new object if successful. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
points = rs.GetPoints(True, message1="Pick 3 or 4 corner points")
if points: rs.AddSrfPt(points)
```

### See Also

AddEdgeSrf, AddSrfControlPtGrid, AddSrfPtGrid

---

## AddSrfPtGrid

### Signature

```python
AddSrfPtGrid(count, points, degree=(3,3), closed=(False,False))
```

### Description

Creates a surface from a grid of points

### Returns

guid: The identifier of the new object if successful. None: if not successful, or on error.

---

## AddSweep1

### Signature

```python
AddSweep1(rail, shapes, closed=False)
```

### Description

Adds a surface created through profile curves that define the surface shape and one curve that defines a surface edge.

### Returns

list(guid, ...): of new surface objects if successful None: if not successful, or on error

### Example

```python
import rhinoscriptsyntax as rs
rail = rs.GetObject("Select rail curve", rs.filter.curve)
if rail:
 shapes = rs.GetObjects("Select cross-section curves", rs.filter.curve)
 if shapes: rs.AddSweep1( rail, shapes )
```

### See Also

AddSweep2, CurveDirectionsMatch, ReverseCurve

---

## AddSweep2

### Signature

```python
AddSweep2(rails, shapes, closed=False)
```

### Description

Adds a surface created through profile curves that define the surface shape and two curves that defines a surface edge.

### Returns

list(guid, ...): of new surface objects if successful None: if not successful, or on error

### Example

```python
import rhinoscriptsyntax as rs
rails = rs.GetObjects("Select two rail curve", rs.filter.curve)
if rails and len(rails)==2:
 shapes = rs.GetObjects("Select cross-section curves", rs.filter.curve)
 if shapes: rs.AddSweep2(rails, shapes)
```

### See Also

AddSweep1, CurveDirectionsMatch, ReverseCurve

---

## AddTorus

** IN USE**

### Signature

```python
AddTorus(base, major_radius, minor_radius, direction=None)
```

### Description

Adds a torus shaped revolved surface to the document

### Returns

guid: The identifier of the new object if successful. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
major_radius = 5.0
minor_radius = major_radius - 2.0
base = rs.GetPoint("Base of torus")
if base:
 direction = rs.GetPoint("Direction of torus", base)
 if direction:
 rs.AddTorus( base, major_radius, minor_radius, direction )
```

### See Also

AddBox, AddCone, AddCylinder, AddSphere

---

## BooleanDifference

** IN USE**

### Signature

```python
BooleanDifference(input0, input1, delete_input=True)
```

### Description

Performs a boolean difference operation on two sets of input surfaces and polysurfaces. For more details, see the BooleanDifference command in the Rhino help file

### Returns

list(guid, ...): of identifiers of newly created objects on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
filter = rs.filter.surface | rs.filter.polysurface
input0 = rs.GetObjects("Select first set of surfaces or polysurfaces", filter)
if input0:
 input1 = rs.GetObjects("Select second set of surfaces or polysurfaces", filter)
 if input1: rs.BooleanDifference(input0, input1)
```

### See Also

BooleanIntersection, BooleanUnion

---

## BooleanIntersection

** IN USE**

### Signature

```python
BooleanIntersection(input0, input1, delete_input=True)
```

### Description

Performs a boolean intersection operation on two sets of input surfaces and polysurfaces. For more details, see the BooleanIntersection command in the Rhino help file

### Returns

list(guid, ...): of identifiers of newly created objects on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
input0 = rs.GetObjects("Select first set of surfaces or polysurfaces", rs.filter.surface | rs.filter.polysurface)
if input0:
 input1 = rs.GetObjects("Select second set of surfaces or polysurfaces", rs.filter.surface | rs.filter.polysurface)
 if input1: rs.BooleanIntersection( input0, input1 )
```

### See Also

BooleanDifference, BooleanUnion

---

## BooleanUnion

** IN USE**

### Signature

```python
BooleanUnion(input, delete_input=True)
```

### Description

Performs a boolean union operation on a set of input surfaces and polysurfaces. For more details, see the BooleanUnion command in the Rhino help file

### Returns

list(guid, ...): of identifiers of newly created objects on success None on error

### Example

```python
import rhinoscriptsyntax as rs
input = rs.GetObjects("Select surfaces or polysurfaces to union", rs.filter.surface | rs.filter.polysurface)
if input and len(input)>1: rs.BooleanUnion(input)
```

### See Also

BooleanDifference, BooleanUnion

---

## BrepClosestPoint

### Signature

```python
BrepClosestPoint(object_id, point)
```

### Description

Returns the point on a surface or polysurface that is closest to a test point. This function works on both untrimmed and trimmed surfaces.

### Returns

tuple(point, [number, number], [number, number], vector): of closest point information if successful. The list will contain the following information: Element Type Description 0 Point3d The 3-D point at the parameter value of the closest point. 1 (U, V) Parameter values of closest point. Note, V is 0 if the component index type is brep_edge or brep_vertex. 2 (type, index) The type and index of the brep component that contains the closest point. Possible types are brep_face, brep_edge or brep_vertex. 3 Vector3d The normal to the brep_face, or the tangent to the brep_edge. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a surface", rs.filter.surface)
if obj:
 point = rs.GetPoint("Pick a test point")
 if point:
 arrCP = rs.BrepClosestPoint(obj, point)
 if arrCP:
 rs.AddPoint(point)
 rs.AddPoint( arrCP[0] )
```

### See Also

EvaluateSurface, IsSurface, SurfaceClosestPoint

---

## CapPlanarHoles

### Signature

```python
CapPlanarHoles(surface_id)
```

### Description

Caps planar holes in a surface or polysurface

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
surface = rs.GetObject("Select surface or polysurface to cap", rs.filter.surface | rs.filter.polysurface)
if surface: rs.CapPlanarHoles( surface )
```

### See Also

ExtrudeCurve, ExtrudeCurvePoint, ExtrudeCurveStraight, ExtrudeSurface

---

## ChangeSurfaceDegree

### Signature

```python
ChangeSurfaceDegree(object_id, degree)
```

### Description

Changes the degree of a surface object. For more information see the Rhino help file for the ChangeDegree command.

### Returns

bool: True of False indicating success or failure. None: on failure.

### See Also

IsSurface

---

## DuplicateEdgeCurves

### Signature

```python
DuplicateEdgeCurves(object_id, select=False)
```

### Description

Duplicates the edge curves of a surface or polysurface. For more information, see the Rhino help file for information on the DupEdge command.

### Returns

list(guid, ..): identifying the newly created curve objects if successful. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select surface or polysurface", rs.filter.surface | rs.filter.polysurface)
if obj:
 rs.DuplicateEdgeCurves( obj, True )
 rs.DeleteObject( obj )
```

### See Also

IsPolysurface, IsSurface

---

## DuplicateSurfaceBorder

### Signature

```python
DuplicateSurfaceBorder(surface_id, type=0)
```

### Description

Create curves that duplicate a surface or polysurface border

### Returns

list(guid, ...): list of curve ids on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
surface = rs.GetObject("Select surface or polysurface", rs.filter.surface | rs.filter.polysurface)
if surface: rs.DuplicateSurfaceBorder( surface )
```

### See Also

DuplicateEdgeCurves, DuplicateMeshBorder

---

## EvaluateSurface

### Signature

```python
EvaluateSurface(surface_id, u, v)
```

### Description

Evaluates a surface at a U,V parameter

### Returns

point: a 3-D point if successful None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
objectId = rs.GetObject("Select a surface")
if rs.IsSurface(objectId):
 domainU = rs.SurfaceDomain(objectId, 0)
 domainV = rs.SurfaceDomain(objectId, 1)
 u = domainU[1]/2.0
 v = domainV[1]/2.0
 point = rs.EvaluateSurface(objectId, u, v)
 rs.AddPoint( point )
```

### See Also

IsSurface, SurfaceClosestPoint

---

## ExplodePolysurfaces

### Signature

```python
ExplodePolysurfaces(object_ids, delete_input=False)
```

### Description

Explodes, or unjoins, one or more polysurface objects. Polysurfaces will be exploded into separate surfaces

### Returns

list(guid, ...): of identifiers of exploded pieces on success

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select polysurface to explode", rs.filter.polysurface)
if rs.IsPolysurface(obj):
 rs.ExplodePolysurfaces( obj )
```

### See Also

IsPolysurface, IsSurface

---

## ExtendSurface

### Signature

```python
ExtendSurface(surface_id, parameter, length, smooth=True)
```

### Description

Lengthens an untrimmed surface object

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
pick = rs.GetObjectEx("Select surface to extend", rs.filter.surface)
if pick:
 parameter = rs.SurfaceClosestPoint(pick[0], pick[3])
 rs.ExtendSurface(pick[0], parameter, 5.0)
```

### See Also

IsSurface

---

## ExtractIsoCurve

### Signature

```python
ExtractIsoCurve(surface_id, parameter, direction)
```

### Description

Extracts isoparametric curves from a surface

### Returns

list(guid, ...): of curve ids on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select surface for isocurve extraction", rs.filter.surface)
point = rs.GetPointOnSurface(obj, "Select location for extraction")
parameter = rs.SurfaceClosestPoint(obj, point)
rs.ExtractIsoCurve( obj, parameter, 2 )
```

### See Also

IsSurface

---

## ExtractSurface

### Signature

```python
ExtractSurface(object_id, face_indices, copy=False)
```

### Description

Separates or copies a surface or a copy of a surface from a polysurface

### Returns

list(guid, ...): identifiers of extracted surface objects on success

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select polysurface", rs.filter.polysurface, True)
if obj: rs.ExtractSurface(obj, 0)
```

### See Also

BrepClosestPoint, IsSurface, IsPolysurface

---

## ExtrudeCurve

### Signature

```python
ExtrudeCurve(curve_id, path_id)
```

### Description

Creates a surface by extruding a curve along a path

### Returns

guid: identifier of new surface on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
curve = rs.AddCircle(rs.WorldXYPlane(), 5)
path = rs.AddLine([5,0,0], [10,0,10])
rs.ExtrudeCurve( curve, path )
```

### See Also

ExtrudeCurvePoint, ExtrudeCurveStraight, ExtrudeSurface

---

## ExtrudeCurvePoint

### Signature

```python
ExtrudeCurvePoint(curve_id, point)
```

### Description

Creates a surface by extruding a curve to a point

### Returns

guid: identifier of new surface on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
curve = rs.AddCircle(rs.WorldXYPlane(), 5)
point = (0,0,10)
rs.ExtrudeCurvePoint( curve, point )
```

### See Also

ExtrudeCurve, ExtrudeCurveStraight, ExtrudeSurface

---

## ExtrudeCurveStraight

** IN USE**

### Signature

```python
ExtrudeCurveStraight(curve_id, start_point, end_point)
```

### Description

Create surface by extruding a curve along two points that define a line

### Returns

guid: identifier of new surface on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
curve = rs.AddCircle(rs.WorldXYPlane(), 5)
rs.ExtrudeCurveStraight( curve, (0,0,0), (0, 10, 10) )
```

### See Also

ExtrudeCurve, ExtrudeCurvePoint, ExtrudeSurface

---

## ExtrudeSurface

### Signature

```python
ExtrudeSurface(surface, curve, cap=True)
```

### Description

Create surface by extruding along a path curve

### Returns

guid: identifier of new surface on success

### Example

```python
import rhinoscriptsyntax as rs
surface = rs.AddSrfPt([(0,0,0), (5,0,0), (5,5,0), (0,5,0)])
curve = rs.AddLine((5,0,0), (10,0,10))
rs.ExtrudeSurface(surface, curve)
```

### See Also

ExtrudeCurve, ExtrudeCurvePoint, ExtrudeCurveStraight

---

## FilletSurfaces

### Signature

```python
FilletSurfaces(surface0, surface1, radius, uvparam0=None, uvparam1=None)
```

### Description

Create constant radius rolling ball fillets between two surfaces. Note, this function does not trim the original surfaces of the fillets

### Returns

guid: ids of surfaces created on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
surface0 = rs.GetObject("First surface", rs.filter.surface)
surface1 = rs.GetObject("Second surface", rs.filter.surface)
rs.FilletSurfaces(surface0, surface1, 2.0)
```

### See Also

IsSurface

---

## FlipSurface

### Signature

```python
FlipSurface(surface_id, flip=None)
```

### Description

Returns or changes the normal direction of a surface. This feature can also be found in Rhino's Dir command

### Returns

vector: if flipped is not specified, the current normal orientation vector: if flipped is specified, the previous normal orientation None: on error

### Example

```python
import rhinoscriptsyntax as rs
surf = rs.GetObject("Select object", rs.filter.surface)
if surf:
 flip = rs.FlipSurface(surf)
 if flip: rs.FlipSurface(surf, False)
```

### See Also

IsSurface

---

## IntersectBreps

### Signature

```python
IntersectBreps(brep1, brep2, tolerance=None)
```

### Description

Intersects a brep object with another brep object. Note, unlike the SurfaceSurfaceIntersection function this function works on trimmed surfaces.

### Returns

list(guid, ...): identifying the newly created intersection curve and point objects if successful. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
brep1 = rs.GetObject("Select the first brep", rs.filter.surface | rs.filter.polysurface)
if brep1:
 brep2 = rs.GetObject("Select the second", rs.filter.surface | rs.filter.polysurface)
 if brep2: rs.IntersectBreps( brep1, brep2)
```

---

## IntersectSpheres

### Signature

```python
IntersectSpheres(sphere_plane0, sphere_radius0, sphere_plane1, sphere_radius1)
```

### Description

Calculates intersections of two spheres

### Returns

list(number, point, number): of intersection results [0] = type of intersection (0=point, 1=circle, 2=spheres are identical) [1] = Point of intersection or plane of circle intersection [2] = radius of circle if circle intersection None: on error

### Example

```python
import rhinoscriptsyntax as rs
plane0 = rs.WorldXYPlane()
plane1 = rs.MovePlane(plane0, (10,0,0))
radius = 10
results = rs.IntersectSpheres(plane0, radius, plane1, radius)
if results:
 if results[0] == 0: rs.AddPoint(results[1])
 else: rs.AddCircle( results[1], results[2])
```

### See Also

IntersectBreps, IntersectPlanes

---

## IsBrep

### Signature

```python
IsBrep(object_id)
```

### Description

Verifies an object is a Brep, or a boundary representation model, object.

### Returns

bool: True if successful, otherwise False. None: on error.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a Brep")
if rs.IsBrep(obj):
 print("The object is a Brep.")
else:
 print("The object is not a Brep.")
```

### See Also

IsPolysurface, IsPolysurfaceClosed, IsSurface

---

## IsCone

### Signature

```python
IsCone(object_id)
```

### Description

Determines if a surface is a portion of a cone

### Returns

bool: True if successful, otherwise False

### Example

```python
import rhinoscriptsyntax as rs
surface = rs.GetObject("Select a surface", rs.filter.surface)
if surface:
 if rs.IsCone(surface):
 print("The surface is a portion of a cone.")
 else:
 print("The surface is not a portion of a cone.")
```

### See Also

IsCylinder, IsSphere, IsSurface, IsTorus

---

## IsCylinder

### Signature

```python
IsCylinder(object_id)
```

### Description

Determines if a surface is a portion of a cone

### Returns

bool: True if successful, otherwise False

### Example

```python
import rhinoscriptsyntax as rs
surface = rs.GetObject("Select a surface", rs.filter.surface)
if surface:
 if rs.IsCylinder(surface):
 print("The surface is a portion of a cylinder.")
 else:
 print("The surface is not a portion of a cylinder.")
```

### See Also

IsCone, IsSphere, IsSurface, IsTorus

---

## IsPlaneSurface

### Signature

```python
IsPlaneSurface(object_id)
```

### Description

Verifies an object is a plane surface. Plane surfaces can be created by the Plane command. Note, a plane surface is not a planar NURBS surface

### Returns

bool: True if successful, otherwise False

### Example

```python
import rhinoscriptsyntax as rs
surface = rs.GetObject("Select surface to trim", rs.filter.surface)
if surface and rs.IsPlaneSurface(surface):
 print("got a plane surface")
else:
 print("not a plane surface")
```

### See Also

IsBrep, IsPolysurface, IsSurface

---

## IsPointInSurface

### Signature

```python
IsPointInSurface(object_id, point, strictly_in=False, tolerance=None)
```

### Description

Verifies that a point is inside a closed surface or polysurface

### Returns

bool: True if successful, otherwise False

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a polysurface", rs.filter.polysurface)
if rs.IsPolysurfaceClosed(obj):
 point = rs.GetPoint("Pick a test point")
 if point:
 if rs.IsPointInSurface(obj, point):
 print("The point is inside the polysurface.")
 else:
 print("The point is not inside the polysurface.")
```

### See Also

IsPointOnSurface

---

## IsPointOnSurface

### Signature

```python
IsPointOnSurface(object_id, point)
```

### Description

Verifies that a point lies on a surface

### Returns

bool: True if successful, otherwise False

### Example

```python
import rhinoscriptsyntax as rs
surf = rs.GetObject("Select a surface")
if rs.IsSurface(surf):
 point = rs.GetPoint("Pick a test point")
 if point:
 if rs.IsPointOnSurface(surf, point):
 print("The point is on the surface.")
 else:
 print("The point is not on the surface.")
```

### See Also

IsPointInSurface

---

## IsPolysurface

** IN USE**

### Signature

```python
IsPolysurface(object_id)
```

### Description

Verifies an object is a polysurface. Polysurfaces consist of two or more surfaces joined together. If the polysurface fully encloses a volume, it is considered a solid.

### Returns

bool: True is successful, otherwise False

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a polysurface")
if rs.IsPolysurface(obj):
 print("The object is a polysurface.")
else:
 print("The object is not a polysurface.")
```

### See Also

IsBrep, IsPolysurfaceClosed

---

## IsPolysurfaceClosed

### Signature

```python
IsPolysurfaceClosed(object_id)
```

### Description

Verifies a polysurface object is closed. If the polysurface fully encloses a volume, it is considered a solid.

### Returns

bool: True is successful, otherwise False

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a polysurface", rs.filter.polysurface)
if rs.IsPolysurfaceClosed(obj):
 print("The polysurface is closed.")
else:
 print("The polysurface is not closed.")
```

### See Also

IsBrep, IsPolysurface

---

## IsSphere

### Signature

```python
IsSphere(object_id)
```

### Description

Determines if a surface is a portion of a sphere

### Returns

bool: True if successful, otherwise False

### Example

```python
import rhinoscriptsyntax as rs
surface = rs.GetObject("Select a surface", rs.filter.surface)
if surface:
 if rs.IsSphere(surface):
 print("The surface is a portion of a sphere.")
 else:
 print("The surface is not a portion of a sphere.")
```

### See Also

IsCone, IsCylinder, IsSurface, IsTorus

---

## IsSurface

** IN USE**

### Signature

```python
IsSurface(object_id)
```

### Description

Verifies an object is a surface. Brep objects with only one face are also considered surfaces.

### Returns

bool: True if successful, otherwise False.

### Example

```python
import rhinoscriptsyntax as rs
objectId = rs.GetObject("Select a surface")
if rs.IsSurface(objectId):
 print("The object is a surface.")
else:
 print("The object is not a surface.")
```

### See Also

IsPointOnSurface, IsSurfaceClosed, IsSurfacePlanar, IsSurfaceSingular, IsSurfaceTrimmed

---

## IsSurfaceClosed

### Signature

```python
IsSurfaceClosed( surface_id, direction )
```

### Description

Verifies a surface object is closed in the specified direction. If the surface fully encloses a volume, it is considered a solid

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a surface", rs.filter.surface)
if rs.IsSurfaceClosed(obj, 0):
 print("The surface is closed in the U direction.")
else:
 print("The surface is not closed in the U direction.")
```

### See Also

IsSurface, IsSurfacePlanar, IsSurfaceSingular, IsSurfaceTrimmed

---

## IsSurfacePeriodic

### Signature

```python
IsSurfacePeriodic(surface_id, direction)
```

### Description

Verifies a surface object is periodic in the specified direction.

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a surface", rs.filter.surface)
if rs.IsSurfacePeriodic(obj, 0):
 print("The surface is periodic in the U direction.")
else:
 print("The surface is not periodic in the U direction.")
```

### See Also

IsSurface, IsSurfaceClosed, IsSurfacePlanar, IsSurfaceSingular, IsSurfaceTrimmed

---

## IsSurfacePlanar

### Signature

```python
IsSurfacePlanar(surface_id, tolerance=None)
```

### Description

Verifies a surface object is planar

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a surface", rs.filter.surface)
if rs.IsSurfacePlanar(obj):
 print("The surface is planar.")
else:
 print("The surface is not planar.")
```

### See Also

IsSurface, IsSurfaceClosed, IsSurfaceSingular, IsSurfaceTrimmed

---

## IsSurfaceRational

### Signature

```python
IsSurfaceRational(surface_id)
```

### Description

Verifies a surface object is rational

### Returns

bool: True if successful, otherwise False

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a surface", rs.filter.surface)
if rs.IsSurfaceRational(obj):
 print("The surface is rational.")
else:
 print("The surface is not rational.")
```

### See Also

IsSurface, IsSurfaceClosed, IsSurfacePlanar, IsSurfaceTrimmed

---

## IsSurfaceSingular

### Signature

```python
IsSurfaceSingular(surface_id, direction)
```

### Description

Verifies a surface object is singular in the specified direction. Surfaces are considered singular if a side collapses to a point.

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a surface", rs.filter.surface)
if rs.IsSurfaceSingular(obj, 0):
 print("The surface is singular.")
else:
 print("The surface is not singular.")
```

### See Also

IsSurface, IsSurfaceClosed, IsSurfacePlanar, IsSurfaceTrimmed

---

## IsSurfaceTrimmed

### Signature

```python
IsSurfaceTrimmed(surface_id)
```

### Description

Verifies a surface object has been trimmed

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a surface", rs.filter.surface)
if rs.IsSurfaceTrimmed(obj):
 print("The surface is trimmed.")
else:
 print("The surface is not trimmed.")
```

### See Also

IsSurface, IsSurfaceClosed, IsSurfacePlanar, IsSurfaceSingular

---

## IsTorus

### Signature

```python
IsTorus(surface_id)
```

### Description

Determines if a surface is a portion of a torus

### Returns

bool: True if successful, otherwise False

### Example

```python
import rhinoscriptsyntax as rs
surface = rs.GetObject("Select a surface", rs.filter.surface)
if surface:
 if rs.IsTorus(surface):
 print("The surface is a portion of a torus.")
 else:
 print("The surface is not a portion of a torus.")
```

### See Also

IsCone, IsCylinder, IsSphere, IsSurface

---

## JoinSurfaces

### Signature

```python
JoinSurfaces(object_ids, delete_input=False, return_all=False)
```

### Description

Joins two or more surface or polysurface objects together to form one polysurface object

### Returns

guid or guid list: identifier, or list of identifiers if return_all == True, of newly created object(s) on success None: on failure

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.GetObjects("Select surfaces in order", rs.filter.surface)
if objs and len(objs)>1: rs.JoinSurfaces(objs)
```

### See Also

ExplodePolysurfaces, IsPolysurface, IsPolysurfaceClosed, IsSurface, IsSurfaceClosed

---

## MakeSurfacePeriodic

### Signature

```python
MakeSurfacePeriodic(surface_id, direction, delete_input=False)
```

### Description

Makes an existing surface a periodic NURBS surface

### Returns

guid: if delete_input is False, identifier of the new surface guid: if delete_input is True, identifier of the modifier surface None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a surface", rs.filter.surface)
if not rs.IsSurfacePeriodic(obj, 0):
 rs.MakeSurfacePeriodic(obj, 0)
```

### See Also

IsSurfacePeriodic

---

## OffsetSurface

### Signature

```python
OffsetSurface(surface_id, distance, tolerance=None, both_sides=False, create_solid=False)
```

### Description

Offsets a trimmed or untrimmed surface by a distance. The offset surface will be added to Rhino.

### Returns

guid: identifier of the new object if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
surface = rs.GetObject("Select a surface", rs.filter.surface)
if rs.IsSurface(surface):
 rs.OffsetSurface( surface, 10.0 )
```

### See Also

OffsetCurve

---

## PullCurve

### Signature

```python
PullCurve(surface, curve, delete_input=False)
```

### Description

Pulls a curve object to a surface object

### Returns

list(guid, ...): of new curves if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
curve = rs.GetObject("Select curve to pull", rs.filter.curve )
surface = rs.GetObject("Select surface that pulls", rs.filter.surface )
rs.PullCurve(surface, curve)
```

### See Also

IsSurface

---

## RebuildSurface

### Signature

```python
RebuildSurface(object_id, degree=(3,3), pointcount=(10,10))
```

### Description

Rebuilds a surface to a given degree and control point count. For more information see the Rhino help file for the Rebuild command

### Returns

bool: True of False indicating success or failure

---

## RemoveSurfaceKnot

### Signature

```python
RemoveSurfaceKnot(surface, uv_parameter, v_direction)
```

### Description

Deletes a knot from a surface object.

### Returns

bool: True of False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs

srf_info = rs.GetSurfaceObject()
if srf_info:
 srf_id = srf_info[0]
 srf_param = srf_info[4]
 rs.RemoveSurfaceKnot(srf_id, srf_param, 1)
```

### See Also

RemoveSurfaceKnot

---

## ReverseSurface

### Signature

```python
ReverseSurface(surface_id, direction)
```

### Description

Reverses U or V directions of a surface, or swaps (transposes) U and V directions.

### Returns

bool: indicating success or failure None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a surface to reverse")
if rs.IsSurface(obj):
 rs.ReverseSurface( obj, 1 )
```

### See Also

FlipSurface, IsSurface

---

## ShootRay

### Signature

```python
ShootRay(surface_ids, start_point, direction, reflections=10)
```

### Description

Shoots a ray at a collection of surfaces

### Returns

list(point, ...): of reflection points on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
def TestRayShooter():
 corners = []
 corners.append((0,0,0))
 corners.append((10,0,0))
 corners.append((10,10,0))
 corners.append((0,10,0))
 corners.append((0,0,10))
 corners.append((10,0,10))
 corners.append((10,10,10))
 corners.append((0,10,10))
 box = rs.AddBox(corners)
 dir = 10,7.5,7
 reflections = rs.ShootRay(box, (0,0,0), dir)
 rs.AddPolyline( reflections )
 rs.AddPoints( reflections )
TestRayShooter()
```

### See Also

IsPolysurface, IsSurface

---

## ShortPath

### Signature

```python
ShortPath(surface_id, start_point, end_point)
```

### Description

Creates the shortest possible curve(geodesic) between two points on a surface. For more details, see the ShortPath command in Rhino help

### Returns

guid: identifier of the new surface on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
surface = rs.GetObject("Select surface for short path", rs.filter.surface + rs.filter.surface)
if surface:
 start = rs.GetPointOnSurface(surface, "First point")
 end = rs.GetPointOnSurface(surface, "Second point")
 rs.ShortPath(surface, start, end)
```

### See Also

EvaluateSurface, SurfaceClosestPoint

---

## ShrinkTrimmedSurface

### Signature

```python
ShrinkTrimmedSurface(object_id, create_copy=False)
```

### Description

Shrinks the underlying untrimmed surfaces near to the trimming boundaries. See the ShrinkTrimmedSrf command in the Rhino help.

### Returns

bool: If create_copy is False, True or False indicating success or failure bool: If create_copy is True, the identifier of the new surface None: on error

### Example

```python
import rhinoscriptsyntax as rs
filter = rs.filter.surface | rs.filter.polysurface
surface = rs.GetObject("Select surface or polysurface to shrink", filter )
if surface: rs.ShrinkTrimmedSurface( surface )
```

### See Also

IsSurfaceTrimmed

---

## SplitBrep

### Signature

```python
SplitBrep(brep_id, cutter_id, delete_input=False)
```

### Description

Splits a brep

### Returns

list(guid, ...): identifiers of split pieces on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
filter = rs.filter.surface + rs.filter.polysurface
brep = rs.GetObject("Select brep to split", filter)
cutter = rs.GetObject("Select cutting brep", filter)
rs.SplitBrep ( brep, cutter )
```

### See Also

IsBrep

---

## SurfaceArea

** IN USE**

### Signature

```python
SurfaceArea(object_id)
```

### Description

Calculate the area of a surface or polysurface object. The results are based on the current drawing units

### Returns

list(number, number): of area information on success (area, absolute error bound) None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a surface", rs.filter.surface)
if obj:
 massprop = rs.SurfaceArea( obj )
 if massprop:
 print("The surface area is: {}".format(massprop[0]))
```

### See Also

SurfaceAreaCentroid, SurfaceAreaMoments

---

## SurfaceAreaCentroid

### Signature

```python
SurfaceAreaCentroid(object_id)
```

### Description

Calculates the area centroid of a surface or polysurface

### Returns

list(point, tuple(number, number, number)): Area centroid information (Area Centroid, Error bound in X, Y, Z) None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a surface", rs.filter.surface)
if obj:
 massprop = rs.SurfaceAreaCentroid(obj)
 if massprop: rs.AddPoint( massprop[0] )
```

### See Also

SurfaceArea, SurfaceAreaMoments

---

## SurfaceAreaMoments

### Signature

```python
SurfaceAreaMoments(surface_id)
```

### Description

Calculates area moments of inertia of a surface or polysurface object. See the Rhino help for "Mass Properties calculation details"

### Returns

list(tuple(number, number,number), ...): of moments and error bounds in tuple(X, Y, Z) - see help topic Index Description [0] First Moments. [1] The absolute (+/-) error bound for the First Moments. [2] Second Moments. [3] The absolute (+/-) error bound for the Second Moments. [4] Product Moments. [5] The absolute (+/-) error bound for the Product Moments. [6] Area Moments of Inertia about the World Coordinate Axes. [7] The absolute (+/-) error bound for the Area Moments of Inertia about World Coordinate Axes. [8] Area Radii of Gyration about the World Coordinate Axes. [9] The absolute (+/-) error bound for the Area Radii of Gyration about World Coordinate Axes. [10] Area Moments of Inertia about the Centroid Coordinate Axes. [11] The absolute (+/-) error bound for the Area Moments of Inertia about the Centroid Coordinate Axes. [12] Area Radii of Gyration about the Centroid Coordinate Axes. [13] The absolute (+/-) error bound for the Area Radii of Gyration about the Centroid Coordinate Axes. None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a surface", rs.filter.surface)
if obj:
 massprop= rs.SurfaceAreaMoments(obj)
 if massprop:
 print("Area Moments of Inertia about the World Coordinate Axes: {}".format(massprop[6]))
```

### See Also

SurfaceArea, SurfaceAreaCentroid

---

## SurfaceClosestPoint

### Signature

```python
SurfaceClosestPoint(surface_id, test_point)
```

### Description

Returns U,V parameters of point on a surface that is closest to a test point

### Returns

list(number, number): The U,V parameters of the closest point on the surface if successful. None: on error.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a surface", rs.filter.surface)
if rs.IsSurface(obj):
 point = rs.GetPointOnSurface(obj, "Pick a test point")
 if point:
 param = rs.SurfaceClosestPoint(obj, point)
 if param:
 print("Surface U parameter: {}".format(str(param[0])))
 print("Surface V parameter: {}".format(str(param[1])))
```

### See Also

BrepClosestPoint, EvaluateSurface, IsSurface

---

## SurfaceCone

### Signature

```python
SurfaceCone(surface_id)
```

### Description

Returns the definition of a surface cone

### Returns

tuple(plane, number, number): containing the definition of the cone if successful [0] the plane of the cone. The apex of the cone is at the plane's origin and the axis of the cone is the plane's z-axis [1] the height of the cone [2] the radius of the cone None: on error

### Example

```python
import rhinoscriptsyntax as rs
cone = rs.AddCone(rs.WorldXYPlane(), 6, 2, False)
if rs.IsCone(cone):
 cone_def = rs.SurfaceCone(cone)
 rs.AddCone( cone_def[0], cone_def[1], cone_def[2], False )
```

---

## SurfaceCurvature

### Signature

```python
SurfaceCurvature(surface_id, parameter)
```

### Description

Returns the curvature of a surface at a U,V parameter. See Rhino help for details of surface curvature

### Returns

tuple(point, vector, number, number, number, number, number): of curvature information [0] point at specified U,V parameter [1] normal direction [2] maximum principal curvature [3] maximum principal curvature direction [4] minimum principal curvature [5] minimum principal curvature direction [6] gaussian curvature [7] mean curvature None: if not successful, or on error

### Example

```python
import rhinoscriptsyntax as rs
srf = rs.GetObject("Select a surface", rs.filter.surface)
if rs.IsSurface(srf):
 point = rs.GetPointOnSurface(srf, "Pick a test point")
 if point:
 param = rs.SurfaceClosestPoint(srf, point)
 if param:
 data = rs.SurfaceCurvature(srf, param)
 if data:
 print("Surface curvature evaluation at parameter {}:".format(param))
 print(" 3-D Point:{}".format(data[0]))
 print(" 3-D Normal:{}".format(data[1]))
 print(" Maximum principal curvature: {} {}".format(data[2], data[3]))
 print(" Minimum principal curvature: {} {}".format(data[4], data[5]))
 print(" Gaussian curvature:{}".format(data[6]))
 print(" Mean curvature:{}".format(data[7]))
```

### See Also

CurveCurvature

---

## SurfaceCylinder

### Signature

```python
SurfaceCylinder(surface_id)
```

### Description

Returns the definition of a cylinder surface

### Returns

tuple(plane, number, number): of the cylinder plane, height, radius on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
cylinder = rs.AddCylinder(rs.WorldXYPlane(), 6, 2, False)
if rs.IsCylinder(cylinder):
 plane, height, radius = rs.SurfaceCylinder(cylinder)
 rs.AddCylinder(plane, height, radius, False)
```

### See Also

SurfaceSphere

---

## SurfaceDegree

### Signature

```python
SurfaceDegree(surface_id, direction=2)
```

### Description

Returns the degree of a surface object in the specified direction

### Returns

number: Single number if `direction` = 0 or 1 tuple(number, number): of two values if `direction` = 2 None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a surface", rs.filter.surface)
if rs.IsSurface(obj):
 print("Degree in U direction: {}".format(rs.SurfaceDegree(obj, 0)))
 print("Degree in V direction: {}".format(rs.SurfaceDegree(obj, 1)))
```

### See Also

IsSurface, SurfaceDomain

---

## SurfaceDomain

### Signature

```python
SurfaceDomain(surface_id, direction)
```

### Description

Returns the domain of a surface object in the specified direction.

### Returns

list(number, number): containing the domain interval in the specified direction None: if not successful, or on error

### Example

```python
import rhinoscriptsyntax as rs
object = rs.GetObject("Select a surface", rs.filter.surface)
if rs.IsSurface(object):
 domainU = rs.SurfaceDomain(object, 0)
 domainV = rs.SurfaceDomain(object, 1)
 print("Domain in U direction: {}".format(domainU))
 print("Domain in V direction: {}".format(domainV))
```

### See Also

IsSurface, SurfaceDegree

---

## SurfaceEditPoints

### Signature

```python
SurfaceEditPoints(surface_id, return_parameters=False, return_all=True)
```

### Description

Returns the edit, or Greville points of a surface object. For each surface control point, there is a corresponding edit point

### Returns

list(point, ...): if return_parameters is False, a list of 3D points list((number, number), ...): if return_parameters is True, a list of U,V parameters None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a surface")
if rs.IsSurface(obj):
 points = rs.SurfaceEditPoints(obj)
 if points: rs.AddPointCloud(points)
```

### See Also

IsSurface, SurfacePointCount, SurfacePoints

---

## SurfaceEvaluate

### Signature

```python
SurfaceEvaluate(surface_id, parameter, derivative)
```

### Description

A general purpose surface evaluator

### Returns

list((point, vector, ...), ...): list length (derivative+1)*(derivative+2)/2 if successful. The elements are as follows: Element Description [0] The 3-D point. [1] The first derivative. [2] The first derivative. [3] The second derivative. [4] The second derivative. [5] The second derivative. [6] etc... None: If not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
def TestSurfaceEvaluate():
 srf = rs.GetObject("Select surface to evaluate", rs.filter.surface, True)
 if srf is None: return
 point = rs.GetPointOnSurface(srf, "Point to evaluate")
 if point is None: return
 der = rs.GetInteger("Number of derivatives to evaluate", 1, 1)
 if der is None: return
 uv = rs.SurfaceClosestPoint(srf, point)
 res = rs.SurfaceEvaluate(srf, uv, der)
 if res is None:
 print("Failed to evaluate surface.")
 return
 for i,r in enumerate(res):
 print("{} = {}".format(i, r))
TestSurfaceEvaluate()
```

### See Also

EvaluateSurface

---

## SurfaceFrame

### Signature

```python
SurfaceFrame(surface_id, uv_parameter)
```

### Description

Returns a plane based on the normal, u, and v directions at a surface U,V parameter

### Returns

plane: plane on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
surface = rs.GetSurfaceObject("Select a surface")
if surface:
 plane = rs.SurfaceFrame(surface[0], surface[4])
 rs.ViewCPlane(None, plane)
```

### See Also

EvaluateSurface, SurfaceClosestPoint, SurfaceNormal

---

## SurfaceIsocurveDensity

### Signature

```python
SurfaceIsocurveDensity(surface_id, density=None)
```

### Description

Returns or sets the isocurve density of a surface or polysurface object. An isoparametric curve is a curve of constant U or V value on a surface. Rhino uses isocurves and surface edge curves to visualize the shape of a NURBS surface

### Returns

number: If density is not specified, then the current isocurve density if successful number: If density is specified, the the previous isocurve density if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a surface", rs.filter.surface | rs.filter.polysurface)
if obj: rs.SurfaceIsocurveDensity( obj, 8 )
```

### See Also

IsPolysurface, IsSurface

---

## SurfaceKnotCount

### Signature

```python
SurfaceKnotCount(surface_id)
```

### Description

Returns the control point count of a surface surface_id = the surface's identifier

### Returns

list(number, number): a list containing (U count, V count) on success

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a surface")
if rs.IsSurface(obj):
 count = rs.SurfaceKnotCount(obj)
 print("Knot count in U direction: {}".format(count[0]))
 print("Knot count in V direction: {}".format(count[1]))
```

### See Also

IsSurface, SurfaceKnots

---

## SurfaceKnots

### Signature

```python
SurfaceKnots(surface_id)
```

### Description

Returns the knots, or knot vector, of a surface object.

### Returns

list(number, number): knot values of the surface if successful. The list will contain the following information: Element Description [0] Knot vector in U direction [1] Knot vector in V direction None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a surface")
if rs.IsSurface(obj):
 knots = rs.SurfaceKnots(obj)
 if knots:
 vector = knots[0]
 print("Knot vector in U direction")
 for item in vector: print("Surface knot value: {}".format(item))
 vector = knots[1]
 print("Knot vector in V direction")
 for item in vector: print("Surface knot value: {}".format(item))
```

### See Also

IsSurface, SurfaceKnotCount

---

## SurfaceNormal

### Signature

```python
SurfaceNormal(surface_id, uv_parameter)
```

### Description

Returns 3D vector that is the normal to a surface at a parameter

### Returns

vector: Normal vector on success

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a surface", rs.filter.surface)
if obj:
 point = rs.GetPointOnSurface(obj)
 if point:
 param = rs.SurfaceClosestPoint(obj, point)
 normal = rs.SurfaceNormal(obj, param)
 rs.AddPoints( [point, point + normal] )
```

### See Also

SurfaceClosestPoint, SurfaceDomain

---

## SurfaceNormalizedParameter

### Signature

```python
SurfaceNormalizedParameter(surface_id, parameter)
```

### Description

Converts surface parameter to a normalized surface parameter; one that ranges between 0.0 and 1.0 in both the U and V directions

### Returns

list(number, number): normalized surface parameter if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select surface")
if rs.IsSurface(obj):
 domain_u = rs.SurfaceDomain(obj, 0)
 domain_v = rs.SurfaceDomain(obj, 1)
 parameter = (domain_u[1] + domain_u[0]) / 2.0, (domain_v[1] + domain_v[0]) / 2.0
 print("Surface parameter: {}".format(parameter))
 normalized = rs.SurfaceNormalizedParameter(obj, parameter)
 print("Normalized parameter: {}".format(normalized))
```

### See Also

SurfaceDomain, SurfaceParameter

---

## SurfaceParameter

### Signature

```python
SurfaceParameter(surface_id, parameter)
```

### Description

Converts normalized surface parameter to a surface parameter; or within the surface's domain

### Returns

tuple(number, number): surface parameter on success

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select surface")
if obj:
 normalized = (0.5, 0.5)
 print("Normalized parameter: {}".format(normalized))
 parameter = rs.SurfaceParameter(obj, normalized)
 print("Surface parameter: {}".format(parameter))
```

### See Also

SurfaceDomain, SurfaceNormalizedParameter

---

## SurfacePointCount

### Signature

```python
SurfacePointCount(surface_id)
```

### Description

Returns the control point count of a surface surface_id = the surface's identifier

### Returns

list(number, number): THe number of control points in UV direction. (U count, V count)

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a surface")
if rs.IsSurface(obj):
 count = rs.SurfacePointCount(obj)
 print("Point count in U direction: {}".format(count[0]))
 print("Point count in V direction: {}".format(count[1]))
```

### See Also

IsSurface, SurfacePoints

---

## SurfacePoints

### Signature

```python
SurfacePoints(surface_id, return_all=True)
```

### Description

Returns the control points, or control vertices, of a surface object

### Returns

list(point, ...): the control points if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
def PrintControlPoints():
 surface = rs.GetObject("Select surface", rs.filter.surface)
 points = rs.SurfacePoints(surface)
 if points is None: return
 count = rs.SurfacePointCount(surface)
 i = 0
 for u in range(count[0]):
 for v in range(count[1]):
 print("CV[{}".format(u, ",", v, "] = ", points[i]))
 i += 1
PrintControlPoints()
```

### See Also

IsSurface, SurfacePointCount

---

## SurfaceSphere

### Signature

```python
SurfaceSphere(surface_id)
```

### Description

Gets the sphere definition from a surface, if possible.

### Returns

(plane, number): The equatorial plane of the sphere, and its radius. None: on error

### Example

```python
import rhinoscriptsyntax as rs
surface = rs.GetObject("Select a surface", rs.filter.surface)
if surface:
 result = rs.SurfaceSphere(surface)
 if result:
 print("The sphere radius is: " + str(result[1]))
```

### See Also

SurfaceCylinder

---

## SurfaceTorus

### Signature

```python
SurfaceTorus(surface_id)
```

### Description

Returns the definition of a surface torus

### Returns

tuple(plane, number, number): containing the definition of the torus if successful [0] the base plane of the torus [1] the major radius of the torus [2] the minor radius of the torus None: on error

### Example

```python
import rhinoscriptsyntax as rs
torus = rs.AddTorus(rs.WorldXYPlane(), 6, 2)
if rs.IsTorus(torus):
 torus_def = rs.SurfaceTorus(torus)
 rs.AddTorus( torus_def[0], torus_def[1], torus_def[2] )
```

---

## SurfaceVolume

** IN USE**

### Signature

```python
SurfaceVolume(object_id)
```

### Description

Calculates volume of a closed surface or polysurface

### Returns

list(number, tuple(X, Y, Z): volume data returned (Volume, Error bound) on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a surface", rs.filter.polysurface)
if rs.IsPolysurfaceClosed(obj):
 massprop = rs.SurfaceVolume(obj)
 if massprop:
 print("The polysurface volume is: {}".format(massprop[0]))
```

### See Also

SurfaceVolume, SurfaceVolumeCentroid, SurfaceVolumeMoments

---

## SurfaceVolumeCentroid

### Signature

```python
SurfaceVolumeCentroid(object_id)
```

### Description

Calculates volume centroid of a closed surface or polysurface

### Returns

list(point, tuple(X, Y, Z): volume data returned (Volume Centriod, Error bound) on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a surface", rs.filter.polysurface)
if rs.IsPolysurfaceClosed(obj):
 massprop= rs.SurfaceVolumeCentroid(obj)
 if massprop: rs.AddPoint( massprop[0] )
```

### See Also

SurfaceVolume, SurfaceVolumeMoments

---

## SurfaceVolumeMoments

### Signature

```python
SurfaceVolumeMoments(surface_id)
```

### Description

Calculates volume moments of inertia of a surface or polysurface object. For more information, see Rhino help for "Mass Properties calculation details"

### Returns

list(tuple(number, number,number), ...): of moments and error bounds in tuple(X, Y, Z) - see help topic Index Description [0] First Moments. [1] The absolute (+/-) error bound for the First Moments. [2] Second Moments. [3] The absolute (+/-) error bound for the Second Moments. [4] Product Moments. [5] The absolute (+/-) error bound for the Product Moments. [6] Area Moments of Inertia about the World Coordinate Axes. [7] The absolute (+/-) error bound for the Area Moments of Inertia about World Coordinate Axes. [8] Area Radii of Gyration about the World Coordinate Axes. [9] The absolute (+/-) error bound for the Area Radii of Gyration about World Coordinate Axes. [10] Area Moments of Inertia about the Centroid Coordinate Axes. [11] The absolute (+/-) error bound for the Area Moments of Inertia about the Centroid Coordinate Axes. [12] Area Radii of Gyration about the Centroid Coordinate Axes. [13] The absolute (+/-) error bound for the Area Radii of Gyration about the Centroid Coordinate Axes. None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select a surface", rs.filter.polysurface)
if rs.IsPolysurfaceClosed(obj):
 massprop = rs.SurfaceVolumeMoments(obj)
 if massprop:
 print("Volume Moments of Inertia about the World Coordinate Axes: {}".format(massprop[6]))
```

### See Also

SurfaceVolume, SurfaceVolumeCentroid

---

## SurfaceWeights

### Signature

```python
SurfaceWeights(object_id)
```

### Description

Returns list of weight values assigned to the control points of a surface. The number of weights returned will be equal to the number of control points in the U and V directions.

### Returns

list(number, ...): point weights. None: on error

### Example

```python
import rhinoscriptsyntax as rs
surf = rs.GetObject("Select a surface")
if rs.IsSurface(surf):
 weights = rs.SurfaceWeights(surf)
 if weights:
 for w in weights:
 print("Surface control point weight value:{}".format(w))
```

### See Also

IsSurface, SurfacePointCount, SurfacePoints

---

## TrimBrep

### Signature

```python
TrimBrep(object_id, cutter, tolerance=None)
```

### Description

Trims a surface using an oriented cutter

### Returns

list(guid, ...): identifiers of retained components on success

### Example

```python
import rhinoscriptsyntax as rs
filter = rs.filter.surface + rs.filter.polysurface
obj = rs.GetObject("Select surface or polysurface to trim", filter)
if obj:
 cutter = rs.GetObject("Select cutting surface or polysurface", filter)
 if cutter:
 rs.TrimBrep(obj,cutter)
```

### See Also

TrimSurface

---

## TrimSurface

### Signature

```python
TrimSurface( surface_id, direction, interval, delete_input=False)
```

### Description

Remove portions of the surface outside of the specified interval

### Returns

guid: new surface identifier on success

### Example

```python
import rhinoscriptsyntax as rs
surface = rs.GetObject("Select surface to split", rs.filter.surface)
if surface:
 domain_u = rs.SurfaceDomain(surface, 0)
 domain_u[0] = (domain_u[1] - domain_u[0]) * 0.25
 rs.TrimSurface( surface, 0, domain_u, True )
```

---

## UnrollSurface

### Signature

```python
UnrollSurface(surface_id, explode=False, following_geometry=None, absolute_tolerance=None, relative_tolerance=None)
```

### Description

Flattens a developable surface or polysurface

### Returns

list(guid, ...): of unrolled surface ids tuple((guid, ...),(guid, ...)): if following_geometry is not None, a tuple [1] is the list of unrolled surface ids [2] is the list of unrolled following geometry

### Example

```python
import rhinoscriptsyntax as rs
surface = rs.GetObject("Select surface or polysurface to unroll", rs.filter.surface + rs.filter.polysurface)
if surface: rs.UnrollSurface(surface)
```

---

# Toolbar

*15 functions | 0 in use*

---

## CloseToolbarCollection

### Signature

```python
CloseToolbarCollection(name, prompt=False)
```

### Description

Closes a currently open toolbar collection

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
names = rs.ToolbarCollectionNames()
if names:
 for name in names: rs.CloseToolbarCollection( name, True )
```

### See Also

IsToolbarCollection, OpenToolbarCollection, ToolbarCollectionCount, ToolbarCollectionNames, ToolbarCollectionPath

---

## HideToolbar

### Signature

```python
HideToolbar(name, toolbar_group)
```

### Description

Hides a previously visible toolbar group in an open toolbar collection

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
file = "C:\\SteveBaer\\AppData\\Roaming\\McNeel\\Rhinoceros\\5.0\\UI\\default.rui"
name = rs.IsToolbarCollection(file)
if names: rs.HideToolbar(name, "Layer")
```

### See Also

IsToolbar, IsToolbarVisible, ShowToolbar, ToolbarCount, ToolbarNames

---

## IsToolbar

### Signature

```python
IsToolbar(name, toolbar, group=False)
```

### Description

Verifies a toolbar (or toolbar group) exists in an open collection file

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
file = "C:\\SteveBaer\\AppData\\Roaming\\McNeel\\Rhinoceros\\5.0\\UI\\default.rui"
name = rs.IsToolbarCollection(file)
if name:
 if rs.IsToolbar(name, "Layer"):
 print("The collection contains the Layer toolbar.")
 else:
 print("The collection does not contain the Layer toolbar.")
```

### See Also

HideToolbar, IsToolbarVisible, ShowToolbar, ToolbarCount, ToolbarNames

---

## IsToolbarCollection

### Signature

```python
IsToolbarCollection(file)
```

### Description

Verifies that a toolbar collection is open

### Returns

str: Rhino-assigned name of the toolbar collection if successful None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
file = "C:\\SteveBaer\\AppData\\Roaming\\McNeel\\Rhinoceros\\5.0\\UI\\default.rui"
name = rs.IsToolbarCollection(file)
if name: print("The default toolbar collection is loaded.")
else: print("The default toolbar collection is not loaded.")
```

### See Also

CloseToolbarCollection, OpenToolbarCollection, ToolbarCollectionCount, ToolbarCollectionNames, ToolbarCollectionPath

---

## IsToolbarDocked

### Signature

```python
IsToolbarDocked(name, toolbar_group)
```

### Description

Verifies that a toolbar group in an open toolbar collection is visible

### Returns

boolean: True or False indicating success or failure None: on error

### Example

```python
import rhinoscriptsyntax as rs
rc = rs.IsToolbarDocked("Default", "Main1")
if rc==True:
 print("The Main1 toolbar is docked.")
elif rc==False:
 print("The Main1 toolbar is not docked.")
else:
 print("The Main1 toolbar is not visible.")
```

### See Also

IsToolbar, IsToolbarVisible

---

## IsToolbarVisible

### Signature

```python
IsToolbarVisible(name, toolbar_group)
```

### Description

Verifies that a toolbar group in an open toolbar collection is visible

### Returns

bool:True or False indicating success or failure None: on error

### Example

```python
import rhinoscriptsyntax as rs
file = "C:\\SteveBaer\\AppData\\Roaming\\McNeel\\Rhinoceros\\5.0\\UI\\default.rui"
name = rs.IsToolbarCollection(file)
if name:
 if rs.IsToolbarVisible(name, "Layer"): print("The Layer toolbar is visible.")
 else: print("The Layer toolbar is not visible.")
```

### See Also

HideToolbar, IsToolbar, ShowToolbar, ToolbarCount, ToolbarNames

---

## OpenToolbarCollection

### Signature

```python
OpenToolbarCollection(file)
```

### Description

Opens a toolbar collection file

### Returns

str: Rhino-assigned name of the toolbar collection if successful None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
file = "C:\\SteveBaer\\AppData\\Roaming\\McNeel\\Rhinoceros\\5.0\\UI\\default.rui"
name = rs.IsToolbarCollection(file)
if name is None: rs.OpenToolbarCollection(file)
```

### See Also

CloseToolbarCollection, IsToolbarCollection, ToolbarCollectionCount, ToolbarCollectionNames, ToolbarCollectionPath

---

## SaveToolbarCollection

### Signature

```python
SaveToolbarCollection(name)
```

### Description

Saves an open toolbar collection to disk

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
name = "Default"
rs.SaveToolbarCollection(name)
```

### See Also

SaveToolbarCollectionAs

---

## SaveToolbarCollectionAs

### Signature

```python
SaveToolbarCollectionAs(name, file)
```

### Description

Saves an open toolbar collection to a different disk file

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
name = "Default"
file = "D:\\NewDefault.rui"
rs.SaveToolbarCollectionAs(name,file)
```

### See Also

SaveToolbarCollection

---

## ShowToolbar

### Signature

```python
ShowToolbar(name, toolbar_group)
```

### Description

Shows a previously hidden toolbar group in an open toolbar collection

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
file = "C:\\SteveBaer\\AppData\\Roaming\\McNeel\\Rhinoceros\\5.0\\UI\\default.rui"
name = rs.IsToolbarCollection(file)
if name: rs.ShowToolbar(name, "Layer")
```

### See Also

HideToolbar, IsToolbar, IsToolbarVisible, ToolbarCount, ToolbarNames

---

## ToolbarCollectionCount

### Signature

```python
ToolbarCollectionCount()
```

### Description

Returns number of currently open toolbar collections

### Returns

number: the number of currently open toolbar collections

### Example

```python
import rhinoscriptsyntax as rs
count = rs.ToolbarCollectionCount()
print("There are {} toolbar(s) collections loaded".format(count))
```

### See Also

CloseToolbarCollection, IsToolbarCollection, OpenToolbarCollection, ToolbarCollectionNames, ToolbarCollectionPath

---

## ToolbarCollectionNames

### Signature

```python
ToolbarCollectionNames()
```

### Description

Returns names of all currently open toolbar collections

### Returns

list(str, ...): the names of all currently open toolbar collections

### Example

```python
import rhinoscriptsyntax as rs
names = rs.ToolbarCollectionNames()
if names:
 for name in names: print(name)
```

### See Also

CloseToolbarCollection, IsToolbarCollection, OpenToolbarCollection, ToolbarCollectionCount, ToolbarCollectionPath

---

## ToolbarCollectionPath

### Signature

```python
ToolbarCollectionPath(name)
```

### Description

Returns full path to a currently open toolbar collection file

### Returns

str: full path on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
names = rs.ToolbarCollectionNames()
if names:
 for name in names: print(rs.ToolbarCollectionPath(name))
```

### See Also

CloseToolbarCollection, IsToolbarCollection, OpenToolbarCollection, ToolbarCollectionCount, ToolbarCollectionNames

---

## ToolbarCount

### Signature

```python
ToolbarCount(name, groups=False)
```

### Description

Returns the number of toolbars or groups in a currently open toolbar file

### Returns

number: number of toolbars on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
names = rs.ToolbarCollectionNames()
if names:
 count = rs.ToolbarCount(names[0])
 print("The {} collection contains {} toolbars.".format(names[0], count))
```

### See Also

HideToolbar, IsToolbar, IsToolbarVisible, ShowToolbar, ToolbarNames

---

## ToolbarNames

### Signature

```python
ToolbarNames(name, groups=False)
```

### Description

Returns the names of all toolbars (or toolbar groups) found in a currently open toolbar file

### Returns

list(str, ...): names of all toolbars (or toolbar groups) on success None: on error

### Example

```python
import rhinoscriptsytax as rs
names = rs.ToolbarCollectionNames()
if names:
 toolbars = rs.ToolbarNames(names[0])
 if toolbars:
 for toolbar in toolbars: print(toolbar)
```

### See Also

HideToolbar, IsToolbar, IsToolbarVisible, ShowToolbar, ToolbarCount

---

# Transformation

*25 functions | 0 in use*

---

## IsXformIdentity

### Signature

```python
IsXformIdentity(xform)
```

### Description

Verifies a matrix is the identity matrix

### Returns

bool: True or False indicating success or failure.

### Example

```python
import rhinoscriptsyntax as rs
xform = rs.XformIdentity()
print(rs.IsXformIdentity(xform))
```

### See Also

IsXformSimilarity, IsXformZero, XformIdentity

---

## IsXformSimilarity

### Signature

```python
IsXformSimilarity(xform)
```

### Description

Verifies a matrix is a similarity transformation. A similarity transformation can be broken into a sequence of dialations, translations, rotations, and reflections

### Returns

bool: True if this transformation is an orientation preserving similarity, otherwise False.

### Example

```python
import rhinoscriptsyntax as rs
xform = rs.BlockInstanceXform(block)
print(rs.IsXformSimilarity(xform))
```

### See Also

IsXformIdentity, IsXformZero

---

## IsXformZero

### Signature

```python
IsXformZero(xform)
```

### Description

verifies that a matrix is a zero transformation matrix

### Returns

bool: True or False indicating success or failure.

### Example

```python
import rhinoscriptsyntax as rs
xform = rs.XformZero()
print(rs.IsXformZero(xform))
```

### See Also

IsXformIdentity, IsXformSimilarity, XformZero

---

## XformCPlaneToWorld

### Signature

```python
XformCPlaneToWorld(point, plane)
```

### Description

Transform point from construction plane coordinates to world coordinates

### Returns

point: A 3D point in world coordinates

### Example

```python
import rhinoscriptsyntax as rs
plane = rs.ViewCPlane()
point = rs.XFormCPlaneToWorld([0,0,0], plane)
if point: print("World point: {}".format(point))
```

### See Also

XformWorldToCPlane

---

## XformChangeBasis

### Signature

```python
XformChangeBasis(initial_plane, final_plane)
```

### Description

Returns a change of basis transformation matrix or None on error

### Returns

transform: The 4x4 transformation matrix if successful None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
import math
objs = rs.GetObjects("Select objects to shear")
if objs:
 cplane = rs.ViewCPlane()
 cob = rs.XformChangeBasis(rs.WorldXYPlane(), cplane)
 shear2d = rs.XformIdentity()
 shear2d[0,2] = math.tan(math.radians(45.0))
 cob_inverse = rs.XformChangeBasis(cplane, rs.WorldXYPlane())
 temp = rs.XformMultiply(shear2d, cob)
 xform = rs.XformMultiply(cob_inverse, temp)
 rs.TransformObjects( objs, xform, True )
```

### See Also

XformCPlaneToWorld, XformWorldToCPlane

---

## XformChangeBasis2

### Signature

```python
XformChangeBasis2(x0,y0,z0,x1,y1,z1)
```

### Description

Returns a change of basis transformation matrix of None on error

### Returns

transform: The 4x4 transformation matrix if successful None: if not successful

---

## XformCompare

### Signature

```python
XformCompare(xform1, xform2)
```

### Description

Compares two transformation matrices

### Returns

number: -1 if xform1<xform2 1 if xform1>xform2 0 if xform1=xform2

### Example

```python
import rhinoscriptsyntax as rs
xform0 = rs.XformZero()
xform1 = rs.XformIdentity()
print(rs.XformCompare(xform0, xform1))
```

### See Also

IsXformIdentity, IsXformSimilarity, IsXformZero

---

## XformDeterminant

### Signature

```python
XformDeterminant(xform)
```

### Description

Returns the determinant of a transformation matrix. If the determinant of a transformation matrix is 0, the matrix is said to be singular. Singular matrices do not have inverses.

### Returns

number: The determinant if successful None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
xform = rs.BlockInstanceXform(obj)
if xform: print(rs.XformDeterminant(xform))
```

### See Also

XformInverse

---

## XformDiagonal

### Signature

```python
XformDiagonal(diagonal_value)
```

### Description

Returns a diagonal transformation matrix. Diagonal matrices are 3x3 with the bottom row [0,0,0,1]

### Returns

transform: The 4x4 transformation matrix if successful None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
def printmatrix(xform):
 for i in range(4):
 print("[{}, {}, {}, {}]".format(xform[i,0], xform[i,1], xform[i,2], xform[i,3]))
printmatrix(rs.XformDiagonal(3))
```

### See Also

XformIdentity, XformZero

---

## XformIdentity

### Signature

```python
XformIdentity()
```

### Description

returns the identity transformation matrix

### Returns

transform: The 4x4 transformation matrix

### Example

```python
import rhinoscriptsyntax as rs
def printmatrix(xform):
 for i in range(4):
 print("[{}, {}, {}, {}]".format(xform[i,0], xform[i,1], xform[i,2], xform[i,3]))
printmatrix(rs.XformIdentity())
```

### See Also

XformDiagonal, XformZero

---

## XformInverse

### Signature

```python
XformInverse(xform)
```

### Description

Returns the inverse of a non-singular transformation matrix

### Returns

transform: The inverted 4x4 transformation matrix if successful. None: if matrix is non-singular or on error.

### Example

```python
import rhinoscriptsyntax as rs
xform = rs.BlockInstanceXform(obj)
if xform:
 rs.TransformObject( obj, rs.XformInverse(xform) )
```

### See Also

XformDeterminant

---

## XformMirror

### Signature

```python
XformMirror(mirror_plane_point, mirror_plane_normal)
```

### Description

Creates a mirror transformation matrix

### Returns

transform: mirror Transform matrix

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.GetObjects("Select objects to mirror")
if objs:
 plane = rs.ViewCPlane()
 xform = rs.XformMirror(plane.Origin, plane.Normal)
 rs.TransformObjects( objs, xform, True )
```

### See Also

XformPlanarProjection, XformRotation1, XformRotation2, XformRotation3, XformRotation4, XformScale, XformShear, XformTranslation

---

## XformMultiply

### Signature

```python
XformMultiply(xform1, xform2)
```

### Description

Multiplies two transformation matrices, where result = xform1 * xform2

### Returns

transform: result transformation on success

### Example

```python
import rhinoscriptsyntax as rs
import math
objs = rs.GetObjects("Select objects to shear")
if objs:
 cplane = rs.ViewCPlane()
 cob = rs.XformChangeBasis(rs.WorldXYPlane(), cplane)
 shear2d = rs.XformIdentity()
 shear2d[0,2] = math.tan(math.radians(45.0))
 cob_inv = rs.XformChangeBasis(cplane, rs.WorldXYPlane())
 temp = rs.XformMultiply(shear2d, cob)
 xform = rs.XformMultiply(cob_inv, temp)
 rs.TransformObjects( objs, xform, True )
```

### See Also

XformPlanarProjection, XformRotation1, XformRotation2, XformRotation3, XformRotation4, XformScale, XformShear, XformTranslation

---

## XformPlanarProjection

### Signature

```python
XformPlanarProjection(plane)
```

### Description

Returns a transformation matrix that projects to a plane.

### Returns

transform: The 4x4 transformation matrix.

### Example

```python
import rhinoscriptsyntax as rs
objects = rs.GetObjects("Select objects to project")
if objects:
 cplane = rs.ViewCPlane()
 xform = rs.XformPlanarProjection(cplane)
 rs.TransformObjects( objects, xform, True )
```

### See Also

XformMirror, XformRotation1, XformRotation2, XformRotation3, XformRotation4, XformScale, XformShear, XformTranslation

---

## XformRotation1

### Signature

```python
XformRotation1(initial_plane, final_plane)
```

### Description

Returns a rotation transformation that maps initial_plane to final_plane. The planes should be right hand orthonormal planes.

### Returns

transform: The 4x4 transformation matrix. None: on error.

---

## XformRotation2

### Signature

```python
XformRotation2(angle_degrees, rotation_axis, center_point)
```

### Description

Returns a rotation transformation around an axis

### Returns

transform: The 4x4 transformation matrix. None: on error.

---

## XformRotation3

### Signature

```python
XformRotation3( start_direction, end_direction, center_point )
```

### Description

Calculate the minimal transformation that rotates start_direction to end_direction while fixing center_point

### Returns

transform: The 4x4 transformation matrix. None: on error.

---

## XformRotation4

### Signature

```python
XformRotation4(x0, y0, z0, x1, y1, z1)
```

### Description

Returns a rotation transformation.

### Returns

transform: The 4x4 transformation matrix. None: on error.

---

## XformScale

### Signature

```python
XformScale(scale, point=None)
```

### Description

Creates a scale transformation

### Returns

transform: The 4x4 transformation matrix on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.GetObjects("Select objects to scale")
if objs:
 xform = rs.XformScale( (3.0,1.0,1.0) )
 rs.TransformObjects( objs, xform, True)
```

### See Also

XformMirror, XformPlanarProjection, XformRotation1, XformRotation2, XformRotation3, XformRotation4, XformShear, XformTranslation

---

## XformScreenToWorld

### Signature

```python
XformScreenToWorld(point, view=None, screen_coordinates=False)
```

### Description

Transforms a point from either client-area coordinates of the specified view or screen coordinates to world coordinates. The resulting coordinates are represented as a 3-D point

### Returns

point: on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
point2d = 200,100
view = rs.CurrentView()
point = rs.XformScreenToWorld(point2d, view)
print(point)
```

### See Also

XformWorldToScreen

---

## XformShear

### Signature

```python
XformShear(plane, x, y, z)
```

### Description

Returns a shear transformation matrix

### Returns

transform: The 4x4 transformation matrix on success

### Example

```python
import rhinoscriptsyntax as rs
objects = rs.GetObjects("Select objects to shear")
if objects:
 cplane = rs.ViewCPlane()
 xform = rs.XformShear(cplane, (1,1,0), (-1,1,0), (0,0,1))
 rs.TransformObjects(objects, xform, True)
```

### See Also

XformMirror, XformPlanarProjection, XformRotation1, XformRotation2, XformRotation3, XformRotation4, XformScale, XformTranslation

---

## XformTranslation

### Signature

```python
XformTranslation(vector)
```

### Description

Creates a translation transformation matrix

### Returns

transform: The 4x4 transformation matrix is successful, otherwise None

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.GetObjects("Select objects to copy")
if objs:
 xform = rs.XformTranslation([1,0,0])
 rs.TransformObjects( objs, xform, True )
```

### See Also

XformMirror, XformPlanarProjection, XformRotation1, XformRotation2, XformRotation3, XformRotation4, XformScale, XformShear

---

## XformWorldToCPlane

### Signature

```python
XformWorldToCPlane(point, plane)
```

### Description

Transforms a point from world coordinates to construction plane coordinates.

### Returns

(point): 3D point in construction plane coordinates

### Example

```python
import rhinoscriptsyntax as rs
plane = rs.ViewCPlane()
point = rs.XformWorldToCPlane([0,0,0], plane)
if point: print("CPlane point:{}".format(point))
```

### See Also

XformCPlaneToWorld

---

## XformWorldToScreen

### Signature

```python
XformWorldToScreen(point, view=None, screen_coordinates=False)
```

### Description

Transforms a point from world coordinates to either client-area coordinates of the specified view or screen coordinates. The resulting coordinates are represented as a 2D point

### Returns

(point): 2D point on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
point = (0.0, 0.0, 0.0)
view = rs.CurrentView()
point2d = rs.XformWorldToScreen(point, view)
print(point2d)
```

### See Also

XformScreenToWorld

---

## XformZero

### Signature

```python
XformZero()
```

### Description

Returns a zero transformation matrix

### Returns

transform: a zero transformation matrix

### Example

```python
import rhinoscriptsyntax as rs
def printmatrix(xform):
 for i in range(4):
 print("[{}, {}, {}, {}]".format(xform[i,0], xform[i,1], xform[i,2], xform[i,3]))
printmatrix( rs.XformZero() )
```

### See Also

XformDiagonal, XformIdentity

---

# Userdata

*12 functions | 0 in use*

---

## DeleteDocumentData

### Signature

```python
DeleteDocumentData(section=None, entry=None)
```

### Description

Removes user data strings from the current document

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
rs.DeleteDocumentData( "MySection1", "MyEntry1" )
rs.DeleteDocumentData( "MySection1", "MyEntry2" )
rs.DeleteDocumentData( "MySection2", "MyEntry1" )
```

### See Also

DocumentDataCount, GetDocumentData, IsDocumentData, SetDocumentData

---

## DocumentDataCount

### Signature

```python
DocumentDataCount()
```

### Description

Returns the number of user data strings in the current document

### Returns

number: the number of user data strings in the current document

### Example

```python
import rhinoscriptsyntax as rs
count = rs.DocumentDataCount()
print("RhinoScript document user data count: {}".format(count))
```

### See Also

DeleteDocumentData, GetDocumentData, IsDocumentData, SetDocumentData

---

## DocumentUserTextCount

### Signature

```python
DocumentUserTextCount()
```

### Description

Returns the number of user text strings in the current document

### Returns

number: the number of user text strings in the current document

### See Also

GetDocumentUserText, IsDocumentUserText, SetDocumentUserText

---

## GetDocumentData

### Signature

```python
GetDocumentData(section=None, entry=None)
```

### Description

Returns a user data item from the current document

### Returns

list(str, ...): of all section names if section name is omitted list(str, ...) of all entry names for a section if entry is omitted str: value of the entry if both section and entry are specified None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
value = rs.GetDocumentData("MySection1", "MyEntry1")
print(value)
value = rs.GetDocumentData("MySection1", "MyEntry2")
print(value)
value = rs.GetDocumentData("MySection2", "MyEntry1")
print(value)
```

### See Also

DeleteDocumentData, DocumentDataCount, IsDocumentData, SetDocumentData

---

## GetDocumentUserText

### Signature

```python
GetDocumentUserText(key=None)
```

### Description

Returns user text stored in the document

### Returns

str: If key is specified, then the associated value if successful. list(str, ...):If key is not specified, then a list of key names if successful. None: If not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
print(rs.GetDocumentUserText("Designer"))
print(rs.GetDocumentUserText("Notes"))
```

### See Also

SetDocumentUserText

---

## GetUserText

### Signature

```python
GetUserText(object_id, key=None, attached_to_geometry=False)
```

### Description

Returns user text stored on an object.

### Returns

str: if key is specified, the associated value if successful list(str, ...): if key is not specified, a list of key names if successful

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if obj:
 print(rs.GetUserText(obj, "PartNo"))
 print(rs.GetUserText(obj, "Price"))
```

### See Also

IsUserText, SetUserText

---

## IsDocumentData

### Signature

```python
IsDocumentData()
```

### Description

Verifies the current document contains user data

### Returns

bool: True or False indicating the presence of Script user data

### Example

```python
import rhinoscriptsyntax as rs
result = rs.IsDocumentData()
if result:
 print("This document contains Script document user data")
else:
 print("This document contains no Script document user data")
```

### See Also

DeleteDocumentData, DocumentDataCount, GetDocumentData, SetDocumentData

---

## IsDocumentUserText

### Signature

```python
IsDocumentUserText()
```

### Description

Verifies the current document contains user text

### Returns

bool: True or False indicating the presence of Script user text

### See Also

GetDocumentUserText, SetDocumentUserText

---

## IsUserText

### Signature

```python
IsUserText(object_id)
```

### Description

Verifies that an object contains user text

### Returns

number: result of test: 0 = no user text 1 = attribute user text 2 = geometry user text 3 = both attribute and geometry user text

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if obj:
 usertext_type = rs.IsUserText(obj)
 if usertext_type==0: print("Object has no user text")
 elif usertext_type==1: print("Object has attribute user text")
 elif usertext_type==2: print("Object has geometry user text")
 elif usertext_type==3: print("Object has attribute and geometry user text")
 else: print("Object does not exist")
```

### See Also

GetUserText, SetUserText

---

## SetDocumentData

### Signature

```python
SetDocumentData(section, entry, value)
```

### Description

Adds or sets a user data string to the current document

### Returns

str: The previous value

### Example

```python
import rhinoscriptsyntax as rs
rs.SetDocumentData( "MySection1", "MyEntry1", "MyValue1" )
rs.SetDocumentData( "MySection1", "MyEntry2", "MyValue2" )
rs.SetDocumentData( "MySection2", "MyEntry1", "MyValue1" )
```

### See Also

DeleteDocumentData, DocumentDataCount, GetDocumentData, IsDocumentData

---

## SetDocumentUserText

### Signature

```python
SetDocumentUserText(key, value=None)
```

### Description

Sets or removes user text stored in the document

### Returns

bool: True or False indicating success

### Example

```python
import rhinoscriptsyntax as rs
rs.SetDocumentUserText("Designer", "Steve Baer")
rs.SetDocumentUserText("Notes", "Added some layer and updated some geometry")
```

### See Also

GetDocumentUserText

---

## SetUserText

### Signature

```python
SetUserText(object_id, key, value=None, attach_to_geometry=False)
```

### Description

Sets or removes user text stored on an object.

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if obj:
 rs.SetUserText( obj, "PartNo", "KM40-4960" )
 rs.SetUserText( obj, "Price", "1.25" )
```

### See Also

GetUserText, IsUserText

---

# Userinterface

*38 functions | 0 in use*

---

## BrowseForFolder

### Signature

```python
BrowseForFolder(folder=None, message=None, title=None)
```

### Description

Display browse-for-folder dialog allowing the user to select a folder

### Returns

str: selected folder None: on error

### Example

```python
import rhinoscriptsyntax as rs
folder = rs.BrowseForFolder("C:\\Program Files\\" )
if folder: print(folder)
```

### See Also

OpenFileName, SaveFileName

---

## CheckListBox

### Signature

```python
CheckListBox(items, message=None, title=None)
```

### Description

Displays a list of items in a checkable-style list dialog box

### Returns

list((str, bool), ...): of tuples containing the input string in items along with their new boolean check value None: on error

### Example

```python
import rhinoscriptsyntax as rs
layers = rs.LayerNames()
if layers:
 items = [(layer, rs.IsLayerOn(layer)) for layer in layers]
 results = rs.CheckListBox(items, "Turn layers on/off", "Layers")
 if results:
 for layer, state in results: rs.LayerVisible(layer, state)
```

### See Also

ComboListBox, ListBox, MultiListBox, PropertyListBox

---

## ComboListBox

### Signature

```python
ComboListBox(items, message=None, title=None)
```

### Description

Displays a list of items in a combo-style list box dialog.

### Returns

str: The selected item if successful None: if not successful or on error

### Example

```python
import rhinoscriptsyntax as rs
layers = rs.LayerNames()
if layers:
 layer = rs.ComboListBox(layers, "Select current layer")
 if layer: rs.CurrentLayer(layer)
```

### See Also

CheckListBox, ListBox, MultiListBox, PropertyListBox

---

## EditBox

### Signature

```python
EditBox(default_string=None, message=None, title=None)
```

### Description

Display dialog prompting the user to enter a string. The string value may span multiple lines

### Returns

str: Multiple lines that are separated by carriage return-linefeed combinations if successful None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
text = rs.EditBox(message="Enter some text")
print(text)
```

### See Also

GetString, StringBox

---

## GetAngle

### Signature

```python
GetAngle(point=None, reference_point=None, default_angle_degrees=0, message=None)
```

### Description

Pause for user input of an angle

### Returns

number: angle in degree if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
point = rs.GetPoint("Base point")
if point:
 reference = rs.GetPoint("Reference point", point)
 if reference:
 angle = rs.GetAngle(point, reference)
 if angle!=None: print("Angle:{}".format(angle))
```

### See Also

GetDistance

---

## GetBoolean

### Signature

```python
GetBoolean(message, items, defaults)
```

### Description

Pauses for user input of one or more boolean values. Boolean values are displayed as click-able command line option toggles

### Returns

list(bool, ...): a list of values that represent the boolean values if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
items = ("Lights", "Off", "On"), ("Cameras", "Disabled", "Enabled"), ("Action", "False", "True")
results = rs.GetBoolean("Boolean options", items, (True, True, True) )
if results:
 for val in results: print(val)
```

### See Also

GetString

---

## GetBox

### Signature

```python
GetBox(mode=0, base_point=None, prompt1=None, prompt2=None, prompt3=None)
```

### Description

Pauses for user input of a box

### Returns

list(point, ...): list of eight Point3d that define the corners of the box on success None: is not successful, or on error

### Example

```python
import rhinoscriptsyntax as rs
box = rs.GetBox()
if box:
 for i, pt in enumerate(box): rs.AddTextDot( i, pt )
```

### See Also

GetRectangle

---

## GetColor

### Signature

```python
GetColor(color=[0,0,0])
```

### Description

Display the Rhino color picker dialog allowing the user to select an RGB color

### Returns

color: RGB tuple of three numbers on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
color = rs.LayerColor("Default")
rgb = rs.GetColor(color)
if rgb: rs.LayerColor("Default", rgb)
```

---

## GetCursorPos

### Signature

```python
GetCursorPos()
```

### Description

Retrieves the cursor's position

### Returns

tuple(point, point, guid, point) containing the following information [0] cursor position in world coordinates [1] cursor position in screen coordinates [2] id of the active viewport [3] cursor position in client coordinates

### Example

```python
import rhinoscriptsyntax as rs
world, screen, view, client = rs.GetCursorPos()
```

### See Also

XformScreenToWorld, XformWorldToScreen

---

## GetDistance

### Signature

```python
GetDistance(first_pt=None, distance=None, first_pt_msg='First distance point', second_pt_msg='Second distance point')
```

### Description

Pauses for user input of a distance.

### Returns

number: The distance between the two points if successful. None: if not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
dist = rs.GetDistance()
if dist:
 print( dist)
```

### See Also

GetAngle

---

## GetEdgeCurves

### Signature

```python
GetEdgeCurves(message=None, min_count=1, max_count=0, select=False)
```

### Description

Prompt the user to pick one or more surface or polysurface edge curves

### Returns

list(tuple[guid, point, point], ...): of selection prompts (curve id, parent id, selection point) None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
edges = rs.GetEdgeCurves()
if edges:
 for edgeinfo in edges:
 print("Curve Id ={}".format(edgeinfo[0]))
 print("Parent Id ={}".format(edgeinfo[1]))
 print("Pick point ={}".format(edgeinfo[2]))
```

### See Also

DuplicateEdgeCurves

---

## GetInteger

### Signature

```python
GetInteger(message=None, number=None, minimum=None, maximum=None)
```

### Description

Pauses for user input of a whole number.

### Returns

number: The whole number input by the user if successful. None: if not successful, or on error

### Example

```python
import rhinoscriptsyntax as rs
color = rs.LayerColor("Default")
color = rs.GetInteger("Enter an RGB color value", color.ToArgb(), 0)
if color: rs.LayerColor("Default", color)
```

---

## GetLayer

### Signature

```python
GetLayer(title="Select Layer", layer=None, show_new_button=False, show_set_current=False)
```

### Description

Displays dialog box prompting the user to select a layer

### Returns

str: name of selected layer if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Select object")
if obj:
 layer = rs.GetLayer("Select Layer", rs.ObjectLayer(obj), True, True)
 if layer: rs.ObjectLayer( obj, layer )
```

---

## GetLayers

### Signature

```python
GetLayers(title="Select Layers", show_new_button=False)
```

### Description

Displays a dialog box prompting the user to select one or more layers

### Returns

str: The names of selected layers if successful

### Example

```python
import rhinoscriptsyntax as rs
layers = rs.GetLayers("Select Layers")
if layers:
 for layer in layers: print(layer)
```

### See Also

GetLayer

---

## GetLine

### Signature

```python
GetLine(mode=0, point=None, message1=None, message2=None, message3=None)
```

### Description

Prompts the user to pick points that define a line

### Returns

line: Tuple of two points on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
line = rs.GetLine()
if line: rs.AddLine( line[0], line[1] )
```

### See Also

GetBox, GetPoint, GetPolyline, GetRectangle

---

## GetLinetype

### Signature

```python
GetLinetype(default_linetype=None, show_by_layer=False)
```

### Description

Displays a dialog box prompting the user to select one linetype

### Returns

str: The names of selected linetype if successful

### Example

```python
import rhinoscriptsyntax as rs
linetype = rs.GetLinetype()
if linetype: print(linetype)
```

### See Also

GetLayer

---

## GetMeshFaces

### Signature

```python
GetMeshFaces(object_id, message="", min_count=1, max_count=0)
```

### Description

Prompts the user to pick one or more mesh faces

### Returns

list(number, ...): of mesh face indices on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
mesh = rs.GetObject("Select mesh", rs.filter.mesh)
if mesh:
 indices = rs.GetMeshFaces(mesh)
 if indices:
 for index in indices: print(index)
```

### See Also

GetMeshVertices, MeshFaces, MeshFaceVertices, MeshVertices

---

## GetMeshVertices

### Signature

```python
GetMeshVertices(object_id, message="", min_count=1, max_count=0)
```

### Description

Prompts the user to pick one or more mesh vertices

### Returns

list(number, ...): of mesh vertex indices on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
mesh = rs.GetObject("Select mesh", rs.filter.mesh)
if mesh:
 indices = rs.GetMeshVertices(mesh)
 if indices:
 for index in indices: print(index)
```

### See Also

GetMeshFaces, MeshFaces, MeshFaceVertices, MeshVertices

---

## GetPoint

### Signature

```python
GetPoint(message=None, base_point=None, distance=None, in_plane=False)
```

### Description

Pauses for user input of a point.

### Returns

point: point on success None: if no point picked or user canceled

### Example

```python
import rhinoscriptsyntax as rs
point1 = rs.GetPoint("Pick first point")
if point1:
 rs.AddPoint(point1)
 point2 = rs.GetPoint("Pick second point", point1)
 if point2:
 rs.AddPoint(point2)
 distance = (point1-point2).Length
 point3 = rs.GetPoint("Pick third point", point2, distance)
 if point3: rs.AddPoint(point3)
```

### See Also

GetPointOnCurve, GetPointOnSurface, GetPoints, GetRectangle

---

## GetPointOnCurve

### Signature

```python
GetPointOnCurve(curve_id, message=None)
```

### Description

Pauses for user input of a point constrainted to a curve object

### Returns

point: 3d point if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject("Pick a curve")
if rs.IsCurve(obj):
 point = rs.GetPointOnCurve(obj, "Point on curve")
 if point: rs.AddPoint(point)
```

### See Also

GetPoint, GetPointOnMesh, GetPointOnSurface, GetPoints

---

## GetPointOnMesh

### Signature

```python
GetPointOnMesh(mesh_id, message=None)
```

### Description

Pauses for user input of a point constrained to a mesh object

### Returns

point: 3d point if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
mesh = rs.GetObject("Pick a mesh", rs.filter.mesh)
if mesh:
 point = rs.GetPointOnMesh(mesh, "Point on mesh")
 if point: rs.AddPoint( point )
```

### See Also

GetPoint, GetPointOnCurve, GetPointOnSurface, GetPoints

---

## GetPointOnSurface

### Signature

```python
GetPointOnSurface(surface_id, message=None)
```

### Description

Pauses for user input of a point constrained to a surface or polysurface object

### Returns

point: 3d point if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
surface = rs.GetObject("Pick a surface")
if surface:
 point = rs.GetPointOnSurface(surface, "Point on surface")
 if point: rs.AddPoint(point)
```

### See Also

GetPoint, GetPointOnCurve, GetPointOnMesh, GetPoints

---

## GetPoints

### Signature

```python
GetPoints(draw_lines=False, in_plane=False, message1=None, message2=None, max_points=None, base_point=None)
```

### Description

Pauses for user input of one or more points

### Returns

list(point, ...): of 3d points if successful None: if not successful or on error

### Example

```python
import rhinoscriptsyntax as rs
points = rs.GetPoints(True)
if points: rs.AddPointCloud(points)
```

### See Also

GetPoint, GetPointOnCurve, GetPointOnSurface, GetRectangle

---

## GetPolyline

### Signature

```python
GetPolyline(flags=3, message1=None, message2=None, message3=None, message4=None, min=2, max=0)
```

### Description

Prompts the user to pick points that define a polyline.

### Returns

list(point, ...): A list of 3-D points that define the polyline if successful. None: if not successful or on error

### Example

```python
import rhinoscriptsyntax as rs
from scriptcontext import doc
arr = rs.GetPolyline()
if arr is not None:
 doc.AddPolyline(arr)
```

### See Also

GetBox, GetLine, GetRectangle

---

## GetReal

### Signature

```python
GetReal(message="Number", number=None, minimum=None, maximum=None)
```

### Description

Pauses for user input of a number.

### Returns

number: The number input by the user if successful. None: if not successful, or on error

### Example

```python
import rhinoscriptsyntax as rs
radius = rs.GetReal("Radius of new circle", 3.14, 1.0)
if radius: rs.AddCircle( (0,0,0), radius )
```

### See Also

RealBox

---

## GetRectangle

### Signature

```python
GetRectangle(mode=0, base_point=None, prompt1=None, prompt2=None, prompt3=None)
```

### Description

Pauses for user input of a rectangle

### Returns

tuple(point, point, point, point): four 3d points that define the corners of the rectangle None: on error

### Example

```python
import rhinoscriptsyntax as rs
rect = rs.GetRectangle()
if rect:
 for i, corner in enumerate(rect):
 rs.AddTextDot( i, corner )
```

### See Also

GetPoint, GetPoints

---

## GetString

### Signature

```python
GetString(message=None, defaultString=None, strings=None)
```

### Description

Pauses for user input of a string value

### Returns

str: The string either input or selected by the user if successful. If the user presses the Enter key without typing in a string, an empty string "" is returned. None: if not successful, on error, or if the user pressed cancel.

### Example

```python
import rhinoscriptsyntax as rs
layer = rs.CurrentLayer()
layer = rs.GetString("Layer to set current", layer)
if layer: rs.CurrentLayer(layer)
```

### See Also

GetBoolean, StringBox

---

## ListBox

### Signature

```python
ListBox(items, message=None, title=None, default=None)
```

### Description

Display a list of items in a list box dialog.

### Returns

str: he selected item if successful None: if not successful or on error

### Example

```python
import rhinoscriptsyntax as rs
layers = rs.LayerNames()
if layers:
 result = rs.ListBox(layers, "Layer to set current")
 if result: rs.CurrentLayer( result )
```

### See Also

CheckListBox, ComboListBox, MultiListBox, PropertyListBox

---

## MessageBox

### Signature

```python
MessageBox(message, buttons=0, title="")
```

### Description

Displays a message box. A message box contains a message and title, plus any combination of predefined icons and push buttons.

### Returns

number: indicating which button was clicked: 1 OK button was clicked. 2 Cancel button was clicked. 3 Abort button was clicked. 4 Retry button was clicked. 5 Ignore button was clicked. 6 Yes button was clicked. 7 No button was clicked.

### Example

```python
import rhinoscriptsyntax as rs
rs.MessageBox("Hello Rhino!")
rs.MessageBox("Hello Rhino!", 4 | 32)
rs.MessageBox("Hello Rhino!", 2 | 48)
```

---

## MultiListBox

### Signature

```python
MultiListBox(items, message=None, title=None, defaults=None)
```

### Description

Displays a list of items in a multiple-selection list box dialog

### Returns

list(str, ...): containing the selected items if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
layers = rs.LayerNames()
if layers:
 layers = rs.MultiListBox(layers, "Layers to lock")
if layers:
 for layer in layers:
 rs.LayerLocked(layer, True)
```

### See Also

CheckListBox, ComboListBox, ListBox, PropertyListBox

---

## OpenFileName

### Signature

```python
OpenFileName(title=None, filter=None, folder=None, filename=None, extension=None)
```

### Description

Displays file open dialog box allowing the user to enter a file name. Note, this function does not open the file.

### Returns

str: file name is successful None: if not successful, or on error

### Example

```python
import rhinoscriptsyntax as rs
filename = rs.OpenFileName()
if filename: rs.MessageBox(filename)
filename = rs.OpenFileName("Open", "Text Files (*.txt)|*.txt||")
if filename: rs.MessageBox(filename)
filename = rs.OpenFileName("Open", "Text Files (*.txt)|*.txt|All Files (*.*)|*.*||")
if filename: rs.MessageBox(filename)
```

### See Also

BrowseForFolder, OpenFileNames, SaveFileName

---

## OpenFileNames

### Signature

```python
OpenFileNames(title=None, filter=None, folder=None, filename=None, extension=None)
```

### Description

Displays file open dialog box allowing the user to select one or more file names. Note, this function does not open the file.

### Returns

list(str, ...): of selected file names

### Example

```python
import rhinoscriptsyntax as rs
filenames = rs.OpenFileNames("Open", "Text Files (*.txt)|*.txt|All Files (*.*)|*.*||")
for filename in filenames: print(filename)
```

### See Also

BrowseForFolder, OpenFileName, SaveFileName

---

## PopupMenu

### Signature

```python
PopupMenu(items, modes=None, point=None, view=None)
```

### Description

Display a context-style popup menu. The popup menu can appear almost anywhere, and can be dismissed by clicking the left or right mouse buttons

### Returns

number: index of the menu item picked or -1 if no menu item was picked

### Example

```python
import rhinoscriptsyntax as rs
items = "Line", "", "Circle", "Arc"
modes = 2,0,0,0
result = rs.PopupMenu(items, modes)
if result>=0: rs.MessageBox(items[result])
```

---

## PropertyListBox

### Signature

```python
PropertyListBox(items, values, message=None, title=None)
```

### Description

Displays list of items and their values in a property-style list box dialog

### Returns

list(str, ..): of new values on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
objs = rs.GetObjects("Select Objects")
if objs:
 names = []
 for obj in objs:
 name = rs.ObjectName(obj)
 if name is None: name=""
 names.append(name)
 results = rs.PropertyListBox(objs, names, "Modify object name(s)")
 if results:
 for i in compat.RANGE(len(objs)):
 rs.ObjectName( objs[i], results[i] )
```

### See Also

CheckListBox, ComboListBox, ListBox, MultiListBox

---

## RealBox

### Signature

```python
RealBox(message="", default_number=None, title="", minimum=None, maximum=None)
```

### Description

Display a dialog box prompting the user to enter a number

### Returns

number: The newly entered number on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
radius = rs.RealBox("Enter a radius value", 5.0 )
if radius:
 point = (0,0,0)
 rs.AddCircle( point, radius )
```

### See Also

GetReal

---

## SaveFileName

### Signature

```python
SaveFileName(title=None, filter=None, folder=None, filename=None, extension=None)
```

### Description

Display a save dialog box allowing the user to enter a file name. Note, this function does not save the file.

### Returns

str: the file name is successful None: if not successful, or on error

### Example

```python
import rhinoscriptsyntax as rs
filename = rs.SaveFileName()
if filename: rs.MessageBox(filename)
filename = rs.SaveFileName ("Save", "Text Files (*.txt)|*.txt||")
if filename: rs.MessageBox(filename)
filename = rrshui.SaveFileName ("Save", "Text Files (*.txt)|*.txt|All Files (*.*)|*.*||")
if filename: rs.MessageBox(filename)
```

### See Also

BrowseForFolder, OpenFileName

---

## StringBox

### Signature

```python
StringBox(message=None, default_value=None, title=None)
```

### Description

Display a dialog box prompting the user to enter a string value.

### Returns

str: the newly entered string value if successful None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
layer = rs.StringBox("New layer name" )
if layer: rs.AddLayer( layer )
```

### See Also

GetString

---

## TextOut

### Signature

```python
TextOut(message=None, title=None)
```

### Description

Display a text dialog box similar to the one used by the _What command.

### Returns

None: in any case

### Example

```python
import rhinoscriptsyntax as rs
rs.TextOut("This is a long string..." )
```

### See Also

MessagBox

---

# Utility

*27 functions | 1 in use*

---

## Angle

### Signature

```python
Angle(point1, point2, plane=True)
```

### Description

Measures the angle between two points

### Returns

tuple(tuple(number, number), number, number, number, number): containing the following elements if successful element 0 = the X,Y angle in degrees element 1 = the elevation element 2 = delta in the X direction element 3 = delta in the Y direction element 4 = delta in the Z direction None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
point1 = rs.GetPoint("First point")
if point1:
 point2 = rs.GetPoint("Second point")
 if point2:
 angle = rs.Angle(point1, point2)
 if angle: print("Angle: {}".format(angle[0]))
```

### See Also

Angle2, Distance

---

## Angle2

### Signature

```python
Angle2(line1, line2)
```

### Description

Measures the angle between two lines

### Returns

tuple(number, number): containing the following elements if successful. 0 The angle in degrees. 1 The reflex angle in degrees. None: If not successful, or on error.

### Example

```python
import rhinoscriptsyntax as rs
point1 = rs.GetPoint("Start of first line")
point2 = rs.GetPoint("End of first line", point1)
point3 = rs.GetPoint("Start of second line")
point4 = rs.GetPoint("End of second line", point3)
angle = rs.Angle2( (point1, point2), (point3, point4))
if angle: print("Angle: {}".format(angle))
```

### See Also

Angle, Distance

---

## ClipboardText

### Signature

```python
ClipboardText(text=None)
```

### Description

Returns or sets a text string to the Windows clipboard

### Returns

str: if text is not specified, the current text in the clipboard str: if text is specified, the previous text in the clipboard None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
txt = rs.ClipboardText("Hello Rhino!")
if txt: rs.MessageBox(txt, 0, "Clipboard Text")
```

---

## ColorAdjustLuma

### Signature

```python
ColorAdjustLuma(rgb, luma, scale=False)
```

### Description

Changes the luminance of a red-green-blue value. Hue and saturation are not affected

### Returns

color: modified rgb value if successful

### Example

```python
import rhinoscriptsyntax as rs
rgb = rs.ColorAdjustLuma((128, 128, 128), 50)
print("Red = {}".format(rs.ColorRedValue(rgb)))
print("Green = {}".format(rs.ColorGreenValue(rgb)))
print("Blue = {}".format(rs.ColorBlueValue(rgb)))
```

### See Also

ColorHLSToRGB, ColorRGBToHLS

---

## ColorBlueValue

### Signature

```python
ColorBlueValue(rgb)
```

### Description

Retrieves intensity value for the blue component of an RGB color

### Returns

number: The blue component if successful, otherwise None

### Example

```python
import rhinoscriptsyntax as rs
rgb = rs.LayerColor("Default")
print("Red = {}".format(rs.ColorRedValue(rgb)))
print("Green = {}".format(rs.ColorGreenValue(rgb)))
print("Blue = {}".format(rs.ColorBlueValue(rgb)))
```

### See Also

ColorGreenValue, ColorRedValue

---

## ColorGreenValue

### Signature

```python
ColorGreenValue(rgb)
```

### Description

Retrieves intensity value for the green component of an RGB color

### Returns

number: The green component if successful, otherwise None

### Example

```python
import rhinoscriptsyntax as rs
rgb = rs.LayerColor("Default")
print("Red = {}".format(rs.ColorRedValue(rgb)))
print("Green = {}".format(rs.ColorGreenValue(rgb)))
print("Blue = {}".format(rs.ColorBlueValue(rgb)))
```

### See Also

ColorBlueValue, ColorRedValue

---

## ColorHLSToRGB

### Signature

```python
ColorHLSToRGB(hls)
```

### Description

Converts colors from hue-lumanence-saturation to RGB

### Returns

color: The RGB color value if successful, otherwise False

### Example

```python
import rhinoscriptsyntax as rs
rgb = rs.ColorHLSToRGB( (160, 120, 0) )
print("Red = {}".format(rs.ColorRedValue(rgb)))
print("Green = {}".format(rs.ColorGreenValue(rgb)))
print("Blue = {}".format(rs.ColorBlueValue(rgb)))
```

### See Also

ColorAdjustLuma, ColorRGBToHLS

---

## ColorRGBToHLS

### Signature

```python
ColorRGBToHLS(rgb)
```

### Description

Convert colors from RGB to HLS

### Returns

color: The HLS color value if successful, otherwise False

### Example

```python
import rhinoscriptsyntax as rs
hls = rs.ColorRGBToHLS((128, 128, 128))
print("Hue = {}".format(hls[0]))
print("Luminance = {}".format(hls[1]))
print("Saturation = {}".format(hls[2]))
```

### See Also

ColorAdjustLuma, ColorHLSToRGB

---

## ColorRedValue

### Signature

```python
ColorRedValue(rgb)
```

### Description

Retrieves intensity value for the red component of an RGB color

### Returns

color: The red color value if successful, otherwise False

### Example

```python
import rhinoscriptsyntax as rs
rgb = rs.LayerColor("Default")
print("Red = {}".format(rs.ColorRedValue(rgb)))
print("Green = {}".format(rs.ColorGreenValue(rgb)))
print("Blue = {}".format(rs.ColorBlueValue(rgb)))
```

### See Also

ColorBlueValue, ColorGreenValue

---

## ContextIsGrasshopper

### Signature

```python
ContextIsGrasshopper()
```

### Description

Return True if the script is being executed in a grasshopper component

### Returns

bool: True if the script is being executed in a grasshopper component

### Example

```python
import rhinoscriptsyntax as rs
print(rs.ContextIsGrasshopper())
```

### See Also

ContextIsRhino

---

## ContextIsRhino

### Signature

```python
ContextIsRhino()
```

### Description

Return True if the script is being executed in the context of Rhino

### Returns

bool: True if the script is being executed in the context of Rhino

### Example

```python
import rhinoscriptsyntax as rs
print(rs.ContextIsRhino())
```

### See Also

ContextIsGrasshopper

---

## CreateColor

### Signature

```python
CreateColor(color, g=None, b=None, a=None)
```

### Description

Converts 'color' into a native color object if possible. The returned data is accessible by indexing, and that is the suggested method to interact with the type. Red index is [0], Green index is [1], Blue index is [2] and Alpha index is [3]. If the provided object is already a color, its value is copied. Alternatively, you can also pass three coordinates singularly for an RGB color, or four for an RGBA color point.

### Returns

color: An object that can be indexed for red, green, blu, alpha. Item[0] is red.

---

## CreateInterval

### Signature

```python
CreateInterval(interval, y=None)
```

### Description

Converts 'interval' into a Rhino.Geometry.Interval. If the provided object is already an interval, its value is copied. In case the conversion fails, an error is raised. In case a single number is provided, it will be translated to an increasing interval that includes the provided input and 0. If two values are provided, they will be used instead.

### Returns

interval: a Rhino.Geometry.Interval. This can be seen as an object made of two items: [0] start of interval [1] end of interval

---

## CreatePlane

### Signature

```python
CreatePlane(plane_or_origin, x_axis=None, y_axis=None, ignored=None)
```

### Description

Converts input into a Rhino.Geometry.Plane object if possible. If the provided object is already a plane, its value is copied. The returned data is accessible by indexing[origin, X axis, Y axis, Z axis], and that is the suggested method to interact with the type. The Z axis is in any case computed from the X and Y axes, so providing it is possible but not required. If the conversion fails, an error is raised.

### Returns

plane: A Rhino.Geometry.plane.

---

## CreatePoint

### Signature

```python
CreatePoint(point, y=None, z=None)
```

### Description

Converts 'point' into a Rhino.Geometry.Point3d if possible. If the provided object is already a point, it value is copied. In case the conversion fails, an error is raised. Alternatively, you can also pass two coordinates singularly for a point on the XY plane, or three for a 3D point.

### Returns

point: a Rhino.Geometry.Point3d. This can be seen as an object with three indices: [0] X coordinate [1] Y coordinate [2] Z coordinate.

---

## CreateVector

### Signature

```python
CreateVector(vector, y=None, z=None)
```

### Description

Converts 'vector' into a Rhino.Geometry.Vector3d if possible. If the provided object is already a vector, it value is copied. If the conversion fails, an error is raised. Alternatively, you can also pass two coordinates singularly for a vector on the XY plane, or three for a 3D vector.

### Returns

a Rhino.Geometry.Vector3d. This can be seen as an object with three indices: result[0]: X component, result[1]: Y component, and result[2] Z component.

---

## CreateXform

### Signature

```python
CreateXform(xform)
```

### Description

Converts input into a Rhino.Geometry.Transform object if possible. If the provided object is already a transform, its value is copied. The returned data is accessible by indexing[row, column], and that is the suggested method to interact with the type. If the conversion fails, an error is raised.

### Returns

transform: A Rhino.Geometry.Transform. result[0,3] gives access to the first row, last column.

---

## CullDuplicateNumbers

### Signature

```python
CullDuplicateNumbers(numbers, tolerance=None)
```

### Description

Removes duplicates from an array of numbers.

### Returns

list(number, ...): numbers with duplicates removed if successful.

### Example

```python
import rhinoscriptsyntax as rs
arr = [1,1,2,2,3,3,4,4,5,5]
arr = rs.CullDuplicateNumbers(arr)
for n in arr: print(n)
```

### See Also

CullDuplicatePoints

---

## CullDuplicatePoints

### Signature

```python
CullDuplicatePoints(points, tolerance=-1)
```

### Description

Removes duplicates from a list of 3D points.

### Returns

list(point, ...): of 3D points with duplicates removed if successful. None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
points = rs.GetPoints(,,"First point", "Next point")
if points:
 points= rs.CullDuplicatePoints(points)
 for p in points: print(p)
```

### See Also

CullDuplicateNumbers

---

## Distance

** IN USE**

### Signature

```python
Distance(point1, point2)
```

### Description

Measures distance between two 3D points, or between a 3D point and an array of 3D points.

### Returns

point: If point2 is a 3D point then the distance if successful. point: If point2 is a list of points, then an list of distances if successful. None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
point1 = rs.GetPoint("First point")
if point1:
 point2 = rs.GetPoint("Second point")
 if point2:
 print("Distance: {}".format(rs.Distance(point1, point2)))
```

### See Also

Angle, Angle2

---

## GetSettings

### Signature

```python
GetSettings(filename, section=None, entry=None)
```

### Description

Returns string from a specified section in a initialization file.

### Returns

list(str, ...): If section is not specified, a list containing all section names list:(str, ...): If entry is not specified, a list containing all entry names for a given section str: If section and entry are specified, a value for entry None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
filename = rs.OpenFileName("Open", "Initialization Files (*.ini)|*.ini||")
if filename:
 sections = rs.GetSettings(filename)
 if sections:
 section = rs.ListBox(sections, "Select a section", filename)
 if section:
 entries = rs.GetSettings(filename, section)
 if entries:
 entry = rs.ListBox(entries, "Select an entry", section)
 if entry:
 value = rs.GetSettings(filename, section, entry)
 if value: rs.MessageBox( value, 0, entry )
```

---

## Polar

### Signature

```python
Polar(point, angle_degrees, distance, plane=None)
```

### Description

Returns 3D point that is a specified angle and distance from a 3D point

### Returns

point: resulting point is successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
point = (1.0, 1.0, 0.0)
result = rs.Polar(point, 45.0, 1.414214)
print(result)
```

### See Also

PointAdd, PointCompare, PointDivide, PointScale, PointSubtract

---

## SimplifyArray

### Signature

```python
SimplifyArray(points)
```

### Description

Flattens an array of 3-D points into a one-dimensional list of real numbers. For example, if you had an array containing three 3-D points, this method would return a one-dimensional array containing nine real numbers.

### Returns

list(number, ...): A one-dimensional list containing real numbers, if successful, otherwise None

### Example

```python
import rhinoscriptsyntax as rs
points = rs.GetPoints()
if points:
 numbers = rs.SimplifyArray(points)
 for n in numbers: print(n)
```

---

## Sleep

### Signature

```python
Sleep(milliseconds)
```

### Description

Suspends execution of a running script for the specified interval

### Returns

None

### Example

```python
import rhinoscriptsyntax as rs
print("This")
rs.Sleep(2000)
print("is")
rs.Sleep(2000)
print("a")
rs.Sleep(2000)
print("slow")
rs.Sleep(2000)
print("message!")
```

---

## SortPointList

### Signature

```python
SortPointList(points, tolerance=None)
```

### Description

Sorts list of points so they will be connected in a "reasonable" polyline order

### Returns

list(point, ...): of sorted 3D points if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
points = rs.GetPointCoordinates()
if points:
 sorted = rs.SortPointList(points)
 rs.AddPolyline(sorted)
```

### See Also

SortPoints

---

## SortPoints

### Signature

```python
SortPoints(points, ascending=True, order=0)
```

### Description

Sorts the components of an array of 3D points

### Returns

list(point, ...): sorted 3-D points if successful None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
points = rs.GetPoints()
if points:
 points = rs.SortPoints(points)
 for p in points: print(p)
```

---

## Str2Pt

### Signature

```python
Str2Pt(point)
```

### Description

convert a formatted string value into a 3D point value

### Returns

point: Point structure from the input string. None: error on invalid format

### Example

```python
import rhinoscriptsyntax as rs
point = rs.Str2Pt("1,2,3")
if point: rs.AddPoint( point )
```

---

# View

*56 functions | 0 in use*

---

## AddDetail

### Signature

```python
AddDetail(layout_id, corner1, corner2, title=None, projection=1)
```

### Description

Add new detail view to an existing layout view

### Returns

guid: identifier of the newly created detail on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
layout = rs.AddLayout("Portrait", (8.5,11))
if layout:
 rs.AddDetail(layout, (0.5,0.5), (8,10.5), None, 7)
```

### See Also

DeleteNamedView, NamedViews, RestoreNamedView

---

## AddLayout

### Signature

```python
AddLayout(title=None, size=None)
```

### Description

Adds a new page layout view

### Returns

guid: id of new layout

### Example

```python
import rhinoscriptsyntax as rs
rs.AddLayout("Portrait")
```

### See Also

DeleteNamedView, NamedViews, RestoreNamedView

---

## AddNamedCPlane

### Signature

```python
AddNamedCPlane(cplane_name, view=None)
```

### Description

Adds new named construction plane to the document

### Returns

atr: name of the newly created construction plane if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
views = rs.ViewNames()
if views:
 for view in views:
 name = view + "_cplane"
 rs.AddNamedCPlane( name, view )
```

### See Also

DeleteNamedCPlane, NamedCPlane, NamedCPlanes, RestoreNamedCPlane

---

## AddNamedView

### Signature

```python
AddNamedView(name, view=None)
```

### Description

Adds a new named view to the document

### Returns

str: name fo the newly created named view if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
views = rs.ViewNames()
if views:
 for view in views:
 name = view + "_view"
 rs.AddNamedView( name, view )
```

### See Also

DeleteNamedView, NamedViews, RestoreNamedView

---

## CurrentDetail

### Signature

```python
CurrentDetail(layout, detail=None, return_name=True)
```

### Description

Returns or changes the current detail view in a page layout view

### Returns

str: if detail is not specified, the title or id of the current detail view str: if detail is specified, the title or id of the previous detail view None: on error

### Example

```python
import rhinoscriptsyntax as rs
layout = rs.CurrentView(return_name=False)
if rs.IsLayout(layout):
 rs.CurrentDetail( layout, layout )
```

### See Also

IsDetail, IsLayout

---

## CurrentView

### Signature

```python
CurrentView(view=None, return_name=True)
```

### Description

Returns or sets the currently active view

### Returns

str: if the title is not specified, the title or id of the current view str: if the title is specified, the title or id of the previous current view None: on error

### Example

```python
import rhinoscriptsyntax as rs
previous = rs.CurrentView("Perspective")
print("The previous current view was {}".format(previous))
viewId = rs.CurrentView( return_name=False )
print("The identifier of the current view is {}".format(viewId))
```

### See Also

IsViewCurrent, ViewNames

---

## DeleteNamedCPlane

### Signature

```python
DeleteNamedCPlane(name)
```

### Description

Removes a named construction plane from the document

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
cplanes = rs.NamedCplanes()
if cplanes:
 for cplane in cplanes: rs.DeleteNamedCPlane(cplane)
```

### See Also

AddNamedCPlane, NamedCPlane, NamedCPlanes, RestoreNamedCPlane

---

## DeleteNamedView

### Signature

```python
DeleteNamedView(name)
```

### Description

Removes a named view from the document

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
views = rs.NamedViews()
if views:
 for view in views: rs.DeleteNamedView(view)
```

### See Also

AddNamedView, NamedViews, RestoreNamedView

---

## DetailLock

### Signature

```python
DetailLock(detail_id, lock=None)
```

### Description

Returns or modifies the projection locked state of a detail

### Returns

bool: if lock==None, the current detail projection locked state bool: if lock is True or False, the previous detail projection locked state None: on error

### Example

```python
import rhinoscriptsyntax as rs
detail = rs.GetObject("select a detail", rs.filter.detail)
if detail: rs.DetailLock(detail,True)
```

### See Also

IsDetail, IsLayout

---

## DetailScale

### Signature

```python
DetailScale(detail_id, model_length=None, page_length=None)
```

### Description

Returns or modifies the scale of a detail object

### Returns

number: current page to model scale ratio if model_length and page_length are both None number: previous page to model scale ratio if model_length and page_length are values None: on error

### Example

```python
import rhinoscriptsyntax as rs
detail = rs.GetObject("select a detail", rs.filter.detail)
if detail: rs.DetailScale(detail,1,1)
```

### See Also

IsDetail, IsLayout

---

## IsDetail

### Signature

```python
IsDetail(layout, detail)
```

### Description

Verifies that a detail view exists on a page layout view

### Returns

bool: True if detail is a detail view bool: False if detail is not a detail view None: on error

### Example

```python
import rhinoscriptsyntax as rs
view = rs.CurrentView()
if rs.IsLayout(view):
 isdetail = rs.IsDetail(view, "Top")
 if isdetail:
 print("Top is a detail view.")
 else:
 print("Top is not a detail view.")
```

### See Also

IsLayout, CurrentDetail

---

## IsLayout

### Signature

```python
IsLayout(layout)
```

### Description

Verifies that a view is a page layout view

### Returns

bool: True if layout is a page layout view bool: False is layout is a standard, model view None: on error

### Example

```python
import rhinoscriptsyntax as rs
view = rs.CurrentView()
if rs.IsLayout(view):
 print("The current view is a page layout view.")
else:
 print("The current view is standard, model view.")
```

### See Also

IsLayout, CurrentDetail

---

## IsView

### Signature

```python
IsView(view)
```

### Description

Verifies that the specified view exists

### Returns

bool: True of False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
title = "Perspective"
result = rs.IsView(title)
if result:
 print("The {} view exists.".format(title))
else:
 print("The {} view does not exist.".format(title))
```

### See Also

ViewNames

---

## IsViewCurrent

### Signature

```python
IsViewCurrent(view)
```

### Description

Verifies that the specified view is the current, or active view

### Returns

bool: True of False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
title = "Perspective"
result = rs.IsViewCurrent(title)
if result:
 print("The {} view is current".format(title))
else:
 print("The {} view is not current".format(title))
```

### See Also

CurrentView

---

## IsViewMaximized

### Signature

```python
IsViewMaximized(view=None)
```

### Description

Verifies that the specified view is maximized (enlarged so as to fill the entire Rhino window)

### Returns

bool: True of False

### Example

```python
import rhinoscriptsyntax as rs
title = rs.CurrentView()
result = rs.IsViewMaximized(title)
if result:
 print("The {} view is maximized".format(title))
else:
 print("The {} view is not maximized".format(title))
```

### See Also

MaximizeRestoreView

---

## IsViewPerspective

### Signature

```python
IsViewPerspective(view)
```

### Description

Verifies that the specified view's projection is set to perspective

### Returns

bool: True of False

### Example

```python
import rhinoscriptsyntax as rs
title = rs.CurrentView()
result = rs.IsViewPerspective(title)
if result:
 print("The {} view is set to perspective projection".format(title))
else:
 print("The {} view is set to parallel projection".format(title))
```

### See Also

ViewProjection

---

## IsViewTitleVisible

### Signature

```python
IsViewTitleVisible(view=None)
```

### Description

Verifies that the specified view's title window is visible

### Returns

bool: True of False

### Example

```python
import rhinoscriptsyntax as rs
title = rs.CurrentView()
vis = rs.IsViewTitleVisible(title)
if vis:
 print("The {} view's title is visible".format(title))
else:
 print("The {} view's title is not visible".format(title))
```

### See Also

ShowViewTitle

---

## IsWallpaper

### Signature

```python
IsWallpaper(view)
```

### Description

Verifies that the specified view contains a wallpaper image

### Returns

bool: True or False

### Example

```python
import rhinoscriptsyntax as rs
view = rs.CurrentView()
filename = rs.OpenFileName()
if filename and not rs.IsWallpaper(view):
 rs.Wallpaper(view, filename)
```

### See Also

Wallpaper

---

## MaximizeRestoreView

### Signature

```python
MaximizeRestoreView(view=None)
```

### Description

Toggles a view's maximized/restore window state of the specified view

### Returns

None

### Example

```python
import rhinoscriptsyntax as rs
title = rs.CurrentView()
if rs.IsViewMaximized(title):
 rs.MaximizeRestoreView( title )
```

### See Also

IsViewMaximized

---

## NamedCPlane

### Signature

```python
NamedCPlane(name)
```

### Description

Returns the plane geometry of the specified named construction plane

### Returns

plane: a plane on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
names = rs.NamedCPlanes()
if names:
 for name in names:
 plane = rs.NamedCPlane(name)
 print("CPlane name:" + name)
 print("CPlane origin:" + plane.Origin)
 print("CPlane x-axis:" + plane.Xaxis)
 print("CPlane y-axis:" + plane.Yaxis)
 print("CPlane z-axis:" + plane.Zaxis)
```

### See Also

AddNamedCPlane, DeleteNamedCPlane, NamedCPlanes, RestoreNamedCPlane

---

## NamedCPlanes

### Signature

```python
NamedCPlanes()
```

### Description

Returns the names of all named construction planes in the document

### Returns

list(str, ...): the names of all named construction planes in the document

### Example

```python
import rhinoscriptsyntax as rs
cplanes = rs.NamedCPlanes()
if cplanes:
 for cplane in cplanes: print(cplane)
```

### See Also

AddNamedCPlane, DeleteNamedCPlane, NamedCPlane, RestoreNamedCPlane

---

## NamedViews

### Signature

```python
NamedViews()
```

### Description

Returns the names of all named views in the document

### Returns

list(str, ...): the names of all named views in the document

### Example

```python
import rhinoscriptsyntax as rs
views = rs.NamedViews()
if views:
 for view in views: print(view)
```

### See Also

AddNamedView, DeleteNamedView, RestoreNamedView

---

## RenameView

### Signature

```python
RenameView(old_title, new_title)
```

### Description

Changes the title of the specified view

### Returns

str: the view's previous title if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
oldtitle = rs.CurrentView()
rs.renameview( oldtitle, "Current" )
```

### See Also

ViewNames

---

## RestoreNamedCPlane

### Signature

```python
RestoreNamedCPlane(cplane_name, view=None)
```

### Description

Restores a named construction plane to the specified view.

### Returns

str: name of the restored named construction plane if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
cplanes = rs.NamedCplanes()
if cplanes: rs.RestoreNamedCPlane( cplanes[0] )
```

### See Also

AddNamedCPlane, DeleteNamedCPlane, NamedCPlane, NamedCPlanes

---

## RestoreNamedView

### Signature

```python
RestoreNamedView(named_view, view=None, restore_bitmap=False)
```

### Description

Restores a named view to the specified view

### Returns

str: name of the restored view if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
views = rs.NamedViews()
if views: rs.RestoreNamedView(views[0])
```

### See Also

AddNamedView, DeleteNamedView, NamedViews

---

## RotateCamera

### Signature

```python
RotateCamera(view=None, direction=0, angle=None)
```

### Description

Rotates a perspective-projection view's camera. See the RotateCamera command in the Rhino help file for more details

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
rs.RotateCamera( angle=15 )
```

### See Also

RotateView, TiltView

---

## RotateView

### Signature

```python
RotateView(view=None, direction=0, angle=None)
```

### Description

Rotates a view. See RotateView command in Rhino help for more information

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
rs.RotateView( angle=90.0 )
```

### See Also

RotateCamera, TiltView

---

## ShowGrid

### Signature

```python
ShowGrid(view=None, show=None)
```

### Description

Shows or hides a view's construction plane grid

### Returns

bool: If show is not specified, then the grid display state if successful bool: If show is specified, then the previous grid display state if successful

### Example

```python
import rhinoscriptsyntax as rs
view = rs.CurrentView()
if rs.ShowGrid(view)==False:
 rs.ShowGrid( view, True )
```

### See Also

ShowGridAxes, ShowWorldAxes

---

## ShowGridAxes

### Signature

```python
ShowGridAxes(view=None, show=None)
```

### Description

Shows or hides a view's construction plane grid axes.

### Returns

bool: If show is not specified, then the grid axes display state bool: If show is specified, then the previous grid axes display state

### Example

```python
import rhinoscriptsyntax as rs
view = rs.CurrentView()
if rs.ShowGridAxes(view)==False:
 rs.ShowGridAxes( view, True )
```

### See Also

ShowGrid, ShowWorldAxes

---

## ShowViewTitle

### Signature

```python
ShowViewTitle(view=None, show=True)
```

### Description

Shows or hides the title window of a view

### Returns

None

### Example

```python
import rhinoscriptsyntax as rs
view = rs.CurrentView()
if rs.IsViewTitleVisible(view)==False:
 rs.ShowViewTitle( view, True )
```

### See Also

IsViewTitleVisible

---

## ShowWorldAxes

### Signature

```python
ShowWorldAxes(view=None, show=None)
```

### Description

Shows or hides a view's world axis icon

### Returns

bool: If show is not specified, then the world axes display state bool: If show is specified, then the previous world axes display state

### Example

```python
import rhinoscriptsyntax as rs
view = rs.CurrentView()
if rs.ShowWorldAxes(view)==False:
 rs.ShowWorldAxes( view, True )
```

### See Also

ShowGrid, ShowGridAxes

---

## TiltView

### Signature

```python
TiltView(view=None, direction=0, angle=None)
```

### Description

Tilts a view by rotating the camera up vector. See the TiltView command in the Rhino help file for more details.

### Returns

bool: True or False indicating success or failure

### Example

```python
import rhinoscriptsyntax as rs
rs.TiltView( angle=15 )
```

### See Also

RotateCamera

---

## ViewCPlane

### Signature

```python
ViewCPlane(view=None, plane=None)
```

### Description

Return or set a view's construction plane

### Returns

plane: If a construction plane is not specified, the current construction plane plane: If a construction plane is specified, the previous construction plane

### Example

```python
import rhinoscriptsyntax as rs
origin = rs.GetPoint("CPlane origin")
if origin:
 plane = rs.ViewCPlane()
 plane = rs.MovePlane(plane,origin)
 rs.ViewCPlane(None, plane)
```

### See Also

ViewCameraLens, ViewCameraTarget, ViewDisplayModes, ViewProjection, ViewSize

---

## ViewCamera

### Signature

```python
ViewCamera(view=None, camera_location=None)
```

### Description

Returns or sets the camera location of the specified view

### Returns

point: If camera_location is not specified, the current camera location point: If camera_location is specified, the previous camera location None: on error

### Example

```python
import rhinoscriptsyntax as rs
view = rs.CurrentView()
camera = rs.GetPoint("Select new camera location")
if camera: rs.ViewCamera(view,camera)
```

### See Also

ViewCameraTarget, ViewTarget

---

## ViewCameraLens

### Signature

```python
ViewCameraLens(view=None, length=None)
```

### Description

Returns or sets the 35mm camera lens length of the specified perspective projection view.

### Returns

number: If lens length is not specified, the current lens length number: If lens length is specified, the previous lens length

### Example

```python
import rhinoscriptsyntax as rs
view = rs.CurrentView()
if rs.IsViewPerspective(view):
 length = rs.ViewCameraLens(view, 100)
```

### See Also

ViewCameraTarget, ViewCPlane, ViewDisplayModes, ViewProjection, ViewSize

---

## ViewCameraPlane

### Signature

```python
ViewCameraPlane(view=None)
```

### Description

Returns the orientation of a view's camera.

### Returns

plane: the view's camera plane if successful None: on error

### Example

```python
import rhinoscriptsyntax as rs
view = rs.CurrentView()
target = rs.ViewTarget(view)
camplane = rs.ViewCameraPlane(view)
plane = rs.MovePlane(camplane, target)
rs.ViewCPlane( view, plane )
```

### See Also

ViewCamera, ViewTarget

---

## ViewCameraTarget

### Signature

```python
ViewCameraTarget(view=None, camera=None, target=None)
```

### Description

Returns or sets the camera and target positions of the specified view

### Returns

list(point, point): if both camera and target are not specified, then the 3d points containing the current camera and target locations is returned point: if either camera or target are specified, then the 3d points containing the previous camera and target locations is returned

### Example

```python
import rhinoscriptsyntax as rs
view = rs.CurrentView()
camera = rs.GetPoint("Select new camera location")
target = rs.GetPoint("Select new target location")
if camera and target:
 rs.ViewCameraTarget( view, camera, target )
```

### See Also

ViewCamera, ViewTarget

---

## ViewCameraUp

### Signature

```python
ViewCameraUp(view=None, up_vector=None)
```

### Description

Returns or sets the camera up direction of a specified

### Returns

vector: if up_vector is not specified, then the current camera up direction vector: if up_vector is specified, then the previous camera up direction

### Example

```python
import rhinoscriptsyntax as rs
view = rs.CurrentView()
upVector = rs.ViewCameraUp(view)
print(up_vector)
```

### See Also

ViewCamera, ViewTarget

---

## ViewDisplayMode

### Signature

```python
ViewDisplayMode(view=None, mode=None, return_name=True)
```

### Description

Return or set a view display mode

### Returns

str: If mode is specified, the previous mode str: If mode is not specified, the current mode

### Example

```python
import rhinoscriptsyntax as rs
views = rs.ViewNames()
for view in views:
 rs.ViewDisplayMode(view, 'Ghosted')
```

### See Also

CurrentView, ViewNames

---

## ViewDisplayModeId

### Signature

```python
ViewDisplayModeId(name)
```

### Description

Return id of a display mode given it's name

### Returns

guid: The id of the display mode if successful, otherwise None

### Example

```python
import rhinoscriptsyntax as rs
modes = rs.ViewDisplayModes(True)
for mode in modes: print("{} = {}".format(mode, rs.ViewDisplayModeId(mode)))
```

### See Also

ViewDisplayMode, ViewDisplayModes

---

## ViewDisplayModeName

### Signature

```python
ViewDisplayModeName(mode_id)
```

### Description

Return name of a display mode given it's id

### Returns

str: The name of the display mode if successful, otherwise None

### Example

```python
import rhinoscriptsyntax as rs
modes = rs.ViewDisplayModes(False)
for mode in modes: print("{} = {}".format(mode, rs.ViewDisplayModeName(mode)))
```

### See Also

ViewDisplayMode, ViewDisplayModes

---

## ViewDisplayModes

### Signature

```python
ViewDisplayModes(return_names=True)
```

### Description

Return list of display modes

### Returns

list(str|guid, ...): strings identifying the display mode names or identifiers if successful

### Example

```python
import rhinoscriptsyntax as rs
modes = rs.ViewDisplayModes(False)
for mode in modes: print("{} = {}".format(mode, rs.ViewDisplayModeName(mode)))
```

### See Also

ViewDisplayMode, ViewDisplayModeName

---

## ViewNames

### Signature

```python
ViewNames(return_names=True, view_type=0)
```

### Description

Return the names, titles, or identifiers of all views in the document

### Returns

list(str|guid, ...): of the view names or identifiers on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
# Print view names
views = rs.ViewNames()
if views:
 for view in views: print(view)
# Print view identifiers
view_ids = rs.ViewNames(False)
if view_ids:
 for id in view_ids:
 print("{} = {}".format(id, rs.ViewTitle(id)))
```

### See Also

IsView, ViewTitle

---

## ViewNearCorners

### Signature

```python
ViewNearCorners(view=None)
```

### Description

Return 3d corners of a view's near clipping plane rectangle. Useful in determining the "real world" size of a parallel-projected view

### Returns

list(point, point, point, point): Four Point3d that define the corners of the rectangle (counter-clockwise order)

### Example

```python
import rhinoscriptsyntax as rs
rect = rs.ViewNearCorners()
if rect:
 for i in range(4): rs.AddTextDot( i, rect[i] )
```

### See Also

CurrentView

---

## ViewProjection

### Signature

```python
ViewProjection(view=None, mode=None)
```

### Description

Return or set a view's projection mode.

### Returns

number: if mode is not specified, the current projection mode for the specified view number: if mode is specified, the previous projection mode for the specified view

### Example

```python
import rhinoscriptsyntax as rs
views = rs.ViewNames()
if views:
 for view in views: rs.ViewProjection(view,1)
```

### See Also

IsViewPerspective

---

## ViewRadius

### Signature

```python
ViewRadius(view=None, radius=None, mode=False)
```

### Description

Returns or sets the radius of a parallel-projected view. Useful when you need an absolute zoom factor for a parallel-projected view

### Returns

number: if radius is not specified, the current view radius for the specified view number: if radius is specified, the previous view radius for the specified view

### Example

```python
import rhinoscriptsyntax as rs
rhParallelView = 1
views = rs.ViewNames()
if views:
 for view in views:
 if rs.ViewProjection(view)==rhParallelView:
 rs.ViewRadius(view, 10.0)
```

### See Also

IsViewPerspective, ViewProjection

---

## ViewSize

### Signature

```python
ViewSize(view=None)
```

### Description

Returns the width and height in pixels of the specified view

### Returns

tuple(number, number): of two numbers identifying width and height

### Example

```python
import rhinoscriptsyntax as rs
size = rs.ViewSize()
if size:
 print("Width: {} pixels".format(size[0]))
 print("Height: {} pixels".format(size[1]))
```

### See Also

ViewCameraLens, ViewCameraTarget, ViewCPlane, ViewDisplayModes, ViewProjection

---

## ViewSpeedTest

### Signature

```python
ViewSpeedTest(view=None, frames=100, freeze=True, direction=0, angle_degrees=5)
```

### Description

Test's Rhino's display performance

### Returns

number: The number of seconds it took to regenerate the view frames number of times, if successful None: if not successful

### Example

```python
import rhinoscriptsyntax as rs
view = "Perspective"
seconds = rs.ViewSpeedTest(view, 100)
if seconds:
 print("Time to regen viewport 100 times = {} secords".format(seconds))
```

---

## ViewTarget

### Signature

```python
ViewTarget(view=None, target=None)
```

### Description

Returns or sets the target location of the specified view

### Returns

point: is target is not specified, then the current target location point: is target is specified, then the previous target location None: on error

### Example

```python
import rhinoscriptsyntax as rs
view = rs.CurrentView()
target = rs.GetPoint("Select new target location")
if target: rs.ViewTarget( view, target )
```

### See Also

ViewCamera, ViewCameraTarget

---

## ViewTitle

### Signature

```python
ViewTitle(view_id)
```

### Description

Returns the name, or title, of a given view's identifier

### Returns

str: name or title of the view on success None: on error

### Example

```python
import rhinoscriptsyntax as rs
view_ids = rs.ViewNames(False)
for id in view_ids:
 print(id + " = " + rs.ViewTitle(id))
```

### See Also

CurrentView, ViewNames

---

## Wallpaper

### Signature

```python
Wallpaper(view=None, filename=None)
```

### Description

Returns or sets the wallpaper bitmap of the specified view. To remove a wallpaper bitmap, pass an empty string ""

### Returns

str: If filename is not specified, the current wallpaper bitmap filename str: If filename is specified, the previous wallpaper bitmap filename

### Example

```python
import rhinoscriptsyntax as rs
view = rs.CurrentView()
filename = rs.OpenFileName()
if filename and not rs.IsWallpaper(view):
 rs.Wallpaper(view, filename)
```

### See Also

IsWallpaper, WallpaperGrayScale, WallpaperHidden

---

## WallpaperGrayScale

### Signature

```python
WallpaperGrayScale(view=None, grayscale=None)
```

### Description

Returns or sets the grayscale display option of the wallpaper bitmap in a specified view

### Returns

bool: If grayscale is not specified, the current grayscale display option bool: If grayscale is specified, the previous grayscale display option

### Example

```python
import rhinoscriptsyntax as rs
view = rs.CurrentView()
if rs.WallpaperGrayScale(view)==False: rs.WallpaperGrayScale(view, True)
```

### See Also

Wallpaper, WallpaperHidden

---

## WallpaperHidden

### Signature

```python
WallpaperHidden(view=None, hidden=None)
```

### Description

Returns or sets the visibility of the wallpaper bitmap in a specified view

### Returns

bool: If hidden is not specified, the current hidden state bool: If hidden is specified, the previous hidden state

### Example

```python
import rhinoscriptsyntax as rs
view = rs.CurrentView()
if rs.WallpaperHidden(view) == False: rs.WallpaperHidden(view, True)
```

### See Also

Wallpaper, WallpaperGrayScale

---

## ZoomBoundingBox

### Signature

```python
ZoomBoundingBox(bounding_box, view=None, all=False)
```

### Description

Zooms to the extents of a specified bounding box in the specified view

### Returns

None

### Example

```python
import rhinoscriptsyntax as rs
obj = rs.GetObject()
if obj:
 bbox = rs.BoundingBox(obj)
 rs.ZoomBoundingBox( bbox )
```

### See Also

ZoomExtents, ZoomSelected

---

## ZoomExtents

### Signature

```python
ZoomExtents(view=None, all=False)
```

### Description

Zooms to extents of visible objects in the specified view

### Returns

None

### Example

```python
import rhinoscriptsyntax as rs
rs.ZoomExtents()
```

### See Also

ZoomBoundingBox, ZoomSelected

---

## ZoomSelected

### Signature

```python
ZoomSelected(view=None, all=False)
```

### Description

Zoom to extents of selected objects in a view

### Returns

None

### Example

```python
import rhinocriptsyntax as rs
obj = rs.GetObject("Select object", select=True)
if obj: rs.ZoomSelected()
```

### See Also

ZoomBoundingBox, ZoomExtents
---

*Documentation generated from official Rhino3D API*
