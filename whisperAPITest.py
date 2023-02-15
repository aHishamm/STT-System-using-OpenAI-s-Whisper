import whisper
import gradio as gr
import pymongo_get_database

def whisperbackend(audiopath, audiopath2): 
    #If one path is None, switch to the other path
    if(audiopath == None): 
        audiopath = audiopath2
    model = whisper.load_model("large") 
    audio = whisper.load_audio(audiopath)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    _, probs = model.detect_language(mel)
    lang = max(probs, key=probs.get)
    #Transcription
    result = model.transcribe(audiopath)['text'] 
    #Translation of Arabic transcription to English
    options = dict(language='ar',beam_size=5,best_of=5)
    translate_options = dict(task="translate",**options)
    translation = model.transcribe(audiopath,**translate_options)['text']
    #printing the translation in the terminal 
    print(translation)

    if lang == 'en': 
        lang = 'English'
    elif lang == 'ar': 
        lang = 'Arabic'
    #send the translated work to the mongoDB database
    pymongo_get_database.create_document(translation)
    return "The detected language is: \n"+lang+"\n Audio transcription: \n"+result+'\n'+translation

demo = gr.Interface(fn=whisperbackend, 
                    inputs=[gr.Audio(source="microphone", type="filepath"),gr.Audio(type="filepath")],
                    outputs="text", cache_examples=True)


demo.launch(share=True) 