# WireWeb2

> I wanna reach my BOSS so we can play PING-PONG but he's not responding!! hmmm...

File : [WireWeb2.pcap](WireWeb2.pcap)

# Solution 

Using wireshark to inspect the network traffic
We notice that grep / search for flag format string wont work.
There are a lot of packets and some of them contains base64 and decrypting that base64 strings may give u wrong flags / non-sense.
So we have to filter the packets basing on some creterias that we'll exclude from the description.
PING-PONG may be a hint to ping ( and these are based on ICMP packets ):

![Screenshot from 2023-09-18 14-25-15](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/375cd2b5-5b2e-4aca-882d-e4ae7765ecee)

We still have a lot of icmp packets with b64.. we need another filtering criteria 
Looking at ip adresses destination we notice 2 types: 
(8.8.8.8) which is google adress and (8.0.5.5) which looks like BOSS that's mentioned in description too !
filtering them with : `icmp && ip.dst == 8.0.5.5` 
will leave us with just 4 packets, assembling the base64 in them and decrypting it will give us the flag ! 

>Flag :ingeniums{N0o0w_itZz_Pr0ToC0l5s_TiiiiiiiM3_956302084642602462462363626477}
