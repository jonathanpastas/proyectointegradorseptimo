
from flask import Flask, render_template, request, session, redirect, url_for
from bdd import queryDatos,menuopciones,perfiluser

app = Flask(__name__)
app.secret_key='jsp1234'

@app.route('/')
def index() -> 'html':
    return render_template('inicial.html', titulo='Sistema de Planificación de Pedidos')

@app.route('/info')
def info() -> 'html':
    return render_template('infopro.html', titulo='Sistema de Planificación de Pedidos')

@app.route('/login')
def login()-> 'html':
    return render_template('login.html')

@app.route('/ingresar' ,methods=['POST'])
def ingreso() -> 'html':
  user=request.form['correo']
  clave = request.form['clave']
  validar=queryDatos(user,clave)
  #print(validar)
  perfil=perfiluser(user)
  #print(perfil)

  if validar == True:
      session['username']=user
      session['pass']=clave
      session['perfil']=perfil
      return redirect(url_for('paginicio'))
  else :
       return  redirect(url_for('login'))


@app.route('/inicio')
def paginicio() -> 'html':

    if 'username' in session :
        print("true")
        menu=menuopciones(str(session['perfil']))
        usuario=session['username']
        return render_template('index.html', menu=menu,user=usuario)


    else :
        return redirect(url_for('index'))

################################# Metodo para cerrar la Sesion #######################################################
@app.route('/logout')
def salir() ->'html':
    session.clear()
    return redirect(url_for('index'))

###########################Ruta de Pruebas ############################################################################
@app.route('/pruebas')
def pruebitas()->'html':
    p="<button type=\"button\" class=\"btn btn-outline-primary\">Primary</button>"
    print(p)
    return render_template('inicios.html')

#######################################################################################################################


app.run(debug=True)

