from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from preditiva_licitacoes_schemas.orgao import OrgaoCreate, Orgao
from preditiva_licitacoes_schemas.produto import ProdutoCreate, Produto


class LicitacaoBase(BaseModel):
    cd_plataforma_categoria: Optional[str] = None
    nm_plataforma_categoria: Optional[str] = None
    nr_cnpj_plataforma: Optional[str] = None
    nm_empresa_plataforma: Optional[str] = None
    ds_url: Optional[str] = None

    cd_licitacao: Optional[str] = None
    cd_licitacao_plataforma: Optional[str] = None

    nr_cnpj_comprador: Optional[str] = None
    nm_comprador: Optional[str] = None

    nm_cotacao_situacao: Optional[str] = None
    ds_objeto: Optional[str] = None
    dt_publicacao: Optional[datetime] = None
    dt_licitacao: Optional[datetime] = None
    dt_limite_proposta: Optional[datetime] = None
    dt_limite_impugnacao: Optional[datetime] = None
    ds_tratamento_diferenciado: Optional[str] = None

    ds_criterio_julgamento: Optional[str] = None
    nm_cotacao_categoria: Optional[str] = None
    nm_autoridade_competente: Optional[str] = None
    nm_pregoeiro: Optional[str] = None
    nm_licitacao_modalidade: Optional[str] = None
    fl_aplicar_cotas: Optional[str] = None
    cd_uasg: Optional[str] = None


class LicitacaoCreate(LicitacaoBase):
    produtos: list[ProdutoCreate]
    orgao: OrgaoCreate

    def as_db_dict(self):
        return self.dict(exclude={'produtos', 'orgao'})


class Licitacao(LicitacaoBase):
    produtos: list[Produto]
    orgao: Orgao
    id_licitacao: int

    class Config:
        orm_mode = True
