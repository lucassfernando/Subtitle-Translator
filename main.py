import webvtt
from deep_translator import GoogleTranslator
import time
from concurrent.futures import ThreadPoolExecutor



start_time = time.time()

def translate_caption(caption):
    text_translated = GoogleTranslator(source='auto', target='portuguese').translate(caption.text)
    return f'{caption.identifier}\n{caption.start} --> {caption.end}\n{text_translated}\n\n'


with open('test.vtt', 'w') as create_file_vtt:
    create_file_vtt.write('WEBVTT\n\n')

captions = list(webvtt.read('file.vtt'))

with ThreadPoolExecutor() as executor:
    translated_captions = executor.map(translate_caption, captions)

    with open('test.vtt', 'a', encoding='utf-8') as file_write_vtt:
        for translated_caption in translated_captions:
            file_write_vtt.writelines(translated_caption)

end_time = time.time()
print("\n\nTIME:", end_time - start_time)
