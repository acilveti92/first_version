#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.





#t::
	If WinExist("ahk_exe chrome.exe"){
		winactivate ahk_exe chrome.exe
		Send ^t	
		}	
		
	else
		run, "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
		WinWait ahk_exe chrome.exe
		WinActivate ahk_exe chrome.exe
		WinWaitActive ahk_exe chrome.exe
Return



^b::
	
	Send ^c
	If WinExist("ahk_exe chrome.exe"){
		winactivate ahk_exe chrome.exe
		Send ^t
		Send ^l
		Send ^v
		Send {Enter}
		
			
		}	
		
	else
		run, "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
		WinWait ahk_exe chrome.exe
		WinActivate ahk_exe chrome.exe
		WinWaitActive ahk_exe chrome.exe
		Send ^l
		Send ^v
		Send {Enter}
Return

!a::
	CoordMode, Mouse, Screen
	MouseMove, (A_ScreenWidth // 2), (A_ScreenHeight // 2)
return

CoordMode, Mouse, screen ; relative to screen not window
return

!s::
mousegetpos,x,y
return

!z::
mousemove,%x%,%y%
return
	










#r::
	IfWinExist ahk_exe SnippingTool.exe
		winactivate ahk_exe SnippingTool.exe
	else
		run, "C:\Windows\System32\SnippingTool.exe"
		WinWait ahk_exe SnippingTool.exe
		WinActivate ahk_exe SnippingTool.exe
		WinWaitActive ahk_exe SnippingTool.exe
Return

#c::
	IfWinExist ahk_exe chrome.exe
		winactivate ahk_exe chrome.exe
	else
		run, "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
		WinWait ahk_exe chrome.exe
		WinActivate ahk_exe chrome.exe
		WinWaitActive ahk_exe chrome.exe
Return

#s::
	IfWinExist ahk_exe spotify.exe
		winactivate ahk_exe spotify.exe
	else
		run, "C:\Program Files (x86)\Spotify\spotify.exe"
		WinWait ahk_exe spotify.exe
		WinActivate ahk_exe spotify.exe
		WinWaitActive ahk_exe spotify.exe
Return

#v::
	IfWinExist ahk_exe evernote.exe
		winactivate ahk_exe evernote.exe
	else
		run, "C:\Program Files (x86)\Evernote\Evernote\evernote.exe"
		WinWait ahk_exe evernote.exe
		WinActivate ahk_exe evernote.exe
		WinWaitActive ahk_exe evernote.exe
Return





#x::
	IfWinExist ahk_exe designspark.exe
		winactivate ahk_exe designspark.exe
	else
		run, "C:\Program Files (x86)\DesignSpark\DesignSpark PCB 8.0\designspark.exe"
		WinWait ahk_exe designspark.exe
		WinActivate ahk_exe designspark.exe
		WinWaitActive ahk_exe designspark.exe
Return






^Escape::
	PostMessage, 0x112, 0xF060,,, A     ; ...so close window        
        Return
	



$Escape::                                               ; Long press (> 0.5 sec) on Esc closes window - but if you change your mind you can keep it pressed for 3 more seconds
    KeyWait, Escape, T0.5                               ; Wait no more than 0.5 sec for key release (also suppress auto-repeat)
    If ErrorLevel                                       ; timeout, so key is still down...
        {
            KeyWait, Escape, T3                         ; Wait no more than 3 more sec for key to be released
            If !ErrorLevel                              ; No timeout, so key was released
                {
                    PostMessage, 0x112, 0xF060,,, A     ; ...so close window        
                    Return
                }
                                                        ; Otherwise,
            KeyWait, Escape                             ; Wait for button to be released
                                                        ; Then do nothing...
            Return
        }
        
    Send {Esc}
 Return






