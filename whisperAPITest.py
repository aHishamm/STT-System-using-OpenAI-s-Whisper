import whisper
import gradio as gr
import spacy_fastlang
import spacy
#import pymongo_get_database

nlp = spacy.load('en_core_web_sm') 
nlp.add_pipe('language_detector')
def find_frequency_and_percentage(items):
    frequency = {}
    total_items = len(items)
    
    for item in items:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    
    for item, count in frequency.items():
        percentage = (count / total_items) * 100
        print(f"{item}: {percentage:.2f}%")
def whisperbackend(audiopath, audiopath2): 
    #If one path is None, switch to the other path
    if(audiopath == None): 
        audiopath = audiopath2
    model = whisper.load_model("base") 
    audio = whisper.load_audio(audiopath)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    _, probs = model.detect_language(mel)
    lang = max(probs, key=probs.get)
    #Transcription
    result = model.transcribe(audiopath)['text'] 
    #spacy lang detection 
    #doc = nlp(result) 
    #print(doc._.language, doc._.language_score)
    #Translation of Arabic transcription to English
    options = dict(language='ar',beam_size=5,best_of=5)
    translate_options = dict(task="translate",**options)
    translation = model.transcribe(audiopath,**translate_options)['text']
    #printing the translation in the terminal 
    #print(translation)
    #store the result in a list of words 
    result_list = result.split() 
    result_lang = [] 
    for i in result_list: 
        doc = nlp(i) 
        result_lang.append(doc._.language)
        #print(doc._.language,'\t',doc._.language_score)
    print(result_list)
    print(result_lang)
    print(find_frequency_and_percentage(result_lang))

    if lang == 'en': 
        lang = 'English'
    elif lang == 'ar': 
        lang = 'Arabic'
    #send the translated work to the mongoDB database
    #pymongo_get_database.create_document(translation)
    return "The detected language is: \n"+lang+"\n Audio transcription: \n"+result+'\n'+translation

demo = gr.Interface(fn=whisperbackend, 
                    inputs=[gr.Audio(source="microphone", type="filepath"),gr.Audio(type="filepath")],
                    outputs="text", cache_examples=True)


demo.launch(share=True) 