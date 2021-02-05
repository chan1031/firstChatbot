from chatbot.utils.Preprocess import Preprocess
from tensorflow.keras import preprocessing
import pickle

# 말뭉치 데이터 읽어오기
def read_corpus_data(filename):
    with open(filename, 'r' , encoding='UTF8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:] #헤더제거
    return data

#말뭉치 데이터 가져오기
corpus_data = read_corpus_data('corpus.txt')

#말뭉치 데이터에서 키워드만 추출해서 사전 리스트 생성
p = Preprocess()
dict = []
for c in corpus_data:
    pos = p.pos(c[1]) #말뭉치 데이터에서 첫번째 배열 즉 문장만 뽑아내서 POS 태킹한다.
    for k in pos:
        dict.append(k[0]) #문장들 중에 단어들만 dict에 추가한다.

#토크나이저를 이용하여 단어들을 토큰화 시킨다.
tokenizer = preprocessing.text.Tokenizer(oov_token='OOV') #oov_token은
tokenizer.fit_on_texts(dict) #fit_on_texts는 문자데이터를 리스트 형태로 변환함
word_index = tokenizer.word_index #word_index는 단어와 숫자의 키-값으로 이루어진 딕셔너리로 변환함

#사전 파일 생성
f = open("chatbot_dict.bin", "wb")
try:
    pickle.dump(word_index, f) #dump(넣을 내용,파일 이름)
except Exception as e:
    print(e)
finally:
    f.close()