from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
#below-connection string used to connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:nia0813@localhost:8889/build-a-blog'
app.config['SQLAlCHEMY_ECHO'] = True #turns on query logging
db = SQLAlchemy(app)#connects the constructor to the app

class Blog(db.Model):# extends the blog class to the database model class

    id = db.Column(db.Integer, primary_key=True)#this will be an integer in this column unique to each blog
    title = db.Column (db.String (150))#title of blog that is created with 150 varchar max
    body = db.Column(db.String(1000))# the body of the blog with 1000 varchar max
    

    def __init__(self, title, body):
        self.title = title
        self.body = body
        

#blog displays post
@app.route('/blog', methods = ['GET'])
def blog_list():
    blog_id = request.args.get('id')
    if (blog_id):
        sin_blog = Blog.query.filter_by(id=blog_id).first()
        return render_template('singleblog.html', sin_blog = sin_blog)
    else:
        all_blogs= Blog.query.all()
        return render_template('blog.html', blogs = all_blogs)

def empty_field(self):
    if self:
        return True
    else:
        return False

@app.route('/newpost', methods=['POST','GET'])
def new_blog():
    if request.method == 'POST':
        title_error = ""
        entry_error = ""
        new_title = request.form['blog_title']
        new_body = request.form['body_blog']
        new_blog = Blog(new_title, new_body)
        print (new_title)
        if empty_field(new_title) and empty_field(new_body):
            db.session.add(new_blog)
            db.session.commit()
            blog_link = "/blog?id=" + str(new_blog.id)
            return redirect(blog_link)
        else:
            if not empty_field(new_title) and not empty_field(new_body):
                title_error = "Please enter blog title"
                entry_error = "Please enter blog text"
                return render_template('newpost.html',title_error=title_error, entry_error=entry_error)
            elif not empty_field(new_title):
                title_error = "Please enter blog title"
                return render_template('newpost.html',title_error=title_error,new_body=new_body)
            elif not empty_field(new_body):
                entry_error = "Please enter blog text"
                return render_template('newpost.html', entry_error=entry_error,new_title=new_title)
    return render_template('newpost.html', title= "Build A Blog")
       

    
   # return redirect('/blog')




    

     #call blog from database
    
        
#blog displays form to fill


if __name__=='__main__':#allow us to use the functions in other projects without starting up the app
    app.run()