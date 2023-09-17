from flask import Flask, request, redirect,render_template

app = Flask(__name__)

nextId = 5
topics = [
    {'id': 1, 'title': '마시멜로 이야기', 'author': '호아킨', 'body': '마시멜로 이야기는 찰리과 조나단이..'},
    {'id': 2, 'title': '마시멜로 두번째 이야기', 'author':'호아킨, 엘런싱어' ,'body': '마시멜로 두번째 이야기는 찰리가 대학을 졸업하고..'},
    {'id': 3, 'title': '청소년을 위한 지금 시작하는 인문학', 'author':'주현성', 'body': '청소년을 위한 지금 시작하는 인문학은 세계의 역사와 인간이 철학을 한 이유 철학을 통하여 얻은 것들..'},
    {'id': 4, 'title': '이토록 공부가 재미있어지는 순간', 'author':'박성혁', 'body': '자신이 왜 공부를 하는지에 대해 다시 한 번 생각해보도록 해주며, 나의 마음에 대해 고민할 수 있게 해준다. 가족과 공부 내 마음에 대해서 다시한 번 돌아볼수 있게 해주었다'}
    
]

def template(contents, title, body):
    return render_template('home.html', contents=contents, title=title, body=body)

def temp(contents, title, author, body, id=None):
    if id != None:
        return render_template('index.html',contents=contents,title=title, author=author, body=body, id=id)
    return render_template('index.html',contents=contents,title=title, author=author, body=body,)

def create_book():
    return render_template('create.html')

@app.route('/')
def index():
    title = ''
    body = '''줄이 길어지면 스크롤이 생기니까 패딩말고 그냥 제일 아래에 붙어있게 할 수 있는 걸 찾아야함'''
    for topic in topics:
        title = topic['title']
    return template(topics, title, body)

@app.route('/read/<int:id>/') 
def read(id):
    title = ''
    body = ''
    author = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            author = topic['author']
            body = topic['body']
            break
    return temp(topics, title, author, body, id)

@app.route('/create/', methods=['GET', 'POST']) 
def create():
    if request.method == 'GET': 
        return create_book()
    elif request.method == 'POST':
        global nextId
        title = request.form['title']
        author = request.form['author']
        body = request.form['body']
        newTopic = {'id': nextId, 'title': title, 'author': author,'body': body}
        topics.append(newTopic)
        url = '/read/'+str(nextId)+'/'
        nextId = nextId + 1
        return redirect(url)

@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    if request.method == 'GET':
        topic = next((t for t in topics if t['id'] == id), None)
        if topic:
            return render_template('update.html', id=id, title=topic['title'], author=topic['author'], body=topic['body'])
    elif request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        body = request.form['body']
        
        for topic in topics:
            if topic['id'] == id:
                topic['title'] = title
                topic['author'] = author
                topic['body'] = body
                break
        
        return redirect(f'/read/{id}/')

@app.route('/delete/<int:id>/', methods=['POST']) 
def delete(id):
    for topic in topics:
        if id == topic['id']:
            topics.remove(topic)
            break
    return redirect('/')


app.run(debug=True)