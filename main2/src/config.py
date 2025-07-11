from pydantic_settings import BaseSettings ,SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env',extra="ignore")
    DATABASE_URL:str
    
config = Settings()
    