import re

Class ExtratorURL:
  def __init__(self, url):
    self.url = self.sanitiza_url(url)
    self.valida_url()


  def sanitiza_url(self,url):
    if type(url) == str:
      return url.strip()
    else: 
      return ""


  def valida_url(self):
    if not self.url:
      raise ValueError("A URL está vazia")

      url_padrao = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
      busca_url_padrao = url_padrao.match(self.url)
    if not busca_url_padrao:
      raise ValueError("A URL não é válida")
      

  def get_url_base(self):
    indice_interrogacao = self.url.find('?')
    url_base = self.url[:indice_interogaçao]


  def get_url_parametros(self):
    indice_interrogacao = self.url.find('?')
    url_parametros = self.url[indice_interrogacao +1:]


  def get_valor_parametro(self, parametro_busca):
    indice_parametro = self.get_url_parametros().find(parametro_busca)
    indice_valor = indice_parametro + len()
    indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
    if indice_e_comercial == -1:
      valor = self.get_url_parametros()[indice_valor:]
    else:
      valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
    return valor


extrator_url = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
valor_quantidade = extrator_url.get.url_parametro('quantidade')
print(valor_quantidade)
    




