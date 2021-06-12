from flask.json import jsonify
#, jsonify, request
from src.config.db import DB

#from src.models.students import students

cursor = DB.cursor()
class StudentsModel():
    
    def getUsuario(self, id):

        cursor.execute('select * from usuario where id = ?',(id,))
        usuario = cursor.fetchone()
    
        return usuario

    def Usuario(self):
        
        cursor.execute('select * from usuario')
        usuario = cursor.fetchall()
        
        return usuario

    def crearUsuario(self, rol_id, identificacion, nombre, apellido, email, semestre, periodo):

        cursor.execute('insert into usuario(rol_id, identificacion, nombre, apellido, email, semestre, periodo) values(?,?,?,?,?,?,?)',(rol_id, identificacion, nombre, apellido, email, semestre, periodo,))
      
    def updateUsuario(self, id, identificacion, nombre, apellido, email, semestre, periodo):

        cursor.execute('update usuario set identificacion = ?, nombre = ?, apellido = ?, email = ?, semestre = ?, periodo = ? where id = ?',(identificacion, nombre, apellido, email, semestre, periodo,id,))

    def deleteUsuario(self, id):
        cursor.execute('delete from usuario where id = ?',(id,))
#------------------------ESPACIO ACADEMICO--------------------------------------------
    def espacio_academico(self):
        cursor.execute('SELECT espacio_academico.id,espacio_academico.nombre, espacio_academico.semestre,curso.nombre FROM espacio_academico INNER JOIN curso ON espacio_academico.curso_id = curso.id')
        espacio_academico = cursor.fetchall()
        return espacio_academico

    def crearEspacio_academico(self, nombre, semestre, curso_id):
        cursor.execute('insert into espacio_academico(nombre, semestre, curso_id) values(?,?,?)',(nombre, semestre, curso_id,))

    def updateEspacio_academico(self, id, nombre, semestre, curso_id):
        cursor.execute('update espacio_academico set nombre = ?, semestre = ?, curso_id = ? where id = ?',(nombre, semestre, curso_id,id,))

    def getEspacio_academico(self, id):
        cursor.execute('select * from espacio_academico where id = ?',(id,))
        espacio_academico = cursor.fetchone()
        return espacio_academico

    def deleteEspacio_academico(self, id):
        cursor.execute('delete from espacio_academico where id = ?',(id,))
#------------------------CURSO (CARRERA O TECNOLOGIA)--------------------------------------------
    def cursos(self):
        cursor.execute('select * from curso')
        cursos = cursor.fetchall()
        return cursos
    
    def crearCursos(self, nombre):
        cursor.execute('insert into curso(nombre) values(?)',(nombre,))

    def updateCursos(self, id, nombre):
        cursor.execute('update curso set nombre = ? where id = ?',(nombre,id,))

    def getCursos(self, id):
        cursor.execute('select * from curso where id = ?',(id,))
        cursos = cursor.fetchone()
        return cursos

    def deleteCursos(self, id):
        cursor.execute('delete from curso where id = ?',(id,))
#-----------------------------SESION----------------------
    def sesion(self):
        cursor.execute('select * from sesion')
        sesion = cursor.fetchall()
        return sesion
    
    def crearSesion(self, docente_id, espacioac_id, fecha, hora_inicial, hora_final):
        cursor.execute('insert into sesion(docente_id, espacioac_id, fecha, hora_inicial, hora_final) values(?,?,?,?,?)',(docente_id, espacioac_id, fecha, hora_inicial, hora_final,))

    def updateSesion(self, id, docente_id, espacioac_id, fecha, hora_inicial, hora_final):
        cursor.execute('update sesion set docente_id = ?,espacioac_id = ?,fecha = ?,hora_inicial = ?,hora_final = ? where id = ?',(docente_id, espacioac_id, fecha, hora_inicial, hora_final,id,))

    def getSesion(self, id):
        cursor.execute('select * from sesion where id = ?',(id,))
        cursos = cursor.fetchone()
        return cursos

    def deleteSesion(self, id):
        cursor.execute('delete from sesion where id = ?',(id,))
#----------------------------ASISTENCIA-----------------------------

    def asistencia(self):
        cursor.execute('SELECT asistencia.id,sesion.fecha,usuario.nombre FROM asistencia INNER JOIN usuario ON asistencia.estudiante_id = usuario.id INNER JOIN sesion ON asistencia.sesion_id = sesion.id ORDER BY sesion.fecha DESC')
        cursos = cursor.fetchall()
        return cursos
    
    def crearAsistencia(self, sesion_id, estudiante_id):
        cursor.execute('insert into asistencia(sesion_id, estudiante_id) values(?,?)',(sesion_id, estudiante_id,))

    def updateAsistencia(self, id, sesion_id, estudiante_id):
        cursor.execute('update asistencia set sesion_id = ?, estudiante_id = ? where id = ?',(sesion_id, estudiante_id,id,))

    def getAsistencia(self, id):
        cursor.execute('select * from asistencia where id = ?',(id,))
        cursos = cursor.fetchone()
        return cursos

    def deleteAsistencia(self, id):
        cursor.execute('delete from asistencia where id = ?',(id,))

    def getAsistencia_Sesion(self, sesion_id):
        cursor.execute('select * from asistencia where sesion_id = ?',(sesion_id,))
        cursos = cursor.fetchall()
        return cursos

    def asistenciaSesion(self, sesion_id):
        cursor.execute('SELECT usuario.nombre FROM asistencia INNER JOIN usuario ON asistencia.estudiante_id = usuario.id WHERE sesion_id = ?',(sesion_id,))
        cursos = cursor.fetchall()
        return cursos

    def sesion_docente_ea(self,sesion_id):
        cursor.execute('SELECT u.nombre,e_a.nombre,sesion.fecha,sesion.hora_inicial,sesion.hora_final FROM sesion INNER JOIN usuario AS u ON sesion.docente_id = u.id INNER JOIN espacio_academico as e_a ON sesion.espacioac_id = e_a.id WHERE sesion.id = ?',(sesion_id,))
        cursos = cursor.fetchone()
        return cursos
#------------Listas--------------------
    def listaSesion(self):
        cursor.execute('SELECT sesion.id,u.nombre,e_a.nombre,sesion.fecha,sesion.hora_inicial,sesion.hora_final FROM sesion INNER JOIN usuario AS u ON sesion.docente_id = u.id INNER JOIN espacio_academico as e_a ON sesion.espacioac_id = e_a.id')
        cursos = cursor.fetchall()
        return cursos
