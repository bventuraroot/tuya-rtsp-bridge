' Hidden backend. No console.
Option Explicit
Dim sh, fso, root, pythonw, server, http
Set sh = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
root = fso.GetParentFolderName(WScript.ScriptFullName)
sh.CurrentDirectory = root
sh.Environment("PROCESS")("TUYA_BRIDGE_ROOT") = root
sh.Environment("PROCESS")("PATH") = root & "\bin;" & root & "\vlc;" & sh.Environment("PROCESS")("PATH")

pythonw = root & "\runtime\pythonw.exe"
If Not fso.FileExists(pythonw) Then pythonw = root & "\runtime\python.exe"
If Not fso.FileExists(pythonw) Then pythonw = root & "\.venv\Scripts\pythonw.exe"
If Not fso.FileExists(pythonw) Then pythonw = root & "\.venv\Scripts\python.exe"
If Not fso.FileExists(pythonw) Then WScript.Quit 1

On Error Resume Next
Set http = CreateObject("MSXML2.ServerXMLHTTP.6.0")
If http Is Nothing Then Set http = CreateObject("MSXML2.XMLHTTP")
http.Open "GET", "http://127.0.0.1:8787/api/state", False
http.setRequestHeader "Cache-Control", "no-cache"
http.Send
If Err.Number <> 0 Or http.Status <> 200 Then
  Err.Clear
  server = root & "\src\server.py"
  sh.Run """" & pythonw & """ -u """ & server & """", 0, False
End If
