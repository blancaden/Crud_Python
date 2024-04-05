from flask import Blueprint, request, jsonify, render_template, redirect, url_for

from src.services.ClientService import ClientService

from ..models.cliente import Cliente

main = Blueprint('client_blueprint',__name__)


@main.route('/', methods=['GET', 'POST', 'DELETE'])

def crud_cliente():

 
    if request.method == 'GET':
        
         clients = ClientService.get_clientes()
         return render_template('index.html', clients=clients)
      
      
    elif request.method== 'POST':
            form_type = request.form['form_type']
            print('ddddddddddd')
            print(form_type)
            if form_type == 'POST':
                dni_cliente = ''
                nombre = request.form['nombre']
            # print(nombre)
            # return ('esto es el post')
                email = request.form['email']
                telefono = request.form['telefono']
                direccion = request.form['direccion']
    
                cliente = Cliente(dni_cliente=dni_cliente,nombre=nombre, email=email, telefono=telefono, direccion=direccion)
                result= ClientService.post_client(cliente)
           
                if result:
                    return jsonify({'message': 'Cliente agregado correctamenTEEE'}), 200
                else:
                    return jsonify({'error': 'Error al agregar el cliente'}), 500
            elif form_type == 'DELETE':
                    print("esto es delete")
                    dni_cliente = request.form['clientelis']
                    print(dni_cliente)
                    print('gggggggggggggggg')
                    delete_result = ClientService.delete_client(dni_cliente)
                    if delete_result:
                        return jsonify({'message': 'Cliente eliminado correctamente'}), 200
                    else:
                        return jsonify({'error': 'Error al eliminar el cliente'}), 500
            elif form_type == 'UPDATE':
                    print("ESTO ES UPDATE")
                    dni_cliente = request.form['id_cliente']
                    # dni_cliente = 42
                    print(dni_cliente)
                    nombre = request.form['nombre']
                    print(nombre)
                    email = request.form['email']
                    telefono = request.form['telefono']
                    direccion = request.form['direccion']
    
                    cliente = Cliente(dni_cliente=dni_cliente,nombre=nombre, email=email, telefono=telefono, direccion=direccion)
                    result_edit= ClientService.editar_clientes(cliente)
                    if result_edit:
                        return jsonify({'message': 'Cliente actualizado correctamente'}), 200
                    else:
                        return jsonify({'Error al actualizar el cliente'}), 500
           
#RUTA PARA GUARDAR USUARIOS EN LA BASE DE DATOS
# @main2.route('/clients', methods=['POST'])  
# def addCliente():
#    try:
#     nombre = request.form['nombre']
#     email = request.form['email']
#     telefono = request.form['telefono']
#     direccion = request.form['direccion']
    
#     cliente = Cliente(nombre=nombre, email=email, telefono=telefono, direccion=direccion)
#     result= ClientService.post_client(cliente)
#     if result:
#             return jsonify({'message': 'Cliente agregado correctamente'}), 200
#     else:
#             return jsonify({'error': 'Error al agregar el cliente'}), 500

#    except Exception as ex:
#     print(ex)

#intentofront   
# @main.route('/clients', methods=['POST'])
# def add_clients():
  
#         try:
#             nombre = request.form['nombre']
#             email = request.form['email']
#             telefono = request.form['telefono']
#             direccion = request.form['direccion']

#             cliente = Cliente(0, nombre, email, telefono, direccion)
#             result= ClientService.post_client(cliente)
#             # return redirect(url_for('client_blueprint.get_client'))
#             return (result)
#         except Exception as ex:
#             print(ex)
  #intentofront          
  #válido
    # try:
        
    #     clients = ClientService.get_client()
        
    #     print(clients)
        
    #     return render_template('index.html', clients=clients)
    # except Exception as ex:
    #     print(ex)
      #válido  

    # ClientService.get_client()
    # print(request.json)

    # nombre = request.json['nombre']
    # email = request.json['email']
    # telefono = request.json['telefono']
    # direccion = request.json['direccion']

    # print(nombre)
    # print(email)
    # print(telefono)
    # print(direccion)

    # cliente = Cliente(0,nombre,email,telefono,direccion)

    # if request.method == 'GET':
    #    get_client=ClientService.get_client()
    #    print(get_client)

    # elif request.method == 'POST':

    #     post_client=ClientService.post_client(cliente)
    #     print(post_client)
        
    # return 'Esto se ve en la página web'

   
   