import langid

def detect_languages(sentence):
    return langid.classify(sentence)

if __name__ == '__main__':
    mixed_sentence = "한국어와 English가 함께 있는 문장입니다."
    
    lang, confidence = detect_languages(mixed_sentence)
    
    print(f"Detected Language: {lang}, Confidence: {confidence:.2f}")