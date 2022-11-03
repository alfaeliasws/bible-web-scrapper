#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%

; Bible Quick
F1 & 5::
Run "E:\<path>\new"
return

F1 & 6::
Run "E:\<path>\old"
return

F1 & 7::
Run "E:\<path>\main"
return

F2 & 5::
Run "E:\<path>\rollback-new"
return

F2 & 6::
Run "E:\<path>\rollback-old"
return

F2 & 7::
Run "E:\<path>\rollback-main"
return