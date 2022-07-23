from flask import request
from flask_restful import Resource, reqparse
from models.book import BookModel
import random
from gensim.models.doc2vec import Doc2Vec

class Today(Resource):  # 오늘의 추천
    def post(self):
        body = request.get_json()
        print(body)
        # bestseller 목록 전체 가져와서 랜덤으로 한 권 뽑기
        books = BookModel.find_by_bestseller()
        randint = random.randint(0, len(books))
        book = books[randint].json()
        # 책 설명 10자 이상 넘어가면 요약
        description = (
            book['summary'][:50] + '...') if len(book['summary']) > 50 else book['summary']
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard": {
                            "title": book['title'],
                            "description": description,
                            "thumbnail": {
                                "imageUrl": book['img']
                            },
                            "profile": {
                                "imageUrl": book['img'],
                                "nickname": book['title']
                            },
                            "social": {
                                "like": 1238,
                                "comment": 8,
                                "share": 780
                            },
                            "buttons": [
                                {
                                    "action": "message",
                                    "label": "읽고 싶어요(저장)",
                                    "messageText": "내가 읽고 싶은 책 목록에 저장했습니다(개발예정)"
                                },
                                {
                                    "action":  "message",
                                    "label": "읽은 책입니다(저장+평점)",
                                    "messageText": "내가 읽은 책 목록에 저장하고 평점 남기기(개발예정)"
                                }
                            ]
                        }
                    }
                ]
            }
        }
        return responseBody

class Similar(Resource):  # 비슷한 책 추천
    def post(self):
        body = request.get_json()
        print(body)
        input_title = body['action']['params']['title']
        return responseBody

class Sense(Resource):  # 비슷한 책 추천
    def post(self):
        body = request.get_json()
        print(body)
        return responseBody

class Social(Resource):  # 비슷한 책 추천
    def post(self):
        body = request.get_json()
        print(body)
        return responseBody