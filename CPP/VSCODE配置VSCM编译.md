本文参考https://www.i4k.xyz/article/qq_34801642/105453161

# 环境变量设置
```
//在Path中添加cl.exe所在文件夹路径。若未找到，直接VS的安装目录下搜索cl.exe即可
C:\Program Files\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.16.27023\bin\Hostx86\x86;

//在系统变量中新建变量INCLUDE，添加cl.exe的包含目录
C:\Program Files\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.16.27023\include;
C:\Program Files\Windows Kits\10\Include\10.0.17763.0\shared;
C:\Program Files\Windows Kits\10\Include\10.0.17763.0\ucrt;
C:\Program Files\Windows Kits\10\Include\10.0.17763.0\um;
C:\Program Files\Windows Kits\10\Include\10.0.17763.0\winrt;

//在系统变量中新建变量LIB，添加cl.exe的库目录
C:\Program Files\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.16.27023\lib\x86;
C:\Program Files\Windows Kits\10\Lib\10.0.17763.0\um\x86;
C:\Program Files\Windows Kits\10\Lib\10.0.17763.0\ucrt\x86;
```

# Lanch.json
```
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "cl.exe - 生成和调试活动文件",
            "type": "cppvsdbg",
            "request": "launch",
            "program": "${fileDirname}\\${fileBasenameNoExtension}.exe",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": false,
            "preLaunchTask": "cl.exe build active file"
        }
    ]
}
```

# tasks.json
{
    "tasks": [
        {
            "type": "shell",
            "label": "cl.exe build active file",
            "command": "cl.exe",
            "args": [
                "/Zi",
                "/EHsc",
                "/Fe:",
                "${fileDirname}\\${fileBasenameNoExtension}.exe",
                "${file}"
            ]
        }
    ],
    "version": "2.0.0"
}