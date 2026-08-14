import logging
from zeep import Client
from zeep.helpers import serialize_object
import xml.etree.ElementTree as ET
import xml.dom.minidom

logging.basicConfig(level=logging.DEBUG)
logging.getLogger('zeep.transports').setLevel(logging.DEBUG)

# Ativa o log para ver o XML completo
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('zeep.transports').setLevel(logging.DEBUG)

wsdl = "http://localhost:8080/g5-senior-services/sapiens_SyncFabioTeste?wsdl"
client = Client(wsdl)

nome_fornecedor = input("Digite o nome do fornecedor: ")

result = client.service.Teste(
    user="senior",
    password="senior",
    encryption=0,
    parameters={
                "flowInstanceID": "",
                "flowName": "",
                "nomFor": nome_fornecedor
    }
)
# ── Salvar retorno em XML ──────────────────────────────────
dados = serialize_object(result)  # converte objeto Zeep para dict

# Monta o XML
root = ET.Element("retorno")
for chave, valor in dados.items():
    filho = ET.SubElement(root, str(chave))
    filho.text = str(valor) if valor is not None else ""

# Formata o XML com indentação (pretty print)
xml_str = xml.dom.minidom.parseString(
    ET.tostring(root, encoding="unicode")
).toprettyxml(indent="  ")

# Salva o arquivo
with open("Fabiows.xml", "w", encoding="utf-8") as f:
    f.write(xml_str)

print("\n✅ Arquivo Fabiows.xml gerado com sucesso!")