from flask import Flask, request, redirect,render_template

app = Flask(__name__)

nextId = 4
topics = [
    {'id': 1, 'title': '마시멜로 이야기', 'author': '호아킨', 'body': '마시멜로 이야기는 찰리과 조나단이..'},
    {'id': 2, 'title': '마시멜로 두번째 이야기', 'author':'호아킨, 엘런싱어' ,'body': '마시멜로 두번째 이야기는 찰리가 대학을 졸업하고..'},
    {'id': 3, 'title': '청소년을 위한 지금 시작하는 인문학', 'author':'주현성', 'body': '청소년을 위한 지금 시작하는 인문학은 세계의 역사와 인간이 철학을 한 이유 철학을 통하여 얻은 것들..'}
    
]

def template(contents, content):
    contentsUI = ''  
    if id != None:
        return f'''<!doctype html>  
        <html>                      
            <body>
                <h1><a href="/">the books I read</a></h1>
                <ol>
                    {contents}
                </ol>
                {content}
                <ul>
                    <li><a href="/create/">create</a></li>
                    {contentsUI}
                </ul>
            </body>
        </html>
        '''
def temp(contents, title, author, body, id=None):
    if id != None:
        return render_template(f'index.html',contents=contents,title=title, author=author, body=body, id=id)
    return render_template(f'index.html',contents=contents,title=title, author=author, body=body,)

def getContents():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags

@app.route('/')
def index():
    return template(getContents(), '책을 읽으며..(다음에 읽을 책 추가하기)')

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
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="author" placeholder="author"></textarea></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="create"></p>
            </form>
        '''
        return template(getContents(), content)
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