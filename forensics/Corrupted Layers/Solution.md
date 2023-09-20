# Corrupted Layers 

> description : my files got into a fight ! you have a lot of things to fix here mate, but always remember,
>  everyone will be better when they return to their origins, and then maybe, separated parts may reconnect!

File : [here](;)

# Solution

In this challenge we'll be needing : <br>
1- Linux general skills <br>
2- Some steganography tools <br>

First of all : most of the file names were named a weird names so that, running commands on terminal will be harder :D
for this it's recomended to use files names betwen "" or '' .

After downloading the file, we'll run bunch of commands to know the type of file, extract it etc, commands are:

![Screenshot from 2023-09-20 06-46-29](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/032f5f28-d67e-4b74-b6c1-efb5fa13883f)

As we see we got this pic where colors seem 
let's use the tool [stegsolve](https://wiki.bi0s.in/steganography/stegsolve/) to examine it ! :

![Screenshot from 2023-09-20 06-50-30](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/ecbff190-56f4-49f7-81b0-c25a29042e32)


![Screenshot from 2023-09-20 06-50-35](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/0338078e-a75e-4d3a-9c7e-0b82de0431bb)

![Screenshot from 2023-09-20 07-13-13](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/a110f4ac-7825-460a-909e-7871149efb47)

As we see here's a flag : **ingeniums{Gr34t_W0** but it seems uncompleted ?? <br>
Back to description's last sentence : `separated parts may reconnect!` we understand that the flag actually is splitted on 2 parts.
And in the first screenshot ( while extracting the fixMe file ) we notice the line fixMe/.png so **There is another file!** <br>
This file is hidden so we have to run `ls -a` to see it.

![Screenshot from 2023-09-20 06-56-11](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/2bca5def-376e-4bb2-b6e2-eee630617265)


As you can see trying to open it says it's not a png actually, running the command `file`

![Screenshot from 2023-09-20 06-56-43](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/75dbc74d-90c3-4596-9f05-4c28ea7df855)

It's a zip file then! and unzipping it doesnt work too, it's Corrupted!
trying to check the file's header by running `hexedit`: 
![Screenshot from 2023-09-20 06-56-59](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/9583b9ea-74b9-4e91-9320-721974403301)

As we notice the "FixMe", we need to fix the header with the correct magic bytes of a zip file ! `50 4B 03 04`
[Here](https://en.wikipedia.org/wiki/List_of_file_signatures) You can find magic bytes/signatures of many type of files ! <br>

After saving the file we get a new file called '--help' ; and running that on terminal will be so hard we can't even rename it and the "" and '' doesnt work ! <br>
So we have to just do that manually from the files.

Opening the file we get a [BrainFuck](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjS9Pncw7iBAxVbUaQEHeV5BlAQFnoECBMQAw&url=https%3A%2F%2Ffr.wikipedia.org%2Fwiki%2FBrainfuck&usg=AOvVaw2E5QhUa_jDfKbm99ifKbnT&opi=89978449) code.<br>
Decrypting that in any online tool will give us the other part of the flag! : K_M4sT3r_FiX3r}.

> Flag : ingeniums{Gr34t_W0rK_M4sT3r_FiX3r}



