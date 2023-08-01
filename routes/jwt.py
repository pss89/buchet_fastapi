from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
from jwt import PyJWTError
from datetime import datetime,timedelta
from db.models.user_model import UserInfo,UserInfoDetail

import json

router = APIRouter(
    prefix='/jwt'
)

# JWT 설정
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# 사용자 정보를 가져오는 함수 (이 부분은 실제로는 데이터베이스에서 가져오는 것이어야 합니다.)
def get_user(username: str):
    # 사용자 정보 조회 로직
    # ...

    return {"username": username, "role": "user"}

# 토큰 발급 함수
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# 토큰 인증 함수
async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")
    except PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    user = get_user(username)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return user

# 토큰을 발급하는 엔드포인트
# @app.post("/token")
@router.post("/token")
def login(userId: str, password: str):
    
    # 회원정보 호출
    users = UserInfo.get_users(userId)
    if users is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # 정보를 딕셔너리 형태로 변환
    userInfo = users[0].__dict__
        
    # 회원아이디 변수에 저장
    userId = userInfo['user_id']
    
    # 회원아이디를 통해 jwt 생성
    access_token = create_access_token(data={"sub": userId})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/get_token")
def request_test(token: str):
    
    decoded_data = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    json_data = json.dumps(decoded_data, indent=2)
    
    print(json_data)
    
    pass

# 토큰을 사용하여 보호된 엔드포인트
# @app.get("/protected")
# @router.get("/protected")
# def protected_route(user: dict = Depends(get_current_user)):
#     return {"message": "This is a protected route.", "user": user}
