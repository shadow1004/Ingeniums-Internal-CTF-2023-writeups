# Sh4d0w5

>  someone sent me this video.. looks like he has a good editing skills but, i can see some shadows here and there? Could u use ur commands to make sure that the video is safe ?

File : [Sh4d0w5.zip](Sh4d0w5.zip)

# Solution

so after unzipping we'll have a video that contains ingeniums logos, there is some shadows of qr code frames in it but it's hard
to get it directly from the video so as the description says, we'll use a command : 'ffmpeg' 

create a new directory and move the video to it then run this : 

`ffmpeg -i Sh4d0w5.mp4 output_frame_%04d.png`

you'll have about ~ 1200 frames from the video 
diving through them u'll find 4 frames : 

 frame 1 : 
 
![output_frame_0133](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/d7022e34-3187-47c7-8c57-fd8f2bf54958)

frame 2 :

![output_frame_0308](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/636db5da-84fe-4c8c-b284-59376ea0f954)

frame3:

![output_frame_1150](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/10f3aa14-bd51-4a9a-9447-3b67d26a870b)

frame4:

![output_frame_1208](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/70b48874-7c43-4ce3-9bd2-b54e12995e79)

Assemble it with any simple pics editor to have the full qr code : 

![frame](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/c7a2b2a8-5de2-4f65-b05f-af334bbe4b98)

Scan it then you'll get the flag ! 

> Flag : Ingeniums{Y0u_H4v3_70_Lo0k_Cl053R}
