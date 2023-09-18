# Noted

> "taal se taal mila" ~~ this song is one of my fav! taal in indian means melody ~ looks like it contains a Meta-message behind the lyrics.. <br>
last OCTober i downloaded this audio file to listen to the song but it looks like the notes r a bit weird ?
could u discover what's happening here ?

File : Oct-taal se taal mila.wav

# Solution 

So we have plenty of hint in description..
"Meta-message" make us checking the metadata of the file ( for exemple `exiftool` ) :

![Screenshot from 2023-09-18 17-40-33](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/7dec736b-2f56-4c8f-931d-51cd771a9a11)

We have a hint in the comment section : "there is something about the notes .. try to use a better audio tool to discover more !
". <br>
We have the known software for audio analyse : **Audacity.**

![Screenshot from 2023-09-18 17-44-49](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/8af531e6-816e-47dd-9cf7-3dd936d874cf)


As we see there is nothing special in the waves so let's recheck the specific meta data here : 

![Screenshot 2023-09-18 17:54:33](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/dad553a4-c35c-4013-94b0-e043e0df3fe0)

![Screenshot from 2023-09-18 17-54-49](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/35568904-30b4-4782-a859-9b0f3ec37e43)

There are some "notes" or numbers in **Track number** section,
and the file name called "Oct-tal" and the numbers are on 3 digits each so,
decrypting these notes from octal will give us the flag ! 

>Flag: ingeniums{Do_Re_mI_you_got_me}

