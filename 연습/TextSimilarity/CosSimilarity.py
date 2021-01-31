from konlpy.tag import Komoran
import numpy as np
from numpy import dot
from numpy.linalg import norm

def cos_sim(vec1, vec2):
    return dot(vec1, vec2) / (norm(vec1) * norm(vec2))

def make_term_doc_mat(sentence_bow, word_dics):
    #ferq_mat이라는 딕셔너리를 만듬
    freq_mat = {}

    #word_dics의 값을 전부 0으로 만듬
    for word in word_dics:
        freq_mat[word] = 0

    for word in word_dics:
        if word in sentence_bow:
            freq_mat[word] += 1

    return freq_mat


def make_vector(tdm):
    vec = []
    for key in tdm:
        vec.append(tdm[key])
    print(vec)
    return vec

#문장 생성
sentence1 = '6월에 뉴턴은 선생님의 제안으로 트리니티에 입학했다.'
sentence2 = '6월에 뉴턴은 선생님의 제안으로 대학교에 입학했다.'
sentence3 = '나는 맛있는 밥을 뉴턴 선생님과 함께 먹었다.'

# 단어 묶음 리스트 생성
komoran = Komoran()
bow1 = komoran.nouns(sentence1) #bow1의 타입은 리스트가 됨
bow2 = komoran.nouns(sentence2)
bow3 = komoran.nouns(sentence3)

#하나의 리스트로 합침
bow = bow1 + bow2 + bow3

#하나로 합쳐진 bow라는 리스트에서 중복되는 단어를 삭제
word_dics = []
for token in bow:
    if token not in word_dics:
        word_dics.append(token)
#word_dics는 세 문장에 들어있는 명사들을 중복되지 않게끔 리스트로 만든 리스트임
print(word_dics)

#단어 문서행렬을 만들어준다.
freq_list1 = make_term_doc_mat(bow1, word_dics) #freq_list들은 딕셔너리 타입임
freq_list2 = make_term_doc_mat(bow2, word_dics)
freq_list3 = make_term_doc_mat(bow3, word_dics)

print(freq_list1)
print(freq_list2)
print(freq_list3)

#앞의 단어 문서행렬을 벡터로 표현
doc1 = np.array(make_vector(freq_list1))
doc2 = np.array(make_vector(freq_list2))
doc3 = np.array(make_vector(freq_list3))

#벡터로 표현된 doc의 값들을 서로 비교하여 유사도 계산
r1 = cos_sim(doc1, doc2)
r2 = cos_sim(doc3, doc1)
print(r1)
print(r2)
