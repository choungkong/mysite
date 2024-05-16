import pymysql
import pymysql.cursors

_db = pymysql.connect(
    host = 'choungkong.mysql.pythonanywhere-services.com',
    user = 'choungkong',
    port = 3306,
    password = "~~kong0540",
    db = 'choungkong$ubion'
    )

# coursor 생성
cursor = _db.cursor(pymysql.cursors.DictCursor)


create_user = """
    create table
    if not exists
    user (
    id varchar(32) primary key,
    password varchar(64) not null,
    name varchar(32) not null
    )
"""

#sql 쿼리문을 실행
cursor.execute(create_user)
# 동기화
_db.connit()
# 서버와의 연결을 종료
_db.close()
print('tavle 생성 완료')