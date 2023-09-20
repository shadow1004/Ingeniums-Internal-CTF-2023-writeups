# Macrosoft

> This PowerPoint presentation is a bit sus ? Im used to pptx extension but what is pptm ?
> I guess i should find out what can this "m" do

File : [MacroSoft.pptm](MacroSoft.pptm)

# Solution

After downloading the file, opening it will give us a powerpoint with 3 slides : 

![bandicam 2023-09-14 18-31-31-695](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/2d53f6a9-f0fb-4e3e-aea2-e91035bfc5a4)

**As we can notice here it requires permission to enable macros. **

![bandicam 2023-09-14 18-31-37-972](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/680a2e1d-7964-409a-aa8a-175d8ea3d381)

**The slides are talking about macros, and so is the title of the challenge kinda** 
**So, what are macros?**

In Microsoft Teams (word,excel,powerpoint..etc), macros are a way to **automate repetitive tasks** and processes within the application. They allow you to create custom scripts or sequences of actions that can be triggered with a single command or button click.
Means;like any **script, macros can perform actions on behalf of the user** who triggers them.
So, giving permission to enable macros of an external file -that you don't trust its author' can pose security risks as it may contain embedded/hidden macros that **may contain malicious code.**
Usually u can write macros with Visual Basic for Applications (VBA) language.
**And thats why our file's extention was pptm, the "m" means the file may execute macros!**

You can read/search about that topic more

So now that we understood this part, we know where to search ' in macros obviously lol ' so we have 2 ways to do this :

# Using WINDOWS

you can directly access the macros from the PowerPoint interface : 

1- click on view, then click on Macros
![bandicam 2023-09-12 12-33-22-026](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/294a0d67-8df4-41dd-8a0d-59c7b8634586)

2- we can see here the macros we have and their names ( here we have one macro called flag ) 
**But watch out, if the macro was hidden, you will not be able to see it until you go into edit mood and try to add a new macro or smth **
![bandicam 2023-09-12 12-33-52-368](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/f4ffa3d0-227b-4eb0-941a-add372cf159d)

3- if we click on it and choose "step into" or "edit" you can see the macro's code : 

![bandicam 2023-09-14 18-49-31-143](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/6ee74280-2638-445c-9f86-65b5fc4181fc)

As we notice the flag is there (I'll explain in linux part why i wrote ingeniums (flag's format ) in a confusing way ).
Running this code - by opening that menu again and click run - will make the flag appear on the slide like this : 

![bandicam 2023-09-12 12-34-09-008](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/b90ecdfd-8cb1-480b-8d30-ffff4a181e9c)

**Important Notes:**.

1- it's not safe to run the macro's code without knowing exactly what it does as it can be dangerous

2- as you see, macros are also useful in that you can with code create slides and elements and adjust them, etc..

and now let's see how to find the flag with another tool and another way ~

# Using LINUX

**1- u can use the LibreOffice interface as well to check macros code by editing it:**

![Screenshot from 2023-09-20 07-58-13](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/7aaf3133-a5d9-463e-8aff-a32588481be5)

![Screenshot 2023-09-20 07:59:24](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/eefa1241-ab66-417f-8c80-33bc254c7807)

![Screenshot from 2023-09-20 08-00-41](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/25d5b61f-9fbd-4356-beab-04baca2b3ad3)


**2- Or, Run this command `olevba MacroSoft.pptm ` <br>**
-ofc after installing required oletools package- and you'll be to able see if there are any macros + their code.

  **Note : PowerPoint files are actually zip files, so if i didnt made the flag format obsfucated, zipping the file and searching with grep may get you the flag as well.**

>Flag: ingeniums{B3_4w4r3_0f_M4lw4r3s}


