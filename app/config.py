from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseModel):
    host: str
    port: int
    username: str
    password: SecretStr
    name: str

    @property
    def url(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.username}:"
            f"{self.password.get_secret_value()}@"
            f"{self.host}:{self.port}/"
            f"{self.name}"
        )


class JwtSettings(BaseModel):
    secret_key: SecretStr
    algorithm: str
    access_token_expire_minutes: int
    refresh_token_expire_days: int


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="APP_",
        env_nested_delimiter="__",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    db: DatabaseSettings
    jwt: JwtSettings


settings = Settings()
