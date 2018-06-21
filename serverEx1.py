# -*- coding: cp1252 -*-
'''
    Exemplo b�sico de servidor web
    -- trata apenas o m�todo GET
    -- responde com um texto html fixo (htmlpage)
'''
import BaseHTTPServer
import BaseHTTPServer, json, os, fnmatch
import queryparser

### texto fixo retornado como resposta ao get
#def resposta(cep):
#    parms = queryparser.parse(cep)
 #   return parms

def consulta(path):
    file = 0
    #@print path
  #  while file != consulta:
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.json'):
            f = open(file)
            txt = f.read()
            lista = json.loads(txt)
            for d in lista:
                for value in d.values():
                    if value==path:
                        return d
                        #print json.dumps(d, sort_keys=True, indent=4)
                        #return 'CEP:',d['CEP'],'Cidade:',d['Cidade'],'Bairro:',d['Bairro'],'Estado:',d['Estado']

### em caso de url inv�lida 
notfound = "File not found"

def resposta(path):
    a = consulta(queryparser.parse(path))
    return json.dumps(a, indent=8)
'''
    classe que estende BaseHHTPRequestHandler:
    -- redefine o m�todo do_Get() para que fa�a o tratamento desejado
    -- os demais m�todos da biblioteca s�o mantidos 'as is'.
'''
class ServidorExemplo1(BaseHTTPServer.BaseHTTPRequestHandler):

        def do_GET(self):
                # inicia o envio da resposta c/ c�digo de retorno 200 (OK)
                self.send_response(200)
                # define o cabe�alho da resposta (neste caso 'avisa' que o conte�do ser� html)
                self.send_header("Content-type","text/html")
                # 'fecha' o cabe�alho
                self.end_headers()
                # 'escreve' o conteudo da resposta
                self.wfile.write(resposta(self.path))
'''
    Cria o servidor web, usando a classe definida acima,
    atendendo as requisi��es na porta 8080
'''
httpserver = BaseHTTPServer.HTTPServer(("",8080), ServidorExemplo1)

'''
    Ativa o servi�o, 'ad infinitum' 
'''
httpserver.serve_forever()

