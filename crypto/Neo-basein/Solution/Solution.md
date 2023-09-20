# Neo-BasINE

> My sister started to work in a laboratory and since then she's acting sus,
> I hacked her laptop to know what she is hiding from me, but all I found is a [list](Nbases.txt) and a [pic](NeoBasine.jpg) of stupid tubes!>> The [list](Nbases.txt) is called bases,
> I thought I'd find some useful numbers but these bases Are `Nu`for me !!
> all I noticed is that everything is on `3 characters` but..
> i'm just a hacker after all!, i understand just `C0mputer 1anguage` ma friend! help me to decrypt this and find the secret!

# Solution 
Looking at the [list](Nbases.txt) file that contains strings like "GUU UUA UUG" which are Nucleo bases!<br>
In science nucleo-bases are translated to dna/rna or amino acides that fabriques protein, and these called "genetique code" or codons!<br>

Googling a bit we'll help you find [This website](https://www.dcode.fr/codons-code-genetique) that can help us decrypting these chains. <br>

![The-codon-table-The-genetic-code-is-composed-of-four-different-letters-U-C-A-and-G](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/dfcd10da-e906-4261-bd82-82f9af485329)

Decrypting the list will give us 'VLLGRPTRVPLGRPAPVALGGAGVVGGAPSGSVALVVAVRLPSGTAGLLRGTGTGVLPSTPAAPLVTARASRLPGARASTPTSGPARA' 
A string of just 8 letters which represent 8 amino acides in the [picture file](NeoBasine.jpg): 

![tubes](https://github.com/shadow1004/Ingeniums-Internal-CTF-2023-writeups/assets/68519098/d8916bea-4e9c-49a7-9cab-4261c3c0ce34)

We notice that every amino acide is associated to a number from 0-7. <br>
Also, in description we have `C0mputer 1anguage` so we understand that we have to map each amino acide to his number but in binary.<br
But here's the trick: for exemple Val = 3 in the picture, how would it become in binary ? 11 ? 011? 0011 ? 0000 0011 ? <br>
Here comes the other hint in description : **all I noticed is that everything is on `3 characters`** so we'll use 3 bits!

[Here](decryptamino.py) is the script using for mapping, after that decrypting the binary result in any online tool will give you the flag!

>Flag :ingeniums{R0u7_Dir_M3DCiN_GG_D0c}


