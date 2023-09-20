# WireWeb1

> i guess someone else used my pc without me knowing that ?
> but luckily a wire-tool i have captured his network traffic while he was online,i guess we can know
> something about him if we analyse the traffic well, network packets may tell as a lot about person,
> specially if he made a request to his web page ?

File : [WireWebLvl1.pcap](WireWebLvl1.pcap)

# Solution 

So this is a challenge to get people introduced to "Wireshark" a tool to analyse network trafic -usually be in .pcap files-.<br>
Opening the file we'll find a bunch of packets and protocols, and going back to description, we're talking about a **request to a web page**
Which known to be in **HTTP** protocol, so we'll filter that kind of packets:

![Screenshot from 2023-09-18 16-07-32](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/078539cd-3476-4ca1-b35f-976030bfb566)


To see more and closer the details of the packet we follow the Tcp stream ( or http in this case both works ) :

![Screenshot 2023-09-18 16:09:16](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/763580f1-b251-440b-8983-bde6b60636b6)

And here after reading that useful introduction we find the flag : 

![Screenshot from 2023-09-18 16-10-01](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/c86d958b-a1c8-45af-8ac8-c637c1905bba)

>Flag : ingeniums{ItTz_4LL_480U7_P4Ck3t5}
