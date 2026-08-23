#define MyAppName "Tuya RTSP Bridge"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Tuya RTSP Bridge contributors"
#define MyAppURL "https://github.com"

[Setup]
AppId={{A7C3E91F-4B2D-4F11-9C08-7E2B91C4D001}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
DefaultDirName={localappdata}\Programs\TuyaRtspBridge
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
LicenseFile=..\LICENSE
OutputDir=output
OutputBaseFilename=TuyaRtspBridge-Setup
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
ShowLanguageDialog=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "german"; MessagesFile: "compiler:Languages\German.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"

[Files]
Source: "..\src\*"; DestDir: "{app}\src"; Flags: ignoreversion recursesubdirs; Excludes: "__pycache__\*,*.pyc"
Source: "..\web\*"; DestDir: "{app}\web"; Flags: ignoreversion recursesubdirs
Source: "..\vendor\tuya-ipc-terminal\*"; DestDir: "{app}\vendor\tuya-ipc-terminal"; Flags: ignoreversion recursesubdirs
Source: "..\bin\tuya-ipc-terminal.exe"; DestDir: "{app}\bin"; Flags: ignoreversion
Source: "..\launch.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\launch-hidden.vbs"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\requirements.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\LICENSE"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\DEPENDENCIES.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\README.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\README.de.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\SECURITY.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\CONTRIBUTING.md"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Tuya RTSP Bridge"; Filename: "{app}\launch.bat"; WorkingDir: "{app}"
Name: "{autodesktop}\Tuya RTSP Bridge"; Filename: "{app}\launch.bat"; WorkingDir: "{app}"; Tasks: desktopicon

[Run]
Filename: "{app}\launch.bat"; Description: "Start Tuya RTSP Bridge"; Flags: nowait postinstall skipifsilent shellexec

[Code]
procedure CurStepChanged(CurStep: TSetupStep);
var
  LangFile: string;
begin
  if CurStep = ssPostInstall then
  begin
    LangFile := ExpandConstant('{userappdata}\TuyaRtspBridge\config.json');
    ForceDirectories(ExtractFilePath(LangFile));
    if ActiveLanguage = 'german' then
      SaveStringToFile(LangFile, '{' + #13#10 + '  "lang": "de"' + #13#10 + '}', False)
    else
      SaveStringToFile(LangFile, '{' + #13#10 + '  "lang": "en"' + #13#10 + '}', False);
  end;
end;
