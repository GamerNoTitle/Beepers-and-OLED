Set fs =CreateObject("scripting.filesystemobject")
Set gs =CreateObject("scripting.filesystemobject")
Set f=fs.opentextfile("All.py",1,true) 'Test.txt是要分割的txt文件
n=0
do while f.atendofstream<>true
n=n+1
data=""
Set g=gs.opentextfile(CStr(n)+".py",2, true) '分割后的文件保存为：1.txt 2.txt 3.txt……
if f.atendofstream<>true then
for a=1 to 100000 '分割后，一个文件保存100000行，空白行同样算一行。
data=f.readline
g.writeline data
next
end if
loop
f.close
g.close
pause