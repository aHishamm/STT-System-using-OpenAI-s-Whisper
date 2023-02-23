import whisper
import gradio as gr
import spacy_fastlang
import spacy
import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 
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
    return frequency,total_items
def whisperbackend(audiopath, audiopath2): 
    if(audiopath == None): 
        audiopath = audiopath2
    model = whisper.load_model("large") 
    audio = whisper.load_audio(audiopath)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    _, probs = model.detect_language(mel)
    lang = max(probs, key=probs.get)
    result = model.transcribe(audiopath)['text'] 
    options = dict(language='ar',beam_size=5,best_of=5)
    translate_options = dict(task="translate",**options)
    translation = model.transcribe(audiopath,**translate_options)['text']
    result_list = result.split() 
    result_lang = [] 
    for i in result_list: 
        doc = nlp(i) 
        result_lang.append(doc._.language)
    freq_list, total_items = find_frequency_and_percentage(result_lang)
    freq_keys = freq_list.keys() 
    freq_values = freq_list.values() 
    freq_df = pd.DataFrame({'Languages':freq_keys,'Percentages':freq_values}) 
    freq_df['Percentages'] = freq_df['Percentages'].apply(lambda x: (x / total_items) *100)
    if lang == 'en': 
        lang = 'English'
    elif lang == 'ar': 
        lang = 'Arabic'
    #pymongo_get_database.create_document(translation)
    fig = (sns.barplot(freq_df,x='Languages',y='Percentages')).get_figure()
    return fig, "The detected language is: \n"+lang+"\n Audio transcription: \n"+result+'\n'+translation
with gr.Blocks() as demo:  
    with gr.Tab("Input & Translation"):
        audio_input1 = gr.Audio(source="microphone",type="filepath") 
        audio_input2 = gr.Audio(type="filepath") 
        text_output1 = gr.Textbox() 
        button1 = gr.Button("Process Audio") 
    with gr.Tab("Visualization"):
        image_output1 = gr.Plot(width=350,height=300) 
    button1.click(whisperbackend,inputs=[audio_input1,audio_input2],
                  outputs=[image_output1,text_output1])
demo.launch(share=True) 