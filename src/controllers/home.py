from flask import request
from flask.json import jsonify
from src import app
from src.models.students import StudentsModel

@app.route('/usuario', methods=['GET'])
def getusuario():
   studentsModel = StudentsModel()
   usuario = studentsModel.Usuario()
   array_usuario=[]
   for elemento in usuario:
      array_usuario.append({
         "Id": elemento[0],
         "rol_id": elemento[1],
         "identificacion": elemento[2],
         "nombre": elemento[3],
         "apellido": elemento[4],
         "email": elemento[5],
         "semestre": elemento[6],
         "periodo": elemento[7]
      })

   return jsonify(array_usuario)

@app.route('/usuario', methods=['POST'])
def addUsuario():

   rol_id = request.json['rol_id']
   identificacion = request.json['identificacion']
   nombre = request.json['nombre']
   apellido = request.json['apellido']
   email = request.json['email']
   semestre = request.json['semestre']
   periodo = request.json['periodo']   

   try: 
      studentsModel = StudentsModel()
      studentsModel.crearUsuario(rol_id, identificacion, nombre, apellido, email, semestre, periodo)
   except:
      return jsonify({'message':'Error'})

   
   return jsonify({'message':'Usuario Creado Satisfactoriamente...','Usuario':{'identificacion': identificacion, 'nombre': nombre,'apellido': apellido, 'email': email, 'semestre': semestre, 'periodo': periodo}})



@app.route('/usuario/<id>', methods=['PUT'])
def updateUsuario(id):
   studentsModel = StudentsModel()
   usuario = studentsModel.getUsuario(id)

   #rol_id = request.json['rol_id']
   identificacion = request.json['identificacion']
   nombre = request.json['nombre']
   apellido = request.json['apellido']
   email = request.json['email']
   semestre = request.json['semestre']
   periodo = request.json['periodo']

   if identificacion == '':
      identificacion = usuario[2]
   if nombre == '':
      nombre = usuario[3]
   if apellido == '':
      apellido = usuario[4]
   if email == '':
      email = usuario[5]
   if semestre == '':
      semestre = usuario[6]
   if periodo == '':
      periodo = usuario[7]

   try:
      studentsModel.updateUsuario(id, identificacion, nombre, apellido, email, semestre, periodo)
   except:
      return jsonify({'message':'Error'})

   return jsonify({'message':'Usuario Editado Satisfactoriamente...','Usuario':{'identificacion': identificacion, 'nombre': nombre,'apellido': apellido, 'email': email, 'semestre': semestre, 'periodo': periodo}})   

@app.route('/usuario/<id>', methods=['DELETE'])
def deleteUsuario(id):
   studentsModel = StudentsModel()
   studentsModel.deleteUsuario(id)

   return jsonify({'message':'Usuario Eliminado Satisfactoriamente...'})

#------------------------ESPACIO ACADEMICO--------------------------------------------
@app.route('/espacio_academico', methods=['GET'])
def espacio_academico():
   studentsModel = StudentsModel()
   espacio_academico = studentsModel.espacio_academico()

   arrayespacio_academico = []   
   for elemento in espacio_academico:
      arrayespacio_academico.append({
         "Id": elemento[0],
         "Espacio Academico": elemento[1],
         "Semestre": elemento[2],
         "Programa": elemento[3],
      })

   return jsonify(arrayespacio_academico)

@app.route('/espacio_academico', methods=['POST'])
def addespacio_academico():
   studentsModel = StudentsModel()
   
   nombre = request.json['nombre']
   semestre = request.json['semestre']
   curso_id = request.json['curso_id']

   studentsModel.crearEspacio_academico(nombre,semestre,curso_id)

   return jsonify({'message':'Espacio Academico Creado Satisfactoriamente...','Espacio Academico':{'nombre': nombre, 'semestre': semestre, 'curso_id': curso_id}})

@app.route('/espacio_academico/<id>', methods=['PUT'])
def updateEspacio_academico(id):
   studentsModel = StudentsModel()
   espacio_academico = studentsModel.getEspacio_academico(id)

   nombre = request.json['nombre']
   semestre = request.json['semestre']
   curso_id = request.json['curso_id']

   if nombre == '':
      nombre = espacio_academico[1]
   if semestre == '':
      semestre = espacio_academico[2]
   if curso_id == '':
      curso_id = espacio_academico[3]

   try:
      studentsModel.updateEspacio_academico(id, nombre, semestre, curso_id)
   except:
      return jsonify({'message':'Error'})

   return jsonify({'message':'Espacio Academico Editado Satisfactoriamente...','Espacio Academico':{'nombre': nombre,'semestre': semestre, 'curso_id': curso_id}})


@app.route('/espacio_academico/<id>', methods=['DELETE'])
def deleteEspacio_academico(id):
   studentsModel = StudentsModel()
   studentsModel.deleteEspacio_academico(id)

   return jsonify({'message':'Espacio Academico Eliminado Satisfactoriamente...'})

#------------------------CURSO (CARRERA O TECNOLOGIA)--------------------------------------------
@app.route('/cursos', methods=['GET'])
def cursos():
   studentsModel = StudentsModel()
   cursos = studentsModel.cursos()
   array_cursos=[]
   for elemento in cursos:
      array_cursos.append({
         "Id": elemento[0],
         "Programa": elemento[1]
      })

   return jsonify(array_cursos)

@app.route('/cursos', methods=['POST'])
def addcursos():
   
   nombre = request.json['nombre']
   
   studentsModel = StudentsModel()
   studentsModel.crearCursos(nombre)

   return jsonify({'message':'Curso Creado Satisfactoriamente...'})

@app.route('/cursos/<id>', methods=['PUT'])
def updateCursos(id):
   studentsModel = StudentsModel()
   cursos = studentsModel.getCursos(id)

   nombre = request.json['nombre']

   if nombre == '':
      nombre = cursos[1]
   
   try:
      studentsModel.updateCursos(id, nombre)
   except:
      return jsonify({'message':'Error'})

   return jsonify({'message':'Curso Editado Satisfactoriamente...','Curso':{'nombre': nombre}})

@app.route('/cursos/<id>', methods=['DELETE'])
def deleteCursos(id):
   studentsModel = StudentsModel()
   studentsModel.deleteCursos(id)

   return jsonify({'message':'Curso Eliminado Satisfactoriamente...'})

#------------------SESION------------------------
@app.route('/sesion', methods=['GET'])
def sesion():
   studentsModel = StudentsModel()
   session = studentsModel.sesion()
   sesion = studentsModel.listaSesion()
   array_Sesion=[]
   for elemento in sesion:
      array_Sesion.append({
         "Id": elemento[0],
         "Docente": elemento[1],
         "Espacio Academico": elemento[2],
         "Fecha": elemento[3],
         "Hora Inicial": elemento[4],
         "Hora Final": elemento[5]
      })

   return jsonify(array_Sesion)

@app.route('/sesion', methods=['POST'])
def addsesion():
   
   docente_id = request.json['docente_id']
   espacioac_id = request.json['espacioac_id']
   fecha = request.json['fecha']
   hora_inicial = request.json['hora_inicial']
   hora_final = request.json['hora_final']
   
   studentsModel = StudentsModel()
   studentsModel.crearSesion(docente_id, espacioac_id, fecha, hora_inicial, hora_final)

   return jsonify({'message':'Sesion Creada Satisfactoriamente...'})

@app.route('/sesion/<id>', methods=['PUT'])
def updateSesion(id):
   studentsModel = StudentsModel()
   sesion = studentsModel.getSesion(id)

   docente_id = request.json['docente_id']
   espacioac_id = request.json['espacioac_id']
   fecha = request.json['fecha']
   hora_inicial = request.json['hora_inicial']
   hora_final = request.json['hora_final']

   if docente_id == '':
      docente_id = sesion[1]
   if espacioac_id == '':
      espacioac_id = sesion[2]
   if fecha == '':
      fecha = sesion[3]
   if hora_inicial == '':
      hora_inicial = sesion[4]
   if hora_final == '':
      hora_final = sesion[5]
   
   try:
      studentsModel.updateSesion(id, docente_id, espacioac_id, fecha, hora_inicial, hora_final)
   except:
      return jsonify({'message':'Error'})

   return jsonify({'message':'Sesion Editada Satisfactoriamente...','Curso':{'docente_id': docente_id,'espacioac_id': espacioac_id,'fecha': fecha,'hora_inicial': hora_inicial,'hora_final': hora_final}})

@app.route('/sesion/<id>', methods=['DELETE'])
def deleteSesion(id):
   studentsModel = StudentsModel()
   try:
      studentsModel.deleteSesion(id)
   except:
      return jsonify({'message':'Error de llaves foraneas, primero eliminar la asistencia de la sesion para así poder eliminar esta sesion'})

   return jsonify({'message':'Sesion Eliminada Satisfactoriamente...'})

#-----------------------ASISTENCIA-----------------------------
@app.route('/asistencia', methods=['GET'])
def asistencia():
   studentsModel = StudentsModel()
   asistencia = studentsModel.asistencia()

   arrayAsistencia = []   
   for asistencia in asistencia:
      arrayAsistencia.append({
         "Id": asistencia[0],
         "Fecha de la Sesion": asistencia[1],
         "Estudiante": asistencia[2]
      })

   return jsonify(arrayAsistencia)
#[(1, 1, 1), (2, 2, 2)]
@app.route('/asistencia', methods=['POST'])
def addasistencia():
   studentsModel = StudentsModel()   
   sesion_id = request.json['sesion_id']
   estudiante_id = request.json['estudiante_id']

   studentsModel.crearAsistencia(sesion_id, estudiante_id)

   return jsonify({'message':'Asistencia Creada Satisfactoriamente...'})

@app.route('/asistencia/<id>', methods=['PUT'])
def updateAsistencia(id):
   studentsModel = StudentsModel()
   asistencia = studentsModel.getAsistencia(id)

   sesion_id = request.json['sesion_id']
   estudiante_id = request.json['estudiante_id']

   if sesion_id == '':
      sesion_id = asistencia[1]
   if estudiante_id == '':
      estudiante_id = asistencia[2]
   
   try:
      studentsModel.updateAsistencia(id, sesion_id, estudiante_id)
   except:
      return jsonify({'message':'Error'})

   return jsonify({'message':'Asistencia Editada Satisfactoriamente...','Asistencia':{'sesion_id': sesion_id,'estudiante_id': estudiante_id}})

@app.route('/asistencia/<id>', methods=['DELETE'])
def deleteAsistencia(id):
   studentsModel = StudentsModel()
   studentsModel.deleteAsistencia(id)

   return jsonify({'message':'Asistencia Eliminada Satisfactoriamente...'})

@app.route('/asistencia/<sesion_id>', methods=['GET'])
def Sesion_Asistencia(sesion_id):
   studentsModel = StudentsModel()
   asistencia = studentsModel.asistenciaSesion(sesion_id)
   sesion = studentsModel.sesion_docente_ea(sesion_id)
   arraySesion = []

   session = ({
      "Docente": sesion[0],
      "Materia": sesion[1],
      "Fecha": sesion[2],
      "Hora Inicial": sesion[3],
      "Hora Final": sesion[4]
   })
 
   for a in asistencia:
      arraySesion.append({
         "estudiante": a[0]
      })

   return jsonify({'Sesion': session,'Asistencia': arraySesion})

