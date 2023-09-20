# Noted

> "taal se taal mila" ~~ this song is one of my fav! taal in indian means melody ~ looks like it contains a Meta-message behind the lyrics.. <br>
last OCTober i downloaded this audio file to listen to the song but it looks like the notes r a bit weird ?
could u discover what's happening here ?

File : Oct-taal se taal mila.wav

# Solution 

So we have plenty of hint in description..
"Meta-message" make us checking the metadata of the file ( for exemple `exiftool` ) :

![Screenshot from 2023-09-18 17-40-33](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/d35e8331-34b8-40b3-9b9a-bf09851ab896)


We have a hint in the comment section : "there is something about the notes .. try to use a better audio tool to discover more !
". <br>
We have the known software for audio analyse : **Audacity.**

![Screenshot from 2023-09-18 17-44-49](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/6d0629b3-6c8d-452f-bd34-b0671c0d207d)

As we see there is nothing special in the waves so let's recheck the specific meta data here : 
![Screenshot 2023-09-18 17:54:33](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/d3fab4b7-f68d-49ee-8350-95f1e3a51ff1)

![Screenshot from 2023-09-18 17-54-49](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/410d5524-1455-44c6-ada4-bdd7d69c70b8)



There are some "notes" or numbers in **Track number** section,
and the file name called "Oct-tal" and the numbers are on 3 digits each so,
decrypting these notes from octal will give us the flag ! 

>Flag: ingeniums{Do_Re_mI_you_got_me}

