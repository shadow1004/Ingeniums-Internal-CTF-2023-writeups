from pydub import AudioSegment
from pydub.generators import Sine

#Nil0V3R 

melody_notes = "151 156 147 145 156 151 165 155 163 173 104 157 137 122 145 137 155 111 137 171 157 165 137 147 157 164 137 155 145 175"

melody = AudioSegment.silent(duration=0)  

note_duration = 500  

for note_code in melody_notes.split():
    note_value = int(note_code)
    freq = 440 * (2 ** ((note_value - 69) / 12))  
    sine_wave = Sine(freq)
    audio_segment = sine_wave.to_audio_segment(duration=note_duration)
    melody += audio_segment

output_file = "Oct-taal se taal mila.wav"
melody.export(output_file, format="wav", tags={"notes": melody_notes})

print(f"Melody with notes saved as {output_file}")
