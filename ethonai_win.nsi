!include "MUI2.nsh"

!define MUI_PRODUCT "SkymelChat"
!define MUI_BRANDINGTEXT "SkymelChat"

#!define MUI_ICON  "graphics\SkymelChat_installer.ico"
#!define MUI_UNICON  "graphics\SkymelChat_installer.ico"
#!define MUI_HEADERIMAGE
#!define MUI_HEADERIMAGE_BITMAP "graphics\installer_bar.bmp"
#!define MUI_VERSION "$%OKP_VERSION%"
!define /date MUI_VERSION "%y.%m.%d.%H%M"

Name "${MUI_PRODUCT} - Installer"
Outfile "${MUI_PRODUCT} ${MUI_VERSION} Installer.exe"
ShowInstDetails "nevershow"
ShowUninstDetails "nevershow"

InstallDir "$PROGRAMFILES\${MUI_PRODUCT}"
InstallDirRegKey HKCU "Software\${MUI_PRODUCT}" ""
;RequestExecutionLevel user

!define MUI_ABORTWARNING

!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

!insertmacro MUI_LANGUAGE "English"

VIProductVersion "${MUI_VERSION}"
VIAddVersionKey /LANG=${LANG_ENGLISH} "ProductName" "${MUI_PRODUCT} - Installer"
VIAddVersionKey /LANG=${LANG_ENGLISH} "FileDescription" "${MUI_PRODUCT} - Installer"
VIAddVersionKey /LANG=${LANG_ENGLISH} "FileVersion" "${MUI_VERSION}"

Section "install" Installation

    SetOutPath "$INSTDIR"
      File /r "dist\windows\SkymelChat\*.*"

    SetShellVarContext all
    CreateShortCut "$DESKTOP\${MUI_BRANDINGTEXT}.lnk" "$INSTDIR\${MUI_BRANDINGTEXT}.exe" ""

    CreateDirectory "$SMPROGRAMS\${MUI_BRANDINGTEXT}"
    CreateShortCut "$SMPROGRAMS\${MUI_BRANDINGTEXT}\Uninstall.lnk" "$INSTDIR\Uninstall.exe" "" "$INSTDIR\Uninstall.exe" 0
    CreateShortCut "$SMPROGRAMS\${MUI_BRANDINGTEXT}\${MUI_BRANDINGTEXT}.lnk" "$INSTDIR\${MUI_BRANDINGTEXT}.exe" "" "$INSTDIR\${MUI_BRANDINGTEXT}.exe" 0

    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${MUI_PRODUCT}" "DisplayName" "${MUI_PRODUCT} (remove only)"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${MUI_PRODUCT}" "UninstallString" "$INSTDIR\Uninstall.exe"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${MUI_PRODUCT}" "DisplayVersion" "${MUI_VERSION}"

    WriteUninstaller "$INSTDIR\Uninstall.exe"

SectionEnd

Section "Uninstall"

    DeleteRegKey HKEY_LOCAL_MACHINE "SOFTWARE\${MUI_PRODUCT}"
    DeleteRegKey HKEY_LOCAL_MACHINE "SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\${MUI_PRODUCT}"

    RMDir /r "$INSTDIR\*.*"
    RMDir "$INSTDIR"

    SetShellVarContext all
    Delete "$DESKTOP\${MUI_BRANDINGTEXT}.lnk"
    Delete "$SMPROGRAMS\${MUI_BRANDINGTEXT}\*.*"
    RmDir "$SMPROGRAMS\${MUI_BRANDINGTEXT}"

SectionEnd

Function .onInit

  ReadRegStr $R0 HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${MUI_PRODUCT}" "UninstallString"
  StrCmp $R0 "" done

  IfSilent 0 +4
    ExecWait '"$INSTDIR\Uninstall.exe" /S _?=$INSTDIR'
    RMDir /r "$INSTDIR\*.*"
    RMDir "$INSTDIR"

  IfSilent +4
    MessageBox MB_OKCANCEL|MB_ICONEXCLAMATION "${MUI_PRODUCT} is already installed. $\n$\nClick `OK` to remove the previous version or `Cancel` to cancel this update." IDOK uninst

  Abort

uninst:
  ClearErrors
  ExecWait '"$INSTDIR\Uninstall.exe" /S _?=$INSTDIR'
  RMDir /r "$INSTDIR\*.*"
  RMDir "$INSTDIR"

  IfErrors no_remove_uninstaller done
  no_remove_uninstaller:

done:

FunctionEnd
