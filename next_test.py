topics = [
    {'id': 1, 'title': '마시멜로 이야기', 'author': '호아킨', 'body': '마시멜로 이야기는 찰리과 조나단이..'},
    {'id': 2, 'title': '마시멜로 두번째 이야기', 'author':'호아킨, 엘런싱어' ,'body': '마시멜로 두번째 이야기는 찰리가 대학을 졸업하고..'},
    {'id': 3, 'title': '청소년을 위한 지금 시작하는 인문학', 'author':'주현성', 'body': '청소년을 위한 지금 시작하는 인문학은 세계의 역사와 인간이 철학을 한 이유 철학을 통하여 얻은 것들..'}
    
]
ids = 3

topic = next((t for t in topics if t['id'] == ids), None)
print(topic)