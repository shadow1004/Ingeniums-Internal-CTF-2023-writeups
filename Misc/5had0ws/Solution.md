# Sh4d0w5

>  someone sent me this video.. looks like he has a good editing skills but, i can see some shadows here and there? Could u use ur commands to make sure that the video is safe ?

File : [Sh4d0w5.zip](Sh4d0w5.zip)

# Solution

So after unzipping we'll have a video that contains ingeniums logos, there is some shadows of qr code frames in it but it's hard
to get it directly from the video so as the description says, we'll use a command : 'ffmpeg'.

Create a new directory and move the video to it then run this : 

`ffmpeg -i Sh4d0w5.mp4 output_frame_%04d.png`

**Note : don't add other parameters like changin fps rate or something, 
because if you change the video's speed/rate while extracting pngs, some frames may be lost**

You'll have about ~ 1200 png frames from the video.
 Diving/scrolling through them u'll find 4 frames : 

 Frame 1 : 
 
 ![output_frame_0133](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/b55532f8-85ac-4d99-8c1c-62cfa9d1e3ae)

Frame 2 :

![output_frame_0308](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/9607752c-9524-4a2f-9e8a-abfe60524d4a)

Frame3:

![output_frame_1150](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/d7d09378-3700-47ec-b552-b4bba60404b1)

Frame4:

![output_frame_1208](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/86d399f0-badb-4ebc-943e-bca74db3cddd)

Assemble it with any simple pics editor to have the full qr code : 

![frame](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/69aa0433-5065-431b-ad8c-2fcc9ee910d6)

Scan it then you'll get the flag ! 

> Flag : Ingeniums{Y0u_H4v3_70_Lo0k_Cl053R}
