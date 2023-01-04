from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class ProdutoBase(BaseModel):
    ds_url: Optional[str] = None
    nr_produto_lote: Optional[str] = None
    ds_produto_lote: Optional[str] = None
    ds_tratamento_diferenciado_produto: Optional[str] = None
    cd_produto: Optional[str] = None
    nm_produto: Optional[str] = None
    ds_adicional_produto: Optional[str] = None
    nm_produto_embalagem: Optional[str] = None
    nr_produto_ordem: Optional[str] = None
    qt_produto: Optional[int] = None
    vl_preco_referencia: Optional[Decimal] = None


class ProdutoCreate(ProdutoBase):
    pass


class Produto(ProdutoBase):
    id_produto: int

    class Config:
        orm_mode = True
