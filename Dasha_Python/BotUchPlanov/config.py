import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "8023981552:AAG3_oU0bn2fTGglgLmTex4VckP1tqEwRVA")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite://study_plans.db")

TOPIC_COMPLEXITY = {
    'легкая': {'hours': 4, 'days': 2},
    'средняя': {'hours': 8, 'days': 4},
    'сложная': {'hours': 12, 'days': 7}
}
