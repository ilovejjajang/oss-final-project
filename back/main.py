from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class UserInput(BaseModel):
    spend_reason: str
    worldview: str
    budget: str

@app.get("/")
async def root():
    return {"msg": "백엔드 서버 작동 중"}

@app.post("/recommend")
async def get_recommendation(user_input: UserInput):
    print(f">> [로그] 입력값: {user_input.spend_reason}, {user_input.worldview}, {user_input.budget}")

    target = "스팀 게임"
    reason = "다양한 장르의 게임을 접해보는 것을 추천합니다."

    if user_input.spend_reason == "캐릭터 외모 (디자인 및 일러스트)":
        if user_input.worldview == "판타지":
            target = "원신"
            reason = "매력적인 판타지 세계관과 개성 있는 캐릭터 디자인이 특징입니다."
        elif user_input.worldview == "현대물 및 SF":
            target = "블루 아카이브"
            reason = "학원물과 밀리터리 요소가 결합된 독특한 감성의 게임입니다."
            
    elif user_input.spend_reason == "성능 및 스펙업 (경쟁과 성취감)":
        if user_input.budget == "10만원 이상":
            target = "메이플스토리"
            reason = "장비 강화와 성장을 통해 확실한 스펙업의 성취감을 느낄 수 있습니다."
        else:
            target = "리그 오브 레전드 (LoL) 또는 발로란트"
            reason = "피지컬과 전략적 판단력으로 경쟁하는 쾌감을 얻을 수 있습니다."
            
    elif user_input.spend_reason == "스토리 및 세계관 (몰입감)":
        if user_input.worldview == "판타지":
            target = "젤다의 전설 시리즈"
            reason = "완성도 높은 스토리와 자유도를 바탕으로 깊은 몰입감을 느낄 수 있습니다."
        else:
            target = "사이버펑크 2077"
            reason = "어두우면서도 매력적인 미래 SF 세계관을 체험할 수 있습니다."
            
    else:
        random_targets = ["명조: 워더링 웨이브", "붕괴: 스타레일", "승리의 여신: 니케"]
        target = random.choice(random_targets)
        reason = "최근 유저들 사이에서 좋은 평가를 받고 있는 서브컬처 게임을 추천합니다."

    print(f">> [로그] 추천 결과: {target}")

    return {
        "recommended_target": target,
        "reason": reason
    }
