# Flask para aplicacion web
from flask import Flask, render_template, request, redirect, url_for
# SQLAlchemy como ORM
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
########### Para crear la Base de Datos ###########
# En consola : 
# sqlite3 database/task.db
# *Ya tener el directorio /database

# Instancia la base de datos - /// -> Para que use el lenguak¿je de sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/dates.db'

db = SQLAlchemy(app)

# Modelo de la base de datos
class Registro(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    nombre     = db.Column(db.String(200))
    apellido   = db.Column(db.String(200))
    contrasena   = db.Column(db.String(200))
    email   = db.Column(db.String(200))
    done        = db.Column(db.Boolean)

class Publicana_post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_empresa = db.Column(db.String(200))
    descripcion_del_trabajo = db.Column(db.String(200))
    categoria_del_trabajo = db.Column(db.String(200))
    modalidad = db.Column(db.String(200))
    monto = db.Column(db.String())
    is_active = db.Column(db.Boolean)

class Ensenana(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    denominacion_del_curso   = db.Column(db.String(200))
    descripcion_del_curso   = db.Column(db.String(200))
    modulos   = db.Column(db.String(200))
    duracion   = db.Column(db.Integer())
    area   = db.Column(db.String(200))
    done        = db.Column(db.Boolean)

# Para renderizar la vista

@app.route("/")     #Llamabamos al metodo route y le pasamos el argumento slug o url
def inicio(): #Creamos la funcion inicio
    #datos = Registro.query.all()
    return render_template('inicio.html')
            #Retornamos la renderizacion de un documento

@app.route("/contrataNabuscar")
def contratana_buscar():
    #datos1 = Contrata.query.all()
    return render_template('contrataNa_Buscar_o_publicar.html')

@app.route("/ensenana", methods=['POST'])
def ensenana():
    datos1 = Ensenana.query.all()
    datos1 = Ensenana(denominacion_del_curso = request.form['denominacion del curso'], descripcion_del_curso = request.form['descripcion del curso'], modulos = request.form['modulos'], duracion = request.form['duracion'], area = request.form['area'], done=False)
    db.session.add(datos1)
    db.session.commit()
    return render_template('ensenana.html')

@app.route("/ingresana", methods=['GET','POST'])
def ingresana():
    if request.method == 'POST':
        datos2 = Registro.query.all()
        datos2 = Registro(email = request.form['email'], contrasena = request.form['contrasena'], done=False)
        db.session.add(datos2)
        db.session.commit()
        return redirect(url_for('inicio'))
    else:
        return render_template('ingresana.html')

@app.route("/registratena", methods=['GET','POST'])
def registratena():
    if request.method == 'POST':
        
        datos3 = Registro.query.all()
        datos3 = Registro(nombre = request.form['nombre'], apellido = request.form['apellido'], contrasena = request.form['contrasena'], email = request.form['email'], is_active =False)
        db.session.add(datos3)
        db.session.commit() # Para que lo guarde/ejecute
        return redirect(url_for('inicio'))
    else:
        return render_template('registratena.html')

@app.route("/formulario", methods=['GET','POST'])
def formulario():
    if request.method == 'POST':
        datos4 = Registro(nombre = request.form['nombre'], apellido = request.form['apellido'], contrasena = request.form['contrasena'], email = request.form['email'], done=False)

        db.session.add(datos4)
        db.session.commit() # Para que lo guarde/ejecute
        return redirect(url_for('inicio'))
    else:
        return render_template('registratena.html')

@app.route("/contrataNaregistro")
def contratareg():
        return render_template('publicana.html')

@app.route("/informatena")
def informatena():
    return render_template('informatena.html')

@app.route('/contactana')
def contactana():
    return redirect(url_for('contactana.html'))


@app.route("/trabajana", methods=['GET'])
def trabajana():
    publicana = Publicana_post.query.all()
    return render_template('trabajana.html', publicana= publicana)

@app.route("/contratana")
def contratana():
    return render_template('contratana.html')

@app.route("/aprendena")
def aprendena():
    return render_template('aprendena.html')


@app.route("/contratana_menu")
def contratana_menu():
    return render_template('contratana_menu.html')


@app.route("/publicana",methods=['GET','POST'] )
def publicana():
    if request.method == 'POST':
        datos5 = Publicana_post(nombre_empresa = request.form['nombre_empresa'], descripcion_del_trabajo = request.form['descripcion_trabajo'], categoria_del_trabajo = request.form['categoria_trabajo'], modalidad = request.form['modalidad'], monto = request.form['monto'], is_active =False)
        db.session.add(datos5)
        db.session.commit() # Para que lo guarde/ejecute
        return redirect(url_for('trabajana'))
        #return render_template('trabajana.html')
    else:
        return render_template('trabajana.html')



@app.route("/profile_card2")
def profile_card2():
    return render_template('profile_card2.html')

@app.route("/prueba")
def prueba():
    if request.method == 'POST':
        datos6 = Publicana_post(
            nombre_empresa = request.form['nombre_empresa'],
            descripcion_del_trabajo = request.form['descripcion_trabajo'],
            categoria_del_trabajo = request.form['categoria_trabajo'],
            modalidad = request.form['modalidad'],
            monto = request.form['monto'],
            is_active =False)
        db.session.add(datos6)
        db.session.commit() # Para que lo guarde/ejecute
        return redirect(url_for('inicio'))
    else:
        return render_template('prueba.html')

@app.route("/buscana")
def buscana():
    return render_template('buscana.html')




if __name__ == "__main__":
    app.run(debug=True)