##매번 구문을 만들기 귀찮으니까 class의 형태로 만들어서 실행하는 것



## sql모듈 생성
## 1.Class생성 Database()
## 2.Class생성이 될 때 pymysql,connect()함수를 사용해서 DB의 정보를 입,cursor생성
## 3.__init__()함수를 제외하고 함수 3개를 생성
## 4.execute()함수 ->매개변수sql, values를 생성,sql문 실행->values값을 같이 넣어서 실행
## 5.executeAll()함수 ->매개변수 sql,values를 생성, sql문 실행 
## ->values값을 같이 넣어서 실행 -> 결과값 받아와서 데이터프레임으로 변경 후 return
## 6.commit() 함수 -> DB에commit 과정
## 7.excute(),excuteAll()함수에서 매개변수 values의 기본값을 () 빈 리스트 형태로 지정

import pymysql
import pandas as pd

class Database():
    def __init__(self):                           ##self변수는 class밖에서는 사용하지 못하 
        self._db = pymysql.connect(
            host = 'localhost',
            user = 'root',
            passwd = '1234',
            db = 'ubion4',
            port = 3306                          ##port 3306은 기본값
        )
        self.cursor = self._db.cursor(pymysql.cursors.DictCursor)

    def execute(self,sql,values=[]):
        self.cursor.execute(sql,values)

    def executeAll(self,sql,values=[]):
        self.cursor.execute(sql,values)
        self.result = self.cursor.fetchall()
        return pd.DataFrame(self.result)        ##pandas에 있는 Dataframe을 사용함
    
    def commit(self):
        self._db.commit()                       ##Commit함수는 DB에 적용


    ## pd.DataFrame()              ->pandas
    ## pd.merge()                   ->라이브러리안에 있는 function사용
    def test(_x,_y):
        result = _x + _y
        return result

