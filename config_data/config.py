from dataclasses import dataclass

from environs import Env 

@dataclass
class TgBot:
    token: str    # Токен для доступа к телеграм-боту
    admin_id: list[int]    # Список id администраторов бота

@dataclass
class Config:
    tg_bot: TgBot

# Создаем функцию, которая будет читать файл .env и возвращать
# экземпляр класса Config с заполненными полями token и admin_id
def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_id=list(map(int, env.list('ADMIN_ID')))
        )
    )