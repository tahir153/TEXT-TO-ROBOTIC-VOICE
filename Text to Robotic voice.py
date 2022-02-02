# hr = gTTS(text=content , lang="en", tld= "co.in",slow=False )
from gtts import gTTS
content =  ""
hr = gTTS(text=content)
hr.save("insta manual.mp3")
