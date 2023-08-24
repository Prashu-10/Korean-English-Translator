from langdetect import detect_langs

def detect_korean_sentences(paragraph):
    # Split the paragraph into sentences
    sentences = paragraph.split('.')
    print(sentences) 
    korean_sentences = []
    for sentence in sentences[:-1]:
        # Detect the language of each sentence
        detected_languages = detect_langs(sentence)
        print(type(detected_languages))
        print(detected_languages)
        for lang in detected_languages:
            if lang.lang == 'ko' and lang.prob > 0.5:  # Adjust threshold as needed
                korean_sentences.append(sentence.strip())
                break  # Stop checking languages for this sentence
        print(korean_sentences)
    
    return korean_sentences

if __name__ == '__main__':
    paragraph = "This is an example. 한국어 문장입니다. English text. 또 다른 한국어 문장입니다."
    korean_sentences = detect_korean_sentences(paragraph)
    
    for idx, sentence in enumerate(korean_sentences, start=1):
        print(f"Korean Sentence {idx}: {sentence}")