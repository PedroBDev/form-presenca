from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired, Optional
from flask import request
import json

caminho_arquivo = "confirmados.json"

class PresencaForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    confirmacao = SelectField('Confirmacao', choices=[
            ("sim", "Sim"),
            ("nao", "Não")
        ], validators=[DataRequired()])
    quantidade = IntegerField('Quantidade', validators=[Optional()])
    observacao = TextAreaField('Observacao', validators=[Optional()])
    submit = SubmitField('Salvar')
    
    def save(self):
            
        dados = {
            "nome" : self.nome.data,
            "telefone" : self.telefone.data,
            "confirmacao" : self.confirmacao.data,
            "quantidade" : self.quantidade.data,
            "observacao" : self.observacao.data
            }
        
        try :
            with open (caminho_arquivo, "r", encoding="utf-8") as arquivo:
                lista = json.load(arquivo)
        except:
            lista = []
            
        lista.append(dados)
        
        
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(lista, arquivo, ensure_ascii=False, indent=4)
        
    