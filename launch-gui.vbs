' Start the desktop GUI with no console window.
Option Explicit
Dim sh, fso, root, pyw, gui
Set sh = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
root = fso.GetParentFolderName(WScript.ScriptFullName)
sh.CurrentDirectory = root
sh.Environment("PROCESS")("TUYA_BRIDGE_ROOT") = root
sh.Environment("PROCESS")("PATH") = root & "\bin;" & root & "\vlc;" & sh.Environment("PROCESS")("PATH")
If fso.FolderExists(root & "\vlc\plugins") Then
  sh.Environment("PROCESS")("VLC_PLUGIN_PATH") = root & "\vlc\plugins"
End If

pyw = ""
If fso.FileExists(root & "\runtime\pythonw.exe") Then
  pyw = root & "\runtime\pythonw.exe"
ElseIf fso.FileExists(root & "\.venv\Scripts\pythonw.exe") Then
  pyw = root & "\.venv\Scripts\pythonw.exe"
ElseIf fso.FileExists(root & "\runtime\python.exe") Then
  pyw = root & "\runtime\python.exe"
ElseIf fso.FileExists(root & "\.venv\Scripts\python.exe") Then
  pyw = root & "\.venv\Scripts\python.exe"
End If
If pyw = "" Then
  sh.Run """" & root & "\launch.bat""", 1, False
  WScript.Quit 0
End If
gui = root & "\src\gui.py"
sh.Run """" & pyw & """ -u """ & gui & """", 0, False
