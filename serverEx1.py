# -*- coding: cp1252 -*-
'''
    Exemplo básico de servidor web
    -- trata apenas o método GET
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

### em caso de url inválida 
notfound = "File not found"

def resposta(path):
    a = consulta(queryparser.parse(path))
    return json.dumps(a, indent=8)
'''
    classe que estende BaseHHTPRequestHandler:
    -- redefine o método do_Get() para que faça o tratamento desejado
    -- os demais métodos da biblioteca são mantidos 'as is'.
'''
class ServidorExemplo1(BaseHTTPServer.BaseHTTPRequestHandler):

        def do_GET(self):
                # inicia o envio da resposta c/ código de retorno 200 (OK)
                self.send_response(200)
                # define o cabeçalho da resposta (neste caso 'avisa' que o conteúdo será html)
                self.send_header("Content-type","text/html")
                # 'fecha' o cabeçalho
                self.end_headers()
                # 'escreve' o conteudo da resposta
                self.wfile.write(resposta(self.path))
'''
    Cria o servidor web, usando a classe definida acima,
    atendendo as requisições na porta 8080
'''
httpserver = BaseHTTPServer.HTTPServer(("",8080), ServidorExemplo1)

'''
    Ativa o serviço, 'ad infinitum' 
'''
httpserver.serve_forever()

