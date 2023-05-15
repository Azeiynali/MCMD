# MCMD
## Detalis
---
version: 1.0.0<br>
language: English<br>
Developer: Tarrahchi<br>
Github: https://github.com/Tarrahchi<br>
Defult Username: root<br>
Defult Password: 000<br>
path for data: C:\\Users\\<font color="yellow">[your usernaem]</font>\\McmdTerm
                This project is under development and may not be considered complete at this stage.
### Used Libraries
- prompt-toolkit
- os
- shutil
- subprocess
- zipfile
- hashlib
- sqlite3
- urllib.request
- colorama
- sys
- prompt_toolkit
- prompt_toolkit.completion
- webbrowser
- keyword
- builtins

### <b>Description</b>:
MCMD stands for "Modified Command" and refers to an enhanced version of the Command Prompt environment. It offers additional features and functionality beyond the standard Command Prompt, providing users with an improved command-line interface for executing commands, managing files and directories, and performing various system operations. MCMD aims to enhance productivity and streamline command-line operations, making it a valuable tool for command-line enthusiasts and system administrators.

## Usage
---
### Installation:
1. Execute the setup.py file: Run the setup.py script by executing the command python setup.py in the terminal. This file typically contains instructions for installing dependencies, configuring the project, and performing any necessary setup tasks.

2. By running the __init__.py file, you are launching the final project, initializing its functionality, and making it ready for use. It acts as the central hub that ties together various modules, functions, and configurations, allowing you to access and utilize the project's features and capabilities.

        By executing these two files in order, you ensure that the project is properly initialized and all necessary setup tasks are performed. This allows you to start working with the project in a consistent and configured environment.

        Please ensure that you have executed the setup.py file before attempting to run the project. Failure to do so may result in incomplete project initialization and prevent the project from functioning correctly.

### Commands:
1. clear: clear screen
2. pwd: print current working directory
3. cd: change directory -> cd [directory name]
4. echo: display a line of text
5. ls: list files and directories
6. unzip: extract files from a ZIP archive -> unzip [name.zip]
7. md5en: Calculate and display the MD5 hash value of a file/text -> md5en <tags> [text/file]<br>
tags:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-F: Calculate and display the MD5 hash value of a file
8. create: create a file or directory -> create <tags> [filename/dirname]<br>
tags: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-FL: create a file<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-FO: create a folder<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-O: Open the file for editing immediately after creating it
9. ddir: Removes an directory
10. dfile: Removes an file
11. fle: Opens the fle file editor for editing files. -> fle [filename], fle /command<br>
commands:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fle /history: display opened files history<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fle /clear: clear the history of opened files<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fle /download [pakage_name]: download a package for fle with additional features or functionality <br>
Pakcages:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python: a Python package for intelligent code suggestions and recommendations, improving your Python coding experience.<br>
codes inside the fle:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<save>: a command in fle to save the changes made to the current file, ensuring that the modifications are persisted and the file is updated with the latest changes.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;quit: a command in fle to exit the editor without saving any changes made to the file. It allows you to discard any modifications and close the file without saving.<br>
12. dop: Copies files or directories
13. User: User Control -> User [command]<br>
commands:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;change username<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;change password<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;change default path<br>
14. help: open README.MD
15. py: Executes Python files
16. pip: Executes pip commands
17. move: Move files or directories from one location to another -> move [filename/directoryname] [directory]
18. tar: Executes tar commands

        Caution: The 'tar' command is required to execute the this command. If you do not have 'tar' installed on your system or it is not accessible from the command line, you will not be able to run these commands.
19. download: download files from the web -> download [url] [file_path]
20. 
21. ifcongig: command displays network interface configuration details
22. prompt: Modifies the command prompt in the command line interface.
23. show: display files -> show [file_name] 
24. exit: terminate the current command prompt or console session

## Picture:
The following screenshots are taken after converting the project to an executable (exe) file:
![1](https://lh3.googleusercontent.com/fife/APg5EOZhyQZoxQLHMs-5nsngC4VIsS0OMwI8j4JarZ3oqHWQmwUuWwYgCAqX1PtNhPrEf5TFYS06dJpy9rEPSnNJcm88xcNd2EcpOC1KLLcz9rnX8kAamf-NgHHhBsedYqJeLjZHqG0M2LSZmAk4atTtI-n8pDSYV9GGSPXrQn9K2gwDO4t2bZT0w-K8-L-2iovSl2o4-tkgcAaMIoHJjIgLxM4TzgrjOPmk8_p9p5zIf6PCXId1tm6uTjso-RJBhRxJf6m_7zvQ90jbJnAYm8PS650zHxfw0tc6O0_l-p6PzlcAgla2vOFVbckNehHecs_Bx7ume9LgMlS8GRwjor1uUSxOzeVhOpoVifXQ80KBaxrPEsMbtKdhkYMTyS4Yty5a7rN4lC7rRQ_xUHlIURXOVMr2S3ce1o2e6llvLa3VTOxnZqKEiJrf4fndMoEQH3642fu3sFebBtu8MTjz6vkkoQ6P7wD9cLhLjoGqfk793t5gsWfzIb-cHQKOFLDMKqNyeD_V_6SBPJkGUoFoaHTlnq9RGRmhXcI0u-_UG0NIn2dxVQV3DKSmnol3o52pGpzrAqJzy7kZui-rp3_mGJ1NFCxP6ulC1Q1s8_0K7kmGVE9JSWj1zMMwreerjBiHsjiDT8G1oqa0CacqB76LNAHswkd3OCBbz8by7O6u42iFWLpEGD6rylbJwYTvCwRZxE8C22DLqfUL73Dh9Feq8yiFTzt-mf6KLXYnmNWyl0ICzhgpLvE0ribWPvEDwDYSG2OahVCUBVJfLoIEG2ZonwRncVd-s70qUWWvgrti8hhYBrCRk6wYXIYTsV6npsiGvh-0ARqCusq2EHlKEr5Pj5d4lSF1iWF8UHzFbBFctYYS-PwcgACjMrGqqz3gaGIUXEv_vXoP3b1G9RJ2VXuHqDwZ6yGtwEnWpQxwCaKQ3MX-nG_Yh9enzMFU7AEyqQEQMAeD458frnIkT2PJu7YSoIuBX15QdUfEbjp_Owf8RW9fNooMBup-y0cuGVGFo3nS1AQyR1uy9VqesFXPNcbeaZIL7NivxOoV3rbgy1wFYeqJHBO_8-ZRc19hMA-q81Zhe7rQR1t9Q9KtCC51OrHpsC5MMaACSUt6zdFidcn4Ym2CHyGCj0Aq0rfKCSzCOftItSmm8YOvR_VjHEqRzquRgY1Fai-Q_8lkJXopaZlBp74velTbc1Jfnb0NSdwekePA8z36CJCxLeTFMe2h77pjc-OJIRC01cgHJOttX2Z2pLpUdxXcwGSVIp76urKh_qDub1W9bLD1OzogOd2P6Ue-1CO4mEGvlYTRwMVUNMwqqGmAkDa3ZN8iHB11RqIzoZIQDLHpW1QKQh8Zu-7ahktO0pqbNBO25e9L_RC67_iG1qY5PeyemxatuWc9InInJdWH8nOCj404T3-XxV95tdELdu9_7GDMtskMlJ03H-WhsxMYky1OO3WwkhY7deLr9P15CfzFQ3pJ0IlK9Fss7pThchpUqUeDIPl_ckiXC1j1O2uIJuUxguZrK6hlUFFOi6Rb3f0=w1366-h615)
![2](https://lh3.googleusercontent.com/fife/APg5EOZImuSRnAAk4lhEppKJxPrNrUi330icw3m0I1bE-KokayzxxAuHGk5-fzJymc_voux3uGKPc9JwSc9I17pDuCh91Y9_g57-xfUyZicDWzFd2gyTufCMddG71I45J6bhL8GcGu9SrUFG1cihwFFXp1DxfNRzspt44A5zPb4OECXcOavDjzkC-f5heBnvve4gqvjX4JXtfu2dfttvALiGvwgG28x2rZ4VX31gtcGvMmsSCZ-nhGL0wVwgYwLLu0tp5ArrfKGbAIXHsywgVYm09Cw5lIlQUkEMMKBY3zgODmd8Zj80EEKiz9n1QT6iIs89E1eskEJsZukXD7D66U2sSb6VC8ts9yZT-N5CDQn6DwZvHyefVY0mGH1GXLrxlMb35lq1GRySSoqXDeieE3pHRcaRVccIss5wYEzXOeEdWPmUdDiSJ2fI3UKMPE7Yf8FGcGSFqTtMp6kvjfH3i4GSP3P3yFN9dxnOSwvWd2HSd4aBXCSI5VYhwbQN6UmZj-8kUvLoDCTZq4exTzMjUWrxA6iqrW-c7IIy52B0KeEb75gksZHxZiEpHluLOvDE8iEvwEK8xSYSVkK0c0_bXYNkQpj3Kzbh3-jFY-6wTlLV5pvHc1B1yWksI8Hxk6jmn7NehP3C7XJwqxsqDk9hvk5C2xyP9ODzqITtGuE-C57x1LJ1U9t3raf3cw-Pb-rRA0eftR65VpZSONVrLkEEy2BLjZi1139FuOak_92PX5Bv3bIR5P2mJD8B_3YfR2Cq47KV4l4TLSCeGkbWY5BP0w4ri8aLNpeO93CrynIu7ryBum1iA0rFFASQs--AlXfZx51eNLyOsAO32xxsXcqIP2O5MJRQcxpNYYGBiNFcJzh9HVFxN-MMuBebwKjnojYFmVpHi8zxdOTn2c4VmXxvvCGQeTtojMFKp0fg-D3BBKqKVZ2qER1ub9HBAQ6l3DpV0lTXvI9bhB3gKjw45tM74y9VGxWaeABhmu1kUefiErPsqzG3XaJrXRnBWWK4b_GC5QexGfyZ8bPZWulfvoppxlqiARxWEKPVkK3mwbzCncvDjVUVwHuqCB5Dv_q8fQVRf-1g6O4RfVhb8Mv_SPHHZVuX2qA7U98xcUko6vCJvtbtDwSlPOdo4EwLgNBDlB0U4nkboz3pkOdSHBMKDVCAg0RmJ8CRBCR0ttHwdn4GEWI5E-ZGry_K4BCECbjwu9k2gzMUSq6gyH4QQBPBfx3OlcuMCLW6Wa4dfDh5C1K3_dk_Ov7GkXLUdKYTPoPs892vjm6mPXx_ptNIoN-u1ejV2AHgwjfjg831LVTY4bZDeKL0nNR12hghiFPArLuzw13ZGjKp54SQltIEyEpRlYmuMOaHY00jF8wQ4zi846Zb1IYlyfPQIJevNvRdONg0jRyjNym1GmqEP_xkbzDC2vYE2pWUZOxIvGgSSfGQ1rF4Wog5TA-9hH9kAloKgf8Fd7wfDCVGPv_JxeUkcz0AT07p4O7d999WvIpy876kY2IXC95ZiGncvRU-iY4D51UTeLB025c=w1366-h295)
![3](https://lh3.googleusercontent.com/fife/APg5EOY1G-5VTgHb_tOZXez5uChDX8-HCmAVYDfQ6xBCiDOevqBXveBk4s1Nut7cEGSfKiK3BUdn0ZzUEaYDKtEQqvIqLHO60G2d4Bnlawy_xd9K_LdtG5M1WLhuN6wYRNOpHAgf6m6A5tNlspJtnc5OaSKYMO4fe50bTzHC15d9k05rsvNknx_X5P_ISkTV2tqeE9Xci2qEFv1ghGHjsY2h-25jpXIhBtvQiIEJwv3DrmCRIBL2B_Rq3UYsScP2ji2LkwWKw3YAWPYg-yirpRtqiaEFN_im9y6brIaZBlkYO3cgOoYmQ6jcWXjRslgf9tsJuNGigoQeusNZ-9a02O-BVeVWdH-KEZg4iNm_7Fc-Dmnj-V49l2EAG5jC33ljFBdEZxf-5O38fLEp4ruacLxj5lnhF0rXIaj2-KFv6E4Y1QOzARpxfXsNSqBtYZJySMIiKqSU8e1xMnqLgc2uoTJc1ezu7Ka9MhGPecb9-J5U2t2yUFN35fkriPwcvuxVLdKpxrnD7--CA72vbzUSXOM_zZP4bM1z1-7WOchkEMSlwbY72ypshg9bN1UW0WpSmeWLKBcGN6rCbXSI8V9pvX6CPgHNJfkJwZn7VB3wq3vbjD1BacVzcLRGj7pCf9U5HW9fv3eTy6OG3hAfJKEahMTiI-I9Rpx1hM3xe2PLOkScQvPeliTus5reqBstljwuZ8mua6xSd-niEYa7-TXhcm_jUAPukFyZoIou_72IAJXPm_C1yRmTYieQEKsKOOD13OfwMUSeb5cTF2wtyGp8DlSC1XcjHlTwt4h79Cs5RaoVnE-RV5dn_KCidyxwsTDh0T4_b7cOvgGTYYM57WoKPAU5wivVnUMn6SbGnetQUlr7sj-_fLoAD8rjTCRKMcb3jQ2lItCuRaw1AkS9Vtp54Aab3eslPrTMUdAQrFpaedW7Pfu8H5dmBfJdxlWrDavsaiw0U_G86ujgRW5S2D9Y5PaHemzIXoJMqQN6WiEuWNi-eWzeNvnjsng0IAHg-xlVWysLIWkY9HlBcJpeNgFuMWRtQ7DYY8MLHkABBRYAe-t-8Px4tDu3aJXTLC5s-NjnN6FMueXRwIPCZF9pl61hYcwfbIpFPl4MpAS6mFCYEeMULqsQRu2atsh6m1-Ibhe_LuWf-MfblCVkF1CdUu2UBfgS0K2_Z0WK2Oh26LQSPJAcAmy7dmIYktyYo8zcYXNyCpY-WQd0PT6ktHLCotOuWa-ADl19JqSIkUBUxEFtRZnyjUulVMcF-qcLtqiLoH0kSOAcdx-Tz3UZWJrICwvGRr9cYGpMj7npcy1M6A7D5kIvBuwEaD6EHQ37ERMcw1v28T_388mIKKl3T1qLfosZtCR45ecOvbcQ7ZbTDzK_oBkv7Rn2m6Dn6bLqnCv9UHgCx_vdboR-0Y1xevNrfLsgfd4wbLXH8UKHbZZl6SWOQsNgb21G1-liMMzm5ZbfRuEgJqidKIVJGSqRf3UlQGKAKLgS7_5IpXNO3B2DMI82xKTqG1cLYJlbqgil2IL5iYz41GU=w1366-h411)