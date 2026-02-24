from models.database import Database
from typing import Optional, Self, Any
from sqlite3 import Cursor

class Desejo:
    """
        Classe para representar um Desejo, com métodos para salvar, obter, excluir tarefas em um banco de dados usando a classe `Database`.
    """
    def __init__(self: Self, titulo_desejo: Optional[str], tipo_desejo: Optional[str], indicado_por: Optional[str], id_desejo: Optional[int] = None, imagem: Optional[str] = None):
        self.titulo_desejo: Optional[str] = titulo_desejo
        self.tipo_desejo: Optional[str] = tipo_desejo
        self.indicado_por: Optional[str] = indicado_por
        self.imagem: Optional[str] = imagem
        self.id_desejo: Optional[int] = id_desejo

    @classmethod
    def id(cls, id: int) -> Self:
        with Database() as db:
            query: str = 'SELECT titulo_desejo, tipo_desejo, indicado_por, id_desejo, imagem FROM desejos WHERE id_desejo = ?;'
            params: tuple = (id,)
            resultado: list[Any] = db.buscar_tudo(query, params)

            [[titulo,tipo,indicado, id, imagem]] = resultado

        return cls(id_desejo=id, titulo_desejo=titulo, tipo_desejo=tipo, indicado_por=indicado, imagem=imagem)

    def salvar_lista(self: Self) -> None:
        with Database () as db:
            query: str = "INSERT INTO desejos (titulo_desejo, tipo_desejo, indicado_por, imagem)VALUES (?, ?, ?, ?);"
            params: tuple = (self.titulo_desejo, self.tipo_desejo, self.indicado_por, self.imagem)
            db.executar(query, params)

    @classmethod
    def obter_lista(cls) -> list[Self]:
        with Database() as db:
            query: str = 'SELECT titulo_desejo, tipo_desejo, indicado_por, id_desejo, imagem FROM desejos;'
            resultados: list[Any] = db.buscar_tudo(query)
            desejos: list[Self] = [cls(titulo_desejo, tipo_desejo, indicado_por, id_desejo, imagem) for titulo_desejo, tipo_desejo, indicado_por, id_desejo, imagem in resultados]
            return desejos
        
    def excluir_desejo(self) -> Cursor:
        with Database() as db:
            query: str = 'DELETE FROM desejos WHERE id_desejo = ?;'
            params:tuple = (self.id_desejo,)
            resultado: Cursor = db.executar(query, params)
            return resultado
        
    def atualizar_desejo(self) -> Cursor:
        with Database() as db:
            query: str = 'UPDATE desejos SET titulo_desejo = ?, tipo_desejo = ?, indicado_por = ?, imagem = ? WHERE id_desejo = ?;'
            params:tuple = (self.titulo_desejo, self.tipo_desejo, self.indicado_por, self.imagem, self.id_desejo)
            resultado: Cursor = db.executar(query, params)
            return resultado
        