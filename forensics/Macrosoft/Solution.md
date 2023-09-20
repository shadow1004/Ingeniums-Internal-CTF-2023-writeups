# Macrosoft

> This PowerPoint presentation is a bit sus ? Im used to pptx extension but what is pptm ?
> I guess i should find out what can this "m" do

File : [MacroSoft.pptm](MacroSoft.pptm)

# Solution

After downloading the file, opening it will give us a powerpoint with 3 slides : 

![bandicam 2023-09-14 18-31-31-695](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/616bdf17-6643-42d9-b26e-052543ce603c)

**As we can notice here it requires permission to enable macros. **

![bandicam 2023-09-14 18-31-37-972](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/80759945-969f-46e7-8799-b80de6f9ed2f)

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
![bandicam 2023-09-12 12-33-22-026](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/c90bb790-03de-493f-89aa-e91449376e22)

2- we can see here the macros we have and their names ( here we have one macro called flag ) 
**But watch out, if the macro was hidden, you will not be able to see it until you go into edit mood and try to add a new macro or smth **
![bandicam 2023-09-12 12-33-52-368](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/43f14efd-49b0-4c1f-98a5-0be32866346e)

3- if we click on it and choose "step into" or "edit" you can see the macro's code : 

![bandicam 2023-09-14 18-49-31-143](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/83bba6e1-4632-461d-aefd-87805928751d)

As we notice the flag is there (I'll explain in linux part why i wrote ingeniums (flag's format ) in a confusing way ).
Running this code - by opening that menu again and click run - will make the flag appear on the slide like this : 

![bandicam 2023-09-12 12-34-09-008](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/4d2172a4-e26d-4d97-b080-0a96615ccf4b)

**Important Notes:**.

1- it's not safe to run the macro's code without knowing exactly what it does as it can be dangerous

2- as you see, macros are also useful in that you can with code create slides and elements and adjust them, etc..

and now let's see how to find the flag with another tool and another way ~

# Using LINUX

**1- u can use the LibreOffice interface as well to check macros code by editing it:**

![Screenshot from 2023-09-20 07-58-13](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/40731a33-b233-4ded-8239-bd16bfe2ec7a)

![Screenshot 2023-09-20 07:59:24](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/a372caa4-fd17-49ff-b009-717fe24de8b2)

![Screenshot from 2023-09-20 08-00-41](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/3f3270a4-9898-40ad-92cc-7f0119106645)


**2- Or, Run this command `olevba MacroSoft.pptm ` <br>**
-ofc after installing required oletools package- and you'll be to able see if there are any macros + their code.

  **Note : PowerPoint files are actually zip files, so if i didnt made the flag format obsfucated, zipping the file and searching with grep may get you the flag as well.**

>Flag: ingeniums{B3_4w4r3_0f_M4lw4r3s}


