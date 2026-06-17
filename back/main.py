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
    return {"msg": "백엔드 서버 켜짐"}

@app.post("/recommend")
async def get_recommendation(user_input: UserInput):
    print(f">> [로그] 입력값: 목적={user_input.spend_reason}, 세계관={user_input.worldview}, 예산={user_input.budget}")

    target = "스팀(Steam) 연쇄할인마"
    reason = "일단 스팀 세일할 때 이것저것 사보는 걸 추천합니다."

    if user_input.spend_reason == "캐릭터 외모 (내 최애가 최고야)":
        if user_input.worldview == "판타지":
            target = "원신"
            reason = "캐릭터 뽑기에 돈 다 털릴 수 있으니 주의하세요. 그래도 예쁘니까 용서됩니다."
        elif user_input.worldview == "현대물/SF":
            target = "블루 아카이브"
            reason = "청춘... 감성... 그리고 가챠. 브금도 좋아서 코딩 과제할 때 노동요로 듣기 좋습니다."
            
    elif user_input.spend_reason == "성능/스펙업 (내가 서버 1짱이 되어야 함)":
        if user_input.budget == "월 10만원 이상 쌉가능":
            target = "메이플스토리" 
            reason = "스펙업의 끝판왕. 큐브 몇 번 돌리다 보면 통장이 텅텅 비는 마술을 볼 수 있습니다."
        else:
            target = "리그 오브 레전드 (LoL) 또는 발로란트"
            reason = "돈 없으면 실력으로 승부합시다. 스킨은 가끔 할인할 때만 사세요."
            
    elif user_input.spend_reason == "스토리/세계관 (몰입감이 중요해)":
        if user_input.worldview == "판타지":
            target = "젤다의 전설 시리즈"
            reason = "가챠할 돈으로 스위치랑 젤다 사서 방학 내내 하는 게 가성비 최고입니다."
        else:
            target = "사이버펑크 2077"
            reason = "스토리 뽕맛 하나는 기가 막힙니다. 단점은 컴 사양이 좋아야 돌아감..."
            
    else:
        random_targets = ["명조: 워더링 웨이브", "붕괴: 스타레일", "승리의 여신: 니케"]
        target = random.choice(random_targets)
        reason = "조건에 딱 맞는 게 없어서 요즘 인기 있는 겜 중에 랜덤으로 돌렸습니다."

    print(f">> [로그] 최종 추천: {target}")

    return {
        "recommended_target": target,
        "reason": reason
    }