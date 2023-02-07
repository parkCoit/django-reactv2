# -*- coding: UTF-8 -*-
from PyKakao import KoGPT

api = KoGPT(service_key="83737e699fa7fe760ecf8b866a016030")
"""
소스 출처: https://wooiljeong.github.io/python/pykakao-kogpt/
"""


class KakaoChatbot:
    def __init__(self):
        pass

    """
    KoGPT의 기본 기능입니다. 주어진 프롬프트 뒤로 이어질 자연스러운 문장을 생성합니다.
    """

    def exec_1(self, sentence):
        # 필수 파라미터
        prompt = f"{sentence}"
        max_tokens = 64

        # 결과 조회
        result = api.generate(prompt, max_tokens, temperature=0.7, top_p=0.8)
        print(result)
        print(result.get('generations')[0]['text'])
        return result.get('generations')[0]['text']

    """
    문장 분류하기
    주어진 프롬프트의 분류 예시를 참고해 마지막 문장을 같은 기준으로 분류(Classification)합니다. 
    분류 대상인 마지막 문장은 예시의 각 문장과 같은 형식으로 입력해야 합니다. 아래는 상품평을 긍정 또는 부정으로 분류 요청하는 예제입니다. 
    결과가 “긍정” 또는 “부정”이어야 하므로 max_tokens은 1로 지정해 요청합니다.
    """

    def exec_2(self, sentence):
        # 필수 파라미터
        prompt = f"""상품 후기를 긍정 또는 부정으로 분류합니다.
        가격대비좀 부족한게많은듯=부정
        재구매 친구들이 좋은 향 난다고 해요=긍정
        ㅠㅠ약간 후회가 됩니다..=부정
        이전에 먹고 만족해서 재구매합니다=긍정
        {sentence}="""
        max_tokens = 1

        # 결과 조회
        result = api.generate(prompt, max_tokens, temperature=0.4)
        # 결과가 “긍정” 또는 “부정”이어야 하므로 max_tokens은 1로 지정해 요청합니다.
        print(result)
        return result.get('generations')[0]['text']

    """
    뉴스 한 줄 요약하기
    주어진 프롬프트의 뉴스 내용을 한 줄 요약합니다. 
    KoGPT가 수행해야 할 과제를 알아볼 수 있도록 프롬프트 끝에 한줄 요약: 
    형식으로 입력을 구성했습니다.
    """

    def exec_3(self, sentence):
        # 필수 파라미터
        prompt = f"""{sentence}
        한줄 요약:"""
        max_tokens = 128

        # 결과 조회
        result = api.generate(prompt, max_tokens, top_p=0.7)
        print(result)
        return result.get('generations')[0]['text']

    """
    질문에 답변하기
    주어진 프롬프트의 복합적인 정보를 참고하여 질문에 답변합니다. 
    KoGPT가 수행해야 할 과제를 알아볼 수 있도록 프롬프트 끝에 정책제안서를 제출하는 시기는 언제인가?:
     형식으로 입력을 구성했습니다.
    """

    def exec_4(self, sentence):
        # 필수 파라미터
        prompt = f"""{sentence}:"""
        max_tokens = 128

        # 결과 조회
        result = api.generate(prompt, max_tokens, temperature=0.2)
        print(result)
        return result.get('generations')[0]['text']

    """
    특정 정보 추려내기
    주어진 프롬프트의 내용에서 요청한 정보를 반환합니다. 
    주어진 사실을 바탕으로 과제를 해결해야 하므로, 
    temperature 파라미터 값을 0.3으로 지정해 비교적 고정적인 결과를 생성하도록 유도합니다.
    """

    def exec_5(self, sentence):
        # 필수 파라미터
        prompt = """임진왜란(壬辰倭亂)은 1592년(선조 25년) 도요토미 정권이 조선을 침략하면서 발발하여 1598년(선조 31년)까지 이어진 전쟁이다. 또한 임진왜란은 동아시아에 막대한 영향을 끼쳤으며, 두번의 침입이 있어서 제2차 침략은 정유재란이라 따로 부르기도 한다. 또한 이때 조선은 경복궁과 창덕궁 등 2개의 궁궐이 소실되었으며 약 백만명의 인구가 소실되었다.
        명칭
        일반적으로 임진년에 일어난 왜의 난리란 뜻으로 지칭되며 그 밖에 조선과 일본 사이에 일어난 전쟁이란 뜻에서 조일전쟁(朝日戰爭), 임진년에 일어난 전쟁이란 뜻에서 임진전쟁(壬辰戰爭), 도자기공들이 일본으로 납치된 후 일본에 도자기 문화가 전파되었다 하여 도자기 전쟁(陶瓷器戰爭)이라고도 한다. 일본에서는 당시 연호를 따서 분로쿠의 역(일본어: 文禄の役 분로쿠노에키[*])이라 하며, 중화인민공화국과 중화민국에서는 당시 명나라 황제였던 만력제의 호를 따 만력조선전쟁(萬曆朝鮮戰爭, 중국어: 萬曆朝鮮之役), 혹은 조선을 도와 왜와 싸웠다 하여 항왜원조(抗倭援朝)라고도 하며, 조선민주주의인민공화국에서는 임진조국전쟁(壬辰祖國戰爭)이라고 한다. 그밖에도 7년간의 전쟁이라 하여 7년 전쟁(七年戰爭)으로도 부른다.
        임진왜란 때 조선의 왕은?
        답:"""
        max_tokens = 1

        # 결과 조회
        result = api.generate(prompt, max_tokens, temperature=0.3)

        print(result)
        return result.get('generations')[0]['text']

    """
    말투 바꾸기
    주어진 프롬프트의 예시를 참고하여, 마지막 문장의 말투를 요청한 방식으로 바꿉니다. 
    아래는 반말을 존댓말로 바꾸는 예제입니다. 
    KoGPT가 참고할 수 있는 예시를 포함해 요청합니다.
    """

    def exec_6(self, sentence):
        # 필수 파라미터
        prompt = """주어진 문장을 존댓말 문장으로 바꿔주세요.

        문장:하지마!
        존댓말:하지 말아주세요.

        문장:나랑 같이 놀러가자
        존댓말:저랑 같이 놀러가지 않으실래요?

        문장:배고파 밥줘
        존댓말:배가고픈데 밥을 먹어도 될까요?

        문장:그거 재밌어?
        존댓말:그것은 재미 있나요?

        문장:뭐하는거야 지금
        존댓말:지금 무엇을 하시는 건가요?

        문장:당장 제자리에 돌려놔
        존댓말:"""
        max_tokens = 10

        # 결과 조회
        result = api.generate(prompt, max_tokens, temperature=0.7)
        print(result)
        return result.get('generations')[0]['text']

    """
    채팅하기
    주어진 프롬프트의 정보와 대화 예시를 참고해 적절한 대화를 이어나갑니다. 
    과제 설명에 화자 특징을 묘사한 뒤, Q:와 A: 형식으로 대화 예시를 전달합니다.
    """

    def exec_7(self, sentence):
        # 필수 파라미터
        prompt = f"""정보:거주지 서울, 나이 30대, 성별 남자, 자녀 두 명, 전공 인공지능, 말투 친절함
        정보를 바탕으로 질문에 답하세요.
        Q:안녕하세요 반갑습니다. 자기소개 부탁드려도 될까요?
        A:안녕하세요. 저는 서울에 거주하고 있는 30대 남성입니다.
        Q:{sentence}?
        A:"""
        max_tokens = 32

        # 결과 조회
        result = api.generate(prompt, max_tokens, temperature=0.3, top_p=0.85)
        print(result)
        print(result.get('generations')[0]['text'])
        return result.get('generations')[0]['text'].replace("\n", " ")


if __name__ == '__main__':
    KakaoChatbot().exec_7("거주지 서울, 나이 30대, 성별 남자, 자녀 두 명, 전공 인공지능, 말투 친절함")