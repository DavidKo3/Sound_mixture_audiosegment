# refer to the fol

from pydub import AudioSegment as aseg
from pydub.playback import play
data1 = "../data/Nightwish_bye.mp3_vocals.wav"
data2 = "../data/Nightwish_bye.mp3_accompaniment.wav"
sound1 = aseg.from_wav(data1)
sound2 = aseg.from_wav(data2)

played_together = sound1.overlay(sound2)

played_together.export("../output/mixed.wav", format="wav")







